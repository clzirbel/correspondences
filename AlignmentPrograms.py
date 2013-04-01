# INPUT:   strings (seq1) and (seq2)
# OUTPUT:  number of matches (matches), strings (a1) and (a2) with hyphens
#          to show where non-aligned characters are, and two lists of sequence
#          positions (p1) and (p2) indicating which positions are aligned

# These lines define the input; change the order of lines to work with different
# sequences

from numpy import *


def RNA_scores():

  RNA_scores = {
  'A':{'A':6,'C':-3, 'G':-3, 'U':-3},
  'C':{'A':-3,'C':6, 'G':-3, 'U':-3},
  'G':{'A':-3,'C':-3, 'G':6, 'U':-3},
  'U':{'A':-3,'C':-3, 'G':-3, 'U':6}}
  
  return RNA_scores  

def DNA_scores():

  DNA_scores = {
  'A':{'A':6,'C':-3,'G':-3,'T':-3},
  'C':{'A':-3,'C':6,'G':-3,'T':-3},
  'G':{'A':-3,'C':-3,'G':6,'T':-3},
  'T':{'A':-3,'C':-3,'G':-3,'T':6}}
  
  return DNA_scores  

def BLOSUM62_scores():

  BLOSUM62={
  'A':{'A': 4,'R':-1,'N':-2,'D':-2,'C': 0,'Q':-1,'E':-1,'G': 0,'H':-2,'I':-1,
      'L':-1,'K':-1,'M':-1,'F':-2,'P':-1,'S': 1,'T': 0,'W':-3,'Y':-2,'V': 0,'X':0},
  'R':{'A':-1,'R': 5,'N': 0,'D':-2,'C':-3,'Q': 1,'E': 0,'G':-2,'H': 0,'I':-3,
      'L':-2,'K': 2,'M':-1,'F':-3,'P':-2,'S':-1,'T':-1,'W':-3,'Y':-2,'V':-3,'X':0},
  'N':{'A':-2,'R': 0,'N': 6,'D': 1,'C':-3,'Q': 0,'E': 0,'G': 0,'H': 1,'I':-3,
      'L':-3,'K': 0,'M':-2,'F':-3,'P':-2,'S': 1,'T': 0,'W':-4,'Y':-2,'V':-3,'X':0},
  'D':{'A':-2,'R':-2,'N': 1,'D': 6,'C':-3,'Q': 0,'E': 2,'G':-1,'H':-1,'I':-3,
      'L':-4,'K':-1,'M':-3,'F':-3,'P':-1,'S': 0,'T':-1,'W':-4,'Y':-3,'V':-3,'X':0},
  'C':{'A': 0,'R':-3,'N':-3,'D':-3,'C': 9,'Q':-3,'E':-4,'G':-3,'H':-3,'I':-1,
      'L':-1,'K':-3,'M':-1,'F':-2,'P':-3,'S':-1,'T':-1,'W':-2,'Y':-2,'V':-1,'X':0},
  'Q':{'A':-1,'R': 1,'N': 0,'D': 0,'C':-3,'Q': 5,'E': 2,'G':-2,'H': 0,'I':-3,
      'L':-2,'K': 1,'M': 0,'F':-3,'P':-1,'S': 0,'T':-1,'W':-2,'Y':-1,'V':-2,'X':0},
  'E':{'A':-1,'R': 0,'N': 0,'D': 2,'C':-4,'Q': 2,'E': 5,'G':-2,'H': 0,'I':-3,
      'L':-3,'K': 1,'M':-2,'F':-3,'P':-1,'S': 0,'T':-1,'W':-3,'Y':-2,'V':-2,'X':0},
  'G':{'A': 0,'R':-2,'N': 0,'D':-1,'C':-3,'Q':-2,'E':-2,'G': 6,'H':-2,'I':-4,
      'L':-4,'K':-2,'M':-3,'F':-3,'P':-2,'S': 0,'T':-2,'W':-2,'Y':-3,'V':-3,'X':0},
  'H':{'A':-2,'R': 0,'N': 1,'D':-1,'C':-3,'Q': 0,'E': 0,'G':-2,'H': 8,'I':-3,
      'L':-3,'K':-1,'M':-2,'F':-1,'P':-2,'S':-1,'T':-2,'W':-2,'Y': 2,'V':-3,'X':0},
  'I':{'A':-1,'R':-3,'N':-3,'D':-3,'C':-1,'Q':-3,'E':-3,'G':-4,'H':-3,'I': 4,
      'L': 2,'K':-3,'M': 1,'F': 0,'P':-3,'S':-2,'T':-1,'W':-3,'Y':-1,'V': 3,'X':0},
  'L':{'A':-1,'R':-2,'N':-3,'D':-4,'C':-1,'Q':-2,'E':-3,'G':-4,'H':-3,'I': 2,
      'L': 4,'K':-2,'M': 2,'F': 0,'P':-3,'S':-2,'T':-1,'W':-2,'Y':-1,'V': 1,'X':0},
  'K':{'A':-1,'R': 2,'N': 0,'D':-1,'C':-3,'Q': 1,'E': 1,'G':-2,'H':-1,'I':-3,
      'L':-2,'K': 5,'M':-1,'F':-3,'P':-1,'S': 0,'T':-1,'W':-3,'Y':-2,'V':-2,'X':0},
  'M':{'A':-1,'R':-1,'N':-2,'D':-3,'C':-1,'Q': 0,'E':-2,'G':-3,'H':-2,'I': 1,
      'L': 2,'K':-1,'M': 5,'F': 0,'P':-2,'S':-1,'T':-1,'W':-1,'Y':-1,'V': 1,'X':0},
  'F':{'A':-2,'R':-3,'N':-3,'D':-3,'C':-2,'Q':-3,'E':-3,'G':-3,'H':-1,'I': 0,
      'L': 0,'K':-3,'M': 0,'F': 6,'P':-4,'S':-2,'T':-2,'W': 1,'Y': 3,'V':-1,'X':0},
  'P':{'A':-1,'R':-2,'N':-2,'D':-1,'C':-3,'Q':-1,'E':-1,'G':-2,'H':-2,'I':-3,
      'L':-3,'K':-1,'M':-2,'F':-4,'P': 7,'S':-1,'T':-1,'W':-4,'Y':-3,'V':-2,'X':0},
  'S':{'A': 1,'R':-1,'N': 1,'D': 0,'C':-1,'Q': 0,'E': 0,'G': 0,'H':-1,'I':-2,
      'L':-2,'K': 0,'M':-1,'F':-2,'P':-1,'S': 4,'T': 1,'W':-3,'Y':-2,'V':-2,'X':0},
  'T':{'A': 0,'R':-1,'N': 0,'D':-1,'C':-1,'Q':-1,'E':-1,'G':-2,'H':-2,'I':-1,
      'L':-1,'K':-1,'M':-1,'F':-2,'P':-1,'S': 1,'T': 5,'W':-2,'Y':-2,'V': 0,'X':0},
  'W':{'A':-3,'R':-3,'N':-4,'D':-4,'C':-2,'Q':-2,'E':-3,'G':-2,'H':-2,'I':-3,
      'L':-2,'K':-3,'M':-1,'F': 1,'P':-4,'S':-3,'T':-2,'W':11,'Y': 2,'V':-3,'X':0},
  'Y':{'A':-2,'R':-2,'N':-2,'D':-3,'C':-2,'Q':-1,'E':-2,'G':-3,'H': 2,'I':-1,
      'L':-1,'K':-2,'M':-1,'F': 3,'P':-3,'S':-2,'T':-2,'W': 2,'Y': 7,'V':-1,'X':0},
  'V':{'A': 0,'R':-3,'N':-3,'D':-3,'C':-1,'Q':-2,'E':-2,'G':-3,'H':-3,'I': 3,
      'L': 1,'K':-2,'M': 1,'F':-1,'P':-2,'S':-2,'T': 0,'W':-3,'Y':-1,'V': 4,'X':0},
  'X':{'A': 0,'R': 0,'N': 0,'D': 0,'C': 0,'Q': 0,'E': 0,'G': 0,'H': 0,'I': 0,
      'L': 0,'K': 0,'M': 0,'F': 0,'P': 0,'S': 0,'T': 0,'W': 0,'Y': 0,'V': 0,'X':0}}

  return BLOSUM62

