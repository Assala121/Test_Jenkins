from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_path = "C:\\Users\\LENOVO\\Desktop\\TryTests\\chromedriver_win32 - Copie\\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
time.sleep(5)

driver.get("https://test2.digitalberry.fr/bcs-dashboard/#/login")
time.sleep(5)
list=[]
time.sleep(5)
#driver.find_element_by_class_name("btn btn-outline-primary font-weight-bold secondary").click()
list = driver.find_elements_by_css_selector("button [type='submit']")
time.sleep(5)

list[0].click()
time.sleep(5)


firstname = driver.find_element_by_name("first_name")
firstname.send_keys("ASSALA")
time.sleep(5)

lastname = driver.find_element_by_id("last_name")
lastname.send_keys("SEHLI")
time.sleep(5)

mail = driver.find_element_by_name("email")
mail.send_keys("assalanum121@gmail.com")
time.sleep(5)


pwd = driver.find_element_by_name("password")
pwd.send_keys("assalanum121***")
time.sleep(5)

cpwd = driver.find_element_by_id("confirmpassword")
cpwd.send_keys("assalanum121***")
time.sleep(5)


driver.quit()







