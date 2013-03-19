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
# AUTHOR:  Jacob Newminster,Richard Nyonyi,Joyce Giciro



def CombineCorrespondences(correspondences1,header1,correspondences2,header2):

  correspondences = {}                            # empty dictionary
  header = []                                     # empty list for headers
  extra = {}                                      # empty dictionary for extras
  
  
  
#Creating the new header line
  header.append('These are inferred correspondences')     
  header.append(header1)
  header.append(' ')
  header.append(header2)

  
  for key, value in correspondences1.iteritems():	#Iterating through the correspondences dictionary
   
    A = key										    # Obtaining the left(A) value
    B = value										# Obtaining the Right(B) value

    if correspondences2.has_key(value):				# Checking if there is a correspondence in C
      C = correspondences2[value]					# Getting the correspondence from C
      correspondences[A] = C						# Assigning the correspondence in the new correspondence dictionary
    
    else:
      extra[A] = B								    # Assigning the non-corresponding to the extra dictionary	
    
  return correspondences, header ,extra				#Returning results.

