from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.Chrome()
try:
    browser.get('https://item.jd.com/4130061.html')
    wait = WebDriverWait(browser, 10)
    detail = browser.find_element_by_id('detail')

    print(detail)
finally:
    browser.close()

user_input = "https://search.jd.com/Search?keyword=插排&enc=utf-8&wq=插排"
chapa_url = "https://search.jd.com/Search?keyword=%E6%8F%92%E6%8E%92&enc=utf-8&wq=%E6%8F%92%E6%8E%92"
