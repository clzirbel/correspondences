# INPUT:   sequence:  A single, ungapped sequence, perhaps from an RNA or protein 3D structure
#          alignmentfile:  The filename of a sequence alignment in FASTA format
# OUTPUT:  correspondences:  A list of correspondences between sequence positions in sequence
#          and columns in the alignment file.
# METHOD:  Read the alignment line by line.  Align sequence to the sequence in
#          each line of the alignment.  Find the best alignment, then figure out
#          how positions in sequence map to columns in the alignment.
# NOTES:   Count positions in sequence and columns in the alignment starting at 1
# AUTHOR:  

def MatchSequenceToAlignment(correspondences1,header1,correspondences2,header2):

  correspondences = {}                                 # empty dictionary






  return correspondences 