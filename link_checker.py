import argparse
import requests
import sys

logo = """ \033[1;34m 
         _____ _ _             __       _     _                         _   _     
        |  ___(_) | ___       / _| ___ | | __| | ___ _ __   _ __   __ _| |_| |__  
        | |_  | | |/ _ \_____| |_ / _ \| |/ _` |/ _ \ '__| | '_ \ / _` | __| '_ \ 
        |  _| | | |  __/_____|  _| (_) | | (_| |  __/ |    | |_) | (_| | |_| | | |
        |_|   |_|_|\___|     |_|  \___/|_|\__,_|\___|_|    | .__/ \__,_|\__|_| |_|
                                                           |_| \n
            [+] Exm : 
            - python3 link_checker.py wordlist.txt --host example.com
            \033[0;31m- Exiting the program .... [Cutrl +C]\033[0;39m                                                
                       \033[1;39m """

print(logo)

parser = argparse.ArgumentParser(description='Link Checker Tool')
parser.add_argument('file', help='Path to the wordlist file')
parser.add_argument('--host', help='Target host')

args = parser.parse_args()

host = args.host or input("\033[1;31m Enter Your Host: \033[1;39m ")

if not host.startswith("http://") and not host.startswith("https://"):
    host = "http://" + host

wordlist = open(args.file, "r")

r = wordlist.read()
words = r.splitlines()

try:
    for word in words:
        url = host + "/" + word
        req = requests.get(url, "html.parser")
        if req.status_code == 200:
            print("\033[1;34m[+] Found: \033[1;39m" + url)

except:
    print("Exit..")
    sys.exit()
