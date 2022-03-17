# Esse self foi orgulhosamente codificado por Tz (https://instagram.com/tzfofo).
# Copyright (c) 2021 🜲 Oi, eu sou o Tz#0001 | https://instagram.com/tzfofo
# Tz Tools sob a Licença Pública Geral GNU v2 (1991).

import requests
import Tz
from colorama import Fore

from util.plugins.common import SlowPrint, getheaders, proxy

def HouseChanger(token, _type):
    house = {
        1: "Hype Squad Bravery",
        2: "Hype Squad Brilliance",
        3: "Hype Squad Balance",
    }
    #cmudar hypesquad
    hypesqad_req = {'house_id': _type}
    requests.post('https://discord.com/api/v9/hypesquad/online', headers=getheaders(token), json=hypesqad_req)
    SlowPrint(f"\n{Fore.GREEN}Hypesquad mudou para {Fore.WHITE}{house[_type]}{Fore.GREEN} ")
    print("Digite qualquer coisa para continuar. . . ", end="")
    input()
    Tz.main()

def StatusChanger(token, Status):
    #mudar status 
    custom_status = {"custom_status": {"text": Status}} #{"text": Status, "emoji_name": "☢"} if you want to add an emoji to the status
    try:
        requests.patch("https://discord.com/api/v9/users/@me/settings", proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=custom_status)
        SlowPrint(f"\n{Fore.GREEN}Status alterado para {Fore.WHITE}{Status}{Fore.GREEN} ")
    except Exception as e:
        print(f"{Fore.RED}Erro:\n{e}\nOcorreu ao tentar alterar o status :/")
    print("Digite qualquer coisa para continuar. . . ", end="")
    input()
    Tz.main()

def BioChanger(token, bio):
    #mudar biografia
    custom_bio = {"bio": str(bio)}
    try:
        requests.patch("https://discord.com/api/v9/users/@me", proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=custom_bio)
        SlowPrint(f"\n{Fore.GREEN}Bio changed to {Fore.WHITE}{bio}{Fore.GREEN} ")
    except Exception as e:
        print(f"{Fore.RED}Erro:\n{e}\nOcorreu ao tentar alterar o status :/")
    print("Digite qualquer coisa para continuar. . . ", end="")
    input()
    Tz.main()
