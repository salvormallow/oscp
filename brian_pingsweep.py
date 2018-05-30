import os, re

ip_list = []

for ip in range(1,255):

    ip = "10.11.1." + str(ip)
    command = "ping -c 1 -W 1 " + ip
    x = os.popen(command).read()
    match = re.search("bytes from", x)
    if match:
        ip_list.append(ip)

print(ip_list)