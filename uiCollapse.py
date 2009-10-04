import sys
import lib.pop.collapse

if __name__=="__main__":
    inName=sys.argv[1]
    defaultOperation=sys.argv[2]
    outName=sys.argv[3]

    if sys.argv[4]=="#":
        groupField=None
    else:
        groupField=sys.argv[4]    
    if sys.argv[5]=="#":
        timeField=None
    else:
        timeField=float(sys.argv[5])
    if sys.argv[6]=="#" or timeField==None:
        timeThreshold=None
    else:
        timeThreshold=sys.argv[6]
    if sys.argv[7]=="#" or sys.argv[8]=="#":
        xField=None
    else:
        xField=sys.argv[7]
    if sys.argv[8]=="#" or sys.argv[7]=="#":
        yField=None
    else:
        yField=sys.argv[8]
    if sys.argv[9]=="#" or xField==None or yField==None:
        distanceThreshold=None
    else:
        distanceThreshold=float(sys.argv[9])

    if groupField == None and timeField == None and xField == None and yField == None:
        raise ValueError, "No field for grouping has been selected. For spatial grouping this may mean that either the X or Y coordinate has not been set."
    
    if sys.argv[10]=="#":
        minimumFields=[]
    else:
        minimumFields=sys.argv[10].split(";")

    if sys.argv[11]=="#":
        meanFields=[]
    else:
        meanFields=sys.argv[11].split(";")

    if sys.argv[12]=="#":
        medianFields=[]
    else:
        medianFields=sys.argv[12].split(";")

    if sys.argv[13]=="#":
        maximumFields=[]
    else:
        maximumFields=sys.argv[13].split(";")

    if sys.argv[14]=="#":
        sumFields=[]
    else:
        sumFields=sys.argv[14].split(";")

    lib.pop.collapse.CollapseFile(inName,defaultOperation,outName,groupField,timeField,timeThreshold,xField,yField,distanceThreshold,minimumFields,meanFields,medianFields,maximumFields,sumFields)