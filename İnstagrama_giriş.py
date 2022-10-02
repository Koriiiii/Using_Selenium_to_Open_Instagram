
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

username = "username"
password = "password"

class Instagram:

    drive_path = "C:/Users/PC/Desktop/python_/Selenium-ChromeDriver/chromedriver"

    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.browser = webdriver.Chrome(Instagram.drive_path)

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(3)

        usernameInput = self.browser.find_element(By.NAME,"username")
        passwordInput = self.browser.find_element(By.NAME,"password")

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        passwordInput.send_keys(Keys.ENTER)


app = Instagram(username, password)

app.signIn()