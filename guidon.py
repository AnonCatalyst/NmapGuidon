import subprocess
import os
import platform
import logging
import time
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

logging.basicConfig(filename='nmap_guidon.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clear_terminal():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_banner():
    print(Fore.GREEN + "██╗  ██╗ ██████╗ ██╗   ██╗██╗██╗")
    print(Fore.GREEN + "╚██╗██╔╝██╔═══██╗██║   ██║██║██║")
    print(Fore.GREEN + " ╚███╔╝ ██║   ██║██║   ██║██║██║")
    print(Fore.GREEN + " ██╔██╗ ██║   ██║╚██╗ ██╔╝██║██║")
    print(Fore.GREEN + "██╔╝ ██╗╚██████╔╝ ╚████╔╝ ██║██║")
    print(Fore.GREEN + "╚═╝  ╚═╝ ╚═════╝   ╚═══╝  ╚═╝╚═╝\n")
    print(f"{Fore.CYAN}Platform: {platform.platform()}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Python Version: {platform.python_version()}{Style.RESET_ALL}")
    utc_now = datetime.utcnow()
    local_tz = timezone('US/Eastern')
    local_time = utc_now.replace(tzinfo=timezone('UTC')).astimezone(local_tz)
    print(f"{Fore.CYAN}Current UTC Time: {utc_now.strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Current Local Time: {local_time.strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}\n")

def colored_menu_item(text, number):
    return f"{Fore.CYAN}{Style.BRIGHT}{str(number).ljust(2)}. {Fore.MAGENTA}{text}{Style.RESET_ALL}"

def menu():
    print(Fore.YELLOW + Style.BRIGHT + "NmapGuidon Command Menu:" + Style.RESET_ALL)
    print(colored_menu_item("Scan a single host", 1))
    print(colored_menu_item("Scan a host range", 2))
    print(colored_menu_item("Scan a subnet", 3))
    print(colored_menu_item("List scan", 4))
    print(colored_menu_item("Version detection", 5))
    print(colored_menu_item("OS detection", 6))
    print(colored_menu_item("Aggressive scan", 7))
    print(colored_menu_item("Service version and script scanning", 8))
    print(colored_menu_item("Scan using a specific script", 9))
    print(colored_menu_item("Scan multiple targets", 10))
    print(colored_menu_item("Firewall evasion techniques", 11))
    print(colored_menu_item("Aggressive service version detection", 12))
    print(colored_menu_item("Show all available NSE scripts", 13))
    print(colored_menu_item("Custom Nmap command", 14))
    print(colored_menu_item("Full TCP port scan", 15))
    print(colored_menu_item("UDP port scan", 16))
    print(colored_menu_item("Timing and performance options", 17))
    print(colored_menu_item("Banner grabbing", 18))
    print(colored_menu_item("Traceroute", 19))
    print(colored_menu_item("Host discovery", 20))
    print(colored_menu_item("Service version and OS detection without host discovery", 21))
    print(colored_menu_item("Aggressive service version detection without host discovery", 22))
    print(colored_menu_item("Scan top N ports", 23))
    print(colored_menu_item("List all open ports", 24))
    print(colored_menu_item("Firewall IDLE scan", 25))
    print(colored_menu_item("Script scan for common vulnerabilities", 26))
    print(colored_menu_item("Scan using the Nmap Scripting Engine (NSE)", 27))
    print(colored_menu_item("Scan for Heartbleed vulnerability", 28))
    print(colored_menu_item("Detect and list SSL/TLS ciphers", 29))
    print(colored_menu_item("Exit", 30))

def nmap_commands():
    nmap_commands = {
        1: ("nmap {}", "target_arg"),
        2: ("nmap {}-{}", "start end"),
        3: ("nmap
