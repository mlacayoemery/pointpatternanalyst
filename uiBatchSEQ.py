"""The user interface to the SEQ."""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"

import sys
import os
import arcgisscripting
import lib.pop.SEQ

if __name__=="__main__":
    #create geoprocessor
    gp = arcgisscripting.create()

    #store parameters
    inFolder=sys.argv[1]
    inName=sys.argv[2]
    aoiField=sys.argv[3]
    aoiTable=sys.argv[4]
    aoiCodeField=sys.argv[5]
    aoiLabelField=sys.argv[6]
    formatTypes=["Clustal G",
                 "State-Sequence (STS)",
                 "State-Permanence (SPS)",
                 "Distinct-State-Sequence (DSS)",
                 "Time-Stamped Event (TSE)",
                 "Person-Peroid",
                 "Shifted-Replicated-Squence (SRS)",
                 "Xbase (DBF)"]
    format=formatTypes.index(sys.argv[7])
    outFolder=sys.argv[8]
    if sys.argv[9]=="#":
        separateField=None
    else:
        separateField=sys.argv[9]
    #ignore OID as a column name, as it is not really in the table
    if sys.argv[10]=="OID":
        orderByField=None
    elif sys.argv[10]=="#":
        orderByField=None
    else:
        orderByField=sys.argv[10]
    if sys.argv[11]=="#":
        scaleByField=None
    else:
        scaleByField=sys.argv[11]
    if sys.argv[12]=="#":
        scaleUnit=1
    else:
        scaleUnit=float(sys.argv[12])

    #loop over each file in the folder, perform sequence creation
    for name in os.listdir(inFolder):
        inName=inFolder+"\\"+name
        #remove dot from ouput file name, as ArcGIS doesn't like it
        outName=outFolder+"\\"+name.replace(".","_")+".txt"
        gp.AddMessage("Processing "+inName)     
        lib.pop.SEQ.Sequence(inName,aoiField,outName,format,separateField,orderByField,scaleByField,scaleUnit,aoiTable,aoiCodeField,aoiLabelField)
    