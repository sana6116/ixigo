from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time


search = input("Enter the item you want to search: ")

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.flipkart.com/search?q="+search)
time.sleep(10)

items = []

name = driver.find_elements(By.CLASS_NAME, "s1Q9rs")
price = driver.find_elements(By.CLASS_NAME, "_30jeq3")
rate = driver.find_elements(By.CLASS_NAME, "_3LWZlK")
details = driver.find_elements(By.CLASS_NAME, "_3Djpdu")

for i in range(len(name)):
    items.append({
    "Name" : name[i].text,
    "Price" : price[i].text,
    "Rate" : rate[i].text,
    "Detail" : details[i].text,
    "URL" : name[i].get_attribute("href"),
    })


df = pd.DataFrame(items)
df.to_csv("items.csv", index=False)



driver.quit()