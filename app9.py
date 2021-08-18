from selenium import webdriver
import time

import selenium

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        username = self.browser.find_element_by_xpath("//*[@id='login_field']")
        password = self.browser.find_element_by_xpath("//*[@id='password']")
        username.send_keys(self.username)
        password.send_keys(self.password)

        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]").click()
    
    
    def getFollowers(self):
        #enter username in #####
        self.browser.get("https://github.com/ceydab?tab=followers")
        time.sleep(2)



#put a valid username and password while calling the class
github = Github("ceydab", "")
github.signIn()    