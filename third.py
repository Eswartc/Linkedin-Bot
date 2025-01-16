from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pickle
from time import sleep, time
import pandas as pd

start = time()
service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

data = 'PYTHON .xlsx'  
df = pd.read_excel(data, sheet_name='Sheet11', header = None)
job_links = df.iloc[:, 0].tolist()

driver.maximize_window()
driver.get('https://www.linkedin.com/')

# Load cookies to maintain session
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

driver.get("https://www.linkedin.com/search/results/PEOPLE/?activelyHiringForJobTitles=%5B%229%22%2C%2239%22%2C%2225206%22%2C%222732%22%2C%22204%22%2C%221586%22%2C%2213447%22%2C%221685%22%2C%221176%22%2C%22456%22%2C%22437%22%2C%22103%22%2C%22513%22%2C%22884%22%2C%229516%22%2C%2210174%22%2C%221592%22%2C%221697%22%2C%2218630%22%2C%22688%22%2C%228155%22%2C%2210326%22%2C%2213163%22%2C%221405%22%2C%221411%22%2C%2216194%22%2C%2217739%22%2C%221845%22%2C%2218890%22%2C%221916%22%2C%221945%22%2C%2219609%22%2C%2221430%22%2C%2225195%22%2C%2225581%22%2C%2225586%22%2C%222721%22%2C%222808%22%2C%2231069%22%2C%22332%22%2C%22424%22%2C%224545%22%2C%225316%22%2C%225459%22%2C%225769%22%2C%225898%22%2C%227319%22%2C%227555%22%2C%22943%22%5D&geoUrn=%5B%22103644278%22%5D&origin=FACETED_SEARCH&page=9&sid=yKW")
sleep(2)
all_buttons = driver.find_elements(By.TAG_NAME, "button")
message = [btn for btn in all_buttons if btn.text.strip() in ["Following", "Connect", "Follow"]]
cnt = 0
for i in message:    
    driver.execute_script("arguments[0].click();", i)
    cnt += 1
    dismiss_button = driver.find_element(By.CSS_SELECTOR, "button.artdeco-modal__dismiss")
    dismiss_button.click()


print(cnt)

sleep(1)
driver.quit()