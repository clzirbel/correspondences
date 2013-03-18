# INPUT:   filename of text file of correspondences
#          mode, which tells which order the correspondences should be recorded
#          Example:  2QBD|1|A|U|5 corresponds_to 3I8H|1|A|U|5 with mode=0
# OUTPUT:  correspondences:  A dictionary of correspondences
#          header:  A list of strings from the file that start with #
#          error: A list of lines from the file that could not be read 
# AUTHOR:  Craig L. Zirbel

import re                                      # import regular expression tools

def ReadCorrespondences(filename,mode=0):

  header = []                                  # empty list for header lines
  correspondences = {}                         # empty dictionary for correspondences
  error = []                                   # empty list for error messages

  f = open(filename,'r')                       # open text file for reading
  
  for line in f:                               # loop through lines of the file
    if line[0] == '#':                         # header lines must begin with #
      header.append(line)                      # add to the header list
    else:
      t = line.split()                         # split line at space or tab
      if len(t) == 3:                          # if there are three entries
        if mode == 0:                          # first column is the key
          correspondences[t[0]] = t[2]         # store the correspondence
        else:
          correspondences[t[2]] = t[0]         # store the other direction
      else:
        error.append(line)                     # something wrong with this line

  f.close()
  
  return correspondences, header, error