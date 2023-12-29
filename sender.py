from time import sleep 
from selenium import webdriver
from selenium.webdriver.common.by import By

from manager import get_word


class AdabBot:
    def __init__(self, url, number):
        self.driver = webdriver.Firefox()
        self.number = number
        self.url = url

    def login(self):
        self.driver.get(self.url)
        sleep(4)
        self.driver.find_element(By.XPATH, '/html/body/app-root/tab-login/div/div/div[2]/div[1]/div/div[3]/div[3]/input[1]').send_keys(self.number)
        self.driver.find_element(By.XPATH, '/html/body/app-root/tab-login/div/div/div[2]/div[1]/div/div[3]/button/div/div').click()

        otp = int(input('Please enter you OTP code: '))
        self.driver.find_element(By.XPATH, '//*[@id="auth-pages"]/div/div[2]/div[1]/div/div[4]/div/input').send_keys(otp)
        sleep(10)

    def send_word(self):
        self.driver.find_element(By.XPATH, '//*[@id="folders-container"]/div[1]/ul/li[1]/div[1]/div').click()
        sleep(2)
        while True:
            self.driver.find_element(By.XPATH, '//*[@id="emoji-dropdown"]/div[1]/div[1]/div[1]/div[3]/div[1]/div/div[2]').send_keys(get_word())
            self.driver.find_element(By.XPATH, '/html/body/app-root/div/div/div[2]/tab-container/div/tab-view/div/tab-conversation/div[3]/div[1]/div[1]/div[2]/button/div[1]/div').click()
            print("=================================")
            sleep(5)

    def run(self):
        self.login()
        self.send_word()


bot = AdabBot('https://web.shad.ir/', '09053853700')
bot.run()