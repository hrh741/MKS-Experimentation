cd /nv/gpfs-gateway-scratch1/3/nhpnp3/2_9_cyc

for f in {0..399}
do
    echo " Submitting $f file..."
    export number=$f;
    msub -V run_script_integrate.sh
done
