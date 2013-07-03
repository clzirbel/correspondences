#!/usr/bin/env python

import sys

from csv import DictReader
from urllib2 import urlopen


def load_interactions(pdb):
    url = 'http://rna.bgsu.edu/rna3dhub_dev/pdb/%s/interactions/fr3d/basepairs/csv'
    response = urlopen(url % pdb)
    # Using DictReader lets us get a dictonary after parsing the csv. We have
    # to define the fieldnames because there is no header line in the given csv
    # string.
    #
    # We could also use the csv.reader function and just get an array, but I
    # think it is clearer to use a dictonary to store data.
    reader = DictReader(response, fieldnames=['nt1', 'family', 'nt2'])
    return [row for row in reader]


def main(pdb):
    print(load_interactions(pdb))


if __name__ == '__main__':
    main(sys.argv[1])
