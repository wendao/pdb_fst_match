for p in $(cat $1)
do
  folder=`echo $p|cut -c 2-3`
  pdb_name=`echo $p|awk -F'_' '{print $1 $2}'`
  fst_name=`echo $p|awk -F'_' '{print tolower($1) "_" $2}'`
  echo $p $folder $fst_name
  cd fst/${folder}/
    grep -A 1 ${fst_name} ../../../database/pdb_seqres.txt > ${p}.fasta
  cd ../..
  cd raw/${folder}/
    #clean TODO
    #grep ^ATOM ${pdb_name}.pdb > ${pdb_name}_clean.pdb
    python ../../../scripts/idealize_pdb.py ${pdb_name}.pdb > ${pdb_name}_clean.pdb
    #pdb seq
    ../../../bin/pdb2fasta ${pdb_name}_clean.pdb > ${pdb_name}.pdb.fst
    #renumber
    python ../../../scripts/match_pdb_fasta.py ${pdb_name}.pdb.fst ../../fst/${folder}/${p}.fasta > ${p}.aln
    #renumber
    python ../../../scripts/renumber_pdb.py -p ${pdb_name}_clean.pdb -l ${p}.aln -o ${pdb_name}_renumber.pdb
  cd ../..
done
