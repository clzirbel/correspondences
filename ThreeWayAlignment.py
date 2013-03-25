# This program combines three sets of correspondences into a 3-way alignment

# INPUT:  Three 2-way correspondences
# OUTPUT: All pairwise correspondences that make consistent triples
#         Plus all pairwise correspondences that are not part of a consistent triple

def ThreeWayAlignment(c1, c2, c3):
	threeWay = []
	twoWay = []
	c2used = []
	c3used = []
	for itemSource, itemTarget in c1.iteritems():
		if (c2.has_key(itemTarget)):
			if (c3.has_key(c2[itemTarget])):
				if (c3[c2[itemTarget]] == itemSource):
					# We have a circular match!
					threeWay.append([itemSource, itemTarget, c2[itemTarget]])
					c2used.append(itemTarget)
					c3used.append(c2[itemTarget])
				else:
					# Target from Correspondence 3 does not match
					twoWay.append([itemSource, itemTarget])
					twoWay.append([itemTarget, c2[itemTarget]])
					twoWay.append([c2[itemTarget], c3[c2[itemTarget]]])
					c2used.append(itemTarget)
					c3used.append(c2[itemTarget])
			else:
				#Target in Correspondence 3 does not exist
				twoWay.append([itemSource, itemTarget])
				twoWay.append([itemTarget, c2[itemTarget]])
				c2used.append(itemTarget)
		else:	
			# Target in Correspondence 2 does not exist
			twoWay.append([itemSource, itemTarget])
	
	# Clear used items out of the correspondences
	for used in c2used:
		del c2[used]
	for used in c3used:
		del c3[used]
	
	# Add in broken items that cannot be reached from Correspondence 1
	for itemSource, itemTarget in c2.iteritems():
		twoWay.append([itemSource, itemTarget])
	
	for itemSource, itemTarget in c3.iteritems():
		twoWay.append([itemSource, itemTarget])
		
	return threeWay, twoWay
	


		