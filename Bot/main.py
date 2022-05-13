from os import system
from Bot_Insta import BotInstagram


if __name__ == '__main__':
    system('cls')
    
    username = str(input('USUÁRIO: ')).strip().lower()
    password = str(input('SENHA: ')).strip()
    tag = str(input('DIGITE UMA TAG OU HASHTAG: ')).strip().lower()
    quantidade = int(input('DIGITE O NÚMERO DE PUBLICAÇÕES: '))

    bot = BotInstagram(username, password)
    bot.login()
    bot.procurarHashtag(tag)
    bot.cutindoPubicação(quantidade)
    bot.exitBrowser()
    
    system('cls')