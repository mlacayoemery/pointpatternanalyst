"""The user interface to the Separate script"""
__author__ = "Martin Lacayo-Emery <positrons@gmail.com>"


import sys
import lib.pop.separate

if __name__=="__main__":
    dbfName=sys.argv[1]
    fieldName=sys.argv[2]
    folder=sys.argv[3]
    if sys.argv[4]=="true":
        stem=dbfName[dbfName.rfind("\\")+1:dbfName.rfind(".")]
    else:
        stem=""
    namingSchemeValues=["Value","Order"]
    namingScheme=namingSchemeValues.index(sys.argv[5])
    lib.pop.separate.separateFile(dbfName,fieldName,folder,stem,namingScheme)