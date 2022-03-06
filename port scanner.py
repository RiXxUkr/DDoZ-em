#Author RiX

#Import Libs
import sys
import socket
import threading
from tkinter import *
from pythonping import ping
from time import sleep

#Scanner class
class Scanner:

    #Define IP & text box
    def __init__(self, ip, textBox):
        self.ip = ip
        self.textBox = textBox

    #Create soket function
    def createSock(self):

        #Create socket
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM,
            socket.IPPROTO_TCP
        )

        #Set socket timeout
        sock.settimeout(self.timeout)

        #Return socket object
        return sock

    #Check IP for correction
    def checkIp(self):
        try:

            #Check for empty IP
            if self.ip == '':

                #Return false if IP invalid
                return False

            #If IP not tmpty
            else:

                #Check IP for correction
                self.ipByHost = socket.gethostbyname(self.ip)
                pingQuery = ping(self.ipByHost, verbose=False, size=2, count=3, timeout=10)

                #Check for timeout
                if pingQuery.rtt_max_ms == 10000:

                    #Return false if IP invalid
                    return False

                #If IP is UP
                else:

                    #Get timeout
                    self.timeout = round(pingQuery.rtt_max_ms)/1000

                    #Return true if IP correct
                    return True

        except:

            #Return false if IP invalid
            return False

    #Scan ports function
    def scanPorts(self, port):
        global stop

        #Pass errors
        try:

            #Check for stop scanning
            if not stop:

                #If connected
                try:

                    #Create socket
                    sock = self.createSock()

                    #Connect to IP by port
                    sock.connect((self.ipByHost, port))

                    #Close connection
                    sock.close()

                    #Return port open true
                    return True

                except:

                    #Close connection
                    sock.close()

                    #Return port open false
                    return False

        except:
            pass

