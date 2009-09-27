import sys
import lib.pop.collapse

if __name__=="__main__":
    inName=sys.argv[1]
    collapseField=sys.argv[2]
    defaultOperation=sys.argv[3]
    outName=sys.argv[4]

    if sys.argv[]=="#":
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

    lib.pop.collapse.CollapseFile(inName,collapseField,defaultOperation,outName,minimumFields,meanFields,medianFields,maximumFields,sumFields)