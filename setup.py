#Author RiX

#Import libs
from os import name, system

if __name__ == '__main__':

    #Clear terminal
    system('cls' if name == 'nt' else 'clear')

    #Auto install for Windows
    if name == 'nt':

        #Print installing info
        print('[i] Installing \'Python 3 Requirements\'...')

        #Install python 3 package
        system('pip3 install -r requirements.txt')

        #Pass 1 row
        print('\n')

    #Auto install for Lunux
    else:

        #Package installing commands
        cmds = [
            'sudo apt-get install python3',
            'sudo apt-get install python3-pip',
            'sudo pip3 install -r requirements.txt'
        ]

        #Installing info list
        info = [
            '[i] Installing \'Python 3\'...',
            '[i] Installing \'Python 3 Pip\'...',
            '[i] Installing \'Python 3 Requirements\'...'
        ]

        #Select package install command
        for cmd in cmds:

            #Print installing info
            print(info[cmds.index(cmd)])

            #Install packages
            system(cmd)

            #Pass 1 row
            print('\n')

    #Print done
    print('[+] Done!\n')
