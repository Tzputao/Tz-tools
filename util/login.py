# Esse self foi orgulhosamente codificado por Rdimo (https://instagram.com/tzfofo).
# Copyright (c) 2021 🜲 Oi, eu sou o Tz#0001 | https://instagram.com/tzfofo
# Tz Nuker sob a Licença Pública Geral GNU v2 (1991).

import requests
import Tz

from time import sleep
from selenium import webdriver, common
from colorama import Fore, Back

from util.plugins.common import getDriver, getheaders, SlowPrint

def TokenLogin(token):
    j = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token)).json()
    user = j["username"] + "#" + str(j["discriminator"])
    script = """
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"%s"`
            location.reload();
        """ % (token)
    type_ = getDriver()

    if type_ == "chromedriver.exe":
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        try:
            driver = webdriver.Chrome(options=opts)
        except common.exceptions.SessionNotCreatedException as e:
            print(e.msg)
            sleep(2)
            SlowPrint("Digite qualquer coisa para continuar. . . ")
            input()
            Tz.main()
    elif type_ == "operadriver.exe":
        opts = webdriver.opera.options.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        try:
            driver = webdriver.Opera(options=opts)
        except common.exceptions.SessionNotCreatedException as e:
            print(e.msg)
            sleep(2)
            SlowPrint("Digite qualquer coisa para continuar. . . ")
            input()
            Tz.main()
    elif type_ == "msedgedriver.exe":
        opts = webdriver.EdgeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        try:
            driver = webdriver.Edge(options=opts)
        except common.exceptions.SessionNotCreatedException as e:
            print(e.msg)
            sleep(2)
            SlowPrint(f"Digite qualquer coisa para continuar. . .")
            input()
            Tz.main()
    else:
        print(f'{Fore.RESET}[{Fore.RED}Erro{Fore.RESET}] : Não foi possível encontrar um driver adequado para fazer login automaticamente {user}')
        sleep(3)
        print(f"{Fore.YELLOW}Cole este script no console de um navegador:{Fore.RESET}\n\n{Back.RED}{script}\n{Back.RESET}")
        print("Digite qualquer coisa para continuar. . . ", end="")
        input()
        Tz.main()

    print(f"{Fore.GREEN}Fazendo login {Fore.CYAN}{user}")
    driver.get("https://discordapp.com/login")
    driver.execute_script(script)
    Tz.main()