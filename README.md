# pdb_fst_match

For chain ID for all single chain, download https://cdn.rcsb.org/resources/sequence/clusters/bc-50.out
For fasta sequence for each chain, download https://ftp.wwpdb.org/pub/pdb/derived_data/pdb_seqres.txt.gz

    cd examples
    python ../scripts/gen_fetch_multi.py sample.list > fetch_all.pml
    pymol -cp fetch_all.pml

    grep -A 1 7ll9_C ../database/pdb_seqres.txt

Then clean the pdb, rename and renumber
