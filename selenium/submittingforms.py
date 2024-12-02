from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("https://login.metafilter.com")
userElem = browser.find_element(By.ID, 'user_name')
userElem.send_keys("your_real_username_here")

passwordElem = browser.find_element(By.ID, 'user_pass')
passwordElem.send_keys('your_real_password_here')
passwordElem.submit()

# browser.get("https://www.bilibili.com")
# userElem = browser.find_element(By.CLASS_NAME, "header-login-entry")
# userElem.click()

# # 睡眠 3 秒等待完全加载完成，再尝试读取 dom 元素
# time.sleep(3)
# userElem = browser.find_elements(By.CLASS_NAME, "login-tab-item")
# print(userElem[1].text)
# userElem[1].click()

# userElem = browser.find_element(By.CSS_SELECTOR, "input[maxlength='15'][placeholder='请输入手机号']")
# userElem.send_keys("13022222222")