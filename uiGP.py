"""Experiments with the geoprocessor"""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"
import arcgisscripting
import sys
import warnings

class messagegp:
    def __init__(self,gp):
        self.gp=gp

    def write(self,msg):
        self.gp.addmessage(msg)
    
class errorgp:
    def __init__(self,gp):
        self.gp=gp
        
    def write(self,msg):
        self.gp.addmessage(msg)

if __name__=="__main__":
    #create geoprocessor object
    gp = arcgisscripting.create()
    sys.stdout = messagegp(gp)
    sys.stderr = errorgp(gp)
    #gp.addmessage("gp.addmessage")
    #gp.addwarning("gp.addwarning")
    print "Message test."
    raise ValueError, "Error test."