from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Game:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(executable_path="chromedriver.exe"))
        self.link = "https://orteil.dashnet.org/cookieclicker/"
        self.cookie_id = "bigCookie"
        self.cookie_count_id = "cookies"
        self.product_price_prefix = "productPrice"
        self.product_prefix = "product"

    def find_element_by_id(self, id):
        return self.driver.find_element(By.ID, id)
    
    def find_element_by_xpath(self, xpath):
        return self.driver.find_element(By.XPATH, xpath)

    def start(self):
        self.driver.get(self.link)
        lang_xpath = "//*[contains(text(), 'English')]"

        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, lang_xpath)))
        self.find_element_by_xpath(lang_xpath).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.ID, self.cookie_id)))

    def play(self):
        time.sleep(10)
        while True:
            self.find_element_by_id(self.cookie_id).click()
            cookie_count_text = self.find_element_by_id(self.cookie_count_id).text.split(" ")[0]
            cookie_count = int(cookie_count_text.replace(",", ""))
            
            for i in range(4):
                product_price_id = self.product_price_prefix + str(i)
                product_id = self.product_prefix + str(i)
                product_price_text = self.find_element_by_id(product_price_id).text.replace(",", "")
                if not product_price_text.isdigit():
                    continue
                product_price = int(product_price_text)
                if cookie_count >= product_price:
                    self.find_element_by_id(product_id).click()
                    break

game = Game()
game.start()
game.play()