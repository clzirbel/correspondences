# TestRemoveGaps tests the ability of RemoveGaps to leave out all-gap columns of an alignment

from RemoveGaps import RemoveGaps

# -------- First test:  remove the columns from this very small alignment

seq = []
seq.append('AG---CCU-G-A')
seq.append('-G--UCUC-A-A')
seq.append('UG---UCC-G-A')

newseq = RemoveGaps(seq)

print newseq

# --------- Second test: read a FASTA file and remove the gaps

header, sequence, fasta = ReadFASTAAlignment("IL_93568.1 IL_1FJG_026 GG16S2012.fasta")

print sequence

newsequence = RemoveGaps(sequence)


