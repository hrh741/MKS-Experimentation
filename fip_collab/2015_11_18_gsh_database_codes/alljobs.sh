cd /panfs/iw-scratch.pace.gatech.edu/v7/nhpnp3/dir_11_12

for f in 1 3 5 7 9 11 13 15 17 19 21
do
    echo " Submitting $f file..."
    export number=$f;
    msub -V run_script.sh
done
