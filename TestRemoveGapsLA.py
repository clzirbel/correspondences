# TestRemoveGaps tests the ability of RemoveGaps to leave out all-gap columns of an alignment

from RemoveGapsLA import RemoveGaps

# -------- First test:  remove the columns from this very small alignment

seq=[]
seq[0] = 'AG---CCU-G-A'
seq[1] = '-G--UCUC-A-A'
seq[2] = 'UG---UCC-G-A'

newseq = RemoveGaps(seq)

print newseq

