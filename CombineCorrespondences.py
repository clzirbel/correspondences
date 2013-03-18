# INPUT:   correspondences1:  A dictionary of correspondences between A and B
#          header1:  Header string for first correspondences
#          correspondences2:  A dictionary of correspondences between B and C
#          header2:  Header string for second correspondences
# OUTPUT:  correspondences:  A dictionary of inferred correspondences between A and C
#          header:  A new header line saying that these are inferred correspondences,
#          then the lines from header1, then a blank header line, then the 
#          lines from header2
# NOTES:   If a value in correspondences1 has no key in correspondences2, skip it
# AUTHOR:  

def CombineCorrespondences(correspondences1,header1,correspondences2,header2):

  return correspondences, header