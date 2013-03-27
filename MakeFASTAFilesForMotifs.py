# INPUT:   motifstring: comma separated list of motif names
#          extractfilename: name of extract file, with comma-separated lines
#          MSAID: identifier for the multiple sequence alignment
# OUTPUT:  individual FASTA-format files for each unique sequence variant
# NOTES:   
# AUTHOR:  Craig L. Zirbel

import os

def MakeFASTAFilesForMotifs(motifstring,extractfilename,MSAID,PDBID,outputpath):

  variants = {}
  
  motifs = motifstring.split(",")
  
  for m in motifs:
    if m not in variants:
      variants[m] = {}
      
  f = open(extractfilename,'r')

  for line in f:                                # read each line of extract file
    if line[0] != ">":                          # header line starts with >
      e = line.replace("\n","").split(",")      # split into fields
      if len(e) != len(motifs):                 # they are supposed to match
        print "Number of motifs",len(motifs),"and number of extracts",len(e),"do not match"
      else:
        currentmotif = ""
        s = ""
        for i in range(0,len(e)):               # loop through fields here
          if motifs[i] == currentmotif:
            s = s + "*" + e[i]                  # another strand in this motif
          else:
	          if len(s) > 0:
	            if s in variants[currentmotif]:   # if this sequence variant is known,
	              variants[currentmotif][s] += 1  # increment the counter
	            else:
	              variants[currentmotif][s] = 1   # add this as a new variant, count 1
	          s = e[i]                            # start the next motif string
	          currentmotif = motifs[i]            # make note of the current motif  
        if len(s) > 0:                          # deal with the last motif
          if s in variants[currentmotif]:       # if this sequence variant is known,
            variants[currentmotif][s] += 1      # increment the counter
          else:
            variants[currentmotif][s] = 1       # add this as a new variant, count 1
        
  f.close()
  
  for m in motifs:
    if len(variants[m]) > 0:
      g = open(outputpath+os.sep+m+" "+MSAID+".fasta",'w')
      p = sorted(variants[m].items(), key=lambda x: -x[1])  # sort in decreasing order
      for r in p:
        g.write(">"+m+" "+str(r[1])+"\n")
        g.write(r[0]+"\n")
      g.close()
    else:
      print("No sequence instances found for this motif")
      print m    
      print variants[m]
    