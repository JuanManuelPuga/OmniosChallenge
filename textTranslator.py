from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class TextTranslator:
    def __init__(self, text):
        self.text = text

    def translateText(self, src, dest):
        browser = webdriver.Chrome()
        #Accessing via URL helps us to skip steps.
        browser.get("https://translate.google.co.in/?sl=" + str(src) + "&tl=" + str(dest) +"&text=" + str(self.text) +"&op=translate")
        #We retrieve the XPATH from the cookie's dialogue to accept them and go on.
        browser.find_element(By.XPATH, "//button[@aria-label='Aceptar todo']").click()
        #Timer to wait for the text to get translated.
        time.sleep(6)
        #Getting the translated text.
        output = browser.find_element(By.CLASS_NAME,'HwtZe').text
        output = output.replace("\n", "")
        browser.close()
        return output