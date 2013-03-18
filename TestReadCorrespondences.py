# TestReadCorrespondences

from ReadCorrespondences import ReadCorrespondences

correspondences, header, error = ReadCorrespondences('2QBD_3I8H_correspondences.txt',0)

print header

print correspondences['2QBD|1|A|A|19']

print error

correspondences, header, error = ReadCorrespondences('2QBD_3I8H_correspondences.txt',1)

print header

print correspondences['3I8H|1|A|C|19']

print error

