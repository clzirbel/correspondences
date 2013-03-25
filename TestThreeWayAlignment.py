# This program combines three sets of correspondences into a 3-way alignment

correspondences1, header1, error1 = ReadCorrespondences('2QBG_3U5H_correspondences_511bdafa59aa6.txt',0)
correspondences2, header2, error2 = ReadCorrespondences('3V2F_3U5H_correspondences_511bdbc4dc920.txt',1)
correspondences3, header3, error3 = ReadCorrespondences('2QBG_3V2F_correspondences_50dd09ef4f614.txt',1)

threeway, twoway = ThreeWayAlignment(correspondences1,correspondences2,correspondences3)