import time

import bson
import console as console
import requests
import sys
import pymongo
from bson import ObjectId
from selenium import webdriver
#def script():

uri = 'mongodb://shoukatmalik:shoukat12345@ds221416.mlab.com:21416/fitotouch';


client = pymongo.MongoClient('mongodb://shoukatmalik:shoukat12345@ds221416.mlab.com:21416/fitotouch')
db = client.fitotouch
#fetch all collection
#cursor = db.orders.find({ })
#fetch single record by Id
#cursor =db.orders.find({'_id': bson.ObjectId("")})
cursor =db.orders.find({ })
#Iterate the cursor and print the documents.
for document in cursor:
 print(document)

 

base_url="http://www.fitotouch.com"
base_url1= "https://www.fitotouch.com/qitouch"
qty: int=2
cart_value : int = 1
driver = webdriver.Chrome('E:/Chrome driver/chromedriver.exe')
driver.maximize_window()
    #function of our 'driver' object.
driver.implicitly_wait(10) #10 is in seconds
driver.get(base_url)
driver.implicitly_wait(10)

driver.find_element_by_name('password').send_keys("fitotouch")
driver.implicitly_wait(10)
driver.find_element_by_class_name('arrow-icon').click()
data = requests.get('http://110.93.230.117:1403/api/order/5e439b7052fcf2189ccb5207').json()
print(data)

driver.implicitly_wait(10)
time.sleep(2.4)

#driver.find_element_by_xpath('//*[@id="header"]/div[2]/div/div[2]/div[3]/div[1]/a/span').click()
time.sleep(2.4)
driver.get('https://www.fitotouch.com/account/login/create')
time.sleep(2.4)
driver.switch_to.frame("accountFrame")
time.sleep(2.4)
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div[1]/div/input').send_keys("Raja")
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div[2]/div/input').send_keys("kumar")
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/input').send_keys("rohit.kumar@danatonline.com")
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[3]/div/input').send_keys("fitotouch")
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[4]/div/input').send_keys("fitotouch")
driver.find_element_by_xpath('//*[@id="root"]/div/div/div/button').click()
driver.get("https://www.fitotouch.com/fitoki/f-001-jing-fang-bai-du-wan")
#product_category=['driver.get("https://www.fitotouch.com/fitoki/f-001-jing-fang-bai-du-wan")','driver.get("https://www.fitotouch.com/soria-chinasor/style-02-hzewl")']
driver.execute_script("window.scrollTo(0, 150)")
time.sleep(2.4)
cart = driver.find_element_by_xpath('/html/body/div[1]/main/article/section/div[2]/div/section/article/section[1]/section/div/div[3]/div/div')

