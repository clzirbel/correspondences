# INPUT:   filename of text file of correspondences to be written
#          correspondences:  A dictionary of correspondences
#          header:  A list of strings from the file that start with #
#          separator:  A string to put in between corresponding units,
#          default separator is "corresponds_to"
# OUTPUT:  a text file on the disk with header lines followed by correspondence lines
# AUTHOR:  

def WriteCorrespondences(filename,correspondences,header,separator="corresponds_to"):

    g = open(filename,'w')
    
    for index in range(0,len(header)):
        g.write(header[index])
    
    for key, value in correspondences.iteritems():
        g.write('%-20s %-15s %s \n' % (key, separator, value))    
        g.write('\n')

    g.close()
    
