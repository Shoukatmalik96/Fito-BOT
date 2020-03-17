import time

import self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

base_url="https://www.fulcrum-pk.com/"
driver = webdriver.Chrome('E:/Chrome driver/chromedriver.exe')
driver.maximize_window()
driver.get(base_url)
 #getting title of a page
web_title= driver.title
 #verifying the page title ()
assert web_title == 'Top Recruitment Agency Pakistan | Local Employment Company'
 #clicking all the social icon tabs
print("Page title" + web_title)
driver.find_element_by_xpath('//*[@id="top-bar-inner"]/div/div[1]/div/span/a[1]/span').click()
driver.find_element_by_xpath('//*[@id="top-bar-inner"]/div/div[1]/div/span/a[2]').click()
driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w')
driver.find_element_by_xpath('//*[@id="top-bar-inner"]/div/div[1]/div/span/a[3]/span').click()
driver.find_element_by_xpath('//*[@id="top-bar-inner"]/div/div[1]/div/span/a[4]').click()
driver.find_element_by_xpath('//*[@id="top-bar-inner"]/div/div[1]/div/span/a[5]').click()
driver.find_element_by_xpath('//*[@id="top-bar-inner"]/div/div[1]/div/span/a[6]').click()


