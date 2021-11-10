import sys, os
from collections import defaultdict

chains = defaultdict(list)
lines = open(sys.argv[1], 'r').readlines()
for l in lines:
  pro = l[:4]
  chn = l.strip()[5:]
  chains[pro].append(chn)

#default cif download dir
os.makedirs("mmcif", exist_ok=True)

print("set fetch_path, mmcif")
for pro in chains.keys():
  print( "fetch " + pro + ", async=0" )
  print( "remove not (alt ''+A) " )
  print( "alter all, alt=''" )
  #https://files.rcsb.org/download/6F5G.[pdb/cif]
  #https://www.rcsb.org/fasta/entry/7ANQ/display
  #fasta
  os.makedirs("fst/%s/" % pro[1:3], exist_ok=True)
  #pdb
  os.makedirs("raw/%s/" % pro[1:3], exist_ok=True)
  for ch in chains[pro]:
    #print( "save fst/%s/%s.fasta, chain %s" % (pro[1:3], pro+ch, ch) )
    print( "save raw/%s/%s.pdb, chain %s" % (pro[1:3], pro+ch, ch) )
  print( "delete all" )
print("quit")
