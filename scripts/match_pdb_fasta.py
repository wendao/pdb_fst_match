import sys
from Bio import SeqIO
pdb = SeqIO.read(sys.argv[1], "fasta")
fst = SeqIO.read(sys.argv[2], "fasta")

from Bio import pairwise2
from Bio.Align import substitution_matrices
blosum62 = substitution_matrices.load("BLOSUM62")
aln = pairwise2.align.globalds(pdb.seq, fst.seq, blosum62, -10, -1)
print(aln[0][0])
print(aln[0][1])
#blosum62['X']['A']=100
#print(blosum62['X'])
