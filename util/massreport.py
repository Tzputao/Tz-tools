# Esse self foi orgulhosamente codificado por Rdimo (https://instagram.com/tzfofo).
# Copyright (c) 2021 🜲 Oi, eu sou o Tz#0001 | https://instagram.com/tzfofo
# Tz Nuker sob a Licença Pública Geral GNU v2 (1991).

import requests
import threading

from colorama import Fore

def MassReport(token, guild_id1, channel_id1, message_id1, reason1):
    for i in range(500, 1000):
        while True:
            threading.Thread(target=Report, args=(token, guild_id1, channel_id1, message_id1, reason1)).start()

def Report(token, guild_id1, channel_id1, message_id1, reason1):
    Responses = {
            '401: Unauthorized': f'{Fore.RED}Token do discord inválido.',
            'Missing Access': f'{Fore.RED}Falta de acesso ao canal ou servidor.',
            'Você precisa verificar sua conta para realizar esta ação.': f'{Fore.RED} Não verificado.'
    }

    report = requests.post(
        'https://discordapp.com/api/v8/report', json={
            'channel_id': channel_id1,
            'message_id': message_id1,
            'guild_id': guild_id1,
            'reason': reason1
        }, headers={
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'sv-SE',
            'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
            'Content-Type': 'application/json',
            'Authorization': token
        }
    )
    
    if (status := report.status_code) == 201:
        print(f"{Fore.GREEN}Report enviado com sucesso!\n")
    elif status in (401, 403):
        print(Responses[report.json()['message']]+"\n")
    else:
        print(f"{Fore.RED}Erro: {report.text} | Código de status: {status}\n")