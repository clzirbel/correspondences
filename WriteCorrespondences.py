# INPUT:   filename of text file of correspondences to be written
#          correspondences:  A dictionary of correspondences
#          header:  A list of strings from the file that start with #
#          separator:  A string to put in between corresponding units,
#          default separator is "corresponds_to"
# OUTPUT:  a text file on the disk with header lines followed by correspondence lines
# AUTHOR:  

def WriteCorrespondences(filename,correspondences,header,separator="corresponds_to", verbose=False):
	# Open the file for writing
	fp = open(filename, "w")	
	
	# Write each line from the header
	for headLine in header:
		fp.write(headLine)
	
	# Write each correspondance to a file
	for key, value in correspondences.iteritems():
		fp.write(key + "\t" + separator + "\t" + value + "\n")
	
	if (verbose):
		print "Wrote " + str(len(correspondences)) + " correspondences to " + filename
	
	# Close the file	
	fp.close()
	
	# Return without an error
	return True
	


