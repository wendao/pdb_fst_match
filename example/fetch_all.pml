set fetch_path, mmcif
fetch 1SXJ, async=0
remove not (alt ''+A) 
alter all, alt=''
save raw/SX/1SXJA.pdb, chain A
delete all
fetch 1PQV, async=0
remove not (alt ''+A) 
alter all, alt=''
save raw/PQ/1PQVD.pdb, chain D
delete all
fetch 1ZY2, async=0
remove not (alt ''+A) 
alter all, alt=''
save raw/ZY/1ZY2A.pdb, chain A
delete all
fetch 1HQM, async=0
remove not (alt ''+A) 
alter all, alt=''
save raw/HQ/1HQMD.pdb, chain D
save raw/HQ/1HQMD.pdb, chain D
delete all
fetch 4QRY, async=0
remove not (alt ''+A) 
alter all, alt=''
save raw/QR/4QRYF.pdb, chain F
delete all
fetch 7LL9, async=0
remove not (alt ''+A) 
alter all, alt=''
save raw/LL/7LL9C.pdb, chain C
delete all
fetch 6UWI, async=0
remove not (alt ''+A) 
alter all, alt=''
save raw/UW/6UWIh.pdb, chain h
delete all
fetch 6RTJ, async=0
remove not (alt ''+A) 
alter all, alt=''
save raw/RT/6RTJA.pdb, chain A
delete all
fetch 3BOG, async=0
remove not (alt ''+A) 
alter all, alt=''
save raw/BO/3BOGA.pdb, chain A
delete all
fetch 1I6V, async=0
remove not (alt ''+A) 
alter all, alt=''
save raw/I6/1I6VD.pdb, chain D
delete all
fetch 1914, async=0
remove not (alt ''+A) 
alter all, alt=''
save raw/91/1914A.pdb, chain A
delete all
quit
