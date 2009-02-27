import sys
import lib.pop.tobiiParse

if __name__=="__main__":
    inName=sys.argv[1]
    outName=sys.argv[2]
    if sys.argv[3]=="true":
        dynamicSpecs=True
    else:
        dynamicSpecs=False
    lib.pop.tobiiParse.tobiiParseFile(inName,outName,dynamicSpecs)