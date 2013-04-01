# TestAlignmentPrograms

from AlignmentPrograms import LocalAlignment

# --------- Simple alignment test first

seq1 = 'AGGCTACG'
seq2 = 'TCGGCATATAAAGGCCG'

matches, score, a1, a2, p1, p2 = LocalAlignment(seq1,seq2,'DNA',3,0)

print matches,"exact matches"
print "Overall score is",score
print a1
print a2
print p1
print p2

# --------- Align two protein sequences

seq1 = 'VLSEEDKSHVKAIWGKVAGHLEEYGAEALERMFCAYPQTKIYFPHFDMSHNSAQIRGHGKKVFAALHDAVNHIDDLAGALCRLSDLHAHNLRVDPVNFKFLSQCILVVFGVHHPCSLTPEVHASLDKFLCAVSAMLTSKYR'
seq2 = 'SLTAKDKSVVKAFWGKISGKADVVGAEALGRDKMLTAYPQTKTYFSHWADLSPGSGPVKKHGGIIMGAIGKAVGLMDDLVGGMSALSDLHAFKLRVDPGNFKILSHNILVTLAIHFPSDFTPEVHIAVDKFLAAVSAALADKYR'  

matches, score, a1, a2, p1, p2 = LocalAlignment(seq1,seq2,'protein',3,0)

print matches,"exact matches"
print "Overall score is",score
print a1
print a2
print p1
print p2

