"""The script that parses Tobii AOI files"""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"
import sys
#add absolute path for shapefile library (relative to file import)
sys.path.append(sys.argv[0][:sys.argv[0].rfind("\\")+1]+"\\lib\\shp")
import databasefile

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

def CollapseFile(inName,collapseField,defaultOperationName,outName,minimumFields,meanFields,medianFields,maximumFields,sumFields):
    inTable=databasefile.DatabaseFile([],[],[],inName)
    outTable=databasefile.DatabaseFile(inTable.fieldnames,inTable.fieldspecs,[])
    Collapse(inTable,collapseField,defaultOperationName,outTable,minimumFields,meanFields,medianFields,maximumFields,sumFields)
    outTable.refreshSpecs()
    outTable.writeFile(outName)

def Collapse(inTable,collapseField,defaultOperationName,outTable,minimumFields,meanFields,medianFields,maximumFields,sumFields):
    tempTable=databasefile.DatabaseFile(inTable.fieldnames,inTable.fieldspecs,[inTable.removeRow(0)])
    collapseFieldIndex=inTable.index(collapseField)

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
    operations[collapseFieldIndex]=identity
    
    #loop over the table and group on collapse field
    for i in range(1,len(inTable)):
        #if in same collapse group add to temp
        if inTable[i][collapseFieldIndex]==tempTable[0][collapseFieldIndex]:
            tempTable.addRow(inTable[i])
        #else perform operation on temp
        else:
            tempRow=[]
            for id,values in enumerate(apply(zip,tempTable.records)):
##                print len(values)
##                print operations[id]
##                print tableTypes[id]
##                print tempRow
                tempRow.append(operations[id](map(tableTypes[id],values)))
            outTable.addRow(tempRow)
            tempTable.records=[inTable[i]]
    tempRow=[]
    for id,values in enumerate(apply(zip,tempTable.records)):
        tempRow.append(operations[id](map(tableTypes[id],values)))
    outTable.addRow(tempRow)


if __name__=="__main__":
    inName=sys.argv[1]
    collapseField=sys.argv[2]
    defaultOperation=sys.argv[3]
    outName=sys.argv[4]

    if sys.argv[5]=="#":
        minimumFields=[]
    else:
        minimumFields=sys.argv[5].split(";")

    if sys.argv[6]=="#":
        meanFields=[]
    else:
        meanFields=sys.argv[6].split(";")

    if sys.argv[7]=="#":
        medianFields=[]
    else:
        medianFields=sys.argv[7].split(";")

    if sys.argv[8]=="#":
        maximumFields=[]
    else:
        maximumFields=sys.argv[8].split(";")

    if sys.argv[9]=="#":
        sumFields=[]
    else:
        sumFields=sys.argv[9].split(";")

    CollapseFile(inName,collapseField,defaultOperation,outName,minimumFields,meanFields,medianFields,maximumFields,sumFields)
    