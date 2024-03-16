from selenium import webdriver
import json

with open('cookie.json', 'r') as file:
    cookies = json.load(file)

driver = webdriver.Chrome()
url = "https://nationaleyecenter.id/nlc-cms/"
driver.get(url)

for cookie in cookies:
    if 'sameSite' in cookie:
        del cookie['sameSite'] 
    driver.add_cookie(cookie)

driver.refresh()
driver.get("https://nationaleyecenter.id/wp-admin/")