#     if qty > 0:
#
#       for i in range(qty):
#        cart.click()
#        time.sleep(2.4)
#       # print("quantity was" +qty)
#
#     else:
#      cart.click()
#
#      url = driver.current_url
#      print(url)
#      #print("quantity was" + qty)
#
# last_row = 0  # example that there are currently 10 rows in the DB table
# while True:
#     # query database for number of rows "SELECT count(id) from table"
#     result = db.fetchone()
#     if result > last_row:
#         script()
#         last_row = result
#     time.sleep(10)
#
# print("Method is called")
#FITO NAMES
# driver.find_element_by_link_text("FiveSeasons").click()
# driver.find_element_by_xpath('/html/body/div[1]/main/article/section/div[2]/div/section/div/div[1]/a').click()
# driver.get("https://www.fitotouch.com/fitoki/f-001-jing-fang-bai-du-wan")
# driver.execute_script("window.scrollTo(0, 150)")
# time.sleep(2.4)
# driver.find_element_by_xpath('//*[@id="sections"]/section/div[2]/div/section/article/section[1]/section/div/div[3]').click()
# time.sleep(2.4)
#
#
#
# #driver.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/div[2]/div[3]/div[2]/a/span/svg').click()
# driver.get("https://www.fitotouch.com/cart")
# time.sleep(2.4)
# #driver.execute_script("window.scrollTo(300, 0)")
# driver.get("https://www.fitotouch.com/checkout")
# driver.find_element_by_xpath('//*[@id="checkout"]/div/div[3]/div/div/div[1]/div[1]/div[2]/form/div[1]/div[1]/input').send_keys("helderpereira.mtc@gmail.com")
#
# driver.find_element_by_xpath('//*[@id="checkout"]/div/div[3]/div/div/div[1]/div[1]/div[2]/form/div[3]/button').click()
#
# driver.find_element_by_xpath('//*[@id="checkout"]/div/div[3]/div/div/div[1]/div[2]/div[2]/form/div[1]/div[1]/div[1]/input').send_keys("helder")
# driver.find_element_by_xpath('//*[@id="checkout"]/div/div[3]/div/div/div[1]/div[2]/div[2]/form/div[1]/div[1]/div[2]/input').send_keys("Malik")
# driver.find_element_by_xpath('//*[@id="checkout"]/div/div[3]/div/div/div[1]/div[2]/div[2]/form/div[1]/div[2]/div[1]/div[1]/input').send_keys("port qasim")
# driver.find_element_by_xpath('//*[@id="checkout"]/div/div[3]/div/div/div[1]/div[2]/div[2]/form/div[1]/div[2]/div[4]/input').send_keys("5426")
# driver.find_element_by_xpath('//*[@id="checkout"]/div/div[3]/div/div/div[1]/div[2]/div[2]/form/div[1]/div[2]/div[5]/input').send_keys("karachi")
# driver.find_element_by_xpath('//*[@id="checkout"]/div/div[3]/div/div/div[1]/div[2]/div[2]/form/div[1]/div[2]/div[6]/input').send_keys("sindh")
# driver.find_element_by_xpath('//*[@id="checkout"]/div/div[3]/div/div/div[1]/div[2]/div[2]/form/div[1]/div[3]/input').send_keys("031545454")
# time.sleep(2.4)
#
# driver.find_element_by_xpath('//*[@id="checkout"]/div/div[3]/div/div/div[1]/div[2]/div[2]/form/div[4]').click()
# time.sleep(2.4)
#
# driver.find_element_by_xpath('//*[@id="checkout"]/div/div[3]/div/div/div[1]/div[3]/div[2]/div/form/div[7]').click()
# time.sleep(2.4)
#
# driver.find_element_by_xpath('//*[@id="checkout"]/div/div[3]/div/div/div[1]/div[4]/div[2]/div[4]').click()
# time.sleep(2.4)
#
# url = driver.current_url
# url1 = url.split('=')[1].split('&')[0]
# print(url1)
# #driver.find_element_by_xpath('/html/body/div[1]/header/div[3]/div/div[2]/div[3]/div[2]').click()
# ''
# #driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div/div/div[2]/button/span').click()
# #driver.find_element_by_link_text("Giovanni Maciocia").click()
# #driver.find_element_by_link_text("Soria - Composor").click()
# #driver.find_element_by_link_text("Fitoki").click()
# #driver.find_element_by_link_text("Soria - Chinasor").click()
# #driver.find_element_by_link_text("Ben Cao").click()
# #driver.find_element_by_link_text("Blue Poppy").click()
# #driver.find_element_by_link_text("Qitouch").click()
#
#
#
#
# #productsURL= ["https://www.fitotouch.com/qitouch/personal-monopost","https://www.fitotouch.com/shop/10023bk","https://www.fitotouch.com/bluepoppy/blue-poppy-zhi-bai-di-huang-wan"]
#
# #for x in productsURL:
# #driver.execute_script("window.open('https://www.fitotouch.com/qitouch');")
# #driver.find_element_by_class_name("sqs-add-to-cart-button-wrapper").click()