def LocalAlignment(seq1,seq2,sequencetype,GapOpenPenalty = 3,Verbose = 0):

  if sequencetype == 'protein':
    ScoreDictionary = BLOSUM62_scores()
  elif sequencetype == 'RNA':
    ScoreDictionary = RNA_scores()
  else:
    ScoreDictionary = DNA_scores()

  s1 = '*' + seq1;
  s2 = '&' + seq2;
  
  m = len(s1)
  n = len(s2)
  
  Score = zeros((m,n))
  BackArrow = zeros((m,n))
  MaxScore = -1
  
  for i in range(0,m):
    for j in range(0,n):
      if i == 0:
        BackArrow[i,j] = 2
        Score[i,j] = 0
      if j == 0:
        BackArrow[i,j] = 1
        Score[i,j] = 0
      if i > 0 and j > 0:
        BackArrow[i,j] = 1
        Score[i,j] = Score[i-1,j] - GapOpenPenalty
        if Score[i,j-1] - GapOpenPenalty > Score[i,j]:
          BackArrow[i,j] = 2
          Score[i,j] = Score[i,j-1] - GapOpenPenalty
        b = ScoreDictionary[s1[i]][s2[j]]
        if Score[i-1,j-1] + b > Score[i,j]:
          BackArrow[i,j] = 3
          Score[i,j] = Score[i-1,j-1] + b
      if Score[i,j] < 0:
        BackArrow[i,j] = 4
        Score[i,j] = 0
      if Score[i,j] > MaxScore:
        MaxScore = Score[i,j]
        imax = i
        jmax = j        

  if Verbose > 0:
    
    # --------------------- Display the dynamic programming matrices
    
    print Score
    print 
    print BackArrow
    print 
    print "MaxScore-", MaxScore, "imax=", imax, "jmax=", jmax
  
  # This part is called the traceback, following the back arrows to produce
  # the optimal alignment itself
  
  i = len(s1)-1
  j = len(s2)-1
  matches = 0
  a1 = ''
  a2 = ''
  p1 = []
  p2 = []

  if imax < i:
    a1 = s1[(imax+1):len(s1)] + a1
    a2 = '-'*(len(s1)-imax-1) + a2
    i = imax
  
  if jmax < j:
    a1 = '-'*(len(s2)-jmax-1) + a1
    a2 = s2[(jmax+1):len(s2)] + a2
    j = jmax
    
  while i > 0 or j > 0:
    if BackArrow[i,j] == 1:
      a1 = s1[i] + a1
      a2 = '-' + a2
      i = i - 1
    elif BackArrow[i,j] == 2:
      a1 = '-' + a1
      a2 = s2[j] + a2
      j = j - 1
    elif BackArrow[i,j] == 3:
      a1 = s1[i] + a1
      a2 = s2[j] + a2
      p1 = [i] + p1
      p2 = [j] + p2
      i = i - 1
      j = j - 1
      matches += 1
    elif BackArrow[i,j] == 4:
      a1 = s1[1:(i+1)] + a1
      a2 = '-' * i + a2
      a1 = '-' * j + a1
      a2 = s2[1:(j+1)] + a2
      i = 0
      j = 0

  if Verbose > 0:  
    # -------------------- Tests to spot obvious bad alignments
    
    a1test = a1.replace('-','')
    a2test = a2.replace('-','')
    
    if a1test == seq1:
      print "String 1 is correctly reproduced"
    else:
      print "********** String 1 is not correctly reproduced"
    
    if a2test == seq2:
      print "String 2 is correctly reproduced"
    else:
      print "********** String 2 is not correctly reproduced"
    
    if len(a1) == len(a2):
      print "Alignment strings have the same length"
    else:
      print "********** Alignment strings do not have the same length"
  
  # -------------------- Display the output on the screen
  
  if Verbose > 0:
    t = ''
    n = ''
    for i in range(1,max(len(s1),len(s2))):
      t = t + str((i/10)%10)
      n = n + str(i%10)
    print t
    print n
    print seq1
    print seq2
    print a1
    print a2
    print p1
    print p2
    print int(matches)
  
  # ------------------- Return alignment information to the calling program
  
  return matches, MaxScore, a1, a2, p1, p2