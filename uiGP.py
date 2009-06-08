import arcgisscripting
import sys

class mygp(arcgisscripting):
    def __init__(self):
        self.create()

    def write(self,msg):
        self.addmessage(msg)
    

if __name__=="__main__":
    #create geoprocessor object
    gp = mygp()
    sys.stdout = gp
    #gp.addmessage("gp.addmessage")
    #gp.addwarning("gp.addwarning")
    print "Test."