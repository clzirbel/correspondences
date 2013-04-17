# TestReadFASTAAlignment

from TransposeFASTAAlignment import TransposeFASTAAlignment

# ------------ Test 1

numcolumns, numlines = TransposeFASTAAlignment("SSU_GG_MSA_escherichia_coli.fasta", "SSU_GG_MSA_escherichia_coli_transpose.txt")

print numcolumns
print numlines
