import sys, databasefile

def Sequence(inName,userField,timeField,aoiField,outName,format):
    d=databasefile.DatabaseFile([],[],[])
    d.readFile(inName[:inName.rfind(".")]+".dbf")

    fieldnames=[]
    fieldspecs=[]
    records=[]

    fieldnames.append(aoiField)
    aoiFieldIndex=d.fieldnames.index(aoiField)
    records=apply(zip,d.records)

    if userField =="#":
        if timeField=="#":
            #single sequence, no time field
            records=[["".join(map(str,apply(zip,d.records)[aoiFieldIndex]))]]
        else:
            #single sequence with time field
            timeFieldIndex=d.fieldnames.index(timeField)
            records=zip(records[timeFieldIndex],records[aoiFieldIndex])
            records.sort()
            records=[["".join(map(str,apply(zip,records)[1]))]]
    elif timeField=="#":
        #user sequences, no time field
        fieldnames=[userField]+fieldnames
        userFieldIndex=d.fieldnames.index(userField)
        users=set(records[userFieldIndex])
        records=dict(zip(users,[""]*len(users)))
        for r in d.records:
            records[r[userFieldIndex]]+=str(r[aoiFieldIndex])
        records=zip(map(str,records.keys()),map(records.get,records.keys()))
    else:
        #user sequences and time field
        fieldnames=[userField]+fieldnames
        userFieldIndex=d.fieldnames.index(userField)
        users=set(records[userFieldIndex])
        records=[]
        timeFieldIndex=d.fieldnames.index(timeField)
        recordsDict=dict(zip(users,[{}]*len(users)))
        for r in d.records:
            recordsDict[r[userFieldIndex]][r[timeFieldIndex]]=r[aoiFieldIndex]
        for k in recordsDict.keys():
            times=recordsDict[k].keys()
            times.sort()
            line=[]
            for t in times:
                line.append(recordsDict[k][t])
            records.append([k,"".join(line)])

    if format=="Comma Separated Values":
        outFile=open(outName,'w')
        outFile.write('\n'.join([",".join(fieldnames)]+map(",".join,records)))
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

    Sequence(inName,userField,timeField,aoiField,outName,format)