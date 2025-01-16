from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pickle
from time import sleep, time
import pandas as pd
from messages import first as first_message

start = time()
service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)

data = 'PYTHON .xlsx'  
df = pd.read_excel(data, sheet_name='Sheet11', header = None)
job_links = df.iloc[2].tolist()
#job_links = ["https://www.linkedin.com/search/results/all/?fetchDeterministicClustersOnly=true&heroEntityKey=urn%3Ali%3Afsd_profile%3AACoAAANbp2gBeFB_bwVj6piv0M1Ej4pIRMQqo0Q&keywords=tejus%20prasad&origin=RICH_QUERY_TYPEAHEAD_HISTORY&position=0&searchId=7137f5e5-bcb6-446a-84f9-726942acdfc3&sid=RFu&spellCorrectionEnabled=true"]

driver.maximize_window()
driver.get('https://www.linkedin.com/')

# Load cookies to maintain session
cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()
cnt = 0
for i in job_links:
    driver.get(i)
    cnt += 1
    sleep(2)
    flag = False
    try:
        wrapper_div = driver.find_element(By.CLASS_NAME, "jobs-search__job-details--wrapper")
    except:
        flag = True
        wrapper_div = driver.find_element(By.CLASS_NAME, "authentication-outlet")
    entry_point = None



    while not entry_point:
        try:
            entry_point = wrapper_div.find_element(By.CLASS_NAME, "entry-point")
        except:
            pass
        if flag:
            driver.execute_script("window.scrollBy(0, 300);")
        driver.execute_script("arguments[0].scrollBy(0, 145);", wrapper_div)
        
    sleep(1)

    all_buttons = driver.find_elements(By.TAG_NAME, "button")
    message_button = [btn for btn in all_buttons if btn.text.strip() == "Message"][0]
    driver.execute_script("arguments[0].click();", message_button)
    sleep(2)
    messaging_div = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Messaging']")
    section = messaging_div.find_element(By.CSS_SELECTOR, "section.msg-inmail-credits-display")    
    paragraph_text = section.find_element(By.CSS_SELECTOR, "p").text
    
    if "Free message" in paragraph_text:
        print("This is a free message.")
        message_text_area = messaging_div.find_element(By.CSS_SELECTOR, "div[aria-label='Write a message…']")
        sleep(1)
        message_text_area.clear()
        sleep(1)
        driver.execute_script("arguments[0].innerHTML = arguments[1];", message_text_area, first_message)

        send = messaging_div.find_element(By.XPATH, "//button[@type = 'submit']")
        

    else:
        print("This is not a free message.")
    sleep(10)
    print(cnt)

print("finished")
finish = time()
print('Time taken', finish - start)