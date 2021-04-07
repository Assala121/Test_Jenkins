from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chrome_path = "C:\\Users\\LENOVO\\Desktop\\TryTests\\chromedriver_win32 - Copie\\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

driver.get("https://test2.digitalberry.fr/bcs-dashboard/#/login")
time.sleep(5)

username = driver.find_element_by_name("emailInput")
username.send_keys("assalanum121@gmail.com")
time.sleep(5)

password = driver.find_element_by_name("passwordInput")
password.send_keys("Assalanum121***")
time.sleep(5)

enter_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-login/div/div[2]/form/button")))
enter_button.click()
time.sleep(5) 

time.sleep(200)
#listtxt= driver.find_elements_by_css_selector("input [type='text']")
#listtxt[1].send_keys("assalanum121@gmail.com")
#driver.find_element_by_css_selector("input[name='emailInput'][value='assalanum121@gmail.com']").click()
#driver.find_element_by_class_name("primary").click()
driver.quit()



