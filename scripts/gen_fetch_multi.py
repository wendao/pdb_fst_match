import sys, os
from collections import defaultdict

chains = defaultdict(list)
lines = open(sys.argv[1], 'r').readlines()
for l in lines:
  pro = l[:4]
  chn = l.strip()[5:]
  chains[pro].append(chn)

print("set fetch_path, /home/wendao/mmcif")
for pro in chains.keys():
  print( "fetch " + pro + ", async=0" )
  print( "remove not (alt ''+A) " )
  print( "alter all, alt=''" )
  os.makedirs("raw/%s/" % pro[1:3], exist_ok=True)
  for ch in chains[pro]:
    print( "save raw/%s/%s.pdb, chain %s" % (pro[1:3], pro+ch, ch) )
  print( "delete all" )
  print()
