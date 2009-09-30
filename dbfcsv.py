import sys
import lib.shp.databasefile

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    inTable=lib.shp.databasefile.DatabaseFile([],[],[],inName)
    inTable.writeCSV(outName)
    