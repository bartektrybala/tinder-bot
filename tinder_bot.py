from selenium import webdriver
from time import sleep

from passwords import email, password

class TinderBot():
 
    def __init__(self):
        self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(2)
        login_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/header/div[1]/div[2]/div/button/span')
        login_btn.click()
        sleep(1)
        fb_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
        fb_btn.click()

        sleep(4)
        # switch to login popup
        base_window = self.driver.window_handles[0]
        popup = self.driver.switch_to_window(self.driver.window_handles[1])

        sleep(5)

        email_in = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_in.send_keys(email)
        
        sleep(2)

        pass_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pass_in.send_keys(password)

        sleep(2)

        login_btn = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_btn.click()

        self.driver.switch_to_window(base_window)

        sleep(2)

        popun_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]/span')
        popun_btn.click()

        sleep(1)

        pupun2_btn = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[2]')
        pupun2_btn.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()
        
    def auto_swipe(self):
        while True:
            sleep(1)
            try:    
                self.like()
            except Exception:
                sleep(1)
                self.close_match()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[3]/button')
        match_popup.click()


bot = TinderBot()
bot.login()
