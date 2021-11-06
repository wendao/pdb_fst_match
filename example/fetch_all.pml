set fetch_path, mmcif
fetch 1SXJ, async=0
remove not (alt ''+A) 
alter all, alt=''
save fst/SX/1SXJA.fasta, chain A
save raw/SX/1SXJA.pdb, chain A
delete all
fetch 1PQV, async=0
remove not (alt ''+A) 
alter all, alt=''
save fst/PQ/1PQVD.fasta, chain D
save raw/PQ/1PQVD.pdb, chain D
delete all
fetch 1ZY2, async=0
remove not (alt ''+A) 
alter all, alt=''
save fst/ZY/1ZY2A.fasta, chain A
save raw/ZY/1ZY2A.pdb, chain A
delete all
fetch 1HQM, async=0
remove not (alt ''+A) 
alter all, alt=''
save fst/HQ/1HQMD.fasta, chain D
save raw/HQ/1HQMD.pdb, chain D
delete all
fetch 4QRY, async=0
remove not (alt ''+A) 
alter all, alt=''
save fst/QR/4QRYF.fasta, chain F
save raw/QR/4QRYF.pdb, chain F
delete all
fetch 7LL9, async=0
remove not (alt ''+A) 
alter all, alt=''
save fst/LL/7LL9C.fasta, chain C
save raw/LL/7LL9C.pdb, chain C
delete all
fetch 6UWI, async=0
remove not (alt ''+A) 
alter all, alt=''
save fst/UW/6UWIh.fasta, chain h
save raw/UW/6UWIh.pdb, chain h
delete all
fetch 6RTJ, async=0
remove not (alt ''+A) 
alter all, alt=''
save fst/RT/6RTJA.fasta, chain A
save raw/RT/6RTJA.pdb, chain A
delete all
fetch 3BOG, async=0
remove not (alt ''+A) 
alter all, alt=''
save fst/BO/3BOGA.fasta, chain A
save raw/BO/3BOGA.pdb, chain A
delete all
fetch 1I6V, async=0
remove not (alt ''+A) 
alter all, alt=''
save fst/I6/1I6VD.fasta, chain D
save raw/I6/1I6VD.pdb, chain D
delete all
fetch 1914, async=0
remove not (alt ''+A) 
alter all, alt=''
save fst/91/1914A.fasta, chain A
save raw/91/1914A.pdb, chain A
delete all
quit
