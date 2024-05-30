from django.shortcuts import redirect
from selenium import webdriver
# from webdriver_manager.firefox import GeckoDriverManager
# from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
LOGIN_URL = 'https://www.facebook.com/login.php'

class FacebookLogin():
    isLogged = False
    def __init__(self, email, password, browser='Chrome'):
        # Store credentials for login
        self.email = email
        self.password = password
        if browser == 'Chrome':
            # Use chrome
            self.driver = webdriver.Chrome()
        elif browser == 'Firefox':
            # Set it to Firefox
            self.driver = webdriver.Firefox()
        self.driver.get(LOGIN_URL)
        time.sleep(1) # Wait for some time to load
 
    def login(self):
        email_element = self.driver.find_element(By.ID, 'email')
        email_element.send_keys(self.email) # Give keyboard input
 
        password_element = self.driver.find_element(By.ID, 'pass')
        password_element.send_keys(self.password) # Give password as input too

        password_element.send_keys(Keys.RETURN)
        time.sleep(3) # Wait for 2 seconds for the page to show up

        if self.driver.title == 'Log in to Facebook':
            self.isLogged = False
            self.driver.close()
        
        else:
            self.isLogged = True
        

