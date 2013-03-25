# This program combines three sets of correspondences into a 3-way alignment
from ReadCorrespondences import ReadCorrespondences
from ThreeWayAlignment import ThreeWayAlignment

correspondences1, header1, error1 = ReadCorrespondences('2QBG_3U5H_correspondences_511bdafa59aa6.txt',0)
correspondences2, header2, error2 = ReadCorrespondences('3V2F_3U5H_correspondences_511bdbc4dc920.txt',1)
correspondences3, header3, error3 = ReadCorrespondences('2QBG_3V2F_correspondences_50dd09ef4f614.txt',1)

threeway, twoway = ThreeWayAlignment(correspondences1,correspondences2,correspondences3)

print "Circular alignments:"
print
for threewayAlign in threeway:
	print "(" + threewayAlign[0] + ", " + threewayAlign[1] + ", " + threewayAlign[2] + ")"

print
print "Broken alignments:"
print
for twowayAlign in twoway:
	print "(" + twowayAlign[0] + ", " + twowayAlign[1] + ")"

# Count the good and bad alignments. Each bad alignment produces two elements	
good = len(threeway)
bad = len(twoway)
print
print "Total circular alignments: " + str(good)
print "Total broken alignments: " + str(bad)

# Make them no longer integers so we get a good decimal. Divide broken alignments by three
# for fair comparison to circular alignments.
good = good * 1.0
bad = bad / 3.0
print "Quality: " + ("%0.2f" % (100 * good / (good + bad))) + "%"