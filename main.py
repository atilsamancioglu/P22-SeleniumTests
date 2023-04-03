from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
'''
driver.get("https://google.com")
input_element_by_class_name = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element_by_name = driver.find_element(By.NAME, "q")

print(input_element_by_class_name)
print(input_element_by_name)
time.sleep(4)

input_element_by_name.send_keys("atil samancioglu")

search_button = driver.find_element(By.NAME, "btnK")
time.sleep(4)
search_button.click()  # element not intractable without sleep
time.sleep(4)
'''
driver.get("https://atilsamancioglu.com")
#time.sleep(4)
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div/header/div[1]/div[3]/nav/div/ul/li[3]/a")))
blog_page = driver.find_element(By.XPATH,"/html/body/div/header/div[1]/div[3]/nav/div/ul/li[3]/a")
blog_page.click()
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME,"button")))
#time.sleep(4)
read_button = driver.find_element(By.CLASS_NAME,"button")
read_button.click()
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div/div[1]/div[2]/aside[4]")))
#time.sleep(4)
#article_list = driver.find_elements(By.XPATH,"/html/body/div/div[1]/div[2]/aside[4]")
article_list = driver.find_element(By.XPATH,"/html/body/div/div[1]/div[2]/aside[4]")
print(f" atilsamancioglu.com has {len(article_list.text.splitlines())} blog posts")


while True:
    continue
