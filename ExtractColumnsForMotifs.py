# UseRetrieveColumnsFromAlignment 

from ReadCorrespondences import ReadCorrespondences
from StructureToSequenceAlignment import ConvertIDRangeString
from RetrieveColumnsFromAlignment import RetrieveColumnsFromAlignment
from MakeFASTAFilesForMotifs import MakeFASTAFilesForMotifs

import os

if os.getcwd().find('zirbel') > 0:              # identify the user
  AlignmentPath = "C:\\Users\\zirbel\\Documents\\My Dropbox\\Alignments"
  GreenGenesPath = "C:\\Users\\zirbel\\Documents\\Alignments"
  MotifPath = "C:\\Users\\zirbel\\Documents\\My Dropbox\\BGSURNA\\Motifs\\lib\\Variants_from_alignments\\IL\\1.0"
  CorrespondencePath = "C:\\Users\\zirbel\\Documents\\My Dropbox\\Alignments"

f = open(MotifPath + os.sep + "Motif_ranges.txt",'r')  # open motif ranges for reading

for line in f:
  t = line.replace("\n","").split("\t")                     # tab delimited
  PDBID = t[0]
  correspondencefile = CorrespondencePath + os.sep + t[1]
  if t[2].find("GG16S") > -1:
    alignmentfile = GreenGenesPath + os.sep + t[2]
  else:
    alignmentfile = AlignmentPath + os.sep + t[2]
  MSAID = t[3]
  rangestring = t[4]
  motifstring = t[5]
  extractfile = GreenGenesPath + os.sep + PDBID + "_" + MSAID + ".tmp"

  print "Working with",PDBID,"and alignment",MSAID    
  print "Reading correspondences between PDB file and alignment columns"
  correspondences, header, error = ReadCorrespondences(correspondencefile)

  print "Converting nucleotide ranges to columns"
  ranges = ConvertIDRangeString(correspondences,rangestring)
  
  print "Retrieving columns from the alignment, writing to an extract file"
  RetrieveColumnsFromAlignment(ranges,alignmentfile,extractfile)
  
  print "Reading extract file, writing FASTA files for motifs"
  MakeFASTAFilesForMotifs(motifstring,extractfile,MSAID,PDBID,MotifPath)
  print
  
