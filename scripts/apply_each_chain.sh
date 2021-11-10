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
    #clean
    #../../../bin/pdb2fasta ${pdb_name}_clean.pdb > ${pdb_name}.pdb.fst
    #renumber
  cd ../..
done
