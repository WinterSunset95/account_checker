#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 19:12:00 2022

@author: winter
"""

from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
import time

proxies =['220.247.171.90:81', '213.226.11.149:41878']

url = "https://in.tradingview.com/"

py = proxies[0]
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % py)
driver = webdriver.Chrome("/home/winter/parrot/linkedin_jobpostchecker/Input/chromedriver_linux/chromedriver", chrome_options= chrome_options)
driver.implicitly_wait(0.6)

driver.get(url)

login = False
login_after = False
email_button = False
forgot_passwd = False

def login_function():
    try:
        login = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[3]/button[1]")
        login.click()
        login = True
        time.sleep(3)
    except:
        print('retry login')
        time.sleep(3)
time.sleep(3)
while login_after == False:
    try:
        login_after = driver.find_element_by_xpath("/html/body/div[6]/div/span/div[1]/div/div/div[1]")
        login_after.click()
        login_after = True
        time.sleep(3)
        break
    except:
        print('retry login_after')
        login_function()
        time.sleep(3)
time.sleep(3)
while email_button == False:
    try:
        email_button = driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div/div/div/div/div/div[1]/div[4]/div")
        email_button.click()
        email_button = True
        time.sleep(3)
        break
    except:
        print('retry email_button')
        time.sleep(3)
while forgot_passwd == False:
    try:
        forgot_passwd = driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div/div/div/div/div/form/div[3]")
        forgot_passwd.click()
        forgot_passwd = True
        time.sleep(3)
        break
    except:
        print('retry forgot_passwd')
        time.sleep(3)

# =============================================================================
# captcha_box = driver.find_element_by_xpath("/html/body/div[2]")
# html = captcha_box.get_attribute('innerHTML')
# soup = (html, 'html5lib')
# print(soup.prettify())
# 
# =============================================================================

try:
    frame = driver.find_element_by_xpath("/html/body/div[6]/div/div[2]/div/div/div/div/div/form/div[3]/div/div/iframe")
    driver.switch_to.frame(frame)
    captcha_check = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[1]/div/div/span/div[1]")
    time.sleep(2.25312)
    captcha_check.click()
except:
    print('there seems to be no captcha')

