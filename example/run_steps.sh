python ../scripts/gen_fetch_multi.py sample.list > fetch_all.pml
pymol -cp fetch_all.pml
../scripts/apply_each_chain.sh sample.list
rm -rf raw/*/fix.pml
