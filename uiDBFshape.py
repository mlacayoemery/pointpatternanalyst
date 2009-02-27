import sys
import lib.pop.tableToShape

if __name__ == "__main__":
    inName=sys.argv[1]
    xField=sys.argv[2]
    yField=sys.argv[3]
    outName=sys.argv[4]
    quadrant=sys.argv[5]
    shape=sys.argv[6]
    if sys.argv[7]=="true":
        changeTypes=True
    else:
        changeTypes=False
        
    lib.pop.tableToShape.TableToShape(inName,xField,yField,outName,quadrant,shape,changeTypes)