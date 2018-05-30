for ip in $(echo 10.11.1.{1..255}); 
do ping -c 1 -W 1 $ip | grep "bytes from" | grep -oP "\d+\.\d+\.\d+\.\d+" >> ./result.txt & 
done
