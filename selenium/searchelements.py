from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://inventwithpython.com')

try:
    web_elem = browser.find_element(By.CLASS_NAME, "cover-thumb")  # WebElement object
    print(f"Found <{web_elem.tag_name}> element with that class name!")
except:
    print("Was not able to find an element with that name.")

# browser.quit()