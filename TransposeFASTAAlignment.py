# INPUT:   filename of text file of alignment in FASTA format
# OUTPUT:  header:  a list of header lines
#          sequence:  a list of sequence lines, with newline characters and spaces removed
# AUTHOR:
# NOTE:    the first version of this program does not account for the fact
#          that some FASTA files have sequence lines spread out over multiple lines

import re                                      # import regular expression tools

def ReadFASTAAlignment(filename):

  header = []                                  # empty list for header lines
  sequence = []                                # empty list for sequence lines
  error = []                                   # empty list for error messages

  f = open(filename,'r')                       # open text file for reading
  
  for line in f:                               # loop through lines of the file
    if line[0] == '>':                         # header lines must begin with >
      header.append(line)                      # add to the header list
    else:
      sequence.append(line)                    # add to the sequence list

  f.close()
  
  return header, sequence, error