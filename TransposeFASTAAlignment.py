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
# AUTHOR:

import re                                      # import regular expression tools

def TransposeFASTAAlignment(filename):

  f = open(filename,'r')                       # open text file for reading
  
  for line in f:                               # loop through lines of the file



  f.close()
  
  return numcolumns, numlines