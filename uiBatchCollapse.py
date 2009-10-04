"""The batch to Xbase script."""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"

import sys
import os
import arcgisscripting
import lib.pop.collapse

if __name__=="__main__":
    #create geoprocessor object
    gp = arcgisscripting.create()

    #store parameters
    inFolder=sys.argv[1]
    #inName=sys.argv[2]
    defaultOperation=sys.argv[3]
    outFolder=sys.argv[4]

    if sys.argv[5]=="#":
        groupField=None
    else:
        groupField=sys.argv[5]    
    if sys.argv[6]=="#":
        timeField=None
    else:
        timeField=float(sys.argv[6])
    if sys.argv[7]=="#" or timeField==None:
        timeThreshold=None
    else:
        timeThreshold=sys.argv[7]
    if sys.argv[8]=="#" or sys.argv[9]=="#":
        xField=None
    else:
        xField=sys.argv[8]
    if sys.argv[8]=="#" or sys.argv[9]=="#":
        yField=None
    else:
        yField=sys.argv[9]
    if sys.argv[10]=="#" or xField==None or yField==None:
        distanceThreshold=None
    else:
        distanceThreshold=float(sys.argv[10])

    if groupField == None and timeField == None and xField == None and yField == None:
        raise ValueError, "No field for grouping has been selected. For spatial grouping this may mean that either the X or Y coordinate has not been set."
    
    if sys.argv[11]=="#":
        minimumFields=[]
    else:
        minimumFields=sys.argv[11].split(";")

    if sys.argv[12]=="#":
        meanFields=[]
    else:
        meanFields=sys.argv[12].split(";")

    if sys.argv[13]=="#":
        medianFields=[]
    else:
        medianFields=sys.argv[13].split(";")

    if sys.argv[14]=="#":
        maximumFields=[]
    else:
        maximumFields=sys.argv[14].split(";")

    if sys.argv[15]=="#":
        sumFields=[]
    else:
        sumFields=sys.argv[15].split(";")

    #run each collapse
    for name in os.listdir(inFolder):
        inName=inFolder+"\\"+name
        #remove dot from name, as ArcGIS doesn't like it
        outName=outFolder+"\\"+name.replace(".","_")+".dbf"
        gp.AddMessage("Converting "+inName)
        lib.pop.collapse.CollapseFile(inName,defaultOperation,outName,groupField,timeField,timeThreshold,xField,yField,distanceThreshold,minimumFields,meanFields,medianFields,maximumFields,sumFields)
        