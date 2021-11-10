import sys
from optparse import OptionParser

def initialize_options() :
    parser = OptionParser()
    parser.add_option( "-p", "--pdb", dest="pdbname", type="string", help="The input pdb that should be renumbered" )
    parser.add_option( "-o", "--output", dest="output", type="string", help="The output file to write the renumbered pdb to; stdout if not given", default="" )
    parser.add_option( "-l", "--align_file", dest="aln", type="string", help="", default="" )
    return parser

def remap_resnum_for_line( lines, mapping ):
    newlines = []
    last_resstr = ""
    resi = 0
    for line in lines:
        left = line[:22]
        right = line[27:]
        resstr = line[22:27]
        if resstr == last_resstr:
            newstr = "%4d " % mapping[resi]
        else:
            last_resstr = resstr
            resi += 1
            newstr = "%4d " % mapping[resi]
        #print("|"+resstr+"|"+newstr+"|")
        newlines.append(left+newstr+right)
    return newlines

if __name__ == "__main__":

    parser = initialize_options()
    (options, args) = parser.parse_args()

    pdblines = open( options.pdbname ).readlines()

    mapping = {}
    #the fasta seq starts from 1, and pdb match with it
    seqlines = open( options.aln ).readlines()
    pdbseq = seqlines[0].strip()
    fstseq = seqlines[1].strip()
    nSeq = len(fstseq)
    assert( len(pdbseq) == nSeq )
    p_pdb = 0
    p_fst = 0
    fst0 = -1
    for i in range(nSeq):
        if fst0 < 0 and fstseq[i] != "-": fst0 = i 
        if fstseq[i] != "-": p_fst = p_fst + 1
        if pdbseq[i] != "-": 
            p_pdb = p_pdb + 1
            mapping[p_pdb] = p_fst
        #print(p_pdb, pdbseq[i], p_fst, fstseq[i])
    #gap in fasta
    if fst0 > 0: 
        for i in range(fst0, 0, -1):
            mapping[i] = i - fst0
    #print(mapping)
    
    newlines = remap_resnum_for_line( pdblines, mapping )
    if options.output == "":
        for line in newlines:
            print(line, end='')
    else:
        open( options.output, "w").writelines(newlines)

