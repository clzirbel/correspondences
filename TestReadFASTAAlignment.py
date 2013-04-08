# TestReadFASTAAlignment

from ReadFASTAAlignment import ReadFASTAAlignment

# ------------ Test 1

header, sequence, error = ReadFASTAAlignment("IL_93568.1 IL_1FJG_026 GG16S2012.fasta")

print header

print sequence

print error

# ------------ Test 2

header, sequence, error = ReadFASTAAlignment()

print header

print sequence

print error
