#copyright
import random
import time
import colorama
import json
import os
from colorama import Fore, Style

#setup colorama colours
colorama.init()
# all the colors so i can type like {red}
colors = {
    "red": Fore.RED,
    "green": Fore.GREEN,
    "blue": Fore.BLUE,
    "yellow": Fore.YELLOW,
    "magenta": Fore.MAGENTA,
    "cyan": Fore.CYAN,
    "white": Fore.WHITE,
    "reset": Style.RESET_ALL
    }
websites = {
    "Google": "https://google.com",
    "YouTube": "https://youtube.com",
    "Facebook": "https://facebook.com",
    "X": "https://x.com",
}
print(colors["magenta"] + """     _ _ _                 _                                      _ 
 ___(_) | |_   _  ___ __ _| |_ ___  __ _ _ __ ___  ___ ___   ___ | |
/ __| | | | | | |/ __/ _` | __/ __|/ _` | '__/ _ \/ __/ _ \ / _ \| |
\__ \ | | | |_| | (_| (_| | |_\__ \ (_| | | |  __/ (_| (_) | (_) | |
|___/_|_|_|\__, |\___\__,_|\__|___/\__,_|_|  \___|\___\___/ \___/|_|
           |___/                                                    """ + colors["reset"])
print(colors["magenta"] + "Welcome to Tom's portfolio." + colors["reset"])
print(colors["green"] + "------------------------------------------------------------" + colors["reset"])
print(colors["magenta"] + "Websites I've worked on:" + colors["reset"])
for key, value in websites.items():
    print(colors["magenta"] + f"{key} - {value}" + colors["reset"])
