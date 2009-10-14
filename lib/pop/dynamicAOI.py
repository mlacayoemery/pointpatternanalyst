import sys, os
import Image

##inFolder="E:\\IJGIS\\BP27Cg"
##for name in os.listdir(inFolder):
##    inName=inFolder+"\\"+name
##    print inName

base="E:\\IJGIS\\BP27Cg\\"
report=open(base+"report.txt","w")
windowStatus=-1
for i in range(0,2051):
    name=("0"*(4-len(str(i))))+str(i)+".jpeg"
    inName=base+name
    im = Image.open(inName)
    if im.getpixel((1482,854))==(227, 254, 255) and (windowStatus==0 or windowStatus == -1):
        report.write(name + " Window open.\n")
        windowStatus=1
    elif im.getpixel((1482,1098))==(235, 251, 255) and (windowStatus==1 or windowStatus == -1):
        report.write(name + " Window closed.\n")
        windowStatus=0
    elif windowStatus==0 or windowStatus==1:
        report.write(name + " Window missing.\n")
        windowStatus=-1
report.close()