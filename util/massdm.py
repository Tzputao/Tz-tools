# Esse self foi orgulhosamente codificado por Rdimo (https://instagram.com/tzfofo).
# Copyright (c) 2021 🜲 Oi, eu sou o Tz#0001 | https://instagram.com/tzfofo
# Tz Nuker sob a Licença Pública Geral GNU v2 (1991).

import requests

from colorama import Fore
from util.plugins.common import setTitle, proxy

def MassDM(token, channels, Message):
    for channel in channels:
        for user in [x["username"]+"#"+x["discriminator"] for x in channel["recipients"]]:
            try:
                setTitle(f"Mensagens "+user)
                requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
                    proxies={"http": f'{proxy()}'},
                    headers={'Authorization': token},
                    data={"content": f"{Message}"})
                print(f"{Fore.RED}Mensagem: {Fore.WHITE}"+user+Fore.RESET)
            except Exception as e:
                print(f"O seguinte erro foi encontrado e está sendo ignorado: {e}")