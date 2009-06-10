"""Generate random sequences"""
__author__ = "Martin Lacayo-Emery <popanalyst@gmail.com>"
import random
import string

def randomSequence(idLength,alphabetSize,wordLength,sequenceLength,totalSequences,outName):
    startChars=string.ascii_uppercase[:alphabetSize]
    endChars=string.ascii_lowercase[:alphabetSize]
    outFile=open(outName,'w')

    #create all sequences
    for i in range(totalSequences):
        #create a Id
        outFile.write("> ")
        for j in range(idLength):
            outFile.write(string.ascii_lowercase[random.randint(0,25)])
        outFile.write("\n")

        #create a sequence
        line=0
        for k in range(sequenceLength):
            #write first letter of word
            if line==72:
                outFile.write("\n")
                line=0            
            outFile.write(startChars[random.randint(0,alphabetSize-1)])
            line=line+1
            #write rest of letters of word
            for l in range(wordLength-1):
                if line==72:
                    outFile.write("\n")
                    line=0
                outFile.write(endChars[random.randint(0,alphabetSize-1)])
                line=line+1
        outFile.write("\n")
    outFile.close()
                
if __name__=="__main__":
    idLength=10
    alphabetSize=26
    wordLength=2
    sequenceLength=20
    totalSequences=10
    outName="E:\\work\\randomseq2.txt"
    randomSequence(idLength,alphabetSize,wordLength,sequenceLength,totalSequences,outName)