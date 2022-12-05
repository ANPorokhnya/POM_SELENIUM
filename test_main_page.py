import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://yandex.ru/search/?text=%D0%B3%D0%B8%D1%82%D0%BB%D0%B0%D0%B1&lr=14")
time.sleep(10)