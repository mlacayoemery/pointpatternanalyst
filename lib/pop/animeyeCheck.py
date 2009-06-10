"""Checks complaince with SensoMotoric format"""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"

import string
import time

def animeyeCheck(inName,outReport,outName,verbose=True):
    inFile=open(inName)
    report=open(outReport,'w')
    if outName != None:
        outFile=open(outName,'w')

    #write report header
    report.write("POP Analyst Animeye TSV file check report")
    if verbose:
        report.write("\n"+str(time.ctime(time.time()))+"\n\n")
        report.write("This check was performed on: \n"+inName+"\n")
        if outName!=None:
            report.write("A corrected file was written to: \n"+outName+"\n")
    else:
        report.write("\n\n")        

    #check for and fix unallowed characters
    header=inFile.readline().strip().split("\t")
    #translate the header to be character compliant
    charmap=string.maketrans(string.punctuation+string.whitespace,
                             "_"*(len(string.punctuation)+len(string.whitespace)))
    correctedHeader=[f.translate(charmap) for f in header]
    if header!=correctedHeader:
        report.write("\nThe column header is not compliant.")
        if verbose:
            report.write("\nThe column header is: "+str(header))
            report.write("\nThe correct header is: "+str(correctedHeader))
    else:
        report.write("\nThe column header is compliant.")

    #write out data if correcting file
    if outName != None:
        outFile.write("\t".join(correctedHeader)+"\n")
        outFile.write(inFile.read())
        outFile.close()

    inFile.close()