from selenium import webdriver

PATH = '/usr/bin/chromewebdriver'
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")