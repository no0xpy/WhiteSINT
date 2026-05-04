#!/usr/bin/python3
import platform
import fade
from colorama import Fore
import os
import sys
import subprocess
from pystyle import System

path = os.path.dirname(os.path.abspath(__file__))
if platform.system() == "Windows":
    clearcmd = "cls"
else:
    clearcmd = "clear"

System.Title("WhiteSINT")
banner = r"""
██╗    ██╗██╗  ██╗██╗████████╗███████╗███████╗██╗███╗   ██╗████████╗                                                
██║    ██║██║  ██║██║╚══██╔══╝██╔════╝██╔════╝██║████╗  ██║╚══██╔══╝
██║ █╗ ██║███████║██║   ██║   █████╗  ███████╗██║██╔██╗ ██║   ██║   
██║███╗██║██╔══██║██║   ██║   ██╔══╝  ╚════██║██║██║╚██╗██║   ██║                                                    
╚███╔███╔╝██║  ██║██║   ██║   ███████╗███████║██║██║ ╚████║   ██║              
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝   ╚═╝   ╚══════╝╚══════╝╚═╝╚═╝  ╚═══╝   ╚═╝   
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
print(Fore.YELLOW + """
1 > IP Lookup              11 > Subdomains Searcher  
2 > WHOIS Lookup           12 > Py To Exe (Windows Only)     
3 > Phone Lookup           13 > Email Tracker
4 > Ports Scanner          14 > User Tracker
5 > Identity Generator     15 > IP Pinger
6 > Password Generator    
7 > Multiple Searcher 
8 > Discord Tools   
9 > Roblox Lookup (ID)
10 > Breach Lookup (Email)  
""")
choice = input(Fore.MAGENTA + "What do you want to do ? ")

if choice == "1":
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/tools/ip-lookup.py'])
elif choice == "2":
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/tools/whois-lookup.py'])
elif choice == "3":
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/tools/phone-lookup.py'])
elif choice == "4":
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/tools/ports-scanner.py'])
elif choice == "5":
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/tools/id-gen.py'])
elif choice == "6":
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/tools/password-gen.py'])
elif choice == "7":
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/tools/multiple-searcher.py'])
elif choice == "8":
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/tools/Discord/discord-menu.py'])
elif choice == "9":
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/tools/roblox-lookup.py'])
elif choice == "10":
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/tools/breach-lookup.py'])
elif choice == "11":
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/tools/subdomains-searcher.py'])
elif choice == "12":
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/tools/py-to-exe.py'])
elif choice == "13":
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/tools/email-tracker.py'])
elif choice == "14":
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/tools/user-tracker.py'])
else:
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/menu.py'])