if 1 > 10:
  PDBID = "2QBG"
  # Matlab:  [rangestring,motifstring] = pRangeStringForMotifsFromStructure('2QBG',MotifRelease)
  rangestring = "2QBG|1|B|U|293:2QBG|1|B|G|295,2QBG|1|B|C|343:2QBG|1|B|A|347,2QBG|1|B|G|481:2QBG|1|B|C|484,2QBG|1|B|G|496:2QBG|1|B|C|509,2QBG|1|B|A|2054:2QBG|1|B|G|2056,2QBG|1|B|C|2612:2QBG|1|B|U|2615,2QBG|1|B|G|858:2QBG|1|B|G|862,2QBG|1|B|C|915:2QBG|1|B|U|919,2QBG|1|B|G|697:2QBG|1|B|C|698,2QBG|1|B|G|763:2QBG|1|B|C|765,2QBG|1|B|C|2512:2QBG|1|B|A|2513,2QBG|1|B|U|2571:2QBG|1|B|G|2574,2QBG|1|B|G|2843:2QBG|1|B|G|2846,2QBG|1|B|C|2870:2QBG|1|B|C|2874,2QBG|1|B|A|2317:2QBG|1|B|U|2321,2QBG|1|B|A|2297:2QBG|1|B|U|2299,2QBG|1|B|G|775:2QBG|1|B|G|777,2QBG|1|B|C|787:2QBG|1|B|C|791,2QBG|1|B|C|2350:2QBG|1|B|G|2353,2QBG|1|B|C|2364:2QBG|1|B|G|2367,2QBG|1|B|G|536:2QBG|1|B|G|539,2QBG|1|B|U|554:2QBG|1|B|C|557,2QBG|1|B|U|2081:2QBG|1|B|G|2083,2QBG|1|B|U|2236:2QBG|1|B|G|2239,2QBG|1|B|C|1526:2QBG|1|B|G|1529,2QBG|1|B|U|1542:2QBG|1|B|G|1546,2QBG|1|B|U|1864:2QBG|1|B|G|1867,2QBG|1|B|C|1874:2QBG|1|B|G|1878,2QBG|1|A|G|23:2QBG|1|A|C|28,2QBG|1|A|G|56:2QBG|1|A|C|60,2QBG|1|B|U|1004:2QBG|1|B|G|1011,2QBG|1|B|C|1150:2QBG|1|B|A|1151,2QBG|1|B|C|1357:2QBG|1|B|G|1361,2QBG|1|B|C|1370:2QBG|1|B|G|1374,2QBG|1|B|U|1513:2QBG|1|B|G|1517,2QBG|1|B|U|1474:2QBG|1|B|G|1478,2QBG|1|A|C|71:2QBG|1|A|G|79,2QBG|1|A|C|97:2QBG|1|A|G|105,2QBG|1|B|U|913:2QBG|1|B|C|915,2QBG|1|B|G|862:2QBG|1|B|A|863,2QBG|1|B|C|2652:2QBG|1|B|C|2658,2QBG|1|B|G|2663:2QBG|1|B|G|2668,2QBG|1|B|C|1043:2QBG|1|B|G|1051,2QBG|1|B|U|1108:2QBG|1|B|G|1112,2QBG|1|B|U|1415:2QBG|1|B|G|1416,2QBG|1|B|C|1582:2QBG|1|B|G|1587,2QBG|1|B|U|1018:2QBG|1|B|G|1024,2QBG|1|B|C|1140:2QBG|1|B|A|1144,2QBG|1|B|G|2454:2QBG|1|B|G|2455,2QBG|1|B|C|2496:2QBG|1|B|C|2498,2QBG|1|B|U|2617:2QBG|1|B|G|2618,2QBG|1|B|C|2050:2QBG|1|B|A|2052,2QBG|1|B|G|757:2QBG|1|B|C|758,2QBG|1|B|G|738:2QBG|1|B|C|740,2QBG|1|B|U|1101:2QBG|1|B|C|1102,2QBG|1|B|G|1087:2QBG|1|B|A|1090,2QBG|1|B|U|1993:2QBG|1|B|C|1994,2QBG|1|B|G|1666:2QBG|1|B|A|1669,2QBG|1|B|A|1603:2QBG|1|B|C|1604,2QBG|1|B|G|1310:2QBG|1|B|U|1313,2QBG|1|A|C|17:2QBG|1|A|G|18,2QBG|1|A|U|65:2QBG|1|A|G|67,2QBG|1|B|U|2493:2QBG|1|B|G|2494,2QBG|1|B|U|2457:2QBG|1|B|A|2459,2QBG|1|B|C|2507:2QBG|1|B|G|2508,2QBG|1|B|U|2580:2QBG|1|B|G|2582,2QBG|1|B|C|1196:2QBG|1|B|U|1198,2QBG|1|B|A|1247:2QBG|1|B|G|1250,2QBG|1|B|A|2459:2QBG|1|B|A|2461,2QBG|1|B|U|2489:2QBG|1|B|U|2493,2QBG|1|B|U|2687:2QBG|1|B|C|2691,2QBG|1|B|G|2718:2QBG|1|B|G|2722,2QBG|1|B|C|1114:2QBG|1|B|C|1117,2QBG|1|B|G|1038:2QBG|1|B|G|1041,2QBG|1|B|G|24:2QBG|1|B|G|30,2QBG|1|B|C|510:2QBG|1|B|C|516,2QBG|1|B|U|434:2QBG|1|B|C|436,2QBG|1|B|G|43:2QBG|1|B|A|44,2QBG|1|B|U|2438:2QBG|1|B|U|2441,2QBG|1|B|A|2070:2QBG|1|B|A|2071,2QBG|1|B|G|1651:2QBG|1|B|C|1656,2QBG|1|B|G|2004:2QBG|1|B|C|2006,2QBG|1|B|U|2522:2QBG|1|B|G|2523,2QBG|1|B|C|2540:2QBG|1|B|G|2543,2QBG|1|B|C|806:2QBG|1|B|G|808,2QBG|1|B|C|672:2QBG|1|B|G|674,2QBG|1|B|A|575:2QBG|1|B|G|577,2QBG|1|B|C|564:2QBG|1|B|U|566,2QBG|1|B|G|856:2QBG|1|B|G|858,2QBG|1|B|U|919:2QBG|1|B|C|921,2QBG|1|B|A|905:2QBG|1|B|G|907,2QBG|1|B|U|870:2QBG|1|B|U|872,2QBG|1|B|C|2232:2QBG|1|B|G|2234,2QBG|1|B|U|2085:2QBG|1|B|G|2087,2QBG|1|B|G|2574:2QBG|1|B|G|2578,2QBG|1|B|C|2510:2QBG|1|B|C|2512,2QBG|1|B|C|2179:2QBG|1|B|U|2181,2QBG|1|B|A|2108:2QBG|1|B|G|2110,2QBG|1|B|C|1990:2QBG|1|B|U|1993,2QBG|1|B|A|1669:2QBG|1|B|G|1674,2QBG|1|B|C|1557:2QBG|1|B|C|1561,2QBG|1|B|G|1432:2QBG|1|B|G|1435,2QBG|1|B|C|239:2QBG|1|B|G|245,2QBG|1|B|C|253:2QBG|1|B|G|258,2QBG|1|B|C|2806:2QBG|1|B|G|2811,2QBG|1|B|C|2889:2QBG|1|B|G|2892,2QBG|1|B|A|844:2QBG|1|B|C|848,2QBG|1|B|G|930:2QBG|1|B|U|934,2QBG|1|B|G|674:2QBG|1|B|C|678,2QBG|1|B|G|799:2QBG|1|B|C|806,2QBG|1|B|C|274:2QBG|1|B|C|281,2QBG|1|B|G|359:2QBG|1|B|G|363,2QBG|1|B|C|1437:2QBG|1|B|U|1440,2QBG|1|B|A|1551:2QBG|1|B|G|1555,2QBG|1|B|G|212:2QBG|1|B|G|214,2QBG|1|B|C|183:2QBG|1|B|C|184,2QBG|1|B|G|940:2QBG|1|B|G|942,2QBG|1|B|C|837:2QBG|1|B|C|838,2QBG|1|B|C|2498:2QBG|1|B|U|2500,2QBG|1|B|A|2453:2QBG|1|B|G|2454,2QBG|1|B|G|926:2QBG|1|B|A|928,2QBG|1|B|U|850:2QBG|1|B|C|851,2QBG|1|B|A|2184:2QBG|1|B|G|2186,2QBG|1|B|C|2103:2QBG|1|B|U|2105,2QBG|1|B|U|1520:2QBG|1|B|G|1524,2QBG|1|B|U|1468:2QBG|1|B|G|1471,2QBG|1|B|G|1202:2QBG|1|B|G|1206,2QBG|1|B|U|1240:2QBG|1|B|C|1243,2QBG|1|B|U|1234:2QBG|1|B|G|1238,2QBG|1|B|C|1208:2QBG|1|B|G|1215,2QBG|1|A|A|34:2QBG|1|A|C|38,2QBG|1|A|G|44:2QBG|1|A|U|48,2QBG|1|B|C|1686:2QBG|1|B|C|1691,2QBG|1|B|G|1696:2QBG|1|B|G|1702,2QBG|1|A|C|30:2QBG|1|A|C|31,2QBG|1|A|G|51:2QBG|1|A|G|54,2QBG|1|B|U|2680:2QBG|1|B|U|2684,2QBG|1|B|A|2725:2QBG|1|B|A|2727,2QBG|1|B|G|864:2QBG|1|B|U|868,2QBG|1|B|A|909:2QBG|1|B|C|912,2QBG|1|B|C|1319:2QBG|1|B|C|1323,2QBG|1|B|G|1331:2QBG|1|B|G|1333,2QBG|1|B|U|2847:2QBG|1|B|G|2852,2QBG|1|B|U|2865:2QBG|1|B|G|2869,2QBG|1|B|C|2636:2QBG|1|B|G|2640,2QBG|1|B|C|2774:2QBG|1|B|G|2782,2QBG|1|B|U|1481:2QBG|1|B|G|1482,2QBG|1|B|C|1507:2QBG|1|B|G|1510,2QBG|1|B|C|201:2QBG|1|B|C|208,2QBG|1|B|G|188:2QBG|1|B|G|194,2QBG|1|B|A|1262:2QBG|1|B|A|1269,2QBG|1|B|U|2011:2QBG|1|B|U|2017,2QBG|1|B|G|1663:2QBG|1|B|A|1665,2QBG|1|B|U|1995:2QBG|1|B|C|1997,2QBG|1|B|U|1742:2QBG|1|B|A|1746,2QBG|1|B|U|1712:2QBG|1|B|G|1718,2QBG|1|B|U|1720:2QBG|1|B|G|1724,2QBG|1|B|U|1736:2QBG|1|B|G|1740,2QBG|1|B|U|703:2QBG|1|B|G|707,2QBG|1|B|U|724:2QBG|1|B|G|728,2QBG|1|B|C|2480:2QBG|1|B|G|2484,2QBG|1|B|C|2466:2QBG|1|B|G|2470,2QBG|1|B|U|606:2QBG|1|B|C|610,2QBG|1|B|G|618:2QBG|1|B|G|622,2QBG|1|B|C|1934:2QBG|1|B|G|1945,2QBG|1|B|C|1961:2QBG|1|B|G|1964,2QBG|1|B|G|81:2QBG|1|B|G|85,2QBG|1|B|C|97:2QBG|1|B|C|105,2QBG|1|B|G|1031:2QBG|1|B|G|1034,2QBG|1|B|C|1121:2QBG|1|B|C|1123,2QBG|1|B|C|1499:2QBG|1|B|G|1500,2QBG|1|B|C|1489:2QBG|1|B|G|1491,2QBG|1|B|U|2220:2QBG|1|B|G|2221,2QBG|1|B|U|2202:2QBG|1|B|G|2204,2QBG|1|B|C|1893:2QBG|1|B|C|1894,2QBG|1|B|G|1846:2QBG|1|B|G|1849,2QBG|1|B|C|1417:2QBG|1|B|G|1421,2QBG|1|B|C|1577:2QBG|1|B|G|1581,2QBG|1|B|C|1376:2QBG|1|B|G|1380,2QBG|1|B|C|1351:2QBG|1|B|G|1355,2QBG|1|B|C|1153:2QBG|1|B|G|1157,2QBG|1|B|C|998:2QBG|1|B|G|1002,2QBG|1|B|C|1837:2QBG|1|B|G|1840,2QBG|1|B|C|1902:2QBG|1|B|G|1903,2QBG|1|B|G|2737:2QBG|1|B|G|2742,2QBG|1|B|C|2762:2QBG|1|B|C|2767,2QBG|1|B|G|36:2QBG|1|B|C|37,2QBG|1|B|G|442:2QBG|1|B|C|444,2QBG|1|B|C|2591:2QBG|1|B|G|2592,2QBG|1|B|C|2601:2QBG|1|B|G|2603,2QBG|1|B|U|1159:2QBG|1|B|G|1160,2QBG|1|B|C|994:2QBG|1|B|A|996,2QBG|1|B|G|1933:2QBG|1|B|C|1934,2QBG|1|B|G|1964:2QBG|1|B|C|1967,2QBG|1|B|C|2442:2QBG|1|B|C|2443,2QBG|1|B|G|2067:2QBG|1|B|G|2069,2QBG|1|B|C|1727:2QBG|1|B|C|1728,2QBG|1|B|G|1731:2QBG|1|B|G|1733,2QBG|1|B|G|2414:2QBG|1|B|G|2415,2QBG|1|B|U|2401:2QBG|1|B|C|2403,2QBG|1|B|U|702:2QBG|1|B|U|703,2QBG|1|B|G|728:2QBG|1|B|A|730,2QBG|1|B|U|1841:2QBG|1|B|G|1842,2QBG|1|B|U|1898:2QBG|1|B|A|1901,2QBG|1|B|G|1770:2QBG|1|B|C|1771,2QBG|1|B|G|1980:2QBG|1|B|U|1982,2QBG|1|B|U|2695:2QBG|1|B|U|2696,2QBG|1|B|A|2711:2QBG|1|B|G|2714,2QBG|1|B|G|2838:2QBG|1|B|G|2839,2QBG|1|B|U|2878:2QBG|1|B|C|2880,2QBG|1|B|G|1149:2QBG|1|B|C|1150,2QBG|1|B|G|1011:2QBG|1|B|C|1013,2QBG|1|B|G|1059:2QBG|1|B|G|1062,2QBG|1|B|C|1076:2QBG|1|B|C|1079,2QBG|1|B|C|269:2QBG|1|B|G|271,2QBG|1|B|C|366:2QBG|1|B|G|370,2QBG|1|B|U|1798:2QBG|1|B|C|1804,2QBG|1|B|G|1813:2QBG|1|B|A|1821"
  motifstring = "IL_00998.1 IL_2QBG_015,IL_00998.1 IL_2QBG_015,IL_02359.2 IL_2QBG_016,IL_02359.2 IL_2QBG_016,IL_05462.1 IL_2QBG_079,IL_05462.1 IL_2QBG_079,IL_05723.1 IL_2QBG_031,IL_05723.1 IL_2QBG_031,IL_06429.3 IL_2QBG_022,IL_06429.3 IL_2QBG_022,IL_06429.3 IL_2QBG_097,IL_06429.3 IL_2QBG_097,IL_09348.4 IL_2QBG_108,IL_09348.4 IL_2QBG_108,IL_10007.2 IL_2QBG_087,IL_10007.2 IL_2QBG_087,IL_13069.2 IL_2QBG_026,IL_13069.2 IL_2QBG_026,IL_13959.2 IL_2QBG_088,IL_13959.2 IL_2QBG_088,IL_13959.2 IL_2QBG_017,IL_13959.2 IL_2QBG_017,IL_21304.1 IL_2QBG_082,IL_21304.1 IL_2QBG_082,IL_22732.1 IL_2QBG_061,IL_22732.1 IL_2QBG_061,IL_22732.1 IL_2QBG_075,IL_22732.1 IL_2QBG_075,IL_23262.3 IL_2QBG_002,IL_23262.3 IL_2QBG_002,IL_24546.2 IL_2QBG_037,IL_24546.2 IL_2QBG_037,IL_24982.3 IL_2QBG_052,IL_24982.3 IL_2QBG_052,IL_24982.3 IL_2QBG_058,IL_24982.3 IL_2QBG_058,IL_25230.2 IL_2QBG_005,IL_25230.2 IL_2QBG_005,IL_25300.1 IL_2QBG_032,IL_25300.1 IL_2QBG_032,IL_31754.1 IL_2QBG_101,IL_31754.1 IL_2QBG_101,IL_34363.1 IL_2QBG_042,IL_34363.1 IL_2QBG_042,IL_37406.1 IL_2QBG_053,IL_37406.1 IL_2QBG_053,IL_38807.2 IL_2QBG_039,IL_38807.2 IL_2QBG_039,IL_39199.2 IL_2QBG_091,IL_39199.2 IL_2QBG_091,IL_39199.2 IL_2QBG_078,IL_39199.2 IL_2QBG_078,IL_39199.2 IL_2QBG_025,IL_39199.2 IL_2QBG_025,IL_39199.2 IL_2QBG_044,IL_39199.2 IL_2QBG_044,IL_39199.2 IL_2QBG_064,IL_39199.2 IL_2QBG_064,IL_39199.2 IL_2QBG_049,IL_39199.2 IL_2QBG_049,IL_39199.2 IL_2QBG_001,IL_39199.2 IL_2QBG_001,IL_39199.2 IL_2QBG_092,IL_39199.2 IL_2QBG_092,IL_39199.2 IL_2QBG_095,IL_39199.2 IL_2QBG_095,IL_40090.2 IL_2QBG_045,IL_40090.2 IL_2QBG_045,IL_40387.4 IL_2QBG_093,IL_40387.4 IL_2QBG_093,IL_41397.2 IL_2QBG_103,IL_41397.2 IL_2QBG_103,IL_41766.2 IL_2QBG_041,IL_41766.2 IL_2QBG_041,IL_44067.2 IL_2QBG_006,IL_44067.2 IL_2QBG_006,IL_44540.2 IL_2QBG_008,IL_44540.2 IL_2QBG_008,IL_44540.2 IL_2QBG_081,IL_44540.2 IL_2QBG_081,IL_45262.2 IL_2QBG_062,IL_45262.2 IL_2QBG_062,IL_46648.1 IL_2QBG_098,IL_46648.1 IL_2QBG_098,IL_47174.5 IL_2QBG_020,IL_47174.5 IL_2QBG_020,IL_47174.5 IL_2QBG_018,IL_47174.5 IL_2QBG_018,IL_47174.5 IL_2QBG_030,IL_47174.5 IL_2QBG_030,IL_47174.5 IL_2QBG_034,IL_47174.5 IL_2QBG_034,IL_47174.5 IL_2QBG_083,IL_47174.5 IL_2QBG_083,IL_47174.5 IL_2QBG_096,IL_47174.5 IL_2QBG_096,IL_47174.5 IL_2QBG_085,IL_47174.5 IL_2QBG_085,IL_47174.5 IL_2QBG_065,IL_47174.5 IL_2QBG_065,IL_47758.1 IL_2QBG_055,IL_47758.1 IL_2QBG_055,IL_49493.2 IL_2QBG_012,IL_49493.2 IL_2QBG_012,IL_52509.1 IL_2QBG_106,IL_52509.1 IL_2QBG_106,IL_52958.1 IL_2QBG_028,IL_52958.1 IL_2QBG_028,IL_53635.2 IL_2QBG_021,IL_53635.2 IL_2QBG_021,IL_53988.1 IL_2QBG_014,IL_53988.1 IL_2QBG_014,IL_55649.1 IL_2QBG_056,IL_55649.1 IL_2QBG_056,IL_56465.2 IL_2QBG_010,IL_56465.2 IL_2QBG_010,IL_56465.2 IL_2QBG_027,IL_56465.2 IL_2QBG_027,IL_56465.2 IL_2QBG_090,IL_56465.2 IL_2QBG_090,IL_56465.2 IL_2QBG_029,IL_56465.2 IL_2QBG_029,IL_56465.2 IL_2QBG_084,IL_56465.2 IL_2QBG_084,IL_57216.1 IL_2QBG_057,IL_57216.1 IL_2QBG_057,IL_64648.1 IL_2QBG_046,IL_64648.1 IL_2QBG_046,IL_65553.4 IL_2QBG_047,IL_65553.4 IL_2QBG_047,IL_70237.3 IL_2QBG_004,IL_70237.3 IL_2QBG_004,IL_72158.2 IL_2QBG_066,IL_72158.2 IL_2QBG_066,IL_73000.2 IL_2QBG_003,IL_73000.2 IL_2QBG_003,IL_73276.1 IL_2QBG_102,IL_73276.1 IL_2QBG_102,IL_73276.1 IL_2QBG_033,IL_73276.1 IL_2QBG_033,IL_73276.1 IL_2QBG_050,IL_73276.1 IL_2QBG_050,IL_79083.2 IL_2QBG_109,IL_79083.2 IL_2QBG_109,IL_80652.1 IL_2QBG_100,IL_80652.1 IL_2QBG_100,IL_81441.1 IL_2QBG_059,IL_81441.1 IL_2QBG_059,IL_85647.2 IL_2QBG_011,IL_85647.2 IL_2QBG_011,IL_85647.2 IL_2QBG_048,IL_85647.2 IL_2QBG_048,IL_86357.2 IL_2QBG_063,IL_86357.2 IL_2QBG_063,IL_87548.1 IL_2QBG_067,IL_87548.1 IL_2QBG_067,IL_87904.3 IL_2QBG_068,IL_87904.3 IL_2QBG_068,IL_87904.3 IL_2QBG_024,IL_87904.3 IL_2QBG_024,IL_87904.3 IL_2QBG_094,IL_87904.3 IL_2QBG_094,IL_87904.3 IL_2QBG_019,IL_87904.3 IL_2QBG_019,IL_89028.4 IL_2QBG_077,IL_89028.4 IL_2QBG_077,IL_89794.1 IL_2QBG_009,IL_89794.1 IL_2QBG_009,IL_90459.2 IL_2QBG_040,IL_90459.2 IL_2QBG_040,IL_91487.1 IL_2QBG_060,IL_91487.1 IL_2QBG_060,IL_91487.1 IL_2QBG_086,IL_91487.1 IL_2QBG_086,IL_92027.2 IL_2QBG_074,IL_92027.2 IL_2QBG_074,IL_93424.2 IL_2QBG_054,IL_93424.2 IL_2QBG_054,IL_93424.2 IL_2QBG_051,IL_93424.2 IL_2QBG_051,IL_93424.2 IL_2QBG_036,IL_93424.2 IL_2QBG_036,IL_94430.3 IL_2QBG_072,IL_94430.3 IL_2QBG_072,IL_97057.2 IL_2QBG_105,IL_97057.2 IL_2QBG_105,IL_97217.5 IL_2QBG_007,IL_97217.5 IL_2QBG_007,IL_97217.5 IL_2QBG_099,IL_97217.5 IL_2QBG_099,IL_97217.5 IL_2QBG_035,IL_97217.5 IL_2QBG_035,IL_97217.5 IL_2QBG_076,IL_97217.5 IL_2QBG_076,IL_97217.5 IL_2QBG_080,IL_97217.5 IL_2QBG_080,IL_97217.5 IL_2QBG_069,IL_97217.5 IL_2QBG_069,IL_97217.5 IL_2QBG_089,IL_97217.5 IL_2QBG_089,IL_97217.5 IL_2QBG_023,IL_97217.5 IL_2QBG_023,IL_97217.5 IL_2QBG_073,IL_97217.5 IL_2QBG_073,IL_97217.5 IL_2QBG_070,IL_97217.5 IL_2QBG_070,IL_97217.5 IL_2QBG_104,IL_97217.5 IL_2QBG_104,IL_97217.5 IL_2QBG_107,IL_97217.5 IL_2QBG_107,IL_97217.5 IL_2QBG_038,IL_97217.5 IL_2QBG_038,IL_98556.4 IL_2QBG_043,IL_98556.4 IL_2QBG_043,IL_98566.1 IL_2QBG_013,IL_98566.1 IL_2QBG_013,IL_98591.2 IL_2QBG_071,IL_98591.2 IL_2QBG_071"
  correspondencefile = "2QBG_23S_Bacterial_Stombaugh_et_al_Sup_Mat_S3_correspondences.txt"
  alignmentfile = "C:\\Users\\zirbel\\Documents\\FR3D\\Alignments\\23S_Bacterial_Stombaugh_et_al_Sup_Mat_S3.fasta"
  extractfile = "2QBG_23S_Bacterial_Stombaugh_et_al_Sup_Mat_S3_extract.txt"
  MSAID = "23S_Bacterial_Stombaugh"
  
  print "Reading correspondences between PDB file and alignment columns"
  correspondences, header, error = ReadCorrespondences(correspondencefile)
  print "Converting nucleotide ranges to columns"
  ranges = ConvertIDRangeString(correspondences,rangestring)
  print "Retrieving columns from the alignment, writing to an extract file"
  RetrieveColumnsFromAlignment(ranges,alignmentfile,extractfile)
  print "Reading extract file, writing FASTA files for motifs"
  MakeFASTAFilesForMotifs(motifstring,extractfile,MSAID,PDBID)

