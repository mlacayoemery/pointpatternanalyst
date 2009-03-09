from ..shp import databasefile
import math

def Sequence(inName,aoiField,outName,format,userField=None,timeField=None,aoiTable=None,aoiCodeField=None,aoiLabelField=None):
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
        for row in aoi:
            trans[row[labelIndex].strip()]=row[codeIndex]
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
        timeIndex=None
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
            t=row[timeIndex]

        seq[user][t]=row[aoiFieldIndex]            

    userKeys=seq.keys()
    userKeys.sort()
    records=[]
    for u in userKeys:
        record=[u,""]
        timeKeys=seq[u].keys()
        timeKeys.sort()
        for t in timeKeys:
            record[1]=record[1]+seq[u][t]
        records.append(record)

    print records
        
    if format=="Clustal G":
        lineWidth=72
        outFile=open(outName,'w')
        #write user id followed by rows of the sequence of no more than lineWidth characters.
        for r in records:
            outFile.write("> "+r[0]+" "+str(len(r[1]))+"\r\n")
            temp=r[1]
            for i in range(int(math.ceil(float(len(temp))/lineWidth))):
                outFile.write(temp[:lineWidth]+"\r\n")
                temp=temp[lineWidth:]
        outFile.close()
                    
    elif format=="Dbase IV":
        databasefile.DatabaseFile(fieldnames,fieldspecs,records).writeFile(outName)    

if __name__=="__main__":
    inName=sys.argv[1]
    userField=sys.argv[2]
    timeField=sys.argv[3]
    aoiField=sys.argv[4]
    outName=sys.argv[5]
    format=sys.argv[6]

    Sequence(inName,aoiField,outName,format,userField,timeField)