#!/usr/bin/python3
import platform
import fade
from colorama import Fore
import os
import sys
import subprocess


path = os.path.dirname(os.path.abspath(__file__))
if platform.system() == "Windows":
    clearcmd = "cls"
else:
    clearcmd = "clear"

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
1 > IP Lookup\t 11 > Subdomains Searcher  
2 > WHOIS Lookup\t       
3 > Phone Lookup\t     
4 > Ports Scanner\t     
5 > Identity Generator\t     
6 > Password Generator\t     
7 > Multiple Searcher\t     
8 > Discord Tools\t     
9 > Roblox Lookup (ID)\t   
10 > Breach Lookup (Email)\t
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
else:
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/menu.py'])