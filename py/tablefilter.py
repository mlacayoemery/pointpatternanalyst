import sys
import databasefile

def filterTable(inName,field,filtertype,equal,minimum,maximum,outName,retype):
    d=databasefile.DatabaseFile([],[],[],inName)
    fieldIndex=d.fieldnames.index(field)
    fieldType=databasefile.specType(d.fieldspecs[fieldIndex])

    if filtertype=="Values to Keep":
        keep=True
    else:
        keep=False

    if equal !="#":
        for i in range(len(d.records)-1,-1,-1):
            if fieldType(d.records[i][fieldIndex].strip())==fieldType(equal.strip()):
                if not keep:
                    d.records.pop(i)
            elif keep:
                d.records.pop(i)                    
    if minimum !="#":
        for i in range(len(d.records)-1,-1,-1):
            if fieldType(d.records[i][fieldIndex].strip())<fieldType(minimum.strip()):
                if not keep:
                    d.records.pop(i)
            elif keep:
                d.records.pop(i)
    if maximum !="#":
        for i in range(len(d.records)-1,-1,-1):
            if fieldType(d.records[i][fieldIndex].strip())>fieldType(maximum.strip()):
                if not keep:
                    d.records.pop(i)
            elif keep:
                d.records.pop(i)

    if retype=="true":
        d.refreshSpecs()
        
    d.writeFile(outName)                

if __name__=="__main__":
    inName=sys.argv[1]
    field=sys.argv[2]
    filtertype=sys.argv[3]
    equal=sys.argv[4]
    minimum=sys.argv[5]
    maximum=sys.argv[6]
    outName=sys.argv[7]
    retype=sys.argv[8]
    filterTable(inName,field,filtertype,equal,minimum,maximum,outName,retype)