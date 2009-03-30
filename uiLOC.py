import sys
import lib.pop.LOC

if __name__=="__main__":
    aoisName=sys.argv[1]
    aoisField=sys.argv[2]
    priorityField=sys.argv[3]
    xField=sys.argv[4]
    yField=sys.argv[5]
    aoisetName=sys.argv[6]
    aoisetField=sys.argv[7]
    aoicodeField=sys.argv[8]
    outName=sys.argv[9]
    lib.pop.LOC.locFile(aoisName,aoisField,priorityField,
                        xField,yField,aoisetName,aoisetField,
                        aoicodeField,outName)