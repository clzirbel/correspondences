import csv
import re
from importingcsv import incomescsv
import os
import urllib2

filenames = os.listdir('.')

for filename in filenames:
    if ("alignment" in filename):
        PDBID = filename[5:9]

        print "Retrieving basepairs from ",PDBID

        urlstring = 'http://rna.bgsu.edu/rna3dhub/pdb/' + PDBID + '/interactions/fr3d/basepairs/csv'
        response = urllib2.urlopen(urlstring)
        data=csv.reader(response)
        data=[row for row in data]

#        data = response.read()

        print data

