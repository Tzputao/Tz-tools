# Esse self foi orgulhosamente codificado por Tz (https://instagram.com/tzfofo).
# Copyright (c) 2021 🜲 Oi, eu sou o Tz#0001 | https://instagram.com/tzfofo
# Tz Tools sob a Licença Pública Geral GNU v2 (1991).

import requests

from colorama import Fore

from util.plugins.common import getheaders, proxy, RandomChinese

def SpamServers(token, icon, name=None):
    if name:
        for i in range(4):
            try:
                #Crie todos os servidores com o nome que você quiser
                payload = {'name': f'{name}', 'region': 'europe', 'icon': icon, 'channels': None}
                requests.post('https://discord.com/api/v7/guilds', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=payload)
                print(f"{Fore.BLUE}Criado {name}.{Fore.RESET}")
            except Exception as e:
                print(f"A seguinte exceção foi encontrada e está sendo ignorada: {e}")
    else:
        for i in range(4):
            server_name = RandomChinese(5,12)
            try:
                #Crie todos os servidores com o nome que você quiser
                payload = {'name': f'{server_name}', 'region': 'europe', 'icon': icon , 'channels': None}
                requests.post('https://discord.com/api/v7/guilds', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=payload)
                print(f"{Fore.BLUE}Criado {server_name}.{Fore.RESET}")
            except Exception as e:
                print(f"A seguinte exceção foi encontrada e está sendo ignorada: {e}")