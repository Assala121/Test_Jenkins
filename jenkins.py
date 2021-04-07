from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

chrome_path = "C:\\Users\\LENOVO\\Desktop\\TryTests\\chromedriver_win32 - Copie\\chromedriver.exe"
driver = webdriver.Chrome(chrome_path)

driver.get("https://keycloak.digitalberry.fr/auth/realms/DBY2/protocol/openid-connect/auth?client_id=jenkins&redirect_uri=https%3A%2F%2Fjenkins.digitalberry.fr%2FsecurityRealm%2FfinishLogin&state=db0e24c3-2e4b-45db-aabc-2d10c5c5baaa&response_type=code&scope=openid")
time.sleep(5)

username = driver.find_element_by_name("username")
username.send_keys("asehli")
time.sleep(5)
username = driver.find_element_by_name("password")
username.send_keys("Azala93933623***")
time.sleep(5)
# driver.find_element_by_css_selector('button[type="submit"]').click()
driver.find_element_by_name("login").click()
time.sleep(3)
driver.find_element_by_name("jenkins").click()
time.sleep(10)
