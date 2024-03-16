from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open('cookie.json', 'r') as file:
    cookies = json.load(file)

driver = webdriver.Chrome()
url = "https://nationaleyecenter.id/nlc-cms/" 
driver.get(url)

for cookie in cookies:
    if 'sameSite' in cookie:
        del cookie['sameSite'] 
    driver.add_cookie(cookie)

def init_urls():
    start_urls = []
    url1 = "https://nationaleyecenter.id/wp-admin/edit.php?post_type=post&all_posts=1"
    url2 = "&paged="

    for page in range(1, 21):
        start_urls.append(url1 + url2 + str(page))
    return start_urls

start_urls = init_urls()
for start_url in start_urls:
    driver.get(start_url)
    time.sleep(3)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "pagination-links")))
    kata_kunci = driver.find_element(By.CSS_SELECTOR, "td.rank_math_seo_details.column-rank_math_seo_details > span:nth-child(3) > span").text
    print(kata_kunci)

driver.get(start_url)
driver.close()

#post-14746 > td.rank_math_seo_details.column-rank_math_seo_details > span:nth-child(3) > span
#post-14288 > td.rank_math_seo_details.column-rank_math_seo_details > span:nth-child(3) > span
#post-14277 > td.rank_math_seo_details.column-rank_math_seo_details > span:nth-child(3) > span