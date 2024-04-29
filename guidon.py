import subprocess
import os
import platform
import logging
from datetime import datetime
from colorama import Fore, Style, init
from pytz import timezone

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
        1: "nmap -Pn -sS -p <port> <host>",  # Scan a single host
        2: "nmap -Pn -sS -p <port> <start_ip>-<end_ip>",  # Scan a host range
        3: "nmap -Pn -sS -p <port> <subnet>",  # Scan a subnet
        4: "nmap -Pn -sL <target>",  # List scan
        5: "nmap -Pn -sV <target>",  # Version detection
        6: "nmap -Pn -O <target>",  # OS detection
        7: "nmap -Pn -A <target>",  # Aggressive scan
        8: "nmap -Pn -sC <target>",  # Service version and script scanning
        9: "nmap -Pn -p <port> --script <script> <target>",  # Scan using a specific script
        10: "nmap -Pn <target1> <target2> ...",  # Scan multiple targets
        11: "nmap -Pn -f -D RND:10 <target>",  # Firewall evasion techniques
        12: "nmap -Pn -sV --version-all <target>",  # Aggressive service version detection
        13: "nmap --script-help all",  # Show all available NSE scripts
        14: "nmap <custom_command>",  # Custom Nmap command
        15: "nmap -Pn -sS -p- <target>",  # Full TCP port scan
        16: "nmap -Pn -sU -p 1-65535 <target>",  # UDP port scan
        17: "nmap -Pn -T<0-5> <target>",  # Timing and performance options
        18: "nmap -Pn -sS -sV -p <port> --script=banner <target>",  # Banner grabbing
        19: "nmap -Pn --traceroute <target>",  # Traceroute
        20: "nmap -Pn -sn <target>",  # Host discovery
        21: "nmap -Pn -Pn -sS -sV -O <target>",  # Service version and OS detection without host discovery
        22: "nmap -Pn -Pn -sS -sV --version-all <target>",  # Aggressive service version detection without host discovery
        23: "nmap -Pn --top-ports <N> <target>",  # Scan top N ports
        24: "nmap -Pn --open <target>",  # List all open ports
        25: "nmap -Pn -p 0-65535 -sI <zombie host> <target>",  # Firewall IDLE scan
        26: "nmap -Pn --script vuln <target>",  # Script scan for common vulnerabilities
        27: "nmap -Pn --script <script> <target>",  # Scan using the Nmap Scripting Engine (NSE)
        28: "nmap -Pn --script ssl-heartbleed <target>",  # Scan for Heartbleed vulnerability
        29: "nmap -Pn --script ssl-enum-ciphers <target>",  # Detect and list SSL/TLS ciphers
        30: None  # Exit
    }
    return nmap_commands

def main():
    while True:
        clear_terminal()
        print_banner()
        menu()
        choice = input("Enter your choice (1-30): ")

        if choice.isdigit():
            choice = int(choice)
            if choice == 30:  # Exit option
                print("Exiting NmapGuidon...")
                break
            elif choice in nmap_commands():
                nmap_command = nmap_commands()[choice]
                if nmap_command:
                    target = input("Enter target(s): ")
                    command = nmap_command.replace("<target>", target)
                    subprocess.run(command, shell=True)
                    input("Press Enter to continue...")
                else:
                    print("Invalid option. Please choose again.")
            else:
                print("Invalid option. Please choose again.")
        else:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()

