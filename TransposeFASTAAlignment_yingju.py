# INPUT:   filename: name of text file of alignment in FASTA format
#          outputfilename: file to write
# OUTPUT:  numcolumns: number of columns found
#          numlines: number of sequence lines found
#          a text file called outputfilename, whose first row is the letters
#          in column 1 of the alignment, second row is the letters in column 2,
#          all in the same order as in the original alignment
# NOTE:    The problem is that the original file may be 10 GB, so you can't
#          load it all into memory at once and then write out each column.
#          It is going to be hard to do!
#          Maybe search online for "transpose large character matrix"
#          For example, http://compgroups.net/comp.unix.shell/how-to-transpose-large-matrix/395899
# AUTHOR:  Ying-Ju Chen

import re                                      # import regular expression tools
import os

def TransposeFASTAAlignment(filename, outputfilename):

  f = open(filename,'r')                       # open text file for reading
  out = open(outputfilename, 'w')              # open text file for writing
  num = 0                                      # count number of seqence lines found, start from 0
  f.readline()                                 # read the first line
  numcolumns =len(f.readline())-1              # number of columns found exclude '/n'   
  TRAN = ['' for item in range(0, numcolumns)] # creat a new list to put the transpose of sequences
  f.seek(0)                                    # go back to the first line 

  for line in f:                               # loop through lines of the file
      num = num + 1
      if num %2 == 0:
          line.replace('\n','')
          for k in range(0, numcolumns):
             TRAN[k] = TRAN[k] + line[k]       # record each letter from each column in each line
    
  out.write("\n".join(TRAN))
  numlines = num
  
  f.close()
  out.close()
  return numcolumns, numlines
