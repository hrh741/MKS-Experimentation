cd /nv/gpfs-gateway-scratch1/3/nhpnp3/3_14_db

for f in {0..39}
do
    echo " Submitting $f file..."
    export number=$f;
    msub -V run_script_Xcalc.sh
done