from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

t=0
name = input('Enter the name of person')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()
while True:

    try:
        online_status = driver.find_element_by_xpath('//span[@title = "{}"]'.format('online'))
        if t==0:
            print(name, " is online")
        t=1
    except:
        if t==1:
            print(name, " went offline")
        t=0                
    time.sleep(1)
    
