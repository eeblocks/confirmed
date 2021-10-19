#!/usr/bin/python3
# BTC TX Confirmation
# Coded by esiquiel

# Dependencies
import requests
import json
import os

from time import sleep

def btc_confirm(refresh, Colors, tx_hash):
    
    os.system(f'title confirmed | {tx_hash}' if os.name == 'nt' else f'echo -ne "\033]0;confirmed | {tx_hash}\007"')

    api = f'https://blockchain.info/tx/{tx_hash}?show_adv=false&format=json'

    headers = {
        'authority': 'blockchain.info',
        'Content-Type': 'application/json',
        'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }

    while True:

        r = requests.get(api, headers=headers)
        info = json.loads(r.text)
        block_height = info["block_height"]

        rlast = requests.get('https://blockchain.info/latestblock', headers=headers)
        height_info = json.loads(rlast.text)
        height = height_info["height"]

        try:
            confirmations = height - block_height + 1

            if block_height != None:
                print(f'{Colors.YELLOW}Confirmations:{Colors.WHITE} {confirmations}')

            elif confirmations > 4:
                print(f'{Colors.GREEN}Confirmed{Colors.WHITE}')
                break

            sleep(5)
            refresh()

        except:
            print(f'{Colors.RED}0 Confirmations{Colors.WHITE}')
            sleep(5)
            refresh()
