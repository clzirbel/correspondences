# TestStructureToSequenceAlignment tests code to convert range strings to lists of lists of integers

from StructureToSequenceAlignment import ConvertIDRangeString
from ReadCorrespondences import ReadCorrespondences

correspondences, header, error = ReadCorrespondences("2QBD_GG16S2012_correspondences.txt")

ranges = ConvertIDRangeString(correspondences,"2QBD|1|A|A|10,2QBD|1|A|G|11:2QBD|1|A|U|14,,2QBD|1|A|U|17")

print ranges