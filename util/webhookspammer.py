# Esse self foi orgulhosamente codificado por Tz (https://instagram.com/tzfofo).
# Copyright (c) 2021 🜲 Oi, eu sou o Tz#0001 | https://instagram.com/tzfofo
# Tz Tools sob a Licença Pública Geral GNU v2 (1991).

import requests
import Tz

from time import sleep
from colorama import Fore

from util.plugins.common import SlowPrint, proxy

def WebhookSpammer(WebHook, Message):
    SlowPrint("\"ctrl + c\" a qualquer momento para parar\n")
    sleep(1.5)
    #spam o webhook com a mensagem 
    while True:
        response = requests.post(
            WebHook,
            proxies={"http": f'{proxy()}'},
            json = {"content" : Message},
            params = {'wait' : True}
        )
        try:
            #verifique se o status foi enviado ou se tem taxa limitada
            if response.status_code == 204 or response.status_code == 200:
                print(f"{Fore.GREEN}Mensagem enviada{Fore.RESET}")
            elif response.status_code == 429:
                print(f"{Fore.YELLOW}Taxa limitada ({response.json()['retry_after']}ms){Fore.RESET}")
                #se tivermos limite de taxa, pause até que o limite de taxa termine
                sleep(response.json()["retry_after"] / 1000)
            else:
                print(f"{Fore.RED}Erro : {response.status_code}{Fore.RESET}")

            sleep(.01)
        except KeyboardInterrupt:
            break

    SlowPrint(f'{Fore.RED}Webhook com spam!{Fore.RESET} ')
    print("Digite qualquer coisa para continuar. . . ", end="")
    input()
    Tz.main()