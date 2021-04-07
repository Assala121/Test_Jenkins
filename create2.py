from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
 
driver = webdriver.Chrome("C:\\Users\\LENOVO\\Desktop\\TryTests\\chromedriver_win32 - Copie\\chromedriver.exe")
driver.get("https://test2.digitalberry.fr/bcs-dashboard/#/login")
driver.maximize_window()
time.sleep(5)
#driver.find_element_by_class_name("btn btn-outline-primary font-weight-bold secondary").click()
#list=[]
#time.sleep(5)
#list = driver.find_element_by_css_selector("button [type='submit']")
#list[1].click()
#driver.find_elements_by_xpath("//button[@title=' Create an account ']").click()
#driver.find_elements_by_xpath('/html/body/app-root/div/app-login/div/div[2]/button').click()
#enter_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-login/div/div[2]/button")))
enter_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-login/div/div[2]/button")))
enter_button.click()

driver.find_element_by_name("first_name").send_keys("ASSALA")
time.sleep(5)

driver.find_element_by_id("last_name").send_keys("SEHLI")
time.sleep(5)

driver.find_element_by_name("email").send_keys("assalanum121@gmail.com")
time.sleep(5)

driver.find_element_by_name("password").send_keys("Assalanum121***")
time.sleep(5)

driver.find_element_by_id("confirmpassword").send_keys("Assalanum121***")
time.sleep(10)



assert "No results Found." not in driver.page_source
driver.quit()