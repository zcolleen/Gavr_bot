import pyautogui as pya
from selenium import webdriver
from time import sleep

class Gavr:

    def __init__(self,username=''):
        
        #отключаем все звуки в браузере на время нашей сессии
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--mute-audio")
        chrome_option.add_argument("--window-size=900,800")

        if username == '':
            self.username = input('Введите ваше имя: ')
        else:
            self.username = username
        if self.username == '':
            self.username = 'bot'

        self.driver = webdriver.Chrome(chrome_options=chrome_option)
        
    def login(self):

        self.driver.get('http://webinar.bmstu.ru/b/vpw-2zy-3k2')# это ссылка на мой баттон
        #http://webinar.bmstu.ru/b/q9y-xew-zr4 - это ссылка на Гаврюшина
        sleep(2)

        code_access = self.driver.find_element_by_xpath('//*[@id="room_access_code"]')
        code_access.send_keys('260165')# мой код
        #601473 - код Гаврюшина
        code_enter = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/form/div/input[2]')
        code_enter.click()
        #//*[@id="_b_q9y-xew-zr4_join_name"]
        name_access = self.driver.find_element_by_xpath('//*[@id="_b_vpw-2zy-3k2_join_name"]')
        name_access.send_keys(self.username)

        name_enter = self.driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div[2]/form/div/span/button')
        name_enter.click()
    

    def header_window(self):

        while True:
            try:
                headers_on = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i')
                break
            except Exception:
                sleep(5)
        # цикл нужен для того чтобы пытаться нажать кнопку через каждые 5 секунд (нужно в случае, если мы запустили бота раньше,
        # чем началась конференция)
            
        headers_on.click()
    
    def texting_ones(self):

        sleep(2)

        choose_text = self.driver.find_element_by_xpath('//*[@id="message-input"]')
        choose_text.send_keys('Здравствуйте')
        
        pya.moveTo(choose_text.location['x'] + 446, choose_text.location['y'] + 347)
        pya.click(button='left')

    def spam_attacker(self):

        sleep(2)

        choose_text = self.driver.find_element_by_xpath('//*[@id="message-input"]')
        pya.moveTo(choose_text.location['x'] + 446, choose_text.location['y'] + 347)

        for i in range(0, 100):
            choose_text.send_keys('Спам')
            pya.click(button='left')


bot = Gavr()
bot.login()
bot.header_window()
#bot.texting_ones()
bot.spam_attacker()

