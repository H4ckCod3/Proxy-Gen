import requests, colorama
from colorama import Fore, Style
from colorama import init

B = Fore.LIGHTBLACK_EX
G = Fore.GREEN
R = Fore.RED

init()


def generar_proxies():
    with requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all", stream=True) as response:
        response.raise_for_status()

        with open("proxies.txt", "w") as f:
            for line in response.iter_lines():
                if line:
                    f.write(line.decode('utf-8') + '\n')
    print(f"{R}[ {B}+ {R}] {G}Proxies generated successfully")

def verificar_proxies(ruta_proxies):
    with open(ruta_proxies, "r") as f:
        proxies = f.readlines()
    
    proxies_validos = []
    for proxy in proxies:
        proxy = proxy.strip()
        try:
            response = requests.get("http://httpbin.org/ip", proxies={"http": proxy, "https": proxy}, timeout=5)
            if response.status_code == 200:
                print(f"{G}[ {B}+ {G}] {G}Proxy valid: {proxy}")
                proxies_validos.append(proxy)
            else:
                print(f"{R}[ {B}- {R}] {R}Proxy invalid: {proxy}")
        except requests.exceptions.RequestException:
            print(f"{R}[ {B}- {R}] {R}Proxy invalid: {proxy}")
    
    with open("valid_proxies.txt", "w") as f_validos:
        for proxy in proxies_validos:
            f_validos.write(proxy + '\n')
    
    return proxies_validos

def menu():
    while True:
        print(f"""{R}

██████╗ ██████╗  ██████╗ ██╗  ██╗██╗███████╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     
██╔══██╗██╔══██╗██╔═══██╗╚██╗██╔╝██║██╔════╝██╔════╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║            {R}[ {B}1 {R}] {R}Proxies Gen{R}
██████╔╝██████╔╝██║   ██║ ╚███╔╝ ██║█████╗  ███████╗       ██║   ██║   ██║██║   ██║██║            {R}[ {B}2 {R}] {R}Proxies Checker{R}
██╔═══╝ ██╔══██╗██║   ██║ ██╔██╗ ██║██╔══╝  ╚════██║       ██║   ██║   ██║██║   ██║██║            {R}[ {B}3 {R}] {R}Exit{R}
██║     ██║  ██║╚██████╔╝██╔╝ ██╗██║███████╗███████║       ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                                           
-----------------------------------------------------------------------------------------------------------------------
""")

        opcion = input(f"{R}[ {B}+ {R}] {B}Enter a choice: ")
        
        if opcion == '1':
            generar_proxies()
        elif opcion == '2':
            proxies_validos = verificar_proxies("proxies.txt")
            print(f"{R}[ {B}+ {R}] {G}Proxyes Validas: {len(proxies_validos)}")
        elif opcion == '3':
            print(f"{R}[ {B}- {R}] {B}Exiting...")
            break
        else:
            print(f"{R}[ {B}- {R}] {B}Invalid option. Try again.")

menu()
