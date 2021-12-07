from tqdm import tqdm
import os,sys

def remap_resnum_for_line(lines, mapping):
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
            if resi != len(mapping):
                resi += 1
            if resi == len(mapping):
                resi = resi
            newstr = "%4d " % mapping[resi]
        #print("|"+resstr+"|"+newstr+"|")
        newlines.append(left+newstr+right)
    return newlines

#f = open('final_path.list', 'r+')
f = open('try.list', 'r+')
l = f.read().splitlines()
f.close()
problem_list = []
empty_list = []
empty_pdb = []

for i in tqdm(range(len(l))):
    pdbname = l[i].split(';')[0]
    aln = l[i].split(';')[2]
    aln_fst_name = l[i].split(';')[1]
    # new_file_name = './tmp_data/single_chain_pdb/raw/' + pdbname.split('/')[-1][1:3] + '/' + aln.split('/')[-1].split('new')[0] + 'renum.pdb'
    new_file_name = './renum_pdb_final/' + aln.split('/')[-1].split('new')[0] + 'renum.pdb' 
    # pdbname = '2F16D_clean.pdb'
    # aln = '2F16D.aln'
    # pdbname = '5CAJA_rename_rew.pdb'
    # aln = '5CAJ_A_2_new_inf.out'
    # aln第一行pdb 第二行fasta
    # 换成.out里的对应内容
    if os.path.exists(pdbname) == False:
        empty_list.append(l[i])
        continue
    if os.path.exists(aln) == False:
        empty_list.append(l[i])
        continue
    if os.path.exists(aln_fst_name) == False:
        empty_list.append(l[i])
        continue
    pdblines = open(pdbname, 'r+').readlines()
    seqlines = open(aln).readlines()
    pdbseq = seqlines[3].strip()
    raw_fstseq = seqlines[1].strip()
    #print(raw_fstseq,len(raw_fstseq))
    newfst = []
    for aa in range(len(raw_fstseq)):
        if raw_fstseq[aa] != '-':
            newfst.append(raw_fstseq[aa])
        if raw_fstseq[aa] == '-':
            newfst.append(pdbseq[aa])
    fstseq = ''
    for bb in range(len(newfst)):
        fstseq = fstseq + newfst[bb]
    #print(fstseq,len(fstseq))


    mapping = {}
    #pdbseq = seqlines[3].strip()
    #fstseq = seqlines[1].strip()
    nSeq = len(fstseq)
    assert( len(pdbseq) == nSeq )
    p_pdb = 0
    p_fst = 0
    fst0 = -1
    for j in range(nSeq):
        if fst0 < 0 and fstseq[j] != "-": fst0 = j 
        if fstseq[j] != "-": p_fst = p_fst + 1
        if pdbseq[j] != "-": 
            p_pdb = p_pdb + 1
            mapping[p_pdb] = p_fst
        #print(p_pdb, pdbseq[i], p_fst, fstseq[i])
    #gap in fasta
    if fst0 > 0: 
        for k in range(fst0, 0, -1):
            mapping[k] = k - fst0
    # print(mapping)

    # assert(pdb尾-首, aligned_fasta)
    aln_fst = open(aln_fst_name, 'r+')
    aln_fst_lines = aln_fst.read().splitlines()
    aln_fasta = aln_fst_lines[1]
    
    if len(pdblines) == 0 or len(pdblines) == 1:
        empty_pdb.append(l[i])
        continue
    
    newlines = remap_resnum_for_line(pdblines, mapping)
    
    start_num = int(newlines[0][22:27])
    end_num = int(newlines[-1][22:27])
    nPDB = end_num - start_num + 1
    print(nPDB)
    print(len(aln_fasta))
    if len(aln_fasta) != nPDB:
        problem_list.append(l[i])
        print('prob_list', problem_list)
    if len(aln_fasta) == nPDB:
        # 写入新文件
        newfile = open(new_file_name, 'w+')
        for p in range(len(newlines)):
            newfile.write(newlines[p])
        newfile.close()
sys.exit()
'''
nf = open('renum_prob_list_prb_pdb_final.list', 'w+')
for i in range(len(problem_list)):
    nf.write(problem_list[i] + '\n')
nf.close()

nf2 = open('renum_empty_list_final.list','w+')
for i in range(len(empty_list)):
    nf2.write(empty_list[i] + '\n')
nf2.close()

nf3 = open('renum_empty_pdb_final.list','w+')
for i in range(len(empty_pdb)):
    nf3.write(empty_pdb[i] + '\n')
nf3.close()
'''
