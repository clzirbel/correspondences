from R3DAlignToID import R3DAlignToID

# Put a R3D Align output filename here:
R3DAlignfilename = "2QBD_3I8H_correspondences_514313b142ec5.csv"

# Put the desired output filename here:
Outputfilename = "2QBD_3I8H_correspondences_514313b142ec5.txt"

f = open(R3DAlignfilename,'r')
g = open(Outputfilename,'w')


sequences = []
organisms = []

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