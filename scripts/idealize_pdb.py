import sys

def residue_loader( fn ):
  lines = open( fn, 'r' ).readlines()
  res_lines = []
  cur_res = "EMPTY"
  for l in lines:
    l = l.strip()
    if l[:6] in ["ATOM  ", "HETATM"]  and l[26]==" ":
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

def HETATOM_to_ATOM( res_lines ):
    new_lines = []
    for l in res_lines:
        new_lines.append("ATOM  "+res_line[6:])
    return new_lines

def replace_atomname( res_lines, new_resn=None, atm_dict={} ):
    new_lines = []
    for l in res_lines:
        atmn = l[13:16]
        resn = l[17:20]
        if atmn in atm_dict.keys():
            new_lines.append(l[:13]+atm_dict[atmn]+l[16]+new_resn+l[20:])
        else: new_lines.append(l[:17]+new_resn+l[20:])
    return new_lines

def delete_atomname( res_lines, new_resn=None, dels=[] ):
    new_lines = []
    for l in res_lines:
        atmn = l[13:16]
        if atmn not in dels:
            new_lines.append(l[:17]+new_resn+l[20:])
    return new_lines

def residue_idealizer( res_lines ):
    #check valid
    resn = res_lines[0][17:20]
    has_CA = False
    for l in res_lines[0:]:
        #assert(resn == l[17:20])
        atmn = l[13:16]
        if atmn == "CA ":
            has_CA = True
            break
    if not has_CA: return []
    #parseG
    if resn in ["HOH","SO4"]:
        return []
    elif resn == "MSE":
        new_lines = HETATOM_to_ATOM( res_lines )
        new_lines = replace_atomname( res_lines, {"SE ":"SD "}, "MET" )
    elif resn == "SEP" or resn == "S1P" :
        new_lines = HETATOM_to_ATOM( res_lines )
        new_lines = delete_atomname( res_lines, [], "SER" )
    elif resn == "TPO" or resn == "T1P":
        new_lines = HETATOM_to_ATOM( res_lines )
        new_lines = delete_atomname( res_lines, [], "THR" )
    elif resn == "PTR" or resn == "Y1P":
        new_lines = HETATOM_to_ATOM( res_lines )
        new_lines = delete_atomname( res_lines, [], "TYR" )
    else:
        #TODO check UNK
        return res_lines
    return new_lines

for res in residue_loader( sys.argv[1] ):
    for l in residue_idealizer(res):
        print(l)
