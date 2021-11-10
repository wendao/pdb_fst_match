# pdb_fst_match

## Full Protocol

For chain ID for all single chain, download https://cdn.rcsb.org/resources/sequence/clusters/bc-100.out

For fasta sequence for each chain, download https://ftp.wwpdb.org/pub/pdb/derived_data/pdb_seqres.txt.gz

    cd examples
    #generate pymol script
    python ../scripts/gen_fetch_multi.py sample.list > fetch_all.pml
    #fetch all cif and pdb
    pymol -cp fetch_all.pml
    #extract fasta
    ../scripts/apply_each_chain.sh sample.list

Then clean the pdb, rename and renumber

## Description

**bc-100.out**: generate single chain id list

**gen_fetch_multi.py**: generate pymol script for downloading cif and single chain PDB (keep alt=A only)

**pdb_seqres.txt**: fasta for every single chain

## TODO
clean pdb: remove col[27] not empty
rename: MSE, PTR, SEP, TPO ...
../../../bin/pdb2fasta 2F16D_clean.pdb > 2F16D.fst
python ../scripts/match_pdb_fasta.py raw/F1/2F16D.fst fst/F1/2F16_D.fasta > raw/F1/2F16D.aln
python ../scripts/renumber_pdb.py -p raw/F1/2F16D_clean.pdb -l raw/F1/2F16D.aln
