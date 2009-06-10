"""Experiments with the geoprocesor field calculator."""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"
import arcgisscripting, sys

def CalculateLength(inputFC,field):
    gp = arcgisscripting.create()
    lExpression = "float(!SHAPE.LENGTH!)"
    gp.CalculateField_management(inputFC, field, lExpression, "PYTHON")

if __name__=="__main__":
    inputFC = sys.argv[1]
    field = sys.argv[2]
    AddGeometry(inputFC,field)