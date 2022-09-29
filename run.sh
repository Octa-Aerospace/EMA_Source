#
runner="poetry run python main.py";

clear;
echo "[$] $runner";
eval $runner;

if [ $? -eq 0 ]; then
    echo "[+] Running ... ";
else
    echo "[-] Error ... ";
fi;

echo "[-] Closing ... ";
exit 0;
