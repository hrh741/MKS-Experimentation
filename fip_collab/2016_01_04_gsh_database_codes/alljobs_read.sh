cd /nv/gpfs-gateway-pace1/project/pme/pme1/nhpnp3/1_19_6deg

for f in {1..11}
do
    echo " Submitting $f file..."
    export number=$f;
    msub -V run_script_read.sh
done
