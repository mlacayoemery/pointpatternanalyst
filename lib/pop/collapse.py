"""The script that parses Tobii AOI files"""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"
import sys
#add absolute path for shapefile library (relative to file import)
sys.path.append(sys.argv[0][:sys.argv[0].rfind("\\")+1]+"\\lib\\shp")
#sys.path.append(sys.argv[0][:sys.argv[0].rfind("\\")+1]+"\\lib\\shp")
import databasefile

def tableDistance(inTableRow,tempTableRow,xFieldIndex,yFieldIndex):
    return ((float(inTableRow[xFieldIndex])-float(tempTableRow[xFieldIndex]))**2\
           + (float(inTableRow[yFieldIndex])-float(tempTableRow[yFieldIndex]))**2)**0.5

def median(values):
    values.sort()
    if len(values)%2:
        return values[len(values)/2]
    else:
        return float(values[(len(values)/2)-1]+values[len(values)/2])/2

def medianString(values):
    """
    returns the median by alphanumeric order
    """
    values.sort()
    return values[len(values)/2]

def mean(values):
    return float(sum(values))/len(values)

def meanString(values):
    """
    returns the mean by frequency
    """
    values.sort()
    currentString=values[0]
    tempString=values[0]
    currentCount=0
    tempCount=0
    for v in values:
        if v==currentString:
            currentCount=currentCount+1
        elif v==tempString:
            tempCount=tempCount+1
        else:
            if currentCount<tempCount:
                currentString=tempString
                currentCount=tempCount
            tempString=v
            tempCount=1
    return currentString

def sumString(values):
    """
    returns the set of values as a space delimited string
    """
    values=list(set(values))
    values.sort()
    return " ".join([v.strip() for v in values])

def identity(values):
    return values[0]

def CollapseFile(inName,defaultOperationName,outName,groupField,timeField,timeThreshold,xField,yField,distanceThreshold,minimumFields,meanFields,medianFields,maximumFields,sumFields):
    inTable=databasefile.DatabaseFile([],[],[],inName)
    outTable=databasefile.DatabaseFile(inTable.fieldnames,inTable.fieldspecs,[])
    Collapse(inTable,defaultOperationName,outTable,groupField,timeField,timeThreshold,xField,yField,distanceThreshold,minimumFields,meanFields,medianFields,maximumFields,sumFields)
    outTable.refreshSpecs()
    outTable.writeFile(outName)

def Collapse(inTable,defaultOperationName,outTable,groupField,timeField,timeThreshold,xField,yField,distanceThreshold,minimumFields,meanFields,medianFields,maximumFields,sumFields):
    tempTable=databasefile.DatabaseFile(inTable.fieldnames,inTable.fieldspecs,[inTable.removeRow(0)])
    if groupField!=None:
        groupFieldIndex=inTable.index(groupField)
    else:
        groupFieldIndex=None
    if timeField!=None:
        timeFieldIndex=inTable.index(timeField)
    else:
        timeFieldIndex=None
    if xField!=None:
        xFieldIndex=inTable.index(xField)
    else:
        xFieldIndex=None
    if yField!=None:
        yFieldIndex=inTable.index(yField)
    else:
        yFieldIndex=None

    #determine the default operation
    if defaultOperationName=="minimum":
        defaultOperation=min
    elif defaultOperationName=="maximum":
        defaultOperation=max
    elif defaultOperationName=="median":
        defaultOperation=median
    elif defaultOperationName=="mean":
        defaultOperation=mean
    elif defaultOperationName=="sum":
        defaultOperation=sum        
    else:
        raise TypeError, defaultOperationName + " is not defined."

    #determine the type and operation for each column
    tableTypes=map(databasefile.specType,inTable.fieldspecs)
    operations=[defaultOperation]*len(inTable.fieldspecs)

    #ensure proper type operation for default operations
    if defaultOperationName=="median":
        for i,t in enumerate(tableTypes):
            if t==str:
                operations[i]=medianString
    if defaultOperationName=="mean":
        for i,t in enumerate(tableTypes):
            if t==str:
                operations[i]=meanString
    if defaultOperationName=="sum":
        for i,t in enumerate(tableTypes):
            if t==str:
                operations[i]=sumString
                
    for fieldName in minimumFields:
        operations[inTable.index(fieldName)]=min
    for fieldName in maximumFields:
        operations[inTable.index(fieldName)]=max
    for fieldName in meanFields:
        fieldIndex=inTable.index(fieldName)
        if tableTypes[fieldIndex]==str:
            operations[fieldIndex]=meanString
        else:
            operations[fieldIndex]=mean
    for fieldName in medianFields:
        fieldIndex=inTable.index(fieldName)
        if tableTypes[fieldIndex]==str:
            operations[fieldIndex]=medianString
        else:
            operations[fieldIndex]=mean
    for fieldName in sumFields:
        fieldIndex=inTable.index(fieldName)
        if tableTypes[fieldIndex]==str:
            operations[fieldIndex]=sumString
        else:
            operations[fieldIndex]=sum
    if groupField!=None:
        operations[groupFieldIndex]=identity
    
    #loop over the table and group on collapse field
    for i in range(1,len(inTable)):
        if (groupField == None or inTable[i][groupFieldIndex]==tempTable[0][groupFieldIndex]) and (distanceThreshold == None or tableDistance(inTable[i],tempTable[0],xFieldIndex,yFieldIndex)<=distanceThreshold):
            tempTable.addRow(inTable[i])
        #else perform operation on temp
        elif timeThreshold == None or float(tempTable[0][timeFieldIndex])-float(tempTable[-1][timeFieldIndex])>=timeThreshold:
            tempRow=[]
            for id,values in enumerate(apply(zip,tempTable.records)):
##                print len(values)
##                print operations[id]
##                print tableTypes[id]
##                print tempRow
                tempRow.append(operations[id](map(tableTypes[id],values)))
            outTable.addRow(tempRow)
            tempTable.records=[inTable[i]]
        else:
            tempTable.records=[inTable[i]]
    if timeThreshold == None or float(tempTable[0][timeFieldIndex])-float(tempTable[-1][timeFieldIndex])>=timeThreshold:
        tempRow=[]
        for id,values in enumerate(apply(zip,tempTable.records)):
            tempRow.append(operations[id](map(tableTypes[id],values)))
        outTable.addRow(tempRow)