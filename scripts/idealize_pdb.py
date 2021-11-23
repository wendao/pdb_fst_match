import sys

def residue_loader( fn ):
  lines = open( fn, 'r' ).readlines()
  res_lines = []
  cur_res = "EMPTY"
  for l in lines:
    l = l.strip()
    if l[:4] == "ATOM" and l[26]==" ":
      resi = l[22:26]
      if resi == cur_res:
          res_lines.append(l)
      else:
          if len(res_lines)>0:
              yield res_lines
          res_lines = [l]
          cur_res = resi
  if len(res_lines)>0: yield res_lines
  return

def residue_idealizer( res ):
    #check resn
    resn = res[0][17:20]
    for l in res[1:]:
        assert(resn == l[17:20])
    if resn not in ["MSE"]:
        return


for res in residue_loader( sys.argv[1] ):
    residue_idealizer(res)
    #for l in res:
    #    print(l)
