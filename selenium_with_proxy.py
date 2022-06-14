#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 07:32:16 2022

@author: winter
"""

from selenium import webdriver

# the proxy server-
# Note that free proxy servers are not persistant and may become invalid after a while
# a list of available proxy servers are available at https://www.proxynova.com/proxy-server-list/
# Make sure you always pick one with an "anonymous" flag
py = '3.128.120.252:80'
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % py)
driver = webdriver.Chrome("/home/winter/parrot/linkedin_jobpostchecker/Input/chromedriver_linux/chromedriver", chrome_options= chrome_options)
driver.implicitly_wait(0.6)

# just a test website
driver.get("http://whatsmyip.com")

# The rest of the code can go here -