if 1 > 10:
  PDBID = "2QBG"
  # Matlab:  [rangestring,motifstring] = pRangeStringForMotifsFromStructure('2QBG',MotifRelease)
  rangestring = "2QBG|1|B|U|293:2QBG|1|B|G|295,2QBG|1|B|C|343:2QBG|1|B|A|347,2QBG|1|B|G|481:2QBG|1|B|C|484,2QBG|1|B|G|496:2QBG|1|B|C|509,2QBG|1|B|A|2054:2QBG|1|B|G|2056,2QBG|1|B|C|2612:2QBG|1|B|U|2615,2QBG|1|B|G|858:2QBG|1|B|G|862,2QBG|1|B|C|915:2QBG|1|B|U|919,2QBG|1|B|G|697:2QBG|1|B|C|698,2QBG|1|B|G|763:2QBG|1|B|C|765,2QBG|1|B|C|2512:2QBG|1|B|A|2513,2QBG|1|B|U|2571:2QBG|1|B|G|2574,2QBG|1|B|G|2843:2QBG|1|B|G|2846,2QBG|1|B|C|2870:2QBG|1|B|C|2874,2QBG|1|B|A|2317:2QBG|1|B|U|2321,2QBG|1|B|A|2297:2QBG|1|B|U|2299,2QBG|1|B|G|775:2QBG|1|B|G|777,2QBG|1|B|C|787:2QBG|1|B|C|791,2QBG|1|B|C|2350:2QBG|1|B|G|2353,2QBG|1|B|C|2364:2QBG|1|B|G|2367,2QBG|1|B|G|536:2QBG|1|B|G|539,2QBG|1|B|U|554:2QBG|1|B|C|557,2QBG|1|B|U|2081:2QBG|1|B|G|2083,2QBG|1|B|U|2236:2QBG|1|B|G|2239,2QBG|1|B|C|1526:2QBG|1|B|G|1529,2QBG|1|B|U|1542:2QBG|1|B|G|1546,2QBG|1|B|U|1864:2QBG|1|B|G|1867,2QBG|1|B|C|1874:2QBG|1|B|G|1878,2QBG|1|A|G|23:2QBG|1|A|C|28,2QBG|1|A|G|56:2QBG|1|A|C|60,2QBG|1|B|U|1004:2QBG|1|B|G|1011,2QBG|1|B|C|1150:2QBG|1|B|A|1151,2QBG|1|B|C|1357:2QBG|1|B|G|1361,2QBG|1|B|C|1370:2QBG|1|B|G|1374,2QBG|1|B|U|1513:2QBG|1|B|G|1517,2QBG|1|B|U|1474:2QBG|1|B|G|1478,2QBG|1|A|C|71:2QBG|1|A|G|79,2QBG|1|A|C|97:2QBG|1|A|G|105,2QBG|1|B|U|913:2QBG|1|B|C|915,2QBG|1|B|G|862:2QBG|1|B|A|863,2QBG|1|B|C|2652:2QBG|1|B|C|2658,2QBG|1|B|G|2663:2QBG|1|B|G|2668,2QBG|1|B|C|1043:2QBG|1|B|G|1051,2QBG|1|B|U|1108:2QBG|1|B|G|1112,2QBG|1|B|U|1415:2QBG|1|B|G|1416,2QBG|1|B|C|1582:2QBG|1|B|G|1587,2QBG|1|B|U|1018:2QBG|1|B|G|1024,2QBG|1|B|C|1140:2QBG|1|B|A|1144,2QBG|1|B|G|2454:2QBG|1|B|G|2455,2QBG|1|B|C|2496:2QBG|1|B|C|2498,2QBG|1|B|U|2617:2QBG|1|B|G|2618,2QBG|1|B|C|2050:2QBG|1|B|A|2052,2QBG|1|B|G|757:2QBG|1|B|C|758,2QBG|1|B|G|738:2QBG|1|B|C|740,2QBG|1|B|U|1101:2QBG|1|B|C|1102,2QBG|1|B|G|1087:2QBG|1|B|A|1090,2QBG|1|B|U|1993:2QBG|1|B|C|1994,2QBG|1|B|G|1666:2QBG|1|B|A|1669,2QBG|1|B|A|1603:2QBG|1|B|C|1604,2QBG|1|B|G|1310:2QBG|1|B|U|1313,2QBG|1|A|C|17:2QBG|1|A|G|18,2QBG|1|A|U|65:2QBG|1|A|G|67,2QBG|1|B|U|2493:2QBG|1|B|G|2494,2QBG|1|B|U|2457:2QBG|1|B|A|2459,2QBG|1|B|C|2507:2QBG|1|B|G|2508,2QBG|1|B|U|2580:2QBG|1|B|G|2582,2QBG|1|B|C|1196:2QBG|1|B|U|1198,2QBG|1|B|A|1247:2QBG|1|B|G|1250,2QBG|1|B|A|2459:2QBG|1|B|A|2461,2QBG|1|B|U|2489:2QBG|1|B|U|2493,2QBG|1|B|U|2687:2QBG|1|B|C|2691,2QBG|1|B|G|2718:2QBG|1|B|G|2722,2QBG|1|B|C|1114:2QBG|1|B|C|1117,2QBG|1|B|G|1038:2QBG|1|B|G|1041,2QBG|1|B|G|24:2QBG|1|B|G|30,2QBG|1|B|C|510:2QBG|1|B|C|516,2QBG|1|B|U|434:2QBG|1|B|C|436,2QBG|1|B|G|43:2QBG|1|B|A|44,2QBG|1|B|U|2438:2QBG|1|B|U|2441,2QBG|1|B|A|2070:2QBG|1|B|A|2071,2QBG|1|B|G|1651:2QBG|1|B|C|1656,2QBG|1|B|G|2004:2QBG|1|B|C|2006,2QBG|1|B|U|2522:2QBG|1|B|G|2523,2QBG|1|B|C|2540:2QBG|1|B|G|2543,2QBG|1|B|C|806:2QBG|1|B|G|808,2QBG|1|B|C|672:2QBG|1|B|G|674,2QBG|1|B|A|575:2QBG|1|B|G|577,2QBG|1|B|C|564:2QBG|1|B|U|566,2QBG|1|B|G|856:2QBG|1|B|G|858,2QBG|1|B|U|919:2QBG|1|B|C|921,2QBG|1|B|A|905:2QBG|1|B|G|907,2QBG|1|B|U|870:2QBG|1|B|U|872,2QBG|1|B|C|2232:2QBG|1|B|G|2234,2QBG|1|B|U|2085:2QBG|1|B|G|2087,2QBG|1|B|G|2574:2QBG|1|B|G|2578,2QBG|1|B|C|2510:2QBG|1|B|C|2512,2QBG|1|B|C|2179:2QBG|1|B|U|2181,2QBG|1|B|A|2108:2QBG|1|B|G|2110,2QBG|1|B|C|1990:2QBG|1|B|U|1993,2QBG|1|B|A|1669:2QBG|1|B|G|1674,2QBG|1|B|C|1557:2QBG|1|B|C|1561,2QBG|1|B|G|1432:2QBG|1|B|G|1435,2QBG|1|B|C|239:2QBG|1|B|G|245,2QBG|1|B|C|253:2QBG|1|B|G|258,2QBG|1|B|C|2806:2QBG|1|B|G|2811,2QBG|1|B|C|2889:2QBG|1|B|G|2892,2QBG|1|B|A|844:2QBG|1|B|C|848,2QBG|1|B|G|930:2QBG|1|B|U|934,2QBG|1|B|G|674:2QBG|1|B|C|678,2QBG|1|B|G|799:2QBG|1|B|C|806,2QBG|1|B|C|274:2QBG|1|B|C|281,2QBG|1|B|G|359:2QBG|1|B|G|363,2QBG|1|B|C|1437:2QBG|1|B|U|1440,2QBG|1|B|A|1551:2QBG|1|B|G|1555,2QBG|1|B|G|212:2QBG|1|B|G|214,2QBG|1|B|C|183:2QBG|1|B|C|184,2QBG|1|B|G|940:2QBG|1|B|G|942,2QBG|1|B|C|837:2QBG|1|B|C|838,2QBG|1|B|C|2498:2QBG|1|B|U|2500,2QBG|1|B|A|2453:2QBG|1|B|G|2454,2QBG|1|B|G|926:2QBG|1|B|A|928,2QBG|1|B|U|850:2QBG|1|B|C|851,2QBG|1|B|A|2184:2QBG|1|B|G|2186,2QBG|1|B|C|2103:2QBG|1|B|U|2105,2QBG|1|B|U|1520:2QBG|1|B|G|1524,2QBG|1|B|U|1468:2QBG|1|B|G|1471,2QBG|1|B|G|1202:2QBG|1|B|G|1206,2QBG|1|B|U|1240:2QBG|1|B|C|1243,2QBG|1|B|U|1234:2QBG|1|B|G|1238,2QBG|1|B|C|1208:2QBG|1|B|G|1215,2QBG|1|A|A|34:2QBG|1|A|C|38,2QBG|1|A|G|44:2QBG|1|A|U|48,2QBG|1|B|C|1686:2QBG|1|B|C|1691,2QBG|1|B|G|1696:2QBG|1|B|G|1702,2QBG|1|A|C|30:2QBG|1|A|C|31,2QBG|1|A|G|51:2QBG|1|A|G|54,2QBG|1|B|U|2680:2QBG|1|B|U|2684,2QBG|1|B|A|2725:2QBG|1|B|A|2727,2QBG|1|B|G|864:2QBG|1|B|U|868,2QBG|1|B|A|909:2QBG|1|B|C|912,2QBG|1|B|C|1319:2QBG|1|B|C|1323,2QBG|1|B|G|1331:2QBG|1|B|G|1333,2QBG|1|B|U|2847:2QBG|1|B|G|2852,2QBG|1|B|U|2865:2QBG|1|B|G|2869,2QBG|1|B|C|2636:2QBG|1|B|G|2640,2QBG|1|B|C|2774:2QBG|1|B|G|2782,2QBG|1|B|U|1481:2QBG|1|B|G|1482,2QBG|1|B|C|1507:2QBG|1|B|G|1510,2QBG|1|B|C|201:2QBG|1|B|C|208,2QBG|1|B|G|188:2QBG|1|B|G|194,2QBG|1|B|A|1262:2QBG|1|B|A|1269,2QBG|1|B|U|2011:2QBG|1|B|U|2017,2QBG|1|B|G|1663:2QBG|1|B|A|1665,2QBG|1|B|U|1995:2QBG|1|B|C|1997,2QBG|1|B|U|1742:2QBG|1|B|A|1746,2QBG|1|B|U|1712:2QBG|1|B|G|1718,2QBG|1|B|U|1720:2QBG|1|B|G|1724,2QBG|1|B|U|1736:2QBG|1|B|G|1740,2QBG|1|B|U|703:2QBG|1|B|G|707,2QBG|1|B|U|724:2QBG|1|B|G|728,2QBG|1|B|C|2480:2QBG|1|B|G|2484,2QBG|1|B|C|2466:2QBG|1|B|G|2470,2QBG|1|B|U|606:2QBG|1|B|C|610,2QBG|1|B|G|618:2QBG|1|B|G|622,2QBG|1|B|C|1934:2QBG|1|B|G|1945,2QBG|1|B|C|1961:2QBG|1|B|G|1964,2QBG|1|B|G|81:2QBG|1|B|G|85,2QBG|1|B|C|97:2QBG|1|B|C|105,2QBG|1|B|G|1031:2QBG|1|B|G|1034,2QBG|1|B|C|1121:2QBG|1|B|C|1123,2QBG|1|B|C|1499:2QBG|1|B|G|1500,2QBG|1|B|C|1489:2QBG|1|B|G|1491,2QBG|1|B|U|2220:2QBG|1|B|G|2221,2QBG|1|B|U|2202:2QBG|1|B|G|2204,2QBG|1|B|C|1893:2QBG|1|B|C|1894,2QBG|1|B|G|1846:2QBG|1|B|G|1849,2QBG|1|B|C|1417:2QBG|1|B|G|1421,2QBG|1|B|C|1577:2QBG|1|B|G|1581,2QBG|1|B|C|1376:2QBG|1|B|G|1380,2QBG|1|B|C|1351:2QBG|1|B|G|1355,2QBG|1|B|C|1153:2QBG|1|B|G|1157,2QBG|1|B|C|998:2QBG|1|B|G|1002,2QBG|1|B|C|1837:2QBG|1|B|G|1840,2QBG|1|B|C|1902:2QBG|1|B|G|1903,2QBG|1|B|G|2737:2QBG|1|B|G|2742,2QBG|1|B|C|2762:2QBG|1|B|C|2767,2QBG|1|B|G|36:2QBG|1|B|C|37,2QBG|1|B|G|442:2QBG|1|B|C|444,2QBG|1|B|C|2591:2QBG|1|B|G|2592,2QBG|1|B|C|2601:2QBG|1|B|G|2603,2QBG|1|B|U|1159:2QBG|1|B|G|1160,2QBG|1|B|C|994:2QBG|1|B|A|996,2QBG|1|B|G|1933:2QBG|1|B|C|1934,2QBG|1|B|G|1964:2QBG|1|B|C|1967,2QBG|1|B|C|2442:2QBG|1|B|C|2443,2QBG|1|B|G|2067:2QBG|1|B|G|2069,2QBG|1|B|C|1727:2QBG|1|B|C|1728,2QBG|1|B|G|1731:2QBG|1|B|G|1733,2QBG|1|B|G|2414:2QBG|1|B|G|2415,2QBG|1|B|U|2401:2QBG|1|B|C|2403,2QBG|1|B|U|702:2QBG|1|B|U|703,2QBG|1|B|G|728:2QBG|1|B|A|730,2QBG|1|B|U|1841:2QBG|1|B|G|1842,2QBG|1|B|U|1898:2QBG|1|B|A|1901,2QBG|1|B|G|1770:2QBG|1|B|C|1771,2QBG|1|B|G|1980:2QBG|1|B|U|1982,2QBG|1|B|U|2695:2QBG|1|B|U|2696,2QBG|1|B|A|2711:2QBG|1|B|G|2714,2QBG|1|B|G|2838:2QBG|1|B|G|2839,2QBG|1|B|U|2878:2QBG|1|B|C|2880,2QBG|1|B|G|1149:2QBG|1|B|C|1150,2QBG|1|B|G|1011:2QBG|1|B|C|1013,2QBG|1|B|G|1059:2QBG|1|B|G|1062,2QBG|1|B|C|1076:2QBG|1|B|C|1079,2QBG|1|B|C|269:2QBG|1|B|G|271,2QBG|1|B|C|366:2QBG|1|B|G|370,2QBG|1|B|U|1798:2QBG|1|B|C|1804,2QBG|1|B|G|1813:2QBG|1|B|A|1821"
  motifstring = "IL_00998.1 IL_2QBG_015,IL_00998.1 IL_2QBG_015,IL_02359.2 IL_2QBG_016,IL_02359.2 IL_2QBG_016,IL_05462.1 IL_2QBG_079,IL_05462.1 IL_2QBG_079,IL_05723.1 IL_2QBG_031,IL_05723.1 IL_2QBG_031,IL_06429.3 IL_2QBG_022,IL_06429.3 IL_2QBG_022,IL_06429.3 IL_2QBG_097,IL_06429.3 IL_2QBG_097,IL_09348.4 IL_2QBG_108,IL_09348.4 IL_2QBG_108,IL_10007.2 IL_2QBG_087,IL_10007.2 IL_2QBG_087,IL_13069.2 IL_2QBG_026,IL_13069.2 IL_2QBG_026,IL_13959.2 IL_2QBG_088,IL_13959.2 IL_2QBG_088,IL_13959.2 IL_2QBG_017,IL_13959.2 IL_2QBG_017,IL_21304.1 IL_2QBG_082,IL_21304.1 IL_2QBG_082,IL_22732.1 IL_2QBG_061,IL_22732.1 IL_2QBG_061,IL_22732.1 IL_2QBG_075,IL_22732.1 IL_2QBG_075,IL_23262.3 IL_2QBG_002,IL_23262.3 IL_2QBG_002,IL_24546.2 IL_2QBG_037,IL_24546.2 IL_2QBG_037,IL_24982.3 IL_2QBG_052,IL_24982.3 IL_2QBG_052,IL_24982.3 IL_2QBG_058,IL_24982.3 IL_2QBG_058,IL_25230.2 IL_2QBG_005,IL_25230.2 IL_2QBG_005,IL_25300.1 IL_2QBG_032,IL_25300.1 IL_2QBG_032,IL_31754.1 IL_2QBG_101,IL_31754.1 IL_2QBG_101,IL_34363.1 IL_2QBG_042,IL_34363.1 IL_2QBG_042,IL_37406.1 IL_2QBG_053,IL_37406.1 IL_2QBG_053,IL_38807.2 IL_2QBG_039,IL_38807.2 IL_2QBG_039,IL_39199.2 IL_2QBG_091,IL_39199.2 IL_2QBG_091,IL_39199.2 IL_2QBG_078,IL_39199.2 IL_2QBG_078,IL_39199.2 IL_2QBG_025,IL_39199.2 IL_2QBG_025,IL_39199.2 IL_2QBG_044,IL_39199.2 IL_2QBG_044,IL_39199.2 IL_2QBG_064,IL_39199.2 IL_2QBG_064,IL_39199.2 IL_2QBG_049,IL_39199.2 IL_2QBG_049,IL_39199.2 IL_2QBG_001,IL_39199.2 IL_2QBG_001,IL_39199.2 IL_2QBG_092,IL_39199.2 IL_2QBG_092,IL_39199.2 IL_2QBG_095,IL_39199.2 IL_2QBG_095,IL_40090.2 IL_2QBG_045,IL_40090.2 IL_2QBG_045,IL_40387.4 IL_2QBG_093,IL_40387.4 IL_2QBG_093,IL_41397.2 IL_2QBG_103,IL_41397.2 IL_2QBG_103,IL_41766.2 IL_2QBG_041,IL_41766.2 IL_2QBG_041,IL_44067.2 IL_2QBG_006,IL_44067.2 IL_2QBG_006,IL_44540.2 IL_2QBG_008,IL_44540.2 IL_2QBG_008,IL_44540.2 IL_2QBG_081,IL_44540.2 IL_2QBG_081,IL_45262.2 IL_2QBG_062,IL_45262.2 IL_2QBG_062,IL_46648.1 IL_2QBG_098,IL_46648.1 IL_2QBG_098,IL_47174.5 IL_2QBG_020,IL_47174.5 IL_2QBG_020,IL_47174.5 IL_2QBG_018,IL_47174.5 IL_2QBG_018,IL_47174.5 IL_2QBG_030,IL_47174.5 IL_2QBG_030,IL_47174.5 IL_2QBG_034,IL_47174.5 IL_2QBG_034,IL_47174.5 IL_2QBG_083,IL_47174.5 IL_2QBG_083,IL_47174.5 IL_2QBG_096,IL_47174.5 IL_2QBG_096,IL_47174.5 IL_2QBG_085,IL_47174.5 IL_2QBG_085,IL_47174.5 IL_2QBG_065,IL_47174.5 IL_2QBG_065,IL_47758.1 IL_2QBG_055,IL_47758.1 IL_2QBG_055,IL_49493.2 IL_2QBG_012,IL_49493.2 IL_2QBG_012,IL_52509.1 IL_2QBG_106,IL_52509.1 IL_2QBG_106,IL_52958.1 IL_2QBG_028,IL_52958.1 IL_2QBG_028,IL_53635.2 IL_2QBG_021,IL_53635.2 IL_2QBG_021,IL_53988.1 IL_2QBG_014,IL_53988.1 IL_2QBG_014,IL_55649.1 IL_2QBG_056,IL_55649.1 IL_2QBG_056,IL_56465.2 IL_2QBG_010,IL_56465.2 IL_2QBG_010,IL_56465.2 IL_2QBG_027,IL_56465.2 IL_2QBG_027,IL_56465.2 IL_2QBG_090,IL_56465.2 IL_2QBG_090,IL_56465.2 IL_2QBG_029,IL_56465.2 IL_2QBG_029,IL_56465.2 IL_2QBG_084,IL_56465.2 IL_2QBG_084,IL_57216.1 IL_2QBG_057,IL_57216.1 IL_2QBG_057,IL_64648.1 IL_2QBG_046,IL_64648.1 IL_2QBG_046,IL_65553.4 IL_2QBG_047,IL_65553.4 IL_2QBG_047,IL_70237.3 IL_2QBG_004,IL_70237.3 IL_2QBG_004,IL_72158.2 IL_2QBG_066,IL_72158.2 IL_2QBG_066,IL_73000.2 IL_2QBG_003,IL_73000.2 IL_2QBG_003,IL_73276.1 IL_2QBG_102,IL_73276.1 IL_2QBG_102,IL_73276.1 IL_2QBG_033,IL_73276.1 IL_2QBG_033,IL_73276.1 IL_2QBG_050,IL_73276.1 IL_2QBG_050,IL_79083.2 IL_2QBG_109,IL_79083.2 IL_2QBG_109,IL_80652.1 IL_2QBG_100,IL_80652.1 IL_2QBG_100,IL_81441.1 IL_2QBG_059,IL_81441.1 IL_2QBG_059,IL_85647.2 IL_2QBG_011,IL_85647.2 IL_2QBG_011,IL_85647.2 IL_2QBG_048,IL_85647.2 IL_2QBG_048,IL_86357.2 IL_2QBG_063,IL_86357.2 IL_2QBG_063,IL_87548.1 IL_2QBG_067,IL_87548.1 IL_2QBG_067,IL_87904.3 IL_2QBG_068,IL_87904.3 IL_2QBG_068,IL_87904.3 IL_2QBG_024,IL_87904.3 IL_2QBG_024,IL_87904.3 IL_2QBG_094,IL_87904.3 IL_2QBG_094,IL_87904.3 IL_2QBG_019,IL_87904.3 IL_2QBG_019,IL_89028.4 IL_2QBG_077,IL_89028.4 IL_2QBG_077,IL_89794.1 IL_2QBG_009,IL_89794.1 IL_2QBG_009,IL_90459.2 IL_2QBG_040,IL_90459.2 IL_2QBG_040,IL_91487.1 IL_2QBG_060,IL_91487.1 IL_2QBG_060,IL_91487.1 IL_2QBG_086,IL_91487.1 IL_2QBG_086,IL_92027.2 IL_2QBG_074,IL_92027.2 IL_2QBG_074,IL_93424.2 IL_2QBG_054,IL_93424.2 IL_2QBG_054,IL_93424.2 IL_2QBG_051,IL_93424.2 IL_2QBG_051,IL_93424.2 IL_2QBG_036,IL_93424.2 IL_2QBG_036,IL_94430.3 IL_2QBG_072,IL_94430.3 IL_2QBG_072,IL_97057.2 IL_2QBG_105,IL_97057.2 IL_2QBG_105,IL_97217.5 IL_2QBG_007,IL_97217.5 IL_2QBG_007,IL_97217.5 IL_2QBG_099,IL_97217.5 IL_2QBG_099,IL_97217.5 IL_2QBG_035,IL_97217.5 IL_2QBG_035,IL_97217.5 IL_2QBG_076,IL_97217.5 IL_2QBG_076,IL_97217.5 IL_2QBG_080,IL_97217.5 IL_2QBG_080,IL_97217.5 IL_2QBG_069,IL_97217.5 IL_2QBG_069,IL_97217.5 IL_2QBG_089,IL_97217.5 IL_2QBG_089,IL_97217.5 IL_2QBG_023,IL_97217.5 IL_2QBG_023,IL_97217.5 IL_2QBG_073,IL_97217.5 IL_2QBG_073,IL_97217.5 IL_2QBG_070,IL_97217.5 IL_2QBG_070,IL_97217.5 IL_2QBG_104,IL_97217.5 IL_2QBG_104,IL_97217.5 IL_2QBG_107,IL_97217.5 IL_2QBG_107,IL_97217.5 IL_2QBG_038,IL_97217.5 IL_2QBG_038,IL_98556.4 IL_2QBG_043,IL_98556.4 IL_2QBG_043,IL_98566.1 IL_2QBG_013,IL_98566.1 IL_2QBG_013,IL_98591.2 IL_2QBG_071,IL_98591.2 IL_2QBG_071"
  correspondencefile = "2QBG_Silva_LSU_Bacteria_2013-03-20_correspondences.txt"
  alignmentfile = "C:\\Users\\zirbel\\Documents\\FR3D\\Alignments\\arb-silva.de_2013-03-20_id87166_gapcompressedvertical_oneline.fasta"
  extractfile = "2QBG_Silva_LSU_Bacteria_2013-03-20_extract.txt"
  MSAID = "Silva_LSU_Bacteria"
  
  print "Reading correspondences between PDB file and alignment columns"
  correspondences, header, error = ReadCorrespondences(correspondencefile)
  print "Converting nucleotide ranges to columns"
  ranges = ConvertIDRangeString(correspondences,rangestring)
  print "Retrieving columns from the alignment, writing to an extract file"
  RetrieveColumnsFromAlignment(ranges,alignmentfile,extractfile)
  print "Reading extract file, writing FASTA files for motifs"
  MakeFASTAFilesForMotifs(motifstring,extractfile,MSAID,PDBID)
