import sys
import lib.pop.animeyeParse

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    dynamicSpecs=sys.argv[3]
    lib.pop.animeyeParse.animeyeParse(inName,outName,dynamicSpecs)