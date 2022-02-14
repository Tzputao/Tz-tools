# Esse self foi orgulhosamente codificado por Rdimo (https://instagram.com/tzfofo).
# Copyright (c) 2021 🜲 Oi, eu sou o Tz#0001 | https://instagram.com/tzfofo
# Tz Nuker sob a Licença Pública Geral GNU v2 (1991).

import requests
import random
import Tz

from time import sleep
from colorama import Fore

from util.plugins.common import SlowPrint, setTitle, getheaders, proxy

def selector(token, users):
    while True:
        try:
            response = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(f"{Fore.RED}Chat em grupo criado")
            elif response.status_code == 429:
                print(f"{Fore.YELLOW}Taxa limitada ({response.json()['retry_after']}ms){Fore.RESET}")
            else:
                print(f"{Fore.RED}Erro: {response.status_code}{Fore.RESET}")
        except Exception:
            pass
        except KeyboardInterrupt:
            break
    Tz.main()

def randomizer(token, ID):
    while True:
        users = random.sample(ID, 2)
        try:
            response = requests.post(f'https://discordapp.com/api/v9/users/@me/channels', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(f"{Fore.RED}Chat em grupo criado")
            elif response.status_code == 429:
                print(f"{Fore.YELLOW}Taxa limitada ({response.json()['retry_after']}ms){Fore.RESET}")
            else:
                print(f"{Fore.RED}Erro: {response.status_code}{Fore.RESET}")
        except Exception:
            pass
        except KeyboardInterrupt:
            break
    Tz.main()


def GcSpammer(token):
    print(f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}Você quer escolher o(s) usuário(s) para o spam de bate-papo em grupo ou deseja selecionar aleatoriamente?')
    sleep(1)
    print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] escolha o(s) usuário(s) você mesmo
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] randomizar os usuários
                        ''')
    secondchoice = int(input(
        f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Segunda chance: {Fore.RED}'))

    if secondchoice not in [1, 2]:
        print(f'{Fore.RESET}[{Fore.RED}Erro{Fore.RESET}] : Segunda escolha inválida')
        sleep(1)
        Tz.main()

    #if they choose to import the users manually
    if secondchoice == 1:
        setTitle(f"Criando bate-papos em grupo")
        #if they choose specific users
        recipients = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Insira os usuários com os quais você deseja criar um bate-papo em grupo (separado por , id,id2,id3): {Fore.RED}')
        user = recipients.split(',')
        if "," not in recipients:
            print(f"\n{Fore.RED}Você não tinha vírgulas (,) o formato é id,id2,id3")
            sleep(3)
            Hazard.main()
        SlowPrint("\"ctrl + c\" a qualquer momento para parar\n")
        sleep(1.5)
        selector(token, user)

    #if they choose to randomize the selection
    elif secondchoice == 2:
        setTitle(f"Criando bate-papos em grupo")
        IDs = []
        #Get all users to spam groupchats with
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'http://{proxy()}'}, headers=getheaders(token)).json()
        for friend in friendIds:
            IDs.append(friend['id'])
        SlowPrint("\"ctrl + c\" a qualquer momento para parar\n")
        sleep(1.5)
        randomizer(token, IDs)