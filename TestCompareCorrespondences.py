# TestCompareCorrespondences reads two correspondences and compares them

from ReadCorrespondences import ReadCorrespondences

# -------- First test:  read two correspondences and compare

correspondences1, header1, error1 = ReadCorrespondences('2QBD_3I8H_correspondences.txt',0)
correspondences2, header2, error2 = ReadCorrespondences('2QBD_3I8H_correspondences_514313b142ec5.txt',0)

identical, in1not2, in2not1 = CompareCorrespondences(correspondences1,header1,correspondences2,header2)

print identical

print in1not2

print in2not2

# --------- Once write correspondences is written, use it to write to file:

WriteCorrespondences('TestCompareCorrespondences_output_1.tmp',identical,['# identical'],"maps_to")
WriteCorrespondences('TestCompareCorrespondences_output_1.tmp',in1not2,['# in 1 not 2'],"maps_to")
WriteCorrespondences('TestCompareCorrespondences_output_1.tmp',in2not1,['# in 2 not 1'],"maps_to")
