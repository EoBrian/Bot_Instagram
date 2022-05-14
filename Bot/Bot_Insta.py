from time import sleep
from os import system

from selenium import webdriver
from selenium.webdriver.opera.options import Options
from selenium.webdriver.common.keys import Keys



class BotInstagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        
        options = Options()
        options.binary_location = "C:/Users/remis/AppData/Local/Programs/Opera GX/launcher.exe"
        
        self.browser = webdriver.Opera(executable_path="operadriver.exe", options = options)


    def login(self):
        browser = self.browser
        browser.get('https://www.instagram.com/')
        
        sleep(1)

        #input name="username"
        usuário = browser.find_element_by_xpath('//input[@name="username"]')
        usuário.clear()
        usuário.send_keys(self.username)
        
        #input name="password"
        senha = browser.find_element_by_xpath("//input[@name='password']")
        senha.clear()
        senha.send_keys(self.password)

        #efetua o login
        sleep(1)
        entrar = browser.find_element_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]')
        entrar.send_keys(Keys.ENTER)


    def procurarHashtag(self, hashtag):
        browser = self.browser

        #Pesquisa a hashtag desejada
        sleep(5)
        browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')


    def cutindoPubicação(self, numero_de_curtidas = 1):
        browser = self.browser

        #Clicando na primeira publicação
        sleep(3)
        browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div[1]/div[2]').click()
  
        for publicação in range(1, numero_de_curtidas):
            #Curte a publicação
            sleep(2)
            try:
                browser.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button').click()
            except:
                self.exitBrowser()

            #comentando nas fotos
            sleep(3)
            comentario = browser.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/textarea')
            comentario.clear()
            comentario.send_keys('Ótimo conteudo!')

            #enviando o comentário
            sleep(3)
            enviar_comentario = browser.find_element_by_xpath('/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/button')
            enviar_comentario.click()

            #passa para a proxima publicação
            sleep(13)
            if publicação == 1:
                browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/div/button').click()
            else:
                browser.find_element_by_xpath('/html/body/div[6]/div[2]/div/div[2]/button').click()


    def exitBrowser(self):
        browser = self.browser
        browser.close()
