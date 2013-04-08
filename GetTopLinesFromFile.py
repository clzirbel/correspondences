# INPUT:   filename of text file that is too big to load in a text editor
#          outputname: name of the text file to write
#          numberoflines: number of lines to read and write
# OUTPUT:
# AUTHOR:

import re                                      # import regular expression tools
import sys

def GetTopLinesFromFile(filename,outputname,numberoflines = 100):

  f = open(filename,'r')                       # open text file for reading
  g = open(outputname,'w')
  c = 0

  for line in f:                               # loop through lines of the file
    c = c + 1
    if c <= numberoflines:
      g.write(line)

  f.close()
  g.close()

def main():
  GetTopLinesFromFile("C:\\Users\\zirbel\\Documents\\Alignments\\arb-silva.de_2013-03-21_id87437_gapcompressedvertical.fasta","broken_lines.fasta",2000)

if __name__ == "__main__":
   main()