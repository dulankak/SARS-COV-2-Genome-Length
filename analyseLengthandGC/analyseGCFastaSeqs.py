import os
import sys
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
usefilepath = os.path.join(THIS_FOLDER, 'gc_content.py')
fileHandle=open(usefilepath).read()
exec(fileHandle)

from pathlib import Path

print("This program tries to compare length and GC content of sequences from multiple FASTA files. It can be used to compare alliles of genes etc.\n")
print(r'Please give the full path(absolute path) of the FASTA files, you can find this using the file properties tab.\n `Ex: C:\analyseLengthandGC\examples\sequence.fasta\n.Special note: This Program is designed and therefore better suited for FASTA files released by NCBI, as header information on files by other sources may differ slightly\n')
print("Trying to load each file individually\n")
#variable to keep count of the number of files to compare
#numOfFastaFiles=0
while True:
    try:
        #ask user how many files he wants to compare
        numOfFastaFiles=int(input("how many files do you want to compare? Please enter a number:\n"))
        break
    except ValueError:
        print("You did not enter a valid number(integer) for number of files you want to compare. Try again...")
    else:
        input("You input an invalid entry.This program will have to shut down. Press any key to quit\n")
        sys.exit(0)    

#create blank 2D array with w columns and h rows
w, h = 4, numOfFastaFiles;
dataTable = [[0 for x in range(w)] for y in range(h)]


fileNum=1
while fileNum<=numOfFastaFiles:
 #print(fileNum)
 	

 #ask user for the file name and location
 fileloc=Path(input("give the location(absolute path and file name) of the FASTA file you want to analyse,file: "+str(fileNum)+"\n"))


 #attempt to load the files one by one, analyze then then store the result only for later comparison
 fastafile=open(fileloc,'r')
 #get header information
 headerInfo=str(fastafile.readline())
 #get and store assesin number
 assesinNo=headerInfo[1:int(headerInfo.find(" "))]
 #print("Accesin No: "+assesinNo)
 #print header info
 print("Header Info: "+headerInfo)
 #read the rest of the file(sequence) to a variable
 fastacontent=fastafile.read()
 
 #print(fastacontent)

 fastafile.close()

 #fastastringhandle3=str(read_Fasta_strings(fileloc))

 fastastringhandle3=str(fastacontent)
 fastastringhandle2=fastastringhandle3.strip()
 fastastringhandle=fastastringhandle2.replace("\n","")
 #print the length of the sequence
 sequenceLength=str(len(fastastringhandle))
 print("Length of this file is "+sequenceLength+"\n")
 #print the file content
 print(fastastringhandle)

 #get GC contect
 #validate=validate_base_sequence(fastastringhandle)
 GCconresult=gc_content(fastastringhandle)
 print(GCconresult)
 GCpercentage=str(round(GCconresult*100,2))
 print("percentage: "+GCpercentage+" %")

 ###add details to table
 arrayIndx=fileNum-1
 dataTable[arrayIndx][0]=fileNum
 dataTable[arrayIndx][1]=assesinNo
 dataTable[arrayIndx][2]=sequenceLength
 dataTable[arrayIndx][3]=GCpercentage+"%"
 #
 
 fileNum+=1

#print results
print("Printing results\n")
print("File No.\t Locus No.\t Sequence Length\t GC content\n")
for r in dataTable:
    for c in r:
        print(c,end = "\t")
    print()

#do the comparisons
smallestLengthValue=0
smallestLengthIndex=0
longestLengthValue=0
longestLengthIndex=0

for row in dataTable:
#comment this
 if (row[0]!=1):
  #this is a normal row,compare and put shortest or longest lenghts,GC contents
  #print ("row "+str(row)+"\n")
  #print(row[1])
  if(int(smallestLengthValue)>=int(row[2])):
   print("came to IF")
   smallestLengthValue=row[2]
   smallestLengthIndex=row[0]
   #print("smallest length value "+smallestLengthValue+"\n")
   
  if(int(longestLengthValue)<=int(row[2])):
   #print("came to IF")
   longestLengthValue=row[2]
   longestLengthIndex=row[0]
 
 elif (row[0]==1):
  #this is the first row.so initialise variables and indexes with the initial values of row 0
  print("came to elif")
  smallestLengthValue=row[2]
  smallestLengthIndex=row[0]
  longestLengthValue=row[2]
  longestLengthIndex=row[0]
  print ("initial: smallest length value is "+str(smallestLengthValue)+" and "+"smallest length index is "+str(smallestLengthIndex))

print ("smallest length value is "+str(smallestLengthValue)+" and "+"smallest length index is "+str(smallestLengthIndex))
print ("longest length value is "+str(longestLengthValue)+" and "+"longest length index is "+str(longestLengthIndex))

#close program
input("press any key to quit\n")
sys.exit(0)
