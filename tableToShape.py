import sys, shapefile, databasefile

def IntegrateSpecs(s1,s2):
    s3=[]
    for s in zip(s1,s2):
        #if either charater type
        if s[0][0]=="C" or s[1][0]=="C":
            #pick the longer of the two
            if s[0][1]>s[1][1]:
                s3.append(("C",s[0][1],0))
            else:
                s3.append(("C",s[1][1],0))
            
        else:
            whole=max([s[0][1]-s[0][2],s[1][1]-s[1][2]])
            fract=max([s[0][2],s[1][2]])
            s3.append(("N",whole+fract,fract))
    return s3
\
def Spec(s):
    try:
        int(s)
        return ("N",len(s),0)
    except ValueError:
        try:
            float(s)
            return ("N",len(s),len(s)-s.rfind("."))
        except ValueError:
            return ("C",len(s),0)

def TableToShape(inName,xField,yField,outName,quadrant):
    inFile=open(inName,'r')
    header=inFile.readline().strip().split(',')
    lines=[l.strip().split(',') for l in inFile.readlines()]
    inFile.close()

    xIndex=header.index(xField)
    yIndex=header.index(yField)

    #set the scaling for the quadrant
    if quadrant=="1":
        xScale=1
        yScale=1
    elif quadrant=="2":
        xScale=-1
        yScale=1
    elif quadrant=="3":
        xScale=-1
        yScale=-1
    else:
        xScale=1
        yScale=-1

    s=shapefile.Shapefile(shapeType=1)
    for l in lines:
        s.add([[float(l[xIndex])*xScale,float(l[yIndex])*yScale]])
    
    specs=map(Spec,lines[0])
    for l in lines:
        tempSpecs=[]
        for n in l:
            tempSpecs.append(Spec(n))
        specs=IntegrateSpecs(specs,tempSpecs)      
            
    d=databasefile.DatabaseFile(header,specs,lines)
    s.table.extend(d)
    s.writeFile(outName[:outName.rfind(".")])
    

if __name__ == "__main__":
    inName=sys.argv[1]
    xField=sys.argv[2]
    yField=sys.argv[3]
    outName=sys.argv[4]
    quadrant=sys.argv[5]
    TableToShape(inName,xField,yField,outName,quadrant)