# INPUT:   sequence: a biological sequnce
#          MSAfilename: the filename of a multiple sequence alignment in FASTA format
#          sequencetype: a string which can be "protein" or "RNA" or "DNA"
# OUTPUT:  sequencenumber: an integer, starting at 1, telling which sequence
#          in the file was the best match
#          header: the header of the best-matching sequence
#          MSAsequence: the best-matching sequence from the alignment
# NOTE:    Some FASTA-formatted files have the sequence spread out over
#          multiple lines and have spaces within the line.  The code below
#          accumulates lines until a line starting with >, which is where
#          the next sequence starts.
# AUTHOR:  

from AlignmentPrograms import LocalAlignment

def FindBestAlignmentRow(sequence,MSAfilename,sequencetype):

  # open MSAfilename for reading


  aligned = ""                                  # accumulating sequence here
  c = 0                                         # sequence counter
  bestscore = 0;
  bestmatches = 0;

  # loop through lines in the file  
  for line in f:
    if line[0] == '>':                          # header line
      c = c + 1                                 # increment counter
      if len(aligned) > 0:                 # enough sequence has been accumulated
        matches, score, a1, a2, p1, p2 = LocalAlignment(sequence,aligned,sequencetype)

        # keep track of which alignment has the most matches, here
        # or keep track of which alignment has the best score
        # save all variables for the best one
                                
    else:
      aligned = aligned + line                  # append new sequence line
  
  return bestnumber, bestheader, bestsequence, bestmatches, bestscore, besta1, besta2, bestp1, bestp2

