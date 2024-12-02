from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.bilibili.com')

linkElem = browser.find_element(By.LINK_TEXT, "热门")
linkElem.click()  # follows the "Read Online for Free" link

# browser.quit()