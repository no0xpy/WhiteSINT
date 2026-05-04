import platform
import fade
from colorama import Fore
import os
import sys
import subprocess
import subbrute

path = os.path.dirname(os.path.abspath(__file__))
if platform.system() == "Windows":
    clearcmd = "cls"
else:
    clearcmd = "clear"

banner = r"""
██████╗ ██╗   ██╗    ████████╗ ██████╗     ███████╗██╗  ██╗███████╗
██╔══██╗╚██╗ ██╔╝    ╚══██╔══╝██╔═══██╗    ██╔════╝╚██╗██╔╝██╔════╝
██████╔╝ ╚████╔╝        ██║   ██║   ██║    █████╗   ╚███╔╝ █████╗  
██╔═══╝   ╚██╔╝         ██║   ██║   ██║    ██╔══╝   ██╔██╗ ██╔══╝  
██║        ██║          ██║   ╚██████╔╝    ███████╗██╔╝ ██╗███████╗
╚═╝        ╚═╝          ╚═╝    ╚═════╝     ╚══════╝╚═╝  ╚═╝╚══════╝                                                              
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
[I] You must be on Windows to use this tool.
""")
try:
 print("Convert .py to .exe with Pyinstaller")
 target = input(Fore.MAGENTA + "Path of the .py file > ")
 os.system('pip install pyinstaller')
 os.system(f'pyinstaller --onefile "{target}"')
 print(Fore.GREEN + "[I] Saved on /dist")
except Exception as e:
 print("[I] Error:", e)

choice = input(Fore.YELLOW + "[?] Do you want to retry ? (Y/n) ")
if choice == "y" or choice =="Y":
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/py-to-exe.py'])
else:
 os.system(clearcmd)
 subprocess.run([sys.executable, f'{path}/../menu.py'])
