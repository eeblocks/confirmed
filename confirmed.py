#!/usr/bin/python3
# confirmed v1.0
# Coded by esiquiel

# Dependencies
import argparse
import time
import os

from btc import btc_confirm


# Argument Settings
parser = argparse.ArgumentParser(description='Control your Confirmations of Crypto Transactions')

parser.add_argument('-btc', '--bitcoin', dest='btc', help='Enter your Bitcoin transaction hash')
parser.add_argument('-eth', '--ethereum', dest='eth', help='Enter your Bitcoin transaction hash')
parser.add_argument('-ada', '--cardano', dest='ada', help='Enter your Bitcoin transaction hash')

args = parser.parse_args()


# Colors class
class Colors:

    WHITE = '\033[37m'
    YELLOW = '\033[33m'
    GREEN = '\033[32m'
    RED = '\033[31m'


# Clear the terminal
def refresh():

    os.system('cls' if os.name == 'nt' else 'clear')
    banner = open('banner.txt', 'r').read()
    print(Colors.YELLOW, banner, Colors.WHITE)


if __name__ == '__main__':

    os.system('title confirmed' if os.name == 'nt' else 'echo -ne "\033]0;confirmed | Coded by esiquiel\007"')
    refresh()

    if args.btc:
        btc_confirm(refresh, Colors, args.btc)

    elif args.eth:
        print('Working on Ethereum confirmation...')
    
    elif args.ada:
        print('Working on Cardano confirmation...')

    else:
        print(f'{Colors.YELLOW}Confirm Crypto Transaction')
        print(f'--------------------------')

        print(f'{Colors.YELLOW}[1]{Colors.WHITE} Bitcoin')
        print(f'{Colors.YELLOW}[2]{Colors.WHITE} Ethereum')
        print(f'{Colors.YELLOW}[3]{Colors.WHITE} Cardano\n')

        print(f'{Colors.YELLOW}#~: {Colors.WHITE}', end='')
        
        choice = int(input(''))

        refresh()

        # Bitcoin Confirmation
        if choice == 1:
            print('-----------------------')
            print('Bitcoin TX Confirmation')
            print('-----------------------\n')

            tx_hash = input('Transaction Hash:\n')

            refresh()
            btc_confirm(refresh, Colors, tx_hash)
        
        # Ethereum Confirmation
        elif choice == 2:
            print('Working on Ethereum confirmation...')

        # Cardano Confirmation
        elif choice == 3:
            print('Working on Cardano confirmation...')