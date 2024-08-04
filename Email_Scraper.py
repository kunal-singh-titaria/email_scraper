from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import csv
import random
import time
scroll=0
service=Service(executable_path="chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.maximize_window()
time.sleep(3)

driver.get("https://google.com")

WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "gLFyf"))
)

input_element=driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("cfo+software+delhi+email+gmail.com site:www.linkedin.com"+ Keys.ENTER)
WebDriverWait(driver, 60).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "gLFyf"))
)

select=driver.find_element(By.CLASS_NAME, ("srp"))
element=driver.find_element(By.TAG_NAME, ("body"))

while True:
 element.send_keys(Keys.PAGE_DOWN)
 scroll=scroll+1
 time.sleep(0.7)
 if(scroll>=20):
  scroll=0
  break

click_element=driver.find_element(By.CLASS_NAME,("RVQdVd")).click()
time.sleep(2)
while True:
 element.send_keys(Keys.PAGE_DOWN)
 scroll=scroll+1
 time.sleep(0.7)
 if(scroll>=3):
  scroll=0
  break

click_element=driver.find_element(By.CLASS_NAME,("RVQdVd")).click()
time.sleep(2)
while True:
 element.send_keys(Keys.PAGE_DOWN)
 scroll=scroll+1
 time.sleep(0.7)
 if(scroll>=3):
  scroll=0
  break
click_element=driver.find_element(By.CLASS_NAME,("RVQdVd")).click()
time.sleep(2)

while True:
 element.send_keys(Keys.PAGE_DOWN)
 scroll=scroll+1
 time.sleep(0.7)
 if(scroll>=3):
  scroll=0
  break
 
click_element=driver.find_element(By.CLASS_NAME,("RVQdVd")).click()
time.sleep(2)

while True:
 element.send_keys(Keys.PAGE_DOWN)
 scroll=scroll+1
 time.sleep(0.7)
 if(scroll>=3):
  scroll=0
  break

click_element=driver.find_element(By.CLASS_NAME,("RVQdVd")).click()
time.sleep(2)

while True:
 element.send_keys(Keys.PAGE_DOWN)
 scroll=scroll+1
 time.sleep(0.7)
 if(scroll>=3):
  scroll=0
  break
 
click_element=driver.find_element(By.CLASS_NAME,("RVQdVd")).click()
time.sleep(2)

while True:
 element.send_keys(Keys.PAGE_DOWN)
 scroll=scroll+1
 time.sleep(0.7)
 if(scroll>=3):
  scroll=0
  break
 
click_element=driver.find_element(By.CLASS_NAME,("RVQdVd")).click()
time.sleep(2)

while True:
 element.send_keys(Keys.PAGE_DOWN)
 scroll=scroll+1
 time.sleep(0.7)
 if(scroll>=3):
  scroll=0
  break
 
time.sleep(2)

select.send_keys(Keys.CONTROL + "a")
time.sleep(3)

select.send_keys(Keys.CONTROL + "c")

time.sleep(2)

driver.get("https://email-checker.net/email-extractor")

click_element=driver.find_element(By.ID,("textInput")).click()

time.sleep(2)

text_area = driver.find_element(By.ID,("textInput"))
text_area.send_keys(Keys.CONTROL + 'v')

time.sleep(2)

extractbutton=driver.find_element(By.CLASS_NAME,("tiny-button.button-primary"))
extractbutton.click()

click_element2=driver.find_element(By.ID,("textInput")).click()

result=driver.find_element(By.ID, ("textInput"))
result.send_keys(Keys.CONTROL + "a")
time.sleep(0.3)
result.send_keys(Keys.CONTROL + "c")

driver.get("https://onlinenotepad.org/notepad")

click_element3=driver.find_element(By.ID,("editor_ifr")).click()
time.sleep(2)
text_area2 = driver.find_element(By.ID,("editor_ifr"))
#text_area2.clear()
text_area2.send_keys(Keys.CONTROL + "v")
#actions = ActionChains(driver)
#actions.send_keys(text_area, Keys.CONTROL + 'v').perform()

time.sleep(2)
click_element4=driver.find_element(By.ID,("mceu_2")).click()
time.sleep(1)
input=driver.find_element(By.ID,("txt_name"))
input.send_keys("Scraped Emails")
time.sleep(3)
click_element3=driver.find_element(By.ID,"mceu_36").click()

time.sleep(3)
driver.quit()