#Window class
class Window:

    #Create window
    def __init__(self):

        #Welcome text
        welcome ="""                Made with <3 by
                oooooooooo......o88...ooooo..oooo
                .888........888...oooo......888..88...
                .888oooo88.......888..........888.....
                .888.....88o.......888........88.888...
                o888o.....88o8.o888o..o88o..o888o
                                               Port Scanner
"""

        #Setup window
        self.win = self.createWin()

        #Setup window items
        self.addItems()

        #Print welcome text
        self.textBox.insert(END, welcome)

        #Run window
        self.win.mainloop()

    #Setup window
    def createWin(self):

        #Create window
        root = Tk()

        #Setup title
        root.title('RiX\'s Port Scanner')

        #Setup window size
        root.geometry('350x500')
        root.resizable(False, False)

        #Setup window style
        root.config(bg='black')

        #Return window label
        return root

    #Scan port optimization function
    def scanInMultiprocessing(self, x):

        #Scan port
        portIsOpen = self.scan.scanPorts(port = x)

        #Print results
        if portIsOpen:

            #Print port state result
            self.textBox.insert(END, '[ + ] Port \'%s\' is opened!\n' % x)

            #Autoscroll
            self.textBox.see(END)

        else:
            pass

    #Scan ports multithreading function
    def scanPortThreads(self):
        global stop

        #Scan for opened ports
        for x in range(self.ports + 1, self.ports + 131):

            #Delay
            sleep(0.001)

            #Check stop
            if not stop:

                #Scan ports
                self.scanInMultiprocessing(x = x)
                #Check for last 35 ports
                if x == 65499:

                    #Scan for opened ports
                    for x in range(65500, 65536):

                        #Scan ports
                        self.scanInMultiprocessing(x = x)

                    #End scanning
                    self.scanButtonPressed()

            #Exit cycle on stop
            else:
                break

        #Exit thread
        sys.exit(0)

    #Scan button pressed function
    def scanButtonPressed(self):
        global Scanner, stop

        #Check button status
        if self.scanButton['text'] == 'Scan':

            #Get IP from entry
            self.ip = self.ipEntry.get()

            #Include scanning part of code
            self.scan = Scanner(ip = self.ip, textBox = self.textBox)

            #Check IP for correction
            isCorrect = self.scan.checkIp()
            if isCorrect:

                #Change button text
                self.scanButton['text'] = 'Stop'

                #Change entry state
                self.ipEntry['state'] = 'disabled'

                #Print results output
                self.textBox.insert(END, '[ i ] Scanning \'%s\' for opened ports...\n' % self.ip)

                #Set stop flag False
                stop = False

                #Set part
                self.ports = 0

                #Start multithreading scan
                for x in range(500):

                    #Setup thread
                    threadScan = threading.Thread(target=self.scanPortThreads)

                    #Run thread
                    threadScan.start()

                    #Delay
                    sleep(0.001)

                    #Set part
                    self.ports += 131

            else:

                #Print results output
                self.textBox.insert(END, '[ x ] IP / Domain \'%s\' is invalid or down!\n\n' % self.ip)

                #Autoscroll
                self.textBox.see(END)

        else:

            #Change button text
            self.scanButton['text'] = 'Scan'

            #Change entry state
            self.ipEntry['state'] = 'normal'

            #Set stop flag True
            stop = True

            #Print results output
            self.textBox.insert(END, '[ i ] Scanning \'%s\' stopped or done!\n\n' % self.ip)

            #Autoscroll
            self.textBox.see(END)

            #Exit thread
            sys.exit(0)

    #Run scanning
    def scanPressed(self):

        #Set thread function
        thread = threading.Thread(target=self.scanButtonPressed)

        #Run thread
        done = thread.start()

    #Setup window items
    def addItems(self):

        #Setup frame container & style for options
        frameOptions = Frame(self.win,
            bg='grey35'
        )
        frameOptions.pack(
            side=TOP,
            fill=X,
            ipady=10
        )

        #Setup frame container & style for IP & button
        frameIp = Frame(frameOptions,
            bg='grey35'
        )
        frameIp.pack(expand=True)

        #Setup frame container & style for output information
        frameInfo = Frame(self.win,
            bg='black'
        )
        frameInfo.pack(expand=True)

        #Setup label & style for IP
        ipLabel = Label(frameIp,
            text='IP / Domain',
            bg='grey35',
            fg='white',
            font=('Arial', '12'),
            anchor=W
        ).grid(row=0, column=0, padx=1, ipadx=5)

        #Setup IP entry & style for IP
        self.ipEntry = Entry(frameIp,
            width=14,
            justify='center',
            relief='solid',
            cursor='X_cursor',
            bg='grey25',
            fg='white',
            selectbackground='grey40',
            insertbackground='white',
            font=('Arial', '12')
        )
        self.ipEntry.grid(row=0, column=1, ipady=2)

        #Setup button & style for scan
        self.scanButton = Button(frameIp,
            text='Scan',
            width=12,
            relief='solid',
            bd=1,
            bg='grey25',
            fg='white',
            activebackground='grey15',
            activeforeground='white',
            font=('Arial', '10')
        )
        self.scanButton['command'] = self.scanPressed
        self.scanButton.grid(row=0, column=2, padx=1, ipadx=5)

        #Setup text box & style for output information
        self.textBox = Text(frameInfo,
            width=47,
            height=32,
            relief='solid',
            cursor='X_cursor',
            bd=0,
            bg='black',
            fg='green3',
            selectbackground='grey40',
            insertbackground='white',
            font=('Arial', '10'),
        )
        self.textBox.pack(side=LEFT)

        #Setup scrollbar for text box
        scrollBar = Scrollbar(frameInfo)
        scrollBar.pack(side=RIGHT, fill=Y)
        self.textBox['yscrollcommand'] = scrollBar.set
        scrollBar['command'] = self.textBox.yview

#Run
if __name__ == '__main__':
    Window()
