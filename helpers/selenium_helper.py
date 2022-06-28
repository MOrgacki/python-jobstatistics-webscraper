
from configparser import ConfigParser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import BaseWebDriver
from selenium.webdriver.chrome.options import Options
from locator import Locator


class SeleniumHelper(BaseWebDriver):

    def __init__(self) -> None:
        self.driver = webdriver.Chrome('./chromedriver')
        # options = Options()
        # options.add_argument('--headless')
        # options.add_argument('--disable-gpu')
        # self.driver = webdriver.Chrome(
        #     './chromedriver', options=options)

    def login(self, username: str, password: str, login_url: ConfigParser) -> None:
        self.driver.get(login_url)
        email_input = self.driver.find_element(
            by=By.CSS_SELECTOR, value=Locator.email)
        password_input = self.driver.find_element(
            by=By.CSS_SELECTOR, value=Locator.password)
        login_button = self.driver.find_element(
            by=By.CSS_SELECTOR, value=Locator.login_btn)

        email_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

    def cookies_handler(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, Locator.accept_cookies_btn)))
        cookies_button = self.driver.find_element(
            by=By.CSS_SELECTOR, value=Locator.accept_cookies_btn)
        cookies_button.click()
