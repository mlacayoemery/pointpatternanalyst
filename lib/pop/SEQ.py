__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"

import sys
#add absolute path for shapefile library (relative to file import)
sys.path.append(sys.argv[0][:sys.argv[0].rfind("\\")+1]+"\\lib\\shp")
import databasefile
import math

def Sequence(inName,aoiField,outName,format,userField=None,timeField=None,scaleField=None,scaleUnit=1,aoiTable=None,aoiCodeField=None,aoiLabelField=None):
    """
    Sequence goes through a shapefile table and creates a sequence by appending the values in a cloumn.
    An user id field and a time field can be provided.
    """
    #read in data
    d=databasefile.DatabaseFile([],[],[],inName)

    #setup variables for sequence
    fieldnames=[]
    fieldspecs=[]
    records=[]

    #add AOI field name to field name list and get index
    fieldnames.append(aoiField)
    aoiFieldIndex=d.fieldnames.index(aoiField)    
    if aoiTable!=None:
        aoi=databasefile.DatabaseFile([],[],[],aoiTable)
        codeIndex=aoi.fieldnames.index(aoiCodeField)
        labelIndex=aoi.fieldnames.index(aoiLabelField)
        trans={}
        #create dictionary for aoi encoding
        for row in aoi:
            trans[row[labelIndex].strip()]=row[codeIndex]
        #replace input aoinames with aoicodes
        for row in d:
            row[aoiFieldIndex]=trans[row[aoiFieldIndex].strip()]

    seq={}
    if userField==None:
        userIndex=None
    else:
        userIndex=d.index(userField)
    if timeField==None:
        timeIndex=None
    else:
        timeIndex=d.index(timeField)
    if scaleField==None:
        scaleIndex=None
        scaleUnit=1
    else:
        scaleIndex=d.index(scaleField)
        
    for row in d:
        if userIndex==None:
            user=1
            if not seq.has_key(user):
                seq[user]={}
        else:
            user=row[userIndex]
            if not seq.has_key(user):
                seq[user]={}
                
        if timeIndex==None:
            t=len(seq[user])
        else:
            t=float(row[timeIndex])

        if scaleIndex==None:
            scale=1
        else:
            scale=float(row[scaleIndex])

        seq[user][t]=(row[aoiFieldIndex],scale)

    #convert dictionary into table
    userKeys=seq.keys()
    userKeys.sort()
    records=[]
    maxLen=0
    for u in userKeys:
        record=[u,[],[]]
        timeKeys=seq[u].keys()
        timeKeys.sort()
        if len(timeKeys)>maxLen:
            maxLen=len(timeKeys)
        for t in timeKeys:
            record[1].append(seq[u][t])
            record[2].append(t)
        records.append(record)

    #give sequence file name if only one
    if len(records)==1:
        records[0][0]=inName[inName.rfind("\\")+1:]
        
    if format==0:#"Clustal G"
        lineWidth=72
        outFile=open(outName,'w')
        #write user id followed by rows of the sequence of no more than lineWidth characters.
        for r in records:
            outFile.write("> "+str(r[0])+"\r\n")
            temp=""
            for aoi,scale in r[1]:
                temp=temp+(aoi*int(scale/scaleUnit))
            for i in range(int(math.ceil(float(len(temp))/lineWidth))):
                outFile.write(temp[:lineWidth]+"\r\n")
                temp=temp[lineWidth:]
        outFile.close()

    elif format==1:#"State-Sequence (STS)"
        outFile=open(outName,'w')
        outFile.write("Id,"+",".join(map(str,range(1,1+maxLen))))
        for r in records:
            outFile.write("\n"+str(r[0]).strip()+","+','.join(apply(zip,r[1])[0]))
        outFile.write("\n")
        outFile.close()

    elif format==2:#"State-Permanence (SPS)"
        outFile=open(outName,'w')
        outFile.write("Sequence")
        for r in records:
            outFile.write("\n"+'-'.join(map(str,r[1])))
        outFile.close()

    elif format==3:#"Distinct-State-Sequence (DSS)"
        raise ValueError, "Sorry the output format is not supported at this time."

    elif format==4:#"Time-Stamped Event (TSE)"
        outFile=open(outName,'w')
        outFile.write("Id Time Event")
        for id,event,time in records:
            for (e,d),t in zip(event,time):
                outFile.write("\n"+' '.join([id.strip(),str(t),e]))
        outFile.close()

    elif format==5:#"Person-Peroid"
        raise ValueError, "Sorry the output format is not supported at this time."

    elif format==6:#"Shifted-Replicated-Squence (SRS)"
        raise ValueError, "Sorry the output format is not supported at this time."

    elif format==7:#"Xbase (DBF)"
        databasefile.DatabaseFile(fieldnames,fieldspecs,records).writeFile(outName)

    else:
        raise ValueError, "Format type "+str(format)+" is not defined."

if __name__=="__main__":
    inName=sys.argv[1]
    userField=sys.argv[2]
    timeField=sys.argv[3]
    aoiField=sys.argv[4]
    outName=sys.argv[5]
    format=sys.argv[6]

    Sequence(inName,aoiField,outName,format,userField,timeField)