from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from time import sleep
import pickle

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)


driver.get('https://www.linkedin.com/login')


email = driver.find_element(By.ID, "username")
email.send_keys('tceswar88@gmail.com')


password = driver.find_element(By.ID, "password")
password.send_keys('Techquadebs8*')


submit = driver.find_element(By.CLASS_NAME, "//button[@type='submit']")
submit.click()


sleep(5)  
pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

driver.quit()
