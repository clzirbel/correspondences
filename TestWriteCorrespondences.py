# TestWriteCorrespondences reads a file of correspondences and displays some information

from ReadCorrespondences import ReadCorrespondences
from WriteCorrespondences import WriteCorrespondences

correspondences, header, error = ReadCorrespondences('2QBD_3I8H_correspondences.txt',0)

print header

print correspondences['2QBD|1|A|A|19']

print error

WriteCorrespondences('Test_output.txt',correspondences,header,"maps_to")
