import sys

pdb = sys.argv[1]
alt = ""
if len(sys.argv)>2:
    alt = sys.argv[2]

print( "load %s" % pdb )
if alt in "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890":
    print( "remove not (alt ''+%s)" % alt )
    print( "alter all, alt=''" )
print( "save %s, all" % pdb )
