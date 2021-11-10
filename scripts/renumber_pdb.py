import sys
from optparse import OptionParser

def initialize_options() :
    parser = OptionParser()
    parser.add_option( "-p", "--pdb", dest="pdbname", type="string", help="The input pdb that should be renumbered" )
    parser.add_option( "-o", "--output", dest="output", type="string", help="The output file to write the renumbered pdb to; stdout if not given", default="" )
    parser.add_option( "-l", "--align_file", dest="aln", type="string", help="", default="" )
    return parser

def remap_resnum_for_line( line, mapping ):
    if line[0:4] != "ATOM": return line
    chain = line[21]
    if chain not in mapping: return line
    resstring = line[22:27]
    resnum, lastresstring = mapping[ chain ]
    if lastresstring == "" or resstring != lastresstring :
        if lastresstring != "" : resnum += 1
        mapping[ chain ] = (resnum, resstring )
    newresstring = str(resnum) + " "
    if len(newresstring) == 2: newresstring = "   " + newresstring
    elif len(newresstring) == 3: newresstring = "  " + newresstring
    elif len(newresstring) == 4: newresstring = " " + newresstring
    return line[0:22] + newresstring + line[27:]

if __name__ == "__main__":

    parser = initialize_options()
    (options, args) = parser.parse_args()

    pdblines = open( options.pdbname ).readlines()
    mapping = {}
    newlines = []
    for line in pdblines:
        newlines.append( remap_resnum_for_line( line, mapping ))
    if options.output == "":
        for line in newlines:
            print(line, end='')
    else:
        open( options.output, "w").writelines(newlines)

