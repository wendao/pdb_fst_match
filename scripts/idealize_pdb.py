import sys

one2three = {
    "A" : "ALA",
    "C" : "CYS",
    "D" : "ASP",
    "E" : "GLU",
    "F" : "PHE",
    "G" : "GLY",
    "H" : "HIS",
    "I" : "ILE",
    "K" : "LYS",
    "L" : "LEU",
    "M" : "MET",
    "N" : "ASN",
    "P" : "PRO",
    "Q" : "GLN",
    "R" : "ARG",
    "S" : "SER",
    "T" : "THR",
    "V" : "VAL",
    "W" : "TRP",
    "Y" : "TYR",
}

L2D = {
    "ALA" : "DAL",
    "CYS" : "DCY",
    "ASP" : "DAS",
    "GLU" : "DGL",
    "PHE" : "DPN",
    "GLN" : "DGN",
    "LYS" : "DLY",
    "ARG" : "DAR",
    "ILE" : "DIL",
    "LEU" : "DLE",
    "MET" : "MED",
    "PRO" : "DPR",
    "THR" : "DTH",
    "TRP" : "DTR",
    "TYR" : "DTY",
    "SER" : "DSN",
    "VAL" : "DVA",
    "ASN" : "DSG",
    "HIS" : "DHI",
    "GLY" : "GLY",
}

D2L = { v: k for k, v in L2D.items() }

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
        new_lines.append("ATOM  "+l[6:])
    return new_lines

def replace_atomname( res_lines, new_resn=None, atm_dict={} ):
    new_lines = []
    for l in res_lines:
        atmn = l[12:16]
        resn = l[17:20]
        if atmn in atm_dict.keys():
            new_lines.append(l[:12]+atm_dict[atmn]+l[16]+new_resn+l[20:])
        else: new_lines.append(l[:17]+new_resn+l[20:])
    return new_lines

def delete_atomname( res_lines, new_resn=None, dels=[] ):
    new_lines = []
    for l in res_lines:
        atmn = l[12:16]
        if atmn not in dels:
            new_lines.append(l[:17]+new_resn+l[20:])
    return new_lines

def has_BB( res_lines, CA_only=False ):
    bb_atm = ["CA ", "O  ", "N  ", "C  "]
    if CA_only: bb_atm = ["CA"]
    new_lines = []
    for l in res_lines:
        atmn = l[12:16]
        if atmn in bb_atm:
            new_lines.append("ATOM  "+l[6:17]+"UNK"+l[20:])
    if len(new_lines) == len(bb_atm): return new_lines
    return []

def residue_idealizer( res_lines ):
    #check valid
    resn = res_lines[0][17:20]
    has_CA = False
    for l in res_lines[0:]:
        #assert(resn == l[17:20])
        atmn = l[12:16]
        if atmn == " CA ":
            has_CA = True
            break
    if not has_CA: return []
    #parseG
    if resn in ["HOH","SO4"]:
        return []
    elif resn == "MSE":
        new_lines = HETATOM_to_ATOM( res_lines )
        new_lines = replace_atomname( new_lines, "MET" , {" SE ":" SD ","SE  ":" SD "})
    elif resn == "SEP" or resn == "S1P" :
        new_lines = HETATOM_to_ATOM( res_lines )
        new_lines = delete_atomname( new_lines, "SER" , [" P  "," O1P"," O2P"," O3P"])
    elif resn == "TPO" or resn == "T1P":
        new_lines = HETATOM_to_ATOM( res_lines )
        new_lines = delete_atomname( new_lines, "THR" , [" P  "," O1P"," O2P"," O3P"])
    elif resn == "PTR" or resn == "Y1P":
        new_lines = HETATOM_to_ATOM( res_lines )
        new_lines = delete_atomname( new_lines, "TYR", [" P  "," O1P"," O2P"," O3P"] )
    elif resn in L2D.values():
        new_lines = HETATOM_to_ATOM( res_lines )
    else:
        if res_lines[0][:6] == "HETATM":
            new_lines = has_BB(res_lines)
        else:
            return res_lines
    return new_lines

for res in residue_loader( sys.argv[1] ):
    for l in residue_idealizer(res):
        print(l)
