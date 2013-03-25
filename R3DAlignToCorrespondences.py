from R3DAlignToID import R3DAlignToID

# Put a R3D Align output filename here:
# Put the desired output filename here:

R3DAlignfilename = "2QBD_2AW7_correspondences_5147462ca4e64.csv"
Outputfilename = "2QBD_2AW7_correspondences_5147462ca4e64.txt"

R3DAlignfilename = "2QBD_3I8H_correspondences_514313b142ec5.csv"
Outputfilename = "2QBD_3I8H_correspondences_514313b142ec5.txt"

R3DAlignfilename = "2QBG_3V2F_correspondences_50dd09ef4f614.csv"
Outputfilename = "2QBG_3V2F_correspondences_50dd09ef4f614.txt"


f = open(R3DAlignfilename,'r')
g = open(Outputfilename,'w')

c = 0

for line in f:
  t = line.split(",")
  if c == 0:
    PDB1 = t[1]
    PDB2 = t[4]
  else:
    if t[0].find(":") > 0 and t[3].find(":") > 0:
      ID1 = R3DAlignToID(PDB1,t[0])
      ID2 = R3DAlignToID(PDB2,t[3])
      g.write(ID1 + " corresponds_to " + ID2 + "\n")
  c += 1
  
f.close()
g.close()