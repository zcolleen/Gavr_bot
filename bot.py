from selenium import webdriver
from time import sleep

class Gavr():
    def __init__(self):
        
#отключаем все звуки в браузере на время нашей сессии
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("--mute-audio")

        self.username = input('Введите ваше имя и фамилию: ')
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
    
    def texting(self):

        headers_on = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i')
        headers_on.click()

        choose_text = self.driver.find_element_by_xpath('//*[@id="message-input"]')
        choose_text.send_keys('Здравствуйте')
    
        send = self.driver.find_elements_by_xpath('//*[contain(@class, "icon--2q1XXw icon-bbb-send")]')
        #//*[@id="tippy-100"]/span[1]/i
        #send.click()
        '''
        rand = 60
        send = []
        while True:
            if len(send) == 0:
                send = self.driver.find_elements_by_xpath('//*[@id="tippy-{}"]/span[1]/i'.format(rand))
                rand += 1
            else:
                print('//*[@id="tippy-{}"]/span[1]/i'.format(rand))
                break
        print(rand)
        '''
        #send.click()
        print('delim')
        print(send)
bot = Gavr()
bot.login()
sleep(5)
bot.texting()