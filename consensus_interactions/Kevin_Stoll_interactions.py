import csv
import re
from importingcsv import incomescsv
from ReadCorrespondences import ReadCorrespondences
import os
import urllib2

# could use incomecsv instead
out=open("4HUB_fr3d_basepairs.csv","r")
data=csv.reader(out)
data=[row for row in data]
out.close()

#Following creates Dictionary of base pair Interactions in 4HUB.
m=len(data)
dk=''                   # never used
interactions = {}       #Empty Dictionary t
extra={}                #Empty Dictionary intended to later help get to input interactions dictionary
for i in range(0,m):
        interactions[data[i][0]+' '+ data[i][2]]=data[i][1] #now a dictionary mapping two interacting nucleuotides with interaction type/shape
        #extra[data[i][0]]=data[i][0]+' '+ data[i][2] #Dictionary mapping each element to the 'two interacting nucleuotides interaction'; however, items get overwritten.  

#Following loads 1S72 base pair interactions
filename = '1S72_fr3d_basepairs.csv'

filenames = os.listdir('.')

tabs = ""

filelist = "4HUB"

for filename in filenames:
    if ("alignment" in filename) and ("4HUB" in filename):

        print "Reading ", filename

        #Following reads correspondences between 4HUB and 1S72 via dictionary.  Problem if this not one-to-one function, so there is overwrite
        correspondences1, header1, error1 = ReadCorrespondences(filename,1)

        PDBID = filename[5:9]

        filelist += '\t' + PDBID

        print "Retrieving basepairs from ",PDBID

        urlstring = 'http://rna.bgsu.edu/rna3dhub/pdb/' + PDBID + '/interactions/fr3d/basepairs/csv'
        response = urllib2.urlopen(urlstring)
        data2=csv.reader(response)
        data2=[row for row in data2]

        tabs += "\t"

        for key in interactions:
            interactions[key] = interactions[key] + '\t'

        #Looping through new interactions
        n=len(data2)
        for i in range(0,n):
            if data2[i][0] in correspondences1 and data2[i][2] in correspondences1:  #If both of interacting 1S72 nucleutides are in correspondence of 1S72 to 4HUB
                seq=correspondences1[data2[i][0]]+' '+correspondences1[data2[i][2]]
                if seq in interactions:
                    interactions[seq] += data2[i][1]
                else:
                    interactions[seq] = tabs + data2[i][1]

        
#print correspondences2
#print data2
#print interactions
for key in interactions:
    print key, interactions[key]


# Write this out to a text file, putting filelist at the top as a header
# Look at the text file with Excel, maybe, to get an idea what is going on
# Do some statistics on the interactions ...
for key in interactions:
    ilist = interactions[key].split('\t')
    # run through this list to see what agreement there is; 
    d = {}
    for x in ilist:
        if x in d:
            d[x] = d[x] + 1
        else:
            d[x] = 1

    # how often is there total conservation, no "near" pairs?







#print interactions['4HUB|1|0|U|22 4HUB|1|0|A|521']





#interactions2={}
#for i in range (0,n):
                                         #correspondences2[data2[i][0]]    #gives element in 4hub that corresponds to the member in 1S72
                                         #extra[correspondences2[data2[i][0]]] #gives input of interactions
    #    if correspondences2[data2[i][0]] in extra:  #and if the element in 4hub that corresponds to the member in 1S72 is in the Dictionary mapping each element to the 'two interacting nucleuotides interaction'; however, items get overwritten.  
    #        interactions[extra[correspondences2[data2[i][0]]]]+= ' ' + data[i][1]
            #interactions2[extra[correspondences2[data2[i][0]]]]= interactions[extra[correspondences2[data2[i][0]]]]+'   ' + data[i][1]

