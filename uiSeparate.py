"""The user interface to the Separate script

"""

__author__ = "Martin Lacayo-Emery <positrons@gmail.com>"
__date__ = "11 March 2009"

__version__ = "$Revision: 1 $"
__credits__ = """Arzu \xc7\xf6ltekin, University of Z\xfcrich, project collaborator
Sara Fabrikant, University of Z\xfcrich, project collaborator
Fulbright Program, funding agency
"""

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