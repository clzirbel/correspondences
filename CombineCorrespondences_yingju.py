# INPUT:   correspondences1:  A dictionary of correspondences between A and B
#          header1:  Header string for first correspondences
#          correspondences2:  A dictionary of correspondences between B and C
#          header2:  Header string for second correspondences
# OUTPUT:  correspondences:  A dictionary of inferred correspondences between A and C
#          header:  A new header line saying that these are inferred correspondences,
#          then the lines from header1, then a blank header line, then the 
#          lines from header2
#          extra:  A dictionary of correspondences in correspondences1 for which
#          there is no further correspondence in correspondences2
# AUTHOR:  

def CombineCorrespondences(correspondences1,header1,correspondences2,header2):

  correspondences = {}                            # empty dictionary
  header = []                                     # empty list for headers
  extra = {}                                      # empty dictionary for extras

  for key, value in correspondences1.iteritems():
    if value in correspondences2:
      correspondences[key] = correspondences2[value]
    else:
      extra[key] = value
    
  header.append("# these are inferred correspondences")
  header.append(header1)
  header.append('# \n')
  header.append(header2)
  

  return correspondences, header, extra 
