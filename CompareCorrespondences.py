# INPUT:   correspondences1:  A dictionary of correspondences between A and B
#          header1:  Header string for first correspondences
#          correspondences2:  A dictionary of correspondences between A and B
#          header2:  Header string for second correspondences
# OUTPUT:  identical:  A dictionary of correspondences that are identical
#          in1not2:  A dictionary of correspondences that are in 1 but not in 2
#          in2not1:  A dictionary of correspondences that are in 2 but not in 1
# AUTHOR:  

def CompareCorrespondences(correspondences1,header1,correspondences2,header2):

  identical = {}                            # empty dictionary
  in1not2 = {}                              # empty dictionary
  in2not1 = {}                              # empty dictionary

  # first, iterate through all key, value pairs in correspondences1.  
  # If the same key, value pair is in correspondences2, add this correspondence
  # to identical.  If not, add it to in1not2. 

  for key, value in correspondences1.iteritems():
    if key in correspondences2:
      if value==correspondences2[key]:
        identical[key]= value
    else:
      in1not2[key] = value
    
  for key, value in correspondences2.iteritems():
    if key in correspondences1:
      if value!=correspondences1[key]:
        in2not1[key] = value
    else:
      in2not1[key] = value     
      
    

  # next, iterate through all key, value pairs in correspondences2.
  # Only look for ones that are not in correspondences1, and add them to
  # in2not1

  return identical, in1not2, in2not1

