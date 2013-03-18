#          This file will have several functions in it, which help to retrieve
#          sequence variants from a multiple sequence alignment that correspond
#          to given nucleotides in a 3D structure file.

import re  # import functions for regular expressions

# INPUT:   a: a string referring to a column in an alignment
#          Example:  a = "GG16S2012|106"
# OUTPUT:  n: the integer at the end of the column specification
# AUTHOR:  

def GetAlignmentColumn(a):

  n = 0                                         # give n a default value

  # use regular expressions to find the integer at the end of a, extract it,
  # and convert it to an integer  

  return
  
  
  
  
# INPUT:   rs: comma and colon separated string of column identifier
#          Example:  a = "GG16S2012|106,GG16S2012|110:GG16S2012|120,,GG16S2012|127"
# OUTPUT:  ranges:  a list of lists of column integers
# NOTES:   single column identifiers should come back as a single integer
#          a range, indicated by a colon, should come back as all integers
#          from the first to the last, including first and last
#          it is possible to return an empty string 
# AUTHOR:  

def ParseRangeString(rs):

  ranges = []
  
  t = rs.split(",")                             # split on commas  

  for r in t:                                   # iterate through ranges
    b = r.split(":")                            # split on colons, if any

    for g in b:
    
      c = GetAlignmentColumn(g)


  return ranges 