cd /gpfs/pace1/project/me-kalidindi/shared/dir_nhp

for f in {0..59}
do
    echo " Submitting $f file..."
    export number=$f;
    msub -V run_script_read.sh
done