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

def ExtractColumnsFromLine(line,ranges):

  line = line.replace(" ","")               # remove any spaces
  line = line.replace("\n","")              # remove newline characters

  s = ''                                    # accumulate extract here
  for i in range(0,len(ranges)):            # loop through ranges
    r = ranges[i]                           # focus on this range now
    if i > 0:
      s = s + ','                           # separate by commas
    if len(r) == 1:                         # single column
      s = s + line[r[0]-1]                  # extract single letter
    elif len(r) == 2:                       # range of columns
      s = s + line[(r[0]-1):r[1]]           # extract range of columns
  
  return s

def RetrieveColumnsFromAlignment(ranges,fastafilename,outputfilename):

  print "Reading",fastafilename
  print "Writing",outputfilename
  
  f = open(fastafilename,'r')
  g = open(outputfilename,'w')

  maxcol = 0;
  for r in ranges:
    for q in r:
      if q > maxcol:
        maxcol = q
    
  aligned = ""
  c = 0
      
  for line in f:
    if line[0] == '>':                          # header line
      c = c + 1
      if len(aligned) > maxcol:                 # enough sequence has been accumulated
        s = ExtractColumnsFromLine(aligned,ranges) # pull out the right columns  
        if c < 0:
          print c
          print "One line of FASTA file has length",str(len(aligned))
          print "One line of FASTA file:",aligned[0:40]
#          print "One line of extracts has length",str(len(s))
#          print "One line of extracts:",s[0:40]
        g.write(header+"\n")
        g.write(s+"\n")                         # write to file
#     else:
#        if len(aligned) > 0:
#          print "Line",str(c),"of FASTA file has length",str(len(aligned)),"but maxcol is ",str(maxcol)
#          print header
#          print aligned
      header = line.replace("\n","")            # save the current line
      aligned = ""                              # start on the next sequence
    else:
      aligned = aligned + line                  # append new sequence line

  if len(aligned) > maxcol:
    s = ExtractColumnsFromLine(aligned,ranges) # pull out the right columns  
    g.write(header+"\n")                    # write header
    g.write(s+"\n")                         # write to file
      
  f.close()
  g.close()