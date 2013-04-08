# TestReadFASTAAlignment

from ReadFASTAAlignment import ReadFASTAAlignment

# ------------ Test 1

header, sequence, error = ReadFASTAAlignment("IL_93568.1 IL_1FJG_026 GG16S2012.fasta")

print header[0]

print sequence[0]

print error

result = raw_input("End of Test 1. Press enter to continue.")

# ------------ Test 2

header, sequence, error = ReadFASTAAlignment("broken_lines.fasta")

print header[0]

print sequence[0]

print error
