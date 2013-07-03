import csv
import re

out=open("4HUB_fr3d_basepairs.csv","rb")
data=csv.reader(out)
data=[row for row in data]
out.close()

#Following creates Dictionary of base pair Interactions in 4HUB.
m=len(data)
dk=''
interactions = {}       #Empty Dictionary t
extra={}                #Empty Dictionary intended to later help get to input interactions dictionary
for i in range(0,m):
        interactions[data[i][0]+' '+ data[i][2]]=data[i][1] #now a dictionary mapping two interacting nucleuotides with interaction type/shape
        #extra[data[i][0]]=data[i][0]+' '+ data[i][2] #Dictionary mapping each element to the 'two interacting nucleuotides interaction'; however, items get overwritten.  

#Following loads 1S72 base pair interactions
from importingcsv import incomescsv
data2=incomescsv('1S72_fr3d_basepairs.csv')

#Following reads correspondences between 4HUB and 1S72 via dictionary.  Problem if this not one-to-one function, so there is overwrite
from ReadCorrespondences import ReadCorrespondences
correspondences1, header1, error1 = ReadCorrespondences('4HUB-1S72-alignment.txt',0)

#Reverse dictionary 1S72 to 4hub...Problem if this not one-to-one function, so there is overwrite
correspondences2={}
for key in correspondences1:
    correspondences2[correspondences1[key]]=key

#Looping through 1S72 interactions
n=len(data2)
for i in range(0,n):
    if data2[i][0] in correspondences2 and data2[i][2] in correspondences2:  #If both of interacting 1S72 nucleutides are in correspondence of 1S72 to 4HUB
        seq=''
        seq=correspondences2[data2[i][0]]+' '+correspondences2[data2[i][2]]
        if seq in interactions:
                interactions[seq]+= ' ' + data2[i][1]
        
#print correspondences2
#print data2
#print interactions
for key in interactions:
    print key, interactions[key]

#print interactions['4HUB|1|0|U|22 4HUB|1|0|A|521']





#interactions2={}
#for i in range (0,n):
                                         #correspondences2[data2[i][0]]    #gives element in 4hub that corresponds to the member in 1S72
                                         #extra[correspondences2[data2[i][0]]] #gives input of interactions
    #    if correspondences2[data2[i][0]] in extra:  #and if the element in 4hub that corresponds to the member in 1S72 is in the Dictionary mapping each element to the 'two interacting nucleuotides interaction'; however, items get overwritten.  
    #        interactions[extra[correspondences2[data2[i][0]]]]+= ' ' + data[i][1]
            #interactions2[extra[correspondences2[data2[i][0]]]]= interactions[extra[correspondences2[data2[i][0]]]]+'   ' + data[i][1]

