import sys

if __name__=="__main__":
    inName=sys.argv[1]
    conversionType=sys.argv[2]
    outName=sys.argv[3]
    if sys.argv[4]=="true":
        dynamicSpecs=True
    else:
        dynamicSpecs=False
    if conversionType=="Tobii":
        import lib.pop.tobiiDBF
        lib.pop.tobiiDBF.tobiiParse(inName,outName,dynamicSpecs)
    elif coversionType=="SensoMotoric":
        import lib.pop.animeyeDBF
        lib.pop.animeyeDBF.animeyeParse(inName,outName,dynamicSpecs)
    else:
        raise ValueError, conversionType + " is not a defined format."