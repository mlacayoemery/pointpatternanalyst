"""The AOI set creation script."""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"
import sys
#add absolute path for shapefile library (relative to file import)
sys.path.append(sys.argv[0][:sys.argv[0].rfind("\\")+1]+"\\lib\\shp")
import databasefile
import shapefile
import geometry
import string
import math

def AOIsetFile(inName,outName,fieldName,label,length,value,fieldX=None,fieldY=None,geoType=0,xScale=1,yScale=1):
    """
    AOIsetFile reads in a DBF and pass it to AOIset with a field index
    """
    dbf=databasefile.DatabaseFile([],[],[],inName)
    fieldIndex=dbf.index(fieldName)
    AOIs=list(AOIset(dbf,fieldIndex))
    AOIs.sort()

    #construct the alphabet and determine word length
    chars=string.ascii_lowercase
    minimumLen=int(math.ceil(math.log(len(AOIs))/math.log(len(chars))))
    if length<minimumLen:
        #raise ValueError, "The minimum code length for your data is "+str(minimumLen)
        length=minimumLen

    #generate code column and codes
    fieldNames=[label,fieldName]
    fieldSpecs=[('C',length,0),dbf.fieldspecs[fieldIndex]]
    if value==0:
        codes=[""]*len(AOIs)
    else:
        codes=uniqueCodes(len(AOIs),length,chars)
    records=zip(codes,AOIs)
    aoiDBF=databasefile.DatabaseFile(fieldNames,fieldSpecs,records)

    #create geometry if specified
    if fieldX==None and fieldY==None:
        aoiDBF.writeFile(outName)
    else:
        s=shapefile.Shapefile(5)
        geo=AOIsetGeo(AOIs,dbf,fieldIndex,dbf.index(fieldX),dbf.index(fieldY),geoType,xScale,yScale)
        for aoi in AOIs:
            s.add(geometry.closedSet(geometry.boundingBoxCoordinates(geo[aoi])))
        s.table.extend(aoiDBF)
        s.writeFile(outName[:outName.rfind(".")])

def AOIset(table,columnIndex):
    """
    AOIset loops over the rows in a row major table and makes a set from one of the columns
    """
    setA=set([])
    for row in table:
        setA.add(row[columnIndex].strip())
    return setA


def uniqueCodes(AOIs,length,chars):
    """
    Creates a list of unique words using of a fixed length using the alphabet
    """
    codes=[""]*AOIs
    digits=map(len(chars).__pow__,range(length-1,0,-1))
    for i,id in enumerate(range(AOIs)):
        for d in digits:
            c,id=divmod(id,d)
            codes[i]+=chars[c]
        codes[i]+=chars[id]
    return [c.capitalize() for c in codes]        

def smartCodes(AOIs,length):
    """
    Creates a list of unique words of a fixed length based on the AOI names
    """
    codes={}
    #create translation tables
    l1Char=string.punctuation+string.whitespace+string.digits
    l1=string.maketrans(l1char,"_"*len(l1char))
    l2Char="aeiou"
    l2=string.maketrans(l2char,"_"*len(l2char))

    #attempt to translate names to unique word    
    for a in AOIs:
        code=a.translate(l1).replace("_","")
        if codes.has_key(code[:length]):
            code=a.translate(l2)
            if codes.has_key(code[:length]):
                pass

def AOIsetGeo(AOIset,dbf,aoiIndex,xIndex,yIndex,geoType,xScale,yScale):
    """
    Constructs geometry for AOIs
    """
    geo=dict(zip(AOIset,[None]*len(AOIset)))
    
    if geoType==0:
        for row in dbf:
            if geo[row[aoiIndex]]==None:
                geo[row[aoiIndex]]=geometry.boundingBox(float(row[xIndex])*xScale,float(row[xIndex])*xScale,
                                                         float(row[yIndex])*yScale,float(row[yIndex])*yScale)
            else:
                geo[row[aoiIndex]]=geometry.extendBoundingBox(geo[row[aoiIndex]],float(row[xIndex])*xScale,
                                                                float(row[yIndex])*yScale)
    return geo