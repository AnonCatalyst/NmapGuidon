import os
import platform
import logging
import time
from datetime import datetime
from pytz import timezone
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

def nmap_scan(option):
    try:
        separator = f"{Fore.YELLOW}{Style.BRIGHT}{'=' * 40}{Style.RESET_ALL}"

        if option == 1:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            target_type = input(f"{Fore.MAGENTA}Choose target type {Fore.CYAN}(1 for a single target, 2 for all IP addresses associated with a domain){Fore.MAGENTA}:{Style.RESET_ALL} ")
            if target_type == "1":
                target_arg = host
            elif target_type == "2":
                target_arg = f"-iL <(host -t A {host} | grep 'has address' | cut -d ' ' -f 4)"
            else:
                print(f"{Fore.RED}Invalid target type choice. Defaulting to a single target.{Style.RESET_ALL}")
                target_arg = host
            os.system(f"nmap {target_arg}")
            print(separator)

        elif option == 2:
            start = input(colored_menu_item("Enter the starting IP:", Fore.CYAN))
            end = input(colored_menu_item("Enter the ending IP:", Fore.CYAN))
            os.system(f"nmap {start}-{end}")
            print(separator)

        elif option == 3:
            subnet = input(colored_menu_item("Enter the target subnet:", Fore.CYAN))
            os.system(f"nmap {subnet}")
            print(separator)

        elif option == 4:
            os.system("nmap -sL")
            print(separator)

        elif option == 5:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            os.system(f"nmap -sV {host}")
            print(separator)

        elif option == 6:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            os.system(f"nmap -O {host}")
            print(separator)

        elif option == 7:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            os.system(f"nmap -A {host}")
            print(separator)

        elif option == 8:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            os.system(f"nmap -sC -sV {host}")
            print(separator)

        elif option == 9:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            script_name = input(colored_menu_item("Enter the script name:", Fore.CYAN))
            os.system(f"nmap -p 80 --script {script_name} {host}")
            print(separator)

        elif option == 10:
            targets = input(colored_menu_item("Enter the target hosts (comma-separated):", Fore.CYAN))
            os.system(f"nmap {targets}")
            print(separator)

        elif option == 11:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            os.system(f"nmap -f {host}")
            print(separator)

        elif option == 12:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            os.system(f"nmap -sV --version-intensity 5 {host}")
            print(separator)

        elif option == 13:
            os.system("ls /usr/share/nmap/scripts/")
            print(separator)

        elif option == 14:
            custom_command = input(colored_menu_item("Enter the custom Nmap command:", Fore.CYAN))
            os.system(custom_command)
            print(separator)

        elif option == 15:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            os.system(f"nmap -p- {host}")
            print(separator)

        elif option == 16:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            os.system(f"nmap -sU {host}")
            print(separator)

        elif option == 17:
            timing = input(colored_menu_item("Enter the timing (e.g., paranoid, sneaky, polite, aggressive):", Fore.CYAN))
            os.system(f"nmap -T {timing}")
            print(separator)

        elif option == 18:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            os.system(f"nmap -sV --script=banner {host}")
            print(separator)

        elif option == 19:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            os.system(f"traceroute {host}")
            print(separator)

        elif option == 20:
            subnet = input(colored_menu_item("Enter the target subnet:", Fore.CYAN))
            os.system(f"nmap -sn {subnet}")
            print(separator)

        elif option == 21:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            os.system(f"nmap -sV -O --version-intensity 0 {host}")
            print(separator)

        elif option == 22:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            os.system(f"nmap -sV --version-intensity 5 {host}")
            print(separator)

        elif option == 23:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            n_ports = input(colored_menu_item("Enter the number of ports to scan:", Fore.CYAN))
            os.system(f"nmap -p- --top-ports {n_ports} {host}")
            print(separator)

        elif option == 24:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            os.system(f"nmap --open {host}")
            print(separator)

        elif option == 25:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            os.system(f"nmap -sI {host}")
            print(separator)

        elif option == 26:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            os.system(f"nmap --script vuln {host}")
            print(separator)

        elif option == 27:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            os.system(f"nmap -sC -sV --script=default {host}")
            print(separator)

        elif option == 28:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            os.system(f"nmap -p 443 --script ssl-heartbleed {host}")
            print(separator)

        elif option == 29:
            host = input(colored_menu_item("Enter the target host or IP:", Fore.CYAN))
            os.system(f"nmap --script ssl-enum-ciphers {host}")
            print(separator)

        # Add more options here based on your needs...

    except Exception as e:
        logging.error(f"[{Fore.RED}Error{Style.RESET_ALL}] in option {option}: [{Fore.RED}{str(e)}{Style.RESET_ALL}]")
        print(f"[{Fore.RED}An error occurred: {str(e)}{Style.RESET_ALL}]")
        print(separator)

def funny_animation():
    for _ in range(3):
        print(Fore.GREEN + Style.BRIGHT + "Thanks for using NmapGuidon!" + Style.RESET_ALL)
        time.sleep(0.5)
        clear_terminal()

def main():
    clear_terminal()
    print_banner()

    while True:
        menu()
        choice = input(colored_menu_item("Enter choice (1-30):", Fore.CYAN))

        if choice.isdigit() and 1 <= int(choice) <= 30:
            choice = int(choice)
            if choice == 30:
                funny_animation()
                break
            else:
                clear_terminal()
                nmap_scan(choice)
        else:
            print(Fore.RED + Style.BRIGHT + "Invalid choice. Enter a number between 1 and 30." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
