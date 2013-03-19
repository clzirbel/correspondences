# This file will have several functions in it, which help to retrieve
# sequence variants from a multiple sequence alignment that correspond
# to given nucleotides in a 3D structure file.

import re  # import functions for regular expressions

# INPUT:   a: a string referring to a column in an alignment
#          Example:  a = "GG16S2012|106"
# OUTPUT:  n: the integer at the end of the column specification
# AUTHOR:  

def GetAlignmentColumn(a):

  n = 0                                         # give n a default value

  # use regular expressions to find the integer at the end of a, extract it,
  # and convert it to an integer  

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

    if len(b) == 1:                             # just one column here
      NTID = b[0]                               # this is a nucleotide ID
      if NTID in correspondences:               # check that there is a correspondence
        ColumnID = correspondences[NTID]        # look up the column ID
        ranges.append([GetAlignmentColumn(ColumnID)]) # append to ranges
      else:
        ranges.append([])                       # blank range
        
    elif len(b) == 2:
      lowerNTID = b[0]
      upperNTID = b[1]
      if (lowerNTID in correspondences) and (upperNTID in correspondences):
        lower = GetAlignmentColumn(lowerNTID)   # number before the colon
        upper = GetAlignmentColumn(upperNTID)   # number after the colon
        newrange = range(lower,upper+1)         # set of integers, inclusive
        ranges.append(newrange)                 # append to ranges
      else:
        ranges.append([])                       # something went wrong; empty list
    else:
      ranges.append([])                         # something went wrong; empty list
    
  return ranges
   