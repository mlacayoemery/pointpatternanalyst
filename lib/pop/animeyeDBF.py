import sys
#add absolute path for shapefile library (relative to file import)
sys.path.append(sys.argv[0][:sys.argv[0].rfind("\\")+1]+"\\lib\\shp")
import databasefile

pairColumnIndex=8

def animeyeParse(inName,outName,dynamicSpecs):
    animeyeParseFile(open(inName),open(outName,'wb'),dynamicSpecs)

def animeyeParseFile(inFile,outFile,dynamicSpecs):
    #read in file, remove header, strip and split lines
    header=inFile.readline().split("\t")
    #get labels for pair columns and remove from header
    labelA,labelB=header.pop(pairColumnIndex).strip().strip("(").strip(")").split(",")
    #retove excess spacing from cells, and create row
    lines=[l.replace(" ","").strip().split("\t") for l in inFile.readlines()]
    inFile.close()

    #determine maximum cells in a row
    cells=max(map(len,lines))
    #construct header for zones by starting at 1 and adding numbers to labels
    for i in range(1,1+cells-pairColumnIndex):
        header.extend([labelA+str(i),labelB+str(i)])

    #loop over the lines and split the paired fields
    for i in range(len(lines)):
        #get the number of pairs in the row
        l = len(lines[i])-pairColumnIndex
        pad=[""]*((cells-len(lines[i]))*2)
        for j in range(l):
            lines[i].extend(lines[i].pop(pairColumnIndex).strip().strip("(").strip(")").split(","))
        #add empty cells for zone columns in other rows
        lines[i].extend(pad)

    #return header,lines
            
    d=databasefile.DatabaseFile(header,None,lines)

    if dynamicSpecs=="true":
        d.dynamicSpecs()
    else:
        d.staticSpecs()
        
    d.write(outFile)