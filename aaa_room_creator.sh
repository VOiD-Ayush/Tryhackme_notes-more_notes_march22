RED='\033[0;31m'
GREEN="\033[0;32m"

echo "${RED}[+] ${GREEN}Directory $1 creatiom complete"
mkdir $1
cd $1
mkdir scans
echo "${RED}[+] ${GREEN}README $1 creatiom complete"
echo "# $1 \n" >> README.md
echo -n "> VOiD | " >> README.md
date >> README.md
echo -n "\nMy IP : " >> README.md
ifconfig tun0 | grep inet | cut -d ' ' -f10 | head -1 >> README.md
echo -n "Target IP : \n\n\n\n\n\n" >> README.md
subl README.md