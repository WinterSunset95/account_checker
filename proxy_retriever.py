#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 11:13:24 2022

@author: winter
"""

from selenium import webdriver
import requests
import re
from bs4 import BeautifulSoup as bs

chrome_options = webdriver.ChromeOptions()


### This section gets a list of usable proxies

proxy_url = 'https://www.proxynova.com/proxy-server-list/elite-proxies/'
page = requests.get(proxy_url)
soup = bs(page.content, 'html5lib')
table = soup.find('table', {'id': 'tbl_proxy_list'})
body = table.find('tbody')
rows = body.find_all('tr')
proxies = []
usable_proxies = []
for row in rows:
    try:
        non_decimal = re.compile(r'[^\d.]+')
        data_list = row.find_all('td')
        ip = data_list[0].text
        ip_re = non_decimal.sub('', ip)
        port = data_list[1].text
        port_re = non_decimal.sub('', port)
        proxy = str(ip_re) + ':' + str(port_re)
        proxies.append(proxy[1:])
    except:
        pass

for proxy in proxies:
    try:
        proxies = { 'https': proxy, 'http': proxy }
        response = requests.get(proxy_url, proxies=proxies, timeout=10)
        usable_proxies.append(proxy)
        print("appended")
        soup = bs(response.content, 'html5lib')
        section = soup.find('section', {'id': 'contact'})
        print(section.text)
    except:
        print("no response")

print(usable_proxies)
### Proxy retrieving section ends here
# The proxy servers in the usable_proxy list should all work
    