import requests

https="https://"
quote="""
░█████╗░██╗░░██╗███╗░░██╗  ░██████╗██╗░░░██╗██████╗░██████╗░░█████╗░███╗░░░███╗░█████╗░██╗███╗░░██╗
██╔══██╗██║░██╔╝████╗░██║  ██╔════╝██║░░░██║██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗██║████╗░██║
███████║█████═╝░██╔██╗██║  ╚█████╗░██║░░░██║██████╦╝██║░░██║██║░░██║██╔████╔██║███████║██║██╔██╗██║
██╔══██║██╔═██╗░██║╚████║  ░╚═══██╗██║░░░██║██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║██╔══██║██║██║╚████║
██║░░██║██║░╚██╗██║░╚███║  ██████╔╝╚██████╔╝██████╦╝██████╔╝╚█████╔╝██║░╚═╝░██║██║░░██║██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝  ╚═════╝░░╚═════╝░╚═════╝░╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░╚══╝
                                                            @Zaid barham
                                                            Paypal:barhamzaid01@gmail.com"""

blue="\033[0;34m"
yellow="\033[1;33m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
print(blue+quote)
file_path=input(yellow+"Enter the subdomains path: ")

with open(file_path, 'r') as file:
    for line in file:
        try:
            subdomain = line.strip()
            if not subdomain:
                continue
            if "https://" in subdomain:
                url =  subdomain
            else:
                url = https+subdomain
            response = requests.get(url,timeout=2)
            if response.status_code == 200:
                print(GREEN+f"[+] {url} is UP {response.status_code}")
            else:
                print(RED+f"[-] {url} responded with status code: {response.status_code}")
        except requests.exceptions.Timeout:
            print(RED+f"[-] {url} timedout")
        except requests.exceptions.RequestException:
            print(RED+f"[-] {url} error")
