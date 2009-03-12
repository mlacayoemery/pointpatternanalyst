import sys
import lib.shp.shapefile

if __name__=="__main__":
    outName=sys.argv[1][:sys.argv[1].rfind(".")]

    if len(sys.argv)==3:
        typeValues=["","point","","line","","polygon"]
        shapeType=typeValues.index(sys.argv[2])
        lib.shp.shapefile.Shapefile(shapeType).writeFile(outName)

    elif len(sys.argv)==7:
        xMin=float(sys.argv[2])
        yMin=float(sys.argv[3])
        xMax=float(sys.argv[4])
        yMax=float(sys.argv[5])
        quadrant=sys.argv[6]

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

        s=lib.shp.shapefile.Shapefile(shapeType=5)
        s.add([[xMin*xScale,yMin*yScale],
              [xMax*xScale,yMin*yScale],
              [xMax*xScale,yMax*yScale],
              [xMin*xScale,yMax*yScale],
              [xMin*xScale,yMin*yScale]])
        s.writeFile(outName)