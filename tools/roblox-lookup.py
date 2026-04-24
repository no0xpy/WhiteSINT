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
██████╗  ██████╗ ██████╗ ██╗      ██████╗ ██╗  ██╗    ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗██║     ██╔═══██╗╚██╗██╔╝    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
██████╔╝██║   ██║██████╔╝██║     ██║   ██║ ╚███╔╝     ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
██╔══██╗██║   ██║██╔══██╗██║     ██║   ██║ ██╔██╗     ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
██║  ██║╚██████╔╝██████╔╝███████╗╚██████╔╝██╔╝ ██╗    ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝                                                                                                                                                                  
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
 target = input(Fore.MAGENTA + "User ID > ")
 oldusr = requests.get(f"https://users.roblox.com/v1/users/{target}/username-history")
 data = oldusr.json()
 usernames = data.get("data", [])
 for pseudo in usernames:
  print(Fore.GREEN + "[+] Old Username Found:", pseudo)
 if not usernames:
  print(Fore.RED + "[-] 0 Old Username Found")

 infos = requests.get(f"https://users.roblox.com/v1/users/{target}")
 print(Fore.GREEN + "[+] Bio:", infos.json()['description'])
 print(Fore.GREEN + "[+] Creation Date:", infos.json()['created'])
 print(Fore.GREEN + "[+] Username:", infos.json()['name'])
 print(Fore.GREEN + "[+] Display Name:", infos.json()['displayName'])

except Exception as e:
 print("[I] Error:", e)

choice = input(Fore.YELLOW + "[?] Do you want to retry ? (Y/n) ")
if choice == "y" or choice =="Y":
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/roblox-lookup.py'])
else:
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/../menu.py'])
