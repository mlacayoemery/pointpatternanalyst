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

def TableToShape(inName,xField,yField,outName,quadrant,shape,eventField,eventString):
    inFile=open(inName,'r')
    header=inFile.readline().strip().split(',')
    lines=[l.strip().split(',') for l in inFile.readlines()]
    inFile.close()

    xIndex=header.index(xField)
    yIndex=header.index(yField)
    

    #keep only certain features
    if eventField!="#":
        eventIndex=header.index(eventField)
        if eventString=="#":
            eventString=""
        for i in range(len(lines)-1,-1,-1):
            if lines[i][eventIndex]!=eventString:
                lines.pop(i)

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

    if shape=="point":
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
    else:
        s=shapefile.Shapefile(shapeType=3)
        lines=apply(zip,lines)
        lines=zip(map(float,lines[xIndex]),map(float,lines[yIndex]))
        lines=[(x*xScale,y*yScale) for x,y in lines]
        s.add(lines)

    s.writeFile(outName[:outName.rfind(".")])
    

if __name__ == "__main__":
    inName=sys.argv[1]
    xField=sys.argv[2]
    yField=sys.argv[3]
    outName=sys.argv[4]
    quadrant=sys.argv[5]
    shape=sys.argv[6]
    eventField=sys.argv[7]
    eventString=sys.argv[8]
    TableToShape(inName,xField,yField,outName,quadrant,shape,eventField,eventString)