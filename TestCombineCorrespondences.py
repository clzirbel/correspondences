# TestCombineCorrespondences reads two correspondences and combines them

from ReadCorrespondences import ReadCorrespondences
from CombineCorrespondences import CombineCorrespondences
# from WriteCorrespondences import WriteCorrespondences

# -------- First test:  read correspondences both ways, combine, which should
# -------- result in nucleotides from 2QBD being aligned to themselves

correspondences1, header1, error1 = ReadCorrespondences('2QBD_3I8H_correspondences.txt',0)
correspondences2, header2, error2 = ReadCorrespondences('2QBD_3I8H_correspondences.txt',1)

correspondences, header = CombineCorrespondences(correspondences1,header1,correspondences2,header2)

print correspondences

print header

# --------- Once write correspondences is written, use it to write to file:

# WriteCorrespondences('TestCombineCorrespondences_output.txt',correspondences,header,"maps_to")
