# INPUT:   PDB identifier and a string listing chain, nucleotide number, and base.
#          Model number is optional, the default is 1
#          Example: '2QBD','A:U5' which means nucleotide 5, uracil, of chain A of 2QBD
#          This is the format used by R3D Align in its basepair listing of the alignment
# OUTPUT:  Nucleotide identifier in universal format
#          Example: '2QBG|1|A|U|5'
# AUTHOR:  Craig L. Zirbel

import re

def R3DAlignToID(PDBID,nucleotide,model="1"):
  a = nucleotide.split(":")                    # split string at the colon
  chain = a[0]                                 # before that is the chain
  nt = a[1]                                    # nucleotide number
  base = nt[0]                                 # first letter is the base
  number = nt[1:len(nt)]                       # remainder is a number

  n = re.sub(r'([0-9]+)([A-Z])',r'\1|||\2',number) # some "numbers" have an extra letter,
                                               # which is set apart by |||
    
  ID = PDBID + "|" + model + "|" + chain + "|" + base + "|" + n

  return ID