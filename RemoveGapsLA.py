# INPUT:   seq: a list of sequences, all with the same lengths
# OUTPUT:  newseq: the same sequences, but with columns that are all gaps removed
# AUTHOR:  

def RemoveGaps(seq):
  print seq[0]
  StatusSeq= []
  for i in range (0,len(seq[0])):
    StatusSeq.append('r')
    print StatusSeq
  for a in seq:
    print a
    for i in range (0,len(a)):
      if a [i] != '-':
        StatusSeq[i]="k"
    print StatusSeq
  for i in range (0,len(seq[0])
    if 'k'
      
  newseq = []
  
  # suggestion:  first loop through all sequences in seq, keeping track of
  # which columns have non-gap characters
  
  # then loop through the sequences again, copying only the needed columns
  # from seq to newseq

  return newseq

