import platform
import fade
from colorama import Fore
import os
import sys
import subprocess
import requests

path = os.path.dirname(os.path.abspath(__file__))
if platform.system() == "Windows":
    clearcmd = "cls"
else:
    clearcmd = "clear"

banner = r"""
██████╗ ██████╗ ███████╗ █████╗  ██████╗██╗  ██╗    ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔════╝██║  ██║    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
██████╔╝██████╔╝█████╗  ███████║██║     ███████║    ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
██╔══██╗██╔══██╗██╔══╝  ██╔══██║██║     ██╔══██║    ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
██████╔╝██║  ██║███████╗██║  ██║╚██████╗██║  ██║    ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝                                                                                                                                                                   
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⠙⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣷⣶⣤⣄⣈⣉⣉⣉⣉⣉⣉⣉⣁⣤⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣠⣶⣾⡏⢀⡈⠛⠻⠿⢿⣿⣿⣿⣿⣿⠿⠿⠟⠛⢁⠀⢶⣤⣀⠀⠀⠀
⠀⢠⣿⣿⣿⣿⡇⠸⣿⣿⣶⣶⣤⣤⣤⣤⣤⣤⣤⣶⣶⣿⡿⠂⣸⣿⣿⣷⡄⠀
⠀⢸⣿⣿⣿⣿⣿⣦⣄⡉⠛⠛⠛⠿⠿⠿⠿⠛⠛⠛⢉⣁⣤⣾⣿⣿⣿⣿⡷⠀
⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣶⣶⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀
⠀⠀⠀⠀⠈⠙⠛⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠛⠛⠉⠁⠀⠀⠀⠀
"""

print(fade.water(banner))
print(Fore.RED + """[!] This tool is intended for legal, moral and ethical use. The developers are not responsible for how you use it.
""")
try:
 target = input(Fore.MAGENTA + "Email Address > ")
 r = requests.get(f'https://api.xposedornot.com/v1/check-email/{target}')
 data = r.json()
 if 'breaches' in data:
    print(Fore.GREEN + f"[+] Breaches found for", target)
    print(data['breaches'])
 else:
    print(Fore.RED + "[-] No breaches found for", target)
 stealerschoice = input(Fore.YELLOW + "[?] Do you want to search in stealers logs ? (Y/n) ")
 if stealerschoice == "y" or stealerschoice == "Y":
    sr = requests.get(f"https://cavalier.hudsonrock.com/api/json/v2/osint-tools/search-by-email?email={target}")
    sdata = sr.json()
    if 'message' in sdata:
     print(Fore.GREEN + f"[+] Stealers logs found for", target)
     print("Date:", sdata['date_compromised'])
     print("Message:", sdata['message'])
    else:
     print(Fore.RED + "[-] No stealers logs found for", target)
 else:
    pass
except Exception as e:
 print("[I] Error:", e)

choice = input(Fore.YELLOW + "[?] Do you want to retry ? (Y/n) ")
if choice == "y" or choice =="Y":
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/breach-lookup.py'])
else:
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/../menu.py'])
