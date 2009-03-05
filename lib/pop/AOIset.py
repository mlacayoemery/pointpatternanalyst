from ..shp import databasefile
import string

def AOIsetFile(inName,outName,fieldName,label,length,value):
    """
    AOIsetFile reads in a DBF and pass it to AOIset with a field index
    """
    dbf=databasefile.DatabaseFile([],[],[],inName)
    fieldIndex=dbf.index(fieldName)
    AOIs=list(AOIset(dbf,fieldIndex))
    AOIs.sort()

    fieldNames=[label,fieldName]
    fieldSpecs=[('C',length,0),dbf.fieldspecs[fieldIndex]]
    if value==0:
        codes=[""]*len(AOIs)
    else:
        codes=uniqueCodes(AOIs,length)
    records=zip(codes,AOIs)
    aoiDBF=databasefile.DatabaseFile(fieldNames,fieldSpecs,records)

    aoiDBF.writeFile(outName)
    
def AOIset(table,columnIndex):
    """
    AOIset loops over the rows in a row major table and makes a set from one of the columns
    """
    setA=set([])
    for row in table:
        setA.add(row[columnIndex])
    return setA



def uniqueCodes(AOIs,length):
    chars=string.ascii_lowercase
    codes=[""]*len(AOIs)
    digits=map(len(chars).__pow__,range(length-1,0,-1))
    for i,id in enumerate(range(len(AOIs))):
        for d in digits:
            c,id=divmod(id,d)
            codes[i]+=chars[c]
        codes[i]+=chars[id]
    return [c.capitalize() for c in codes]
        
        

def smartCodes(AOIs,length):
    codes={}
    l1Char=string.punctuation+string.whitespace+string.digits
    l1=string.maketrans(l1char,"_"*len(l1char))
    l2Char="aeiou"
    l2=string.maketrans(l2char,"_"*len(l2char))
    
    for a in AOIs:
        code=a.translate(l1).replace("_","")
        if codes.has_key(code[:length]):
            code=a.translate(l2)
            if codes.has_key(code[:length]):
                pass