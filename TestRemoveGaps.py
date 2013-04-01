# TestRemoveGaps tests the ability of RemoveGaps to leave out all-gap columns of an alignment

from RemoveGaps import RemoveGaps

# -------- First test:  remove the columns from this very small alignment

seq = []
seq.append('AG---CCU-G-A')
seq.append('-G--UCUC-A-A')
seq.append('UG---UCC-G-A')

newseq = RemoveGaps(seq)

print newseq

