#python selenium basic example web scraping
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary(r'"C:\Program Files\Mozilla Firefox\firefox.exe"')
driver = webdriver.Firefox(firefox_binary=binary)

driver.get('http://forums.animesuki.com')
driver.find_element_by_id('navbar_username').send_keys('username')
driver.find_element_by_id('navbar_password').send_keys('password')
driver.find_element_by_xpath('//input[@value=\'Log in\']').click()   //or driver.find_element_by_id(“submit”).click()  - there are many ways to find an element
#[https://crossbrowsertesting.com/blog/test-automation/automate-login-with-selenium/, https://selenium-python.readthedocs.io/locating-elements.html]