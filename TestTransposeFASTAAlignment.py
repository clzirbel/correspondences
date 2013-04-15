# TestReadFASTAAlignment

from TransposeFASTAAlignment import TransposeFASTAAlignment

# ------------ Test 1

numcolumns, numlines = TransposeFASTAAlignment("SSU_GG_MSA_escherichia_coli.fasta")

print numcolumns
print numlines