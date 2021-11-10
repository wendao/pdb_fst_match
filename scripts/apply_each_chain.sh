for p in $(cat $1)
do
  folder=`echo $p|cut -c 2-3`
  fst_name=`echo $p|awk -F'_' '{print tolower($1) "_" $2}'`
  echo $p $folder $fst_name
  cd fst/${folder}/
    grep -A 1 ${fst_name} ../../../database/pdb_seqres.txt > ${p}.fasta
  cd ../..
  cd raw/${folder}/
    
  cd ../..
done
