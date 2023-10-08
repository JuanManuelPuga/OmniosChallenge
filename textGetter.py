from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TextGetter:
    def __init__(self, title):
        self.title = title

    def getText(self):
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)
        driver.maximize_window()
        driver.get("https://deepai.org/machine-learning-model/text-generator")
        #Waiting for the cookie's dialogue to appear and click in the Accept button.
        result = wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/button[2]"))).click()
        text = "The text of " + self.title + " is: "
        driver.find_element(By.NAME, "text").send_keys(text)
        driver.find_element(By.ID, "modelSubmitButton").click()
        #Waiting to the text to appear. This web has a placeholder picture so its easier to wait for the element to appear.
        result = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "pre"))).text
        driver.close()
        return result