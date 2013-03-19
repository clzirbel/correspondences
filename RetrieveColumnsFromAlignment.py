# INPUT:   ranges:  a list of lists of columns in an alignment
#          fastafilename:  a string telling the location of an alignment in FASTA format
#          outputfilename:  a string telling the location of the file to write the results into
# OUTPUT:  for each line of the alignment, a comma-separated set of nucleotides
#          this matches the format of a range string
#          Example:  2QBD|1|A|A|10,2QBD|1|A|G|11:2QBD|1|A|U|14,,2QBD|1|A|U|17
#          Example:  A,GGCU,,C
# NOTES:   writing to a file is safer than returning a variable because very
#          large alignments may be used, and one might run out of RAM
# AUTHOR:  Craig L. Zirbel

def GetAlignmentColumn(a):

  t = a.split('|');                             # split on | character
  n = int(t[-1]);                               # convert to number

  return n
  
# INPUT:   rs: command colon separated string of nucleotide IDs
#          correspondences:  correspondences between a 3D structure and a 
#          sequence alignment.
#          Example: 
# OUTPUT:  ranges:  a list of lists of column integers
# NOTES:   Loop through the list, converting nucleotide IDs to column IDs, then
#          convert to lists of integers, one for each range
# AUTHOR:  

def ConvertIDRangeString(correspondences,rs):

  ranges = []
  
  t = rs.split(",")                             # split on commas  

  print t

  for r in t:                                   # iterate through ranges
    b = r.split(":")                            # split on colons, if any

    if len(b) == 1:                             # just one nucleotide here
      NTID = b[0]                               # this is a nucleotide ID
      if NTID in correspondences:               # check that there is a correspondence
        ColumnID = correspondences[NTID]        # look up the column ID
        ranges.append([GetAlignmentColumn(ColumnID)]) # append to ranges
      else:
        ranges.append([])                       # blank range
        
    elif len(b) == 2:                           # two-nucleotide range
      lowerNTID = b[0]
      upperNTID = b[1]
      if (lowerNTID in correspondences) and (upperNTID in correspondences):
        lowerColumnID = correspondences[lowerNTID]  # map NT to alignment column
        upperColumnID = correspondences[upperNTID]  # mat NT to alignment column
        lower = GetAlignmentColumn(lowerColumnID)   # number before the colon
        upper = GetAlignmentColumn(upperColumnID)   # number after the colon
        newrange = range(lower,upper+1)         # set of integers, inclusive
        ranges.append(newrange)                 # append to ranges
      else:
        ranges.append([])                       # something went wrong; empty list
    else:
      ranges.append([])                         # something went wrong; empty list
    
  return ranges
   