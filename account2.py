import email
from random import Random
from numpy import number
from selenium import webdriver
#from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
import json
import time
from time import sleep
from selenium import webdriver
import csv
import pandas as pd 
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import requests
import re 
import csv
import pandas as pd
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys




driver = webdriver.Chrome(executable_path=r'C:\Users\prince\nk\input\chromedriver.exe')
driver.maximize_window()

mobile=["9322523916", "9819700659"]
emails=["pranitajaiswal960@gmail.com","brijjaiswarpranita@gmail.com","sdgdgsdgds@gmail.com"]
Random_password="wewererr23@U"
username = "jaiswar111"

flag_account_found=False
flag_account_source=""
flag_account_type=""

#to open portalignorelist
with open(r"C:\Users\prince\nk\input\portalignorelist") as f:
        lines = f.readlines()
        lines=str(lines)
        lines.split()
        
# to open_chrome
def open_chrome():
      driver_path = r"C:\Users\prince\nk\input\chromedriver.exe"
      chrome_path = "C:\Program Files\Google\Chrome\Application"
      chrome_options = webdriver.ChromeOptions()
      #PROXY = "118.67.221.82:8080"
      #chrome_options.add_argument('--proxy-server=%s' % PROXY)
      driver = webdriver.Chrome(executable_path=driver_path, chrome_options=chrome_options)
      return driver
      #To deletecache,cookies and localdata in chrome
def delete_cache():
      driver=open_chrome()
      driver.execute_script("window.open('');")
      time.sleep(2)
      driver.switch_to.window(driver.window_handles[-1])
      time.sleep(2)
      driver.get('chrome://settings/clearBrowserData') # for old chromedriver versions use cleardriverData
      time.sleep(2)
      actions = ActionChains(driver) 
      actions.send_keys(Keys.TAB * 3 + Keys.DOWN * 3) # send right combination
      actions.perform()
      time.sleep(2)
      actions = ActionChains(driver) 
      actions.send_keys(Keys.TAB * 4 + Keys.ENTER) # confirm
      actions.perform()
      time.sleep(5) # wait some time to finish
      driver.close() # close this tab
      driver.switch_to.window(driver.window_handles[0]) # switch back
delete_cache()
 
# 1 99 design is done 

def design(emails):
      k=0
      for i in range(len(emails)):
            driver.get("https://99designs.com/accounts/resetpassword")
            try:
                  sleep(2)
                  pos = driver.find_element_by_name('username')
                  pos.send_keys(emails[k])
                  sleep(3)
                  driver.find_element_by_css_selector('body > div > div.oc-content--main > div > div > div > form > div:nth-child(4) > button').click()
                  sleep(3)
                  msg = "That email address is not registered with 99designs."
            
                  comic1 = [[], [], []]
                  sleep(5)
                  pmg = "Please follow the instructions in the email to reset your password."
                  try:
                        if driver.find_element_by_css_selector('body > div > div.oc-content--main > div > div > div > form > div.field.field--icon-label > div.field__validation > div'):
                              cmsg = driver.find_element_by_css_selector('body > div > div.oc-content--main > div > div > div > form > div.field.field--icon-label > div.field__validation > div').text

                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in comikart')
                                    comic1[0].append("not found")
                                    print("99 design:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                  except:
                        if driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/p'):
                              cmsg2=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div/p').text
                              if cmsg2 == pmg:
                                    comic = str(emails[k] + ' ' + 'is    Registered in behance')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("99 design :" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in comikart")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
design(emails)


# 2 https://app.hubspot.com/login is done 

def hubspot(emails):
      k=0

      for i in range(len(emails)):
            driver.get("https://app.hubspot.com/login")
            msg_hubspot = "The email address you've entered doesn't appear to exist. Please check your entry and try again."
                  
            sleep(1)
            hubspot = [[], [], []]
            pmg_hubspot = "You've entered an invalid password. For more detail on why this could be happening, please read "
            pmg_hubspot.split()
            print( pmg_hubspot[0])
                  
            try:
                  sleep(2)
                  pos = driver.find_element_by_id('username')
                  pos.send_keys(emails[k])
                  sleep(3)
                  hub_password=driver.find_element_by_id('password')
                  hub_password.send_keys(Random_password)
                  sleep(3)
                  driver.find_element_by_id('loginBtn').click()
                  sleep(5)
                  try:
                        if driver.find_element_by_css_selector('#hs-login > div.alert.private-alert.alert-danger.private-alert--danger.m-bottom-4.text-left > div > div > i18n-string'):
                              cmsg = driver.find_element_by_css_selector('#hs-login > div.alert.private-alert.alert-danger.private-alert--danger.m-bottom-4.text-left > div > div > i18n-string').text

                              if cmsg == msg_hubspot:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in hubspot')
                                    hubspot[0].append("not found")
                                    print("hubspot:" + '{' + "\n" + "account_Status=" + hubspot[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    cmsg = driver.find_element_by_css_selector('#hs-login > div.alert.private-alert.alert-danger.private-alert--danger.m-bottom-4.text-left > div > div > i18n-string').text.split()
                                    print(cmsg)
                              elif cmsg[1] == pmg_hubspot[1]:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in hubspot')
                                    hubspot[0].append("account found")
                                    hubspot[1].append("email")
                                    hubspot[2].append(emails[k])
                                    print("hubspot:" + '{' + "\n" + "account_Status=" + hubspot[0][0] + "\n" + "found_with_type=" + hubspot[1][0] + "\n" + "found_with_id=" + hubspot[2][0] + "\n" + '}')
                              else:
                                    ou=0
                  except:
                      print("Hello")
                        
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(("Error, hubspot, error messages have changed, pls revisit"))
                  f.close()
                  hubspot[0].append("Not Checked")
                  print("not checked")
            sleep(3)
            k=k+1
hubspot(emails)


# 3 https://www.newegg.com/
def newegg(emails):
      k=0
      for i in range(len(emails)):
            driver.get("https://www.newegg.com/")
            sleep(5)
            msg = "We didn't find an account for this email address."
            
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Protect Your Account"
      

            try:  
                  sleep(3)
                  driver.find_element_by_css_selector('#app > header > div.page-content-inner > div:nth-child(1) > div.section-right > div.header2021-nav.header2021-account > a > div.header2021-nav-subtitle').click()
                  sleep(3)
                  pos = driver.find_element_by_name('signEmail')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_id("signInSubmit").click()
                  sleep(3)
                  
                  try:
                        if driver.find_element_by_css_selector('#app > div > div.signin-wrap > div.signin-body > div > div > div > form > div > div:nth-child(2) > p'):
                              cmsg = driver.find_element_by_css_selector('#app > div > div.signin-wrap > div.signin-body > div > div > div > form > div > div:nth-child(2) > p').text

                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in newegg')
                                    comic1[0].append("not found")
                                    print("neweggg:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                  except:
                        if driver.find_element_by_css_selector('#app > div > div.signin-body > div > div.signin-title'):
                              
                              cmsg=driver.find_element_by_css_selector('#app > div > div.signin-body > div > div.signin-title').text
                              print(cmsg)
                              if cmsg==pmg:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in newegg')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("neweggs :" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in newweggs")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
newegg(emails)

# 4 https://solitaired.com/
def sol(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://solitaired.com/")
            sleep(5)
            msg = "Incorrect username or email."
            
            comic1 = [[], [], []]

            pmg = "Incorrect password."
            pmg.split()

            try:  
                  sleep(3)
                  driver.find_element_by_css_selector('#loginLink').click()
                  sleep(2)
                  pos = driver.find_element_by_id('loginUsername')
                  pos.send_keys(emails[k])
                  sleep(2)
                  pass_P=driver.find_element_by_id('loginPassword')
                  pass_P.send_keys(Random_password)
                  sleep(2)
                  driver.find_element_by_css_selector("#loginForm > div:nth-child(4) > button").click()
                  sleep(2)
                  
                  try:
                        if driver.find_element_by_css_selector('#loginForm > div.message.alert.alert-danger'):
                              cmsg = driver.find_element_by_css_selector('#loginForm > div.message.alert.alert-danger').text

                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in hubspot')
                                    comic1[0].append("not found")
                                    print("hubspot:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    cmsg = driver.find_element_by_css_selector('#loginForm > div.message.alert.alert-danger').text.split()
                                    print(cmsg)
                              elif cmsg[1] == pmg[1]:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in hubspot')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("solitred:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                              else:
                                    ou=0
                  except:
                      print("Hello")
                        
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(("Error, solitared, error messages have changed, pls revisit"))
                  f.close()
                  comic1[0].append("Not Checked")
                  print("not checked")
            sleep(3)
            k=k+1
sol(emails)

# 5 https://taxguru.in/wp-login.php

def taxguru(emails):
      k=0
      for i in range(len(emails)):
            driver.get("https://taxguru.in/wp-login.php")
            sleep(5)
            msg = "Unknown email address. Check again or try your username."
            
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Error: The password you entered for the username"
            
            pmg.split()
            print( pmg[0])
            try:  

                  sleep(2)
                  pos = driver.find_element_by_id('user_login')
                  pos.send_keys(emails[k])
                  sleep(2)
                  pass_P=driver.find_element_by_id('user_pass')
                  pass_P.send_keys(Random_password)
                  sleep(2)
                  driver.find_element_by_css_selector("#wp-submit").click()
                  sleep(2)
                  
                  try:
                        if driver.find_element_by_id('login_error'):
                              cmsg = driver.find_element_by_id('login_error').text

                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in taxguru')
                                    comic1[0].append("not found")
                                    print("taxguru:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    cmsg = driver.find_element_by_id('login_error').text.split()
                                    print(cmsg)
                              elif cmsg[1] == pmg[1]:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in hubspot')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("taxguru:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                              else:
                                    ou=0
                  except:
                      print("Hello")
                        
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(("Error,taxguru, error messages have changed, pls revisit"))
                  f.close()
                  comic1[0].append("Not Checked")
                  print("not checked")
            sleep(3)
            k=k+1

taxguru(emails)
#6 amazon 

def amazon(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.amazon.in/ap/forgotpassword?showRememberMe=true&openid.pape.max_auth_age=0&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=inflex&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_signin&prevRID=JX5FXPDXD2CN4T01HN61&openid.assoc_handle=inflex&openid.mode=checkid_setup&prepopulatedLoginId=eyJjaXBoZXIiOiJiSE50dHRUZFFIT0d1SmErSzRSRGR5LzBqSWdMK0x0R01vY2F0WE5ZSFVVPSIsIklWIjoiVVpGcmFtMC9oYWRxQSt3bWFFd0hDQT09IiwidmVyc2lvbiI6MX0%3D&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&timestamp=1651630906000")
            sleep(5)
            msg = "We're sorry. We weren't able to identify you given the information provided."
            
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Enter OTP"
      

            try:  
                  
                  sleep(3)
                  pos = driver.find_element_by_id('ap_email')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_id("continue").click()
                  sleep(3)
                  
                  try:
                        if driver.find_element_by_css_selector('#auth-error-message-box > div > div > ul > li > span'):
                              cmsg = driver.find_element_by_css_selector('#auth-error-message-box > div > div > ul > li > span').text

                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in amazon')
                                    comic1[0].append("not found")
                                    print("amazon:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                  except:
                        if driver.find_element_by_css_selector('#verification-code-form > div:nth-child(11) > div.a-row.a-spacing-micro.cvf-widget-input-code-label'):
                              
                              cmsg=driver.find_element_by_css_selector('#verification-code-form > div:nth-child(11) > div.a-row.a-spacing-micro.cvf-widget-input-code-label').text
                              print(cmsg)
                              if cmsg==pmg:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in amazon')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("amazon:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in newweggs")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1

amazon(emails)



#  7 https://www.comeon.com/

def comeon(emails):
      k=0
      for i in range(len(emails)):
            driver.get("https://www.comeon.com/in/sportsbook?sidebar=reset-password")
            sleep(5)
            msg = "Your email address couldnt be found. Please try again or contact support."
            msg.split()
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Please verify your identity by entering the code we sent to you via email."
            pmg.split()
            print(pmg[0])


            try:  
                  
                  sleep(3)
                  pos = driver.find_element_by_id('reset-password-email')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_css_selector("#sidebar > div > div:nth-child(1) > div > footer > div > button").click()
                  sleep(3)
                  
         
                  if driver.find_element_by_class_name('notification-wrap__error-text-msg'):
                        cmsg = driver.find_element_by_class_name('notification-wrap__error-text-msg').text

                        if cmsg == msg:
                              comic = str(emails[k] + ' ' + 'is not   Registered in comeon')
                              comic1[0].append("not found")
                              print("comeon:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
            
                  
                        if cmsg == pmg:
                              comic = str(emails[k] + ' ' + 'is    Registered in comeon')
                              comic1[0].append("account found")
                              comic1[1].append("email")
                              comic1[2].append(emails[k])
                              print("comeon :" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in comeon")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
            
comeon(emails)

#  8 https://www.dancelifemap.com/
 
k=0
for i in range(len(emails)):
      driver.get("https://www.dancelifemap.com/")
      sleep(5)
      msg = "Invalid email or user doesn't exists."
      msg.split()
      comic1 = [[], [], []]
      sleep(5)
      pmg = "Please check your email."
      pmg.split()
      print(pmg[0])


      try:  
            
            sleep(3)
            driver.find_element_by_css_selector('#menu-item-18886 > a').click()
            sleep(3)
            driver.find_element_by_css_selector('body > div.modal.fade.uwp-auth-modal.bsui.show > div > div > div > div.card-body > form > div.uwp-footer-links > div.uwp-footer-link.float-right > a').click()
            sleep(3)
            pos = driver.find_element_by_name('email')
            pos.send_keys(emails[k])
            sleep(3)
            
            driver.find_element_by_name("uwp_forgot_submit").click()
            sleep(3)
            
            try:
                  if driver.find_element_by_css_selector('body > div.modal.fade.uwp-auth-modal.bsui.show > div > div > div > div > div.card-body > div > div > div'):
                        cmsg = driver.find_element_by_css_selector('body > div.modal.fade.uwp-auth-modal.bsui.show > div > div > div > div > div.card-body > div > div > div').text

                        if cmsg == msg:
                              comic = str(emails[k] + ' ' + 'is not   Registered in dance')
                              comic1[0].append("not found")
                              print("dance:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                              cmsg = driver.find_element_by_css_selector('body > div.modal.fade.uwp-auth-modal.bsui.show > div > div > div > div > div.card-body > div > div > div').text.split()
                              print(cmsg)
                        elif cmsg[1] == pmg[1]:
                              flag_account_found=True
                              flag_account_source=emails[k]
                              flag_account_type="email"
                              comic = str(emails[k] + ' ' + 'is    Registered in dance')
                              comic1[0].append("account found")
                              comic1[1].append("email")
                              comic1[2].append(emails[k])
                              print("dance:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                        else:
                              ou=0
            except:
                  print("Hello")
                       
                        
      except:
                 
            f = open("error.log", "a")
            f.write(("Error,dance, error messages have changed, pls revisit"))
            f.close()
            comic1[0].append("Not Checked")
            print("not checked")
      sleep(3)
      k=k+1


# 9 https://www.facebook.com/


def facebook(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0")
            sleep(5)
            msg = "Your search did not return any results. Please try again with other information."
            
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Reset Your Password"
      

            try:  
                  
                  sleep(3)
                  pos = driver.find_element_by_id('identify_email')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_id("did_submit").click()
                  sleep(3)
                  
                  try:
                        if driver.find_element_by_css_selector('#identify_yourself_flow > div > div.phl.ptm.uiInterstitialContent > div.pam.uiBoxRed > div._9o4h'):
                              cmsg = driver.find_element_by_css_selector('#identify_yourself_flow > div > div.phl.ptm.uiInterstitialContent > div.pam.uiBoxRed > div._9o4h').text

                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in facebook')
                                    comic1[0].append("not found")
                                    print("facebook:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                  except:
                        if driver.find_element_by_css_selector('#initiate_interstitial > div.uiHeader.uiHeaderBottomBorder.mhl.mts.uiHeaderPage.interstitialHeader > div > div:nth-child(2) > h2'):
                              
                              cmsg=driver.find_element_by_css_selector('#initiate_interstitial > div.uiHeader.uiHeaderBottomBorder.mhl.mts.uiHeaderPage.interstitialHeader > div > div:nth-child(2) > h2').text
                              print(cmsg)
                              if cmsg==pmg:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in facebook')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("facebook:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in facebook")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
facebook(emails)

# 10 greenindia

def green(emails):
      k=0
      for i in range(len(emails)):
            driver.get("https://www.greendindia.com/account-details/lost-password/")
            sleep(5)
            msg = "Invalid username or email."
            msg.split()
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Password reset email has been sent."
            pmg.split()

            try:  
                  
                  sleep(3)
                  
                  pos = driver.find_element_by_id('user_login')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_css_selector("#page-wrapper > main > div > div > div.main-content.col-lg-9.col-md-9.col-sm-8.col-xs-12 > div > div > form > p:nth-child(4) > button").click()
                  sleep(3)
                  
                  try:
                        if driver.find_element_by_css_selector('#page-wrapper > main > div > div > div.main-content.col-lg-9.col-md-9.col-sm-8.col-xs-12 > div > div > ul'):
                              cmsg = driver.find_element_by_css_selector('#page-wrapper > main > div > div > div.main-content.col-lg-9.col-md-9.col-sm-8.col-xs-12 > div > div > ul').text

                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in facebook')
                                    comic1[0].append("not found")
                                    print("greenindia:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                  except:
                        if driver.find_element_by_css_selector('#page-wrapper > main > div > div > div.main-content.col-lg-9.col-md-9.col-sm-8.col-xs-12 > div > div > div'):
                              
                              cmsg=driver.find_element_by_css_selector('#page-wrapper > main > div > div > div.main-content.col-lg-9.col-md-9.col-sm-8.col-xs-12 > div > div > div').text
                              print(cmsg)
                              if cmsg==pmg:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in india')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("greenindia:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in greenindia")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
green(emails)



# 11 https://www.jeetplay.com/# 

def jeetplay(emails):
      

      k=0
      for i in range(len(emails)):
            driver.get("https://www.jeetplay.com/#")
            sleep(3)
            msg = "We can't find a user with that e-mail address."
            msg.split()
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Reset Your Password"
            pmg.split()

            try:  
                  
                  sleep(3)
                  driver.find_element_by_class_name('text').click()
                  sleep(2)
                  driver.find_element_by_class_name('forget-link').click()
                  sleep(2)
                  pos = driver.find_element_by_css_selector('body > div.reset-popup.active > div > div.popup-entry > div.popup-form > form > div.row > div > input[type=text]')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_css_selector("body > div.reset-popup.active > div > div.popup-entry > div.popup-form > form > div.send-btn-block > button").click()
                  sleep(3)
                  

                  
                  try:
                        if driver.find_element_by_css_selector('body > div.simple-popup.active > div > div.popup-text-block'):
                              cmsg = driver.find_element_by_css_selector('body > div.simple-popup.active > div > div.popup-text-block').text

                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in jeetplay')
                                    comic1[0].append("not found")
                                    print("jeetplay:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    driver.find_element_by_css_selector("body > div.simple-popup.active > div > div.btn-block > button").click()
                                    sleep(3)
                  except: 
                        if driver.find_element_by_css_selector('#activatedPoUp > h3'):
                              
                              cmsg=driver.find_element_by_css_selector('#activatedPoUp > h3').text
                              print(cmsg)
                              if cmsg==pmg:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in india')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("jeetplay:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in jeetplay")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1

jeetplay(emails)


# 12 https://www.lenovo.com/in/en/login/pw/request

def lenovo(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.lenovo.com/in/en/login/pw/request")
            sleep(8)
            msg = "Your account does not exist, please check your email address."
            msg.split()
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Password reset confirmation"
            pmg.split()

            try:  
                  
                  sleep(3)
                  # driver.find_element_by_css_selector('#forgot-password > div.form-input > div > div > input').click()
                  # sleep(2)
                  # driver.find_element_by_css_selector('#login > div:nth-child(3) > div > div > a').click()
                  # sleep(2)
                  pos = driver.find_element_by_id('forgottenPwd.email')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_css_selector("#forgottenPwdForm > div > p:nth-child(4) > button").click()

                  sleep(3)
                  
                  try:  
                        sleep(3)
                        if driver.find_element_by_css_selector('#email\.errors'):
                              cmsg = driver.find_element_by_css_selector('#email\.errors').text

                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in lenova')
                                    comic1[0].append("not found")
                                    print("lenova:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    driver.find_element_by_css_selector('#activatedPoUp > button.push-btn.close-button').click()
                  except: 
                        
                        sleep(3)
                        if driver.find_element_by_css_selector('#mainContent > div.success-wrapper > div > div > h2'):
                              
                              cmsg=driver.find_element_by_css_selector('#mainContent > div.success-wrapper > div > div > h2').text
                              print(cmsg)
                              if cmsg==pmg:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in lenova')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("lenova:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in lenova")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1

lenovo(emails)

# 13 https://www.myindianart.com/ 


def myindia(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.myindianart.com/")
            sleep(10)
            msg = "Sorry! This email id is not registered with us."
            msg.split()
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Email Successfully sent!!"

            
            try:  
                  sleep(3)
                  driver.find_element_by_css_selector('body > header > div.topbar-outr > div > div > ul.login-mnu > li:nth-child(1) > a > span').click()
                  sleep(3)
                  driver.find_element_by_css_selector('#loginFrm > div.login-btn-outr > a').click()
                  sleep(3)
                  driver.find_element_by_css_selector('#sociable_connect > div.mian-field-box.first-screen > div:nth-child(1)').click()
                  sleep(2)
                  driver.find_element_by_css_selector('#main_login > div.mian-field-box > div.links.js-remember-links > a').click()
                  sleep(4)
                  
                  pos = driver.find_element_by_id('forgetemail')
                  pos.send_keys(emails[k])
                  sleep(5)
                  
                  driver.find_element_by_class_name('btn view-btn type1 button read-btn').click()

                  sleep(4)
                  
            
                  if driver.find_element_by_css_selector('#forgetError'):
                        cmsg = driver.find_element_by_css_selector('#forgetError').text

                  if cmsg == msg:
                        comic = str(emails[k] + ' ' + 'is not   Registered in myindia')
                        comic1[0].append("not found")
                        print("myindia:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                  
                        
                  cmsg=driver.find_element_by_css_selector('#thankyouForgetModal > div > div > div.modal-header.catalog-modal-header > h5').text
                  print(cmsg)
                  if cmsg[1]==pmg[1]:
                        flag_account_found=True
                        flag_account_source=emails[k]
                        flag_account_type="email"
                        comic = str(emails[k] + ' ' + 'is    Registered in myindia')
                        comic1[0].append("account found")
                        comic1[1].append("email")
                        comic1[2].append(emails[k])
                        print("myindia:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                                    
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in myindia")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
      
myindia(emails)


# 14 mylo 


def mylo(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.mylo.id/")
            sleep(8)
            msg = "We couldn’t find your account. Please check your spelling or sign up."
            msg.split()
            comic1 = [[], [], []]
            sleep(5)
            pmg = "If an account with this email exists, an email is on the way. Please click the link to set your new password."
            pmg.split()

            try:  
                  
                  sleep(3)
                  driver.find_element_by_css_selector('body > header > div > a.login').click()
                  sleep(2)
                  driver.find_element_by_css_selector('#root > div.styles__Layout-sc-1aun290-1.gdbWfI > div.styles__LayoutInner-sc-1aun290-3.bEtpzF > div > div > form > a').click()
                  sleep(2)
                  pos = driver.find_element_by_css_selector('#email')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_css_selector("#root > div.styles__Layout-sc-1aun290-1.gdbWfI > div.styles__LayoutInner-sc-1aun290-3.bEtpzF > div > div.FormLayout__FormContainerWrapper-sc-12xb9uv-2.dJkmur > form > div.Button__ButtonWrapper-sc-4u4hat-0.dVgUZc > button").click()

                  sleep(3)
                  
      
                  
                        
                  if driver.find_element_by_css_selector('#root > div.styles__Layout-sc-1aun290-1.gdbWfI > div.styles__LayoutInner-sc-1aun290-3.bEtpzF > div > div.FormLayout__FormContainerWrapper-sc-12xb9uv-2.dJkmur > div > div'):
                        cmsg = driver.find_element_by_css_selector('#root > div.styles__Layout-sc-1aun290-1.gdbWfI > div.styles__LayoutInner-sc-1aun290-3.bEtpzF > div > div.FormLayout__FormContainerWrapper-sc-12xb9uv-2.dJkmur > div > div').text

                        if cmsg == msg:
                              comic = str(emails[k] + ' ' + 'is not   Registered in mylo')
                              comic1[0].append("not found")
                              print("mylo:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                              driver.find_element_by_css_selector('#activatedPoUp > button.push-btn.close-button').click()
            
                        cmsg=driver.find_element_by_css_selector('#root > div.styles__Layout-sc-1aun290-1.gdbWfI > div.styles__LayoutInner-sc-1aun290-3.bEtpzF > div > div.FormLayout__FormContainerWrapper-sc-12xb9uv-2.dJkmur > div > p.Confirmation__MessageText-sc-682aoz-0.klZOa').text
                        print(cmsg)
                        if cmsg[1]==pmg[1]:
                              flag_account_found=True
                              flag_account_source=emails[k]
                              flag_account_type="email"
                              comic = str(emails[k] + ' ' + 'is    Registered in mylo')
                              comic1[0].append("account found")
                              comic1[1].append("email")
                              comic1[2].append(emails[k])
                              print("mylo:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                                    
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in mylo")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
mylo(emails)
      
# 15 https://www.popads.net/users/forgot

def popads(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.popads.net/users/forgot")
            sleep(8)
            msg = "The supplied email does not exist in our records."
            msg.split()
            comic1 = [[], [], []]
            sleep(5)
            pmg = "An internal error occurred during password reset, please try again."
            pmg.split()

            try:  
                  
                  sleep(3)
                  driver.find_element_by_css_selector('#forgot-password > div.form-input > div > div > input').click()
                  sleep(2)
                  driver.find_element_by_css_selector('#login > div:nth-child(3) > div > div > a').click()
                  sleep(2)
                  pos = driver.find_element_by_css_selector('#UserEmail')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_css_selector("#UserForgotForm > div.submit > input[type=submit]").click()

                  sleep(3)
                  
                  
                  try:
                        if driver.find_element_by_css_selector('#generic_content > div > span'):
                              cmsg = driver.find_element_by_css_selector('#generic_content > div > span').text

                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in popads')
                                    comic1[0].append("not found")
                                    print("popads:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    cmsg = driver.find_element_by_css_selector('#generic_content > div > span').text.split()
                                    print(cmsg)
                              elif cmsg[1] == pmg[1]:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in popads')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("popads:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                              else:
                                    ou=0
                  except:
                      print("Hello")
                        
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(("Error,popads, error messages have changed, pls revisit"))
                  f.close()
                  comic1[0].append("Not Checked")
                  print("not checked")
            sleep(3)
            k=k+1
popads(emails)

# 16 https://accounts.practo.com/login

def practo(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://accounts.practo.com/login")
            sleep(8)
            msg = "Email is not registered"
            msg.split()
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Incorrect password If you don't remember your password, you can reset it here. You have 4 more attempts remaining before your account is blocked"
            pmg.split()

            try:  
                  
                  sleep(3)
                  driver.find_element_by_css_selector('#forgot-password > div.form-input > div > div > input').click()
                  sleep(2)
                  driver.find_element_by_css_selector('#login > div:nth-child(3) > div > div > a').click()
                  sleep(2)
                  pos = driver.find_element_by_css_selector('#username')
                  pos.send_keys(emails[k])
                  sleep(3)
                  pss_p=driver.find_element_by_css_selector('#password')
                  pss_p.send_keys(Random_password)
                  sleep(3)
                  driver.find_element_by_css_selector("#login").click()

                  sleep(3)
                  
                  try:  
                        sleep(3)
                        if driver.find_element_by_css_selector('#usernameErrorBlock'):
                              cmsg = driver.find_element_by_css_selector('#usernameErrorBlock').text

                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in lenova')
                                    comic1[0].append("not found")
                                    print("practo:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    driver.find_element_by_css_selector('#activatedPoUp > button.push-btn.close-button').click()
                  except: 
                        
                        sleep(3)
                        if driver.find_element_by_css_selector('#passwordErrorBlock'):
                              
                              cmsg=driver.find_element_by_css_selector('#passwordErrorBlock').text
                              print(cmsg)
                              if cmsg[1]==pmg[1]:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in practo')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("practo:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in practo")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
practo(emails)


# 17 https://www.scoopwhoop.com/?ref=password

def scoop(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.scoopwhoop.com/?ref=password")
            sleep(15)
            msg = "Please enter a valid email address."
            msg.split()
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Forget password link sent to your registered email id"
            pmg.split()

            try:  
                  
                  sleep(3)
                  driver.find_element_by_css_selector('#userProfilePage').click()
                  sleep(2)
                  driver.find_element_by_css_selector('#loginBox > div.login__body > div > div > div > div.login__inputs > button:nth-child(2)').click()
                  sleep(2)
                  pos = driver.find_element_by_css_selector('#forgotEmail')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_css_selector("#forgotButton").click()
                  sleep(2)
                  
                  
                  try:
                        
                        sleep(2)
                        if driver.find_element_by_css_selector('#errorForgot'):
                              cmsg = driver.find_element_by_css_selector('#errorForgot').text

                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in scoopwhoop')
                                    comic1[0].append("not found")
                                    print("scoopwhoop:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    cmsg = driver.find_element_by_css_selector('#errorForgot').text.split()
                                    print(cmsg)
                              elif cmsg == pmg:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in popads')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("scoopwhoop:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                              else:
                                    ou=0
                  except:
                      print("Hello")
                        
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(("Error,scoopwhoop, error messages have changed, pls revisit"))
                  f.close()
                  comic1[0].append("Not Checked")
                  print("not checked")
            sleep(3)
            k=k+1

scoop(emails)

#18 https://9gag.com/login 

def gag(emails):
      
      m=0
      msg8='An error occured.'
      cg8=[[], [], []]
      cg81=[[], [], []]
      for i in range(len(emails)):
            driver.get('https://9gag.com/login')
            sleep(5)
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/section/form/div/button[2]').click()
            sleep(5)
            pol=driver.find_element_by_name('email')
            pol.send_keys(emails[m])
            sleep(3)
            driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[2]/div/div/button').click()
            sleep(3)
      try:
            if driver.find_element_by_class_name('error-message'):
                  po=driver.find_element_by_class_name('error-message').text
                  if po==msg8:
                        cg8[0].append("not found")
                        print("9gag:" + '{' + "\n" + "account_Status=" + cg8[0][0] + "\n" +  "email_id:"+emails[m] + "\n" + '}')
      except:
            if driver.find_element_by_xpath('/html/body/div[3]/div/div'):
                  flag_account_found=True
                  flag_account_source=emails[k]
                  flag_account_type="email"
                  cg81[0].append("account found")
                  cg81[1].append("email")
                  cg81[2].append(emails[m])
                  print("9gag :" + '{' + "\n" + "account_Status=" + cg81[0][0] + "\n" + "found_with_type=" + cg81[1][0] + "\n" + "found_with_id=" + cg81[2][0] + "\n" + '}')

            else:
                  f = open("error.log", "a")
                  f.write(msg8 + " " "messages are not found in archive")
                  f.close()
                  cg8[0].append("Not Checked")
      m=m+1
gag(emails)


# 19 https://www.saatchiart.com/

def saatchiart(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.saatchiart.com/")
            sleep(8)
            msg = "Account with this email doesn’t exist."
            msg.split()
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Thank you!"
            pmg.split()
            sleep(3)
            try:  
                  
                  sleep(3)
                  driver.find_element_by_css_selector('#__next > div > nav > div > div:nth-child(1) > div:nth-child(2) > div > div > a:nth-child(1)').click()
                  sleep(2)
                  driver.find_element_by_css_selector('#modal > div > div > div.sc-1bcbi6q-1.cSTDxt > aside > div.sc-1bcbi6q-5.huwWST > form > fieldset > button:nth-child(5)').click()
                  sleep(2)
                  pos = driver.find_element_by_css_selector('#modal > div > div > div.sc-1bcbi6q-1.cSTDxt > aside > div.sc-1bcbi6q-5.huwWST > form > fieldset > div.ji4k8v-15.eVQiXx > input[type=email]')
                  pos.send_keys(emails[k])
                  sleep(3)
            
                  driver.find_element_by_css_selector('#modal > div > div > div.sc-1bcbi6q-1.cSTDxt > aside > div.sc-1bcbi6q-5.huwWST > form > fieldset > button').click()

                  sleep(3)
                  
                  try:  
                        sleep(3)
                        if driver.find_element_by_css_selector('#modal > div > div > div.sc-1bcbi6q-1.cSTDxt > aside > div.sc-1bcbi6q-5.huwWST > form > fieldset > p'):
                              cmsg = driver.find_element_by_css_selector('#modal > div > div > div.sc-1bcbi6q-1.cSTDxt > aside > div.sc-1bcbi6q-5.huwWST > form > fieldset > p').text

                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in lenova')
                                    comic1[0].append("not found")
                                    print("saatchiart:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    
                  except: 
                        
                        sleep(3)
                        if driver.find_element_by_css_selector('#modal > div > div > div.sc-1bcbi6q-1.cSTDxt > aside > div.sc-1bcbi6q-5.huwWST > form > p:nth-child(1)'):
                              
                              cmsg2=driver.find_element_by_css_selector('#modal > div > div > div.sc-1bcbi6q-1.cSTDxt > aside > div.sc-1bcbi6q-5.huwWST > form > p:nth-child(1)').text
                              print(cmsg)
                              if cmsg2[1]==pmg[1]:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in saatchiart')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("saatchiart:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in saatchiart")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
saatchiart(emails)

# 20  https://accounts.zoho.com/password?servicename=VirtualOffice&serviceurl=https%3A%2F%2Fmail.zoho.com%2F&signupurl=https%3A%2F%2Fwww.zoho.com%2Fworkplace%2Fpricing.html

def zoho(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.zoho.com/")
            sleep(3)
            
            msg = "This account cannot be found. Please use a different account or sign up for a new account."
            
            comic1 = [[], [], []]
            sleep(5)
            
            try:  
                  
                  sleep(3)
                  driver.find_element_by_css_selector('body > div.main-container-wrapper > div.zh-header-wrap > div > a.zh-login').click()
                  sleep(2)
                  
                  pos = driver.find_element_by_css_selector('#login_id')
                  pos.send_keys(emails[k])
                  sleep(3)
            
                  driver.find_element_by_css_selector('#nextbtn').click()

                  sleep(8)
                  try:
                        if driver.find_element_by_css_selector('#getusername > span > div.fielderror.errorlabel'):
                              cmsg =driver.find_element_by_css_selector('#getusername > span > div.fielderror.errorlabel').text
                              

                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in zoho')
                                    comic1[0].append("not found")
                                    print("zoho:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                  except:                  
                        
                        if driver.find_element_by_id("password"):      
                              flag_account_found=True
                              flag_account_source=emails[k]
                              flag_account_type="email"
                              comic = str(emails[k] + ' ' + 'is    Registered in mylo')
                              comic1[0].append("account found")
                              comic1[1].append("email")
                              comic1[2].append(emails[k])
                              print("zoho:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                                          
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in zoho")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
zoho(emails)       

# 21 https://bazaar.shopclues.com/?__ar=Y

def bazaar(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://bazaar.shopclues.com/?__ar=Y")
            sleep(5)
            msg = "Account doesn't exist with this email id. Register now."
            msg.split()
            comic1 = [[], [], []]
            sleep(5)
            pmg = "(If OTP is missing in Inbox, please check your spam folder)."
            pmg.split()
            sleep(3)
            try:  
                  
                  sleep(3)
                  driver.find_element_by_css_selector('#sign-in > a').click()
                  sleep(2)
                  driver.find_element_by_css_selector('#modal > div > div > div.sc-1bcbi6q-1.cSTDxt > aside > div.sc-1bcbi6q-5.huwWST > form > fieldset > button:nth-child(5)').click()
                  sleep(2)
                  pos = driver.find_element_by_css_selector('#main_user_login')
                  pos.send_keys(emails[k])
                  sleep(3)
            
                  driver.find_element_by_css_selector('#login_via_otp').click()

                  sleep(3)
                  if driver.find_element_by_css_selector('#login > form > fieldset > div.s_row > div:nth-child(4) > span'):
                        cmsg = driver.find_element_by_css_selector('#login > form > fieldset > div.s_row > div:nth-child(4) > span').text

                        if cmsg == msg:
                              comic = str(emails[k] + ' ' + 'is not   Registered in bazaar')
                              comic1[0].append("not found")
                              print("bazaar:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                              
            
                        cmsg=driver.find_element_by_css_selector('#loginModelBox > div > div.login_sec > div.loginviaotp_ver_layer.popup_inr_dv > div > form > div.title > p > span.email_spam_mail_msg').text
                        print(cmsg)
                        if cmsg[1]==pmg[1]:
                              flag_account_found=True
                              flag_account_source=emails[k]
                              flag_account_type="email"
                              comic = str(emails[k] + ' ' + 'is    Registered in bazaar')
                              comic1[0].append("account found")
                              comic1[1].append("email")
                              comic1[2].append(emails[k])
                              print("bazaar:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                                    
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in bazaar")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
bazaar(emails)
            

#22 https://accounts.430o(tax.in/v2/forgot-password?product=cleartax&return_path=L015QWNjb3VudC9zdGFydD9yZWY9c3Nv&flow=login&__hstc=82924105.f3e85ffc01485d028d3b715acdc9b603.1648721875386.1651644612755.1651666090846.19&__hssc=82924105.1.1651666090846&__hsfp=2930199737

def tax(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://accounts.cleartax.in/v2/forgot-password?product=save&return_path=L2xhdW5jaHBhZD9zb3VyY2U9ZWZpbGluZw%3D%3D&flow=login&__hstc=82924105.f3e85ffc01485d028d3b715acdc9b603.1648721875386.1651644612755.1651666090846.19&__hssc=82924105.1.1651666090846&__hsfp=2930199737")
            sleep(10)
            msg = "This email is not registered with ClearTax."
            msg.split()
            comic1 = [[], [], []]

            pmg = "A password reset link has been sent to"
                        
            pmg.split()
            sleep(3)
            try:  
                  
                  
            
                  sleep(4)
                  pos = driver.find_element_by_css_selector('#userEmailForgot')
                  pos.clear()
                  pos.send_keys(emails[k])
                  
                  sleep(3)
      
                  driver.find_element_by_css_selector('#submitEmailForgot').click()
                  sleep(3)

                  
                  try:  
                        sleep(3)
                        if driver.find_element_by_css_selector('#mainContent > div.lil-w-8\/12.lil-flex.lil-items-center.lil-justify-center.lil-relative.lg\:lil-w-7\/12.md\:lil-w-7\/12.sm\:lil-w-full > div > main > div > section > div.lil-w-full.lil-justify-center.lil-flex > div > div > div.text-field-group.required.lil-pt-6.lil-w-full > div.error-message-v2.lil-text-s-12.lil-text-red.lil-font-medium.lil-pt-3'):
                              cmsg = driver.find_element_by_css_selector('#mainContent > div.lil-w-8\/12.lil-flex.lil-items-center.lil-justify-center.lil-relative.lg\:lil-w-7\/12.md\:lil-w-7\/12.sm\:lil-w-full > div > main > div > section > div.lil-w-full.lil-justify-center.lil-flex > div > div > div.text-field-group.required.lil-pt-6.lil-w-full > div.error-message-v2.lil-text-s-12.lil-text-red.lil-font-medium.lil-pt-3').text

                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in cleartax')
                                    comic1[0].append("not found")
                                    print("cleartax:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    
                  except: 
                        
                        sleep(3)
                        if driver.find_element_by_css_selector('#mainContent > div.lil-w-8\/12.lil-flex.lil-items-center.lil-relative.lil-justify-center.lg\:lil-w-7\/12.md\:lil-w-7\/12.sm\:lil-w-full > div > main > section > div > p.lil-text-s-18.lil-text-center.lil-pt-4.lil-font-semibold'):
                              
                              cmsg2=driver.find_element_by_css_selector('#mainContent > div.lil-w-8\/12.lil-flex.lil-items-center.lil-relative.lil-justify-center.lg\:lil-w-7\/12.md\:lil-w-7\/12.sm\:lil-w-full > div > main > section > div > p.lil-text-s-18.lil-text-center.lil-pt-4.lil-font-semibold').text
                              print(cmsg2)
                              if cmsg2[1]==pmg[1]:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in cleartax')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("cleartax:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in cleartax")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
tax(emails)

#23 https://deltapage.com/account/forgotten
def delta(emails):
      k=0
      for i in range(len(emails)):
            driver.get("https://deltapage.com/account/forgotten")
            sleep(4)
            msg = "Warning: The E-Mail Address was not found in our records, please try again!"
            msg.split()
            comic1 = [[], [], []]

            pmg = "An email with a confirmation link has been sent your email address."
                        
            pmg.split()
            sleep(3)
            try:  
                  
                  sleep(3)
                  driver.find_element_by_css_selector('body > app-root > app-header > header > div > div.header-right.ng-star-inserted > ul > li:nth-child(4) > a > span > span.headerlink__text').click()
                  sleep(2)
                  driver.find_element_by_css_selector('#modal > div > div > div.sc-1bcbi6q-1.cSTDxt > aside > div.sc-1bcbi6q-5.huwWST > form > fieldset > button:nth-child(5)').click()
                  sleep(2)
                  pos = driver.find_element_by_css_selector('#input-email')
                  pos.send_keys(emails[k])
                  sleep(3)
      
                  driver.find_element_by_css_selector('#content > form > div > div.pull-right > button').click()
                  sleep(3)

                  
                  try:  
                        sleep(3)
                        if driver.find_element_by_css_selector('#account-forgotten > div.alert.alert-danger.alert-dismissible'):
                              cmsg = driver.find_element_by_css_selector('#account-forgotten > div.alert.alert-danger.alert-dismissible').text

                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in deltapage')
                                    comic1[0].append("not found")
                                    print("delta:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    
                  except: 
                        
                        sleep(3)
                        if driver.find_element_by_css_selector('#account-login > div.alert.alert-success.alert-dismissible'):
                              
                              cmsg2=driver.find_element_by_css_selector('#account-login > div.alert.alert-success.alert-dismissible').text
                              print(cmsg2)
                              if cmsg2[1]==pmg[1]:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in deltapage')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("deltapage:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in deltapage")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
delta(emails)

#24 https://dsp.bidsopt.com/forgotpassword 

def bidspot(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://dsp.bidsopt.com/forgotpassword")
            sleep(6)
            msg = "Provided email does not exist."
            msg.split()
            comic1 = [[], [], []]

            pmg = "Problem in resetting the password for your account, please contact Support Team."
                        
            pmg.split()
            sleep(3)
            
                  
            try:
                  sleep(3)
                  
                  pos = driver.find_element_by_css_selector('#exampleInputEmail1')
                  pos.send_keys(emails[k])
                  sleep(3)
      
                  driver.find_element_by_css_selector('#reset_id').click()
                  sleep(3)
                  
                  if driver.find_element_by_css_selector('#errorspan'):
                        cmsg = driver.find_element_by_css_selector('#errorspan').text

                        if cmsg == msg:
                              comic = str(emails[k] + ' ' + 'is not   Registered in bidsopt.com')
                              comic1[0].append("not found")
                              print("bidspot:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                        

                        cmsg=driver.find_element_by_css_selector('#successs-span').text
                        print(cmsg)
                        if cmsg[1]==pmg[1]:
                              flag_account_found=True
                              flag_account_source=emails[k]
                              flag_account_type="email"
                              comic = str(emails[k] + ' ' + 'is    Registered in bidsopt.com')
                              comic1[0].append("account found")
                              comic1[1].append("email")
                              comic1[2].append(emails[k])
                              print("bidsopt.com:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                                    
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in bidsopt.com")
                  f.close()
                  comic1[0].append("Not Checked")
            
            k=k+1   
bidspot(emails)
      

##  25 https://i.thechive.com/password/email
def thechive(email):
      driver=open_chrome()
      k=0
      kp="thechive"
      if kp in lines:
            print(kp+" "+'is present in the ignore_list')
            lk="Error, comikart, error messages have changed, pls revisit"
            fk = open(r"error.log", "w")
            fk.write(lk)
            fk.write('\n')
            fk.close()
      else:
            for i in range(len(emails)):
                  driver.get("https://i.thechive.com/auth/login")
                  sleep(4)
                  msg = "We cannot find a user with that email address."
            
                  comic1 = [[], [], []]

                  pmg ="We have emailed your password reset link. If you do not find it in your inbox, please double check your spam folder."
                  print(pmg[0:2])          
                  
                  sleep(3)
                  try:  
                        
                        sleep(3)
                        driver.find_element_by_css_selector('#login > form > div.additional-fields > a').click()
                        sleep(2)
                        # driver.find_element_by_css_selector('#innerApp > div.css-jqtfa0 > div.css-1d7igk2 > div.css-aknk > div.css-1r8j6uz > button').click()
                        # sleep(2)
                        pos = driver.find_element_by_css_selector('#login > form > div:nth-child(3) > input')
                        pos.send_keys(emails[k])
                        sleep(3)
            
                        driver.find_element_by_css_selector('#login > form > div:nth-child(4) > button').click()
                        sleep(3)
                        
                        
                        try:  
                              sleep(3)
                              if driver.find_element_by_css_selector('body > div.body-inner > div.content-wrapper.js-content > div:nth-child(1) > div > ul'):
                                    cmsg = driver.find_element_by_css_selector('body > div.body-inner > div.content-wrapper.js-content > div:nth-child(1) > div > ul').text

                                    if cmsg == msg:
                                          comic = str(emails[k] + ' ' + 'is not   Registered in thechive.com')
                                          comic1[0].append("not found")
                                          print("thechive.com:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                          
                        except: 
                              
                        
                              if driver.find_element_by_css_selector('body > div.body-inner > div.content-wrapper.js-content > div:nth-child(1) > div'):
                                    
                                    cmsg2=driver.find_element_by_css_selector('body > div.body-inner > div.content-wrapper.js-content > div:nth-child(1) > div').text.split()
                                    print(cmsg2[1])
                                    if cmsg2[1]==pmg[0:2]:
                                          flag_account_found=True
                                          flag_account_source=emails[k]
                                          flag_account_type="email"
                                          comic = str(emails[k] + ' ' + 'is    Registered in thechive.com')
                                          comic1[0].append("account found")
                                          comic1[1].append("email")
                                          comic1[2].append(emails[k])
                                          print("deltapage:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                        
                                    
                  except:
                        fp = open(r"C:\Users\prince\nk\input\portalignorelist", "a")
                        fp.write("thechive")
                        fp.write('\n')
                        f.close()
                        f = open("error.log", "a")
                        f.write(msg + " " "messages are not found in thechive.com")
                        f.close()
                        comic1[0].append("Not Checked")
                  sleep(3)
                  k=k+1
thechive(emails)

# 26 https://www.dell.com/en-in msg is not detecting 

def dell(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.dell.com/en-in")
            sleep(10)
            msg = "We are unable to match the details you entered with our records"
            
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Verify One-Time Password"
            pmg.split()

            try:  
                  
                  sleep(2)
                  driver.find_element_by_id('um-si-label').click()
                  sleep(3)
                  driver.find_element_by_css_selector('#unified-masthead > div.mh-top > div.right-column > div.mh-myaccount > div > div.flyout > div > div.mh-myaccount-unauth-dropdown > div.mh-myaccount-ctas > a.mh-btn.mh-btn-primary.navigate').click()
                  sleep(2)
                  driver.find_element_by_id('linkforgotpassword').click()
                  sleep(2)
                  pos = driver.find_element_by_id('EmailAddress')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_id("btnFogotPasswordSend").click()

                  sleep(3)
                  
                  try:  
                        sleep(3)
                        if driver.find_element_by_id('validationSummaryText-c12a7870-643c-4a22-bbbc-07d1db90e8fc'):
                              cmsg = driver.find_element_by_id('validationSummaryText-c12a7870-643c-4a22-bbbc-07d1db90e8fc').text.split()
                              print(cmsg)
                              if cmsg[0] == msg[0]:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in dell')
                                    comic1[0].append("not found")
                                    print("dell:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                              
                  except: 
                        
                        sleep(3)
                        if driver.find_element_by_class_name('phone-otp-title'):
                              
                              cmsg1=driver.find_element_by_class_name('phone-otp-title').text.split()
                              print(cmsg1)
                              if cmsg1[0]==pmg[0]:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in dell')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("dell:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in dell")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
dell(emails)

# 27 https://accounts.magicbricks.com/userauth/login 

def magic(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://accounts.magicbricks.com/userauth/login")
            sleep(5)
            msg = "No User found with this Email id."
            
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Forgot Password?"
            pmg.split()

            try:  
                  
                  
                  sleep(2)
                  pos = driver.find_element_by_css_selector('#firstLoginDiv > div.m-login > div:nth-child(1) > label')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_css_selector("#btnStep1").click()

                  sleep(3)
                  
            

                                          
                                          
                  if driver.find_element_by_css_selector('#step1Error'):
                        cmsg = driver.find_element_by_css_selector('#step1Error').text
                        print(cmsg)
                        if cmsg == msg:
                              comic = str(emails[k] + ' ' + 'is not   Registered in magicbricks')
                              comic1[0].append("not found")
                              print("magicbricks:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                              driver.find_element_by_css_selector('#activatedPoUp > button.push-btn.close-button').click()

                                          
                        sleep(3)
                        if driver.find_element_by_css_selector('#loginForm > div > div.m-login__fieldset.clearfix > div.m-login__forgot > a'):
                                                
                              cmsg=driver.find_element_by_css_selector('#loginForm > div > div.m-login__fieldset.clearfix > div.m-login__forgot > a').text
                              print(cmsg)
                              if cmsg==pmg:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in magicbricks')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("magicbricks:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                                    
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in magicbricks")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1

magic(emails)

# 28 https://economictimes.indiatimes.com/login.cms


k=0
for i in range(len(emails)):
      driver.get("https://economictimes.indiatimes.com/login.cms")
      sleep(15)
      msg = "Set your password"
      
      comic1 = [[], [], []]
      sleep(5)
      pmg = "Enter your password"
      pmg.split()

      try:  
            
            sleep(2)
            driver.find_element_by_css_selector('#lg_login_option > form > div > div.lg_obtn.clk.clr.lg_sso > span').click()
            sleep(2)
            pos = driver.find_element_by_css_selector('#lg_login > form > div.lg_row > input')
            pos.send_keys(emails[k])
            sleep(3)
            
            driver.find_element_by_css_selector("#lg_login > form > div:nth-child(2) > input").click()

            sleep(3)
            
      

            if driver.find_element_by_css_selector('#lg_register > h2'):
                  cmsg = driver.find_element_by_css_selector('#lg_register > h2').text
                  print(cmsg)
                  if cmsg == msg:
                        comic = str(emails[k] + ' ' + 'is not   Registered in economictimes')
                        comic1[0].append("not found")
                        print("economictimes:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                        driver.find_element_by_css_selector('#activatedPoUp > button.push-btn.close-button').click()
  
                  
            sleep(3)
            if driver.find_element_by_css_selector('#lg_password > h2'):
                        
                  cmsg=driver.find_element_by_css_selector('#lg_password > h2').text
                  print(cmsg)
                  if cmsg==pmg:
                        flag_account_found=True
                        flag_account_source=emails[k]
                        flag_account_type="email"
                        comic = str(emails[k] + ' ' + 'is    Registered in economictimes')
                        comic1[0].append("account found")
                        comic1[1].append("email")
                        comic1[2].append(emails[k])
                        print("economictimes:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
            
                        
      except:
                 
            f = open("error.log", "a")
            f.write(msg + " " "messages are not found in economictimes")
            f.close()
            comic1[0].append("Not Checked")
      sleep(3)
      k=k+1


# 29 https://access.trivago.com/oauth/en-IN/login  the accesssed denied 

def trivago(emails):
      k=0
      for i in range(len(emails)):
            driver.get("https://access.trivago.com/oauth/en-IN/login")
            sleep(15)
            msg = "Create your account"
            
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Welcome back!"
            pmg.split()

            try:  
                  
                  
                  sleep(2)
                  pos = driver.find_element_by_css_selector('#check_email')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_class_name("btn btn btn--icon-leading btn--primary btn--regular btn--w-100 btn--icon-text-centered btn--signup").click()

                  sleep(3)
                  
            

                  if driver.find_element_by_css_selector('#unified-sign-in > section > div > div > h1'):
                        cmsg = driver.find_element_by_css_selector('#unified-sign-in > section > div > div > h1').text
                        print(cmsg)
                        if cmsg == msg:
                              comic = str(emails[k] + ' ' + 'is not   Registered in trivago')
                              comic1[0].append("not found")
                              print("trivago:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                              driver.find_element_by_css_selector('#activatedPoUp > button.push-btn.close-button').click()
      
                        
                  sleep(3)
                  if driver.find_element_by_css_selector('#unified-sign-in > section > div > div > h1'):
                              
                        cmsg=driver.find_element_by_css_selector('#unified-sign-in > section > div > div > h1').text
                        print(cmsg)
                        if cmsg==pmg:
                              flag_account_found=True
                              flag_account_source=emails[k]
                              flag_account_type="email"
                              comic = str(emails[k] + ' ' + 'is    Registered in trivago')
                              comic1[0].append("account found")
                              comic1[1].append("email")
                              comic1[2].append(emails[k])
                              print("trivago:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in trivago")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
trivago(emails)

# 30 https://in.explara.com/a/forgot-password

def exp(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://in.explara.com/a/forgot-password")
            sleep(15)
            msg = "Account does not exists"
            
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Resend Verification Code"
            pmg.split()

            try:  
                  
                  
                  sleep(2)
                  pos = driver.find_element_by_css_selector('#email')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_css_selector("#forgotUsr").click()

                  sleep(3)
                  
            

                  try:  
                        sleep(3)
                        if driver.find_element_by_css_selector('#warning > div.iziToast-body > div.iziToast-texts > p'):
                              cmsg = driver.find_element_by_css_selector('#warning > div.iziToast-body > div.iziToast-texts > p').text
                              print(cmsg)
                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in explara')
                                    comic1[0].append("not found")
                                    print("explara:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    
                  except: 
                        
                        sleep(3)
                        if driver.find_element_by_css_selector('body > div.container-fluid.login-container > section > div > div > div.row.no-gutters.justify-content-center.align-items-center.login-wrapper_container.verify-otp > div > div.row.no-gutters.form > div > div > label > a'):
                              
                              cmsg=driver.find_element_by_css_selector('body > div.container-fluid.login-container > section > div > div > div.row.no-gutters.justify-content-center.align-items-center.login-wrapper_container.verify-otp > div > div.row.no-gutters.form > div > div > label > a').text
                              print(cmsg)
                              if cmsg==pmg:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in explara')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("explara:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in explara")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
exp(emails)

# 31 https://login.live.com/login.srf the msg is not detecting 

def login(emails):
      
      k=0
      for i in range(len(mobile)):
            driver.get("https://login.live.com/login.srf")
            sleep(15)
            msg = "Create one!"
            
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Enter password"
            pmg.split()

            try:  
                  
                  
                  sleep(2)
                  pos = driver.find_element_by_css_selector('#i0116')
                  pos.send_keys(mobile[k])
                  sleep(3)
                  
                  driver.find_element_by_css_selector("#idSIButton9").click()

                  sleep(3)
                  
            

                  try:  
                        sleep(3)
                        if driver.find_element_by_css_selector('#signup'):
                              cmsg = driver.find_element_by_css_selector('#signup').text
                              print(cmsg)
                              if cmsg == msg:
                                    comic = str(mobile[k] + ' ' + 'is not   Registered in explara')
                                    comic1[0].append("not found")
                                    print("Microsoft:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+mobile[k] +"\n"+'}')
                                    
                  except: 
                        
                        sleep(3)
                        if driver.find_element_by_css_selector('#loginHeader > div'):
                              
                              cmsg=driver.find_element_by_css_selector('#loginHeader > div').text
                              print(cmsg)
                              if cmsg==pmg:
                                    flag_account_found=True
                                    flag_account_source=mobile[k]
                                    flag_account_type="mobile"
                                    comic = str(mobile[k] + ' ' + 'is    Registered in micorsoft')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(mobile[k])
                                    print("microsdft:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in microsoft")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
login(emails)


# 32 https://mega.nz/recovery

def mega(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://mega.nz/recovery")
            sleep(15)
            msg = "Email address not found, please try again. If you cannot remember the email address associated with your MEGA account, clear the input field and click Start again to skip this step."
            
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Do you have a backup of your Recovery Key?"
            pmg.split()

            try:  
                  
                  
                  sleep(2)
                  pos = driver.find_element_by_css_selector('#recover-input1')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_css_selector("#startholder > div.bottom-page.scroll-block > div.main-pad-block > div > div.block-wrapper > div > div > div > div.card-container > div > div.button-container > div:nth-child(1) > button").click()

                  sleep(3)
                  
            

            
                        
                  if driver.find_element_by_css_selector('#startholder > div.bottom-page.scroll-block > div.main-pad-block > div > div.block-wrapper > div > div > div > div.card-container > div > div.recover-account-email-block > div > div.message-container.mega-banner'):
                        cmsg = driver.find_element_by_css_selector('#startholder > div.bottom-page.scroll-block > div.main-pad-block > div > div.block-wrapper > div > div > div > div.card-container > div > div.recover-account-email-block > div > div.message-container.mega-banner').text
                        print(cmsg)
                        if cmsg == msg:
                              comic = str(emails[k] + ' ' + 'is not   Registered in mega')
                              comic1[0].append("not found")
                              print("mega:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    

                        sleep(2)    
                        cmsg1=driver.find_element_by_css_selector('#startholder > div.bottom-page.scroll-block > div.main-pad-block > div > div.block-wrapper > div > div > div > div.card-container > div > h1').text
                        print(cmsg1)
                        if cmsg1==pmg:
                              flag_account_found=True
                              flag_account_source=emails[k]
                              flag_account_type="emails"
                              comic = str(emails[k] + ' ' + 'is    Registered in mega')
                              comic1[0].append("account found")
                              comic1[1].append("email")
                              comic1[2].append(emails[k])
                              print("mega:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in microsoft")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1

mega(emails)

# 33 https://products.ganeshaspeaks.com/login/ 

def product(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://products.ganeshaspeaks.com/login/")
            sleep(15)
            msg = "Unknown email address. Check again or try your username."
            
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Error"
            pmg.split()

            try:  
                  sleep(2)
                  driver.find_element_by_css_selector('#socialLogin > a:nth-child(3) > img').click()
                  sleep(2)
                  pos = driver.find_element_by_css_selector('#user_email')
                  pos.send_keys(emails[k])
                  sleep(3)
                  pos_p=driver.find_element_by_css_selector('#user_password')
                  pos_p.send_keys(Random_password)
                  sleep(2)
                  driver.find_element_by_css_selector("#submit_email_login").click()

                  sleep(3)
                  
            

            
                  
                  if driver.find_element_by_css_selector('#invalid_password'):
                        cmsg = driver.find_element_by_css_selector('#invalid_password').text
                        print(cmsg)
                        if cmsg == msg:
                              comic = str(emails[k] + ' ' + 'is not   Registered in ganeshaspeaks')
                              comic1[0].append("not found")
                              print("ganeshaspeaks:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    

                        
                  sleep(3)
                  if driver.find_element_by_css_selector('#invalid_password > strong:nth-child(1)'):
                              
                        cmsg=driver.find_element_by_css_selector('#invalid_password > strong:nth-child(1)').text
                        print(cmsg)
                        if cmsg[0]==pmg[0]:
                              flag_account_found=True
                              flag_account_source=emails[k]
                              flag_account_type="email"
                              comic = str(mobile[k] + ' ' + 'is    Registered in ganeshaspeaks')
                              comic1[0].append("account found")
                              comic1[1].append("email")
                              comic1[2].append(emails[k])
                              print("ganeshaspeaks:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in ganeshaspeaks")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
product(emails)

# 34 https://soundcloud.com/ not detecting xpath and css 

def sound(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://soundcloud.com/")
            sleep(10)
            msg = "Choose a password"
            
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Welcome back!"
            pmg.split()

            try:  
                  sleep(2)
                  driver.find_element_by_xpath('//*[@id="content"]/div/div/div[1]/div/div[2]/button[1]').click()
                  sleep(2)
                  # driver.find_element_by_css_selector('#gh-ug > a').click()
                  # sleep(2)
                  pos = driver.find_element_by_id('sign_in_up_email')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_css_selector("#sign_in_up_submit").click()

                  sleep(3)
                  
            

                  try:  
                        sleep(3)
                        if driver.find_element_by_css_selector('#app > div > div > form > div:nth-child(2) > div > label'):
                              cmsg = driver.find_element_by_css_selector('#app > div > div > form > div:nth-child(2) > div > label').text
                              print(cmsg)
                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in soundcloud')
                                    comic1[0].append("not found")
                                    print("soundcloud:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    
                  except: 
                        
                        sleep(3)
                        if driver.find_element_by_css_selector('#app > div > div > h2'):
                              
                              cmsg=driver.find_element_by_css_selector('#app > div > div > h2').text
                              print(cmsg)
                              if cmsg==pmg:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(mobile[k] + ' ' + 'is    Registered in soundcloud')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("soundcloud:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in soundcloud")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
sound(emails)

# 34 https://twitter.com/i/flow/login 

def twitter(emails):
      
            k=0
            for i in range(len(emails)):
                  driver.get("https://twitter.com/i/flow/login")
                  sleep(10)
                  msg = "css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0"
                  
                  comic1 = [[], [], []]
                  sleep(5)
                  pmg = "Verify your personal information"
                  pmg.split()

                  try:  
                        sleep(2)
                        driver.find_element_by_css_selector('#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div.css-18t94o4.css-1dbjc4n.r-1niwhzg.r-1ets6dv.r-sdzlij.r-1phboty.r-rs99b7.r-ywje51.r-usiww2.r-2yi16.r-1qi8awa.r-1ny4l3l.r-ymttw5.r-o7ynqc.r-6416eg.r-lrvibr.r-13qz1uu > div > span > span').click()
                        sleep(2)
                        pos = driver.find_element_by_css_selector('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div.css-1dbjc4n.r-mk0yit.r-1f1sjgu > label > div > div.css-1dbjc4n.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div > input')
                        pos.send_keys(emails[k])
                        sleep(3)
                        
                        driver.find_element_by_css_selector("#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-1isdzm1 > div > div > div > div").click()

                        sleep(1)
                        
                  

                        try:  
                              sleep(1)
                              if driver.find_element_by_css_selector('#layers > div:nth-child(3) > div > div > div > div > div.css-901oao.r-1wbh5a2.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-1e081e0.r-qvutc0 > span'):
                                    cmsg = driver.find_element_by_css_selector('#layers > div:nth-child(3) > div > div > div > div > div.css-901oao.r-1wbh5a2.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-1e081e0.r-qvutc0 > span').text
                                    print(cmsg)
                                    if cmsg == msg:
                                          comic = str(emails[k] + ' ' + 'is not   Registered in twitter')
                                          comic1[0].append("not found")
                                          print("twitter:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                          
                        except: 
                              
                              sleep(3)
                              if driver.find_element_by_css_selector('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div:nth-child(1) > div > div.css-901oao.r-37j5jr.r-1yjpyg1.r-b88u0q.r-ueyrd6.r-bcqeeo.r-qvutc0 > span > span'):
                                    
                                    cmsg=driver.find_element_by_css_selector('#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div:nth-child(1) > div > div.css-901oao.r-37j5jr.r-1yjpyg1.r-b88u0q.r-ueyrd6.r-bcqeeo.r-qvutc0 > span > span').text
                                    print(cmsg)
                                    if cmsg==pmg:
                                          flag_account_found=True
                                          flag_account_source=emails[k]
                                          flag_account_type="email"
                                          comic = str(mobile[k] + ' ' + 'is    Registered in soundcloud')
                                          comic1[0].append("account found")
                                          comic1[1].append("email")
                                          comic1[2].append(emails[k])
                                          print("twitter:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                        
                                    
                  except:
                        
                        f = open("error.log", "a")
                        f.write(msg + " " "messages are not found in twitter")
                        f.close()
                        comic1[0].append("Not Checked")
                  sleep(3)
                  k=k+1
twitter(emails)

# 35 https://22bet.com/in/ showing captcha 


k=0
for i in range(len(emails)):
      driver.get("https://22bet.com/in/")
      sleep(10)
      msg = "E-mail not found!"
      
      comic1 = [[], [], []]
      sleep(5)
      pmg = "A message has been sent to your e-mail"
      pmg.split()

      try:  
            sleep(2)
            driver.find_element_by_css_selector('#cookie-agree-policy > div').click()
            sleep(3)
            driver.find_element_by_css_selector('#curLoginForm > span.name').click()
            sleep(3)
            driver.find_element_by_css_selector('#loginout > div.fLogin2 > div > div > div.loginDropTop_div > div:nth-child(1) > form > div.clearSave > a').click()
            sleep(3)
            if driver.find_element_by_id("recaptcha-accessible-status"):
                  driver.delete_all_cookies()
                  driver.get("https://22bet.com/in/")
                  
            pos = driver.find_element_by_css_selector('#forgot_pass_div > div.forgot-wrap > div.forgot__input.forgot__input_email > input')
            pos.send_keys(emails[k])
            sleep(3)
            
            driver.find_element_by_css_selector("#forgot_pass_div > a").click()

            sleep(3)
            
      

            try:  
                  sleep(3)
                  if driver.find_element_by_css_selector('#swal2-content'):
                        cmsg = driver.find_element_by_css_selector('#swal2-content').text
                        print(cmsg)
                        if cmsg == msg:
                              comic = str(emails[k] + ' ' + 'is not   Registered in bet22')
                              comic1[0].append("not found")
                              print("twitter:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                              
            except: 
                  
                  sleep(3)
                  if driver.find_element_by_css_selector('#swal2-content'):
                        
                        cmsg=driver.find_element_by_css_selector('#swal2-content').text
                        print(cmsg)
                        if cmsg==pmg:
                              flag_account_found=True
                              flag_account_source=emails[k]
                              flag_account_type="email"
                              comic = str(mobile[k] + ' ' + 'is    Registered in bet22')
                              comic1[0].append("account found")
                              comic1[1].append("email")
                              comic1[2].append(emails[k])
                              print("bet22:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
            
                        
      except:
                 
            f = open("error.log", "a")
            f.write(msg + " " "messages are not found in bet22")
            f.close()
            comic1[0].append("Not Checked")
      sleep(3)
      k=k+1


#36 https://www.1mg.com/


k=0
for i in range(len(emails)):
      driver.get("https://www.1mg.com/")
      sleep(10)
      msg = "Oops! We could not find an account associated with your email address. Please try with a different email/number"
      
      comic1 = [[], [], []]
      sleep(5)
      pmg = "Edit"
      pmg.split()
      msg2="Maximum attempts made for sending OTP. Please try again after 5 minutes."
      try:  
            sleep(2)
            driver.find_element_by_css_selector('#header > div.row.hidden-xs.styles__top-row___1GOEC > div.col-sm-4.pad0.lang-profile > div > div.hidden-xs.styles__user-info___1cXqm > div > a:nth-child(1) > span').click()
            
                  
            pos = driver.find_element_by_css_selector('#login-signup-modal--react > div > div > div > div > div > div > div > div.style__right-side-wrapper___32zVC > div.style__auth-wrapper___2Z5D3 > div > div > div:nth-child(1) > div:nth-child(2) > div > div.style__wrapper___EMT3C.style__input-error___3piwq > div > input')
            pos.send_keys(emails[k])
            sleep(3)
            
            driver.find_element_by_css_selector("#login-signup-modal--react > div > div > div > div > div > div > div > div.style__right-side-wrapper___32zVC > div.style__auth-wrapper___2Z5D3 > div > div > div:nth-child(2) > div:nth-child(1) > a").click()

            sleep(3)
            
      

           
         
            if driver.find_element_by_css_selector('#login-signup-modal--react > div > div > div > div > div > div > div > div.style__right-side-wrapper___32zVC > div.style__auth-wrapper___2Z5D3 > div > div > div:nth-child(1) > div:nth-child(2) > div > div.style__inline-error-wrapper___1i2-5.style__color-error___qUdd8 > span'):
                  cmsg = driver.find_element_by_css_selector('#login-signup-modal--react > div > div > div > div > div > div > div > div.style__right-side-wrapper___32zVC > div.style__auth-wrapper___2Z5D3 > div > div > div:nth-child(1) > div:nth-child(2) > div > div.style__inline-error-wrapper___1i2-5.style__color-error___qUdd8 > span').text
                  print(cmsg)
                  if cmsg == msg or msg2:
                        comic = str(emails[k] + ' ' + 'is not   Registered in 1mg')
                        comic1[0].append("not found")
                        print("1mg:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                              
       
                  
                
                        
                  cmsg2=driver.find_element_by_css_selector('#login-signup-modal--react > div > div > div > div > div > div > div > div.style__right-side-wrapper___32zVC > div.style__auth-wrapper___2Z5D3 > div > div > div:nth-child(1) > div:nth-child(1) > div.style__explanation-wrapper___2Uqb6 > span > span.style__link___1dTKd').text
                  print(cmsg2)
                  if cmsg2[0]==pmg[0]:
                        flag_account_found=True
                        flag_account_source=emails[k]
                        flag_account_type="email"
                        comic = str(mobile[k] + ' ' + 'is    Registered in 1mg')
                        comic1[0].append("account found")
                        comic1[1].append("email")
                        comic1[2].append(emails[k])
                        print("1mg:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
            
                        
      except:
                 
            f = open("error.log", "a")
            f.write(msg + " " "messages are not found in 1mg")
            f.close()
            comic1[0].append("Not Checked")
      sleep(3)
      k=k+1


# 37 https://www.arkadium.com/


k=0
for i in range(len(emails)):
      driver.get("https://www.arkadium.com/")
      sleep(10)
      msg = "Sorry, we can't locate that email address."
      
      comic1 = [[], [], []]
      sleep(5)
      pmg = "Resend"
      pmg.split()

      try:  
            sleep(2)
            driver.find_element_by_css_selector('#root > div > div > div.fresnel-container.fresnel-lessThan-ARK_SMALL_DESKTOP > nav > div > button:nth-child(4) > span').click()
            sleep(3)
            driver.find_element_by_css_selector('#root > div > div > div.RightSlideInPanel-panel-SchVCpB_.RightSlideInPanel-leveled-QJFd0yIL > div.RightSlideInPanel-content-mltRbS4a > div > div.SignUpPanel-subHeader-onXNZMIa > button > span').click()
            sleep(3)
            driver.find_element_by_css_selector('#root > div > div > div.RightSlideInPanel-panel-SchVCpB_.RightSlideInPanel-leveled-QJFd0yIL > div.RightSlideInPanel-content-mltRbS4a > div > div.SignInPanel-inputFields-WSFwBTcH > button > span').click()
            sleep(3)
            
                  
            pos = driver.find_element_by_css_selector('#root > div > div > div.RightSlideInPanel-panel-SchVCpB_.RightSlideInPanel-leveled-QJFd0yIL > div.RightSlideInPanel-content-mltRbS4a > div > div.ResetPasswordPanel-inputRow-QeILi7k5 > div.Input-root-gwcpBWQx > div > input')
            pos.send_keys(emails[k])
            sleep(3)
            
            driver.find_element_by_css_selector("#root > div > div > div.RightSlideInPanel-panel-SchVCpB_.RightSlideInPanel-leveled-QJFd0yIL > div.RightSlideInPanel-content-mltRbS4a > div > div.MobilePanelFooter-footer-FM9i7ZNH > div > button > span").click()

            sleep(3)
            
      

            try:  
                  sleep(3)
                  if driver.find_element_by_css_selector('#text-error-message'):
                        cmsg = driver.find_element_by_css_selector('#text-error-message').text
                        print(cmsg)
                        if cmsg == msg:
                              comic = str(emails[k] + ' ' + 'is not   Registered in arkadium')
                              comic1[0].append("not found")
                              print("arkadium:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                              
            except: 
                  
                  sleep(3)
                  if driver.find_element_by_css_selector('#root > div > div > div.RightSlideInPanel-panel-SchVCpB_.RightSlideInPanel-leveled-QJFd0yIL > div.RightSlideInPanel-content-mltRbS4a > div > div.ThankYouPanel-middleButton-ycWN1Kzq > button > span'):
                        
                        cmsg1=driver.find_element_by_css_selector('#root > div > div > div.RightSlideInPanel-panel-SchVCpB_.RightSlideInPanel-leveled-QJFd0yIL > div.RightSlideInPanel-content-mltRbS4a > div > div.ThankYouPanel-middleButton-ycWN1Kzq > button > span').text
                        print(cmsg1)
                        if cmsg1[0]==pmg[0]:
                              flag_account_found=True
                              flag_account_source=emails[k]
                              flag_account_type="email"
                              comic = str(mobile[k] + ' ' + 'is    Registered in arkadium')
                              comic1[0].append("account found")
                              comic1[1].append("email")
                              comic1[2].append(emails[k])
                              print("arkadium:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
            
                        
      except:
                 
            f = open("error.log", "a")
            f.write(msg + " " "messages are not found in arkadium")
            f.close()
            comic1[0].append("Not Checked")
      sleep(3)
      k=k+1


# 38 https://www.91mobiles.com/#

k=0
for i in range(len(emails)):
      driver.get("https://www.91mobiles.com/#")
      sleep(10)
      msg = "This email address is not registered with us"
      
      comic1 = [[], [], []]
      sleep(5)
      pmg = "Email Sent!! Please check you inbox."
      pmg.split()

      try:  
            sleep(2)
            driver.find_element_by_css_selector('#login_wrap > span.variousCommon.links').click()
            sleep(3)
            driver.find_element_by_css_selector('#frmlogin > span > a').click()
            sleep(3)
            
            
                  
            pos = driver.find_element_by_css_selector('#emailId_forgot')
            pos.send_keys(emails[k])
            sleep(3)
            
            driver.find_element_by_css_selector("#frmForgotPasswort > input.reset").click()

            sleep(3)
            
      

         

            if driver.find_element_by_css_selector('#errCon_forgot'):
                cmsg = driver.find_element_by_css_selector('#errCon_forgot').text
                print(cmsg)
                if cmsg == msg:
                      comic = str(emails[k] + ' ' + 'is not   Registered in 91mobiles')
                      comic1[0].append("not found")
                      print("91mobiles:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                              
       
                  
                
                if cmsg[0]==pmg[0]:
                  flag_account_found=True
                  flag_account_source=emails[k]
                  flag_account_type="email"
                  comic = str(emails[k] + ' ' + 'is    Registered in 91mobiles')
                  comic1[0].append("account found")
                  comic1[1].append("email")
                  comic1[2].append(emails[k])
                  print("91mobiles:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
            
                        
      except:
                 
            f = open("error.log", "a")
            f.write(msg + " " "messages are not found in 91mobiles")
            f.close()
            comic1[0].append("Not Checked")
      sleep(3)
      k=k+1


## 39 https://auth.services.adobe.com/en_US/index.html?callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2FBehanceWebSusi1%2FAdobeID%2Ftoken%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.behance.net%252Fonboarding%2523from_ims%253Dtrue%2526old_hash%253D%2526api%253Dauthorize%26state%3D%257B%2522ac%2522%253A%2522behance.net%2522%252C%2522csrf%2522%253A%25220eadad3c-410a-4122-98be-b9d08b0cd3fd%2522%252C%2522version%2522%253A1%257D%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=BehanceWebSusi1&scope=AdobeID%2Copenid%2Cgnav%2Csao.cce_private%2Ccreative_cloud%2Ccreative_sdk%2Cbe.pro2.external_client%2Cadditional_info.roles&denied_callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fdenied%2FBehanceWebSusi1%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.behance.net%252Fonboarding%2523from_ims%253Dtrue%2526old_hash%253D%2526api%253Dauthorize%26response_type%3Dtoken%26state%3D%257B%2522ac%2522%253A%2522behance.net%2522%252C%2522csrf%2522%253A%25220eadad3c-410a-4122-98be-b9d08b0cd3fd%2522%252C%2522version%2522%253A1%257D&state=%7B%22ac%22%3A%22behance.net%22%2C%22csrf%22%3A%220eadad3c-410a-4122-98be-b9d08b0cd3fd%22%2C%22version%22%3A1%7D&relay=2d6609ce-0f1e-4e1f-9bee-9647a86015ad&locale=en_US&flow_type=token&dctx_id=bhnc_22989526-955d-49e3-9a7d-f093e8f3dbf5&idp_flow_type=login&ab_test=signup-phone%2Csignup-phone-default&s_p=apple%2Cfacebook%2Cgoogle#/
# msg not detecting

k=0
for i in range(len(emails)):
      driver.get("https://auth.services.adobe.com/en_US/index.html?callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fadobeid%2FBehanceWebSusi1%2FAdobeID%2Ftoken%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.behance.net%252Fonboarding%2523from_ims%253Dtrue%2526old_hash%253D%2526api%253Dauthorize%26state%3D%257B%2522ac%2522%253A%2522behance.net%2522%252C%2522csrf%2522%253A%25220eadad3c-410a-4122-98be-b9d08b0cd3fd%2522%252C%2522version%2522%253A1%257D%26code_challenge_method%3Dplain%26use_ms_for_expiry%3Dtrue&client_id=BehanceWebSusi1&scope=AdobeID%2Copenid%2Cgnav%2Csao.cce_private%2Ccreative_cloud%2Ccreative_sdk%2Cbe.pro2.external_client%2Cadditional_info.roles&denied_callback=https%3A%2F%2Fims-na1.adobelogin.com%2Fims%2Fdenied%2FBehanceWebSusi1%3Fredirect_uri%3Dhttps%253A%252F%252Fwww.behance.net%252Fonboarding%2523from_ims%253Dtrue%2526old_hash%253D%2526api%253Dauthorize%26response_type%3Dtoken%26state%3D%257B%2522ac%2522%253A%2522behance.net%2522%252C%2522csrf%2522%253A%25220eadad3c-410a-4122-98be-b9d08b0cd3fd%2522%252C%2522version%2522%253A1%257D&state=%7B%22ac%22%3A%22behance.net%22%2C%22csrf%22%3A%220eadad3c-410a-4122-98be-b9d08b0cd3fd%22%2C%22version%22%3A1%7D&relay=2d6609ce-0f1e-4e1f-9bee-9647a86015ad&locale=en_US&flow_type=token&dctx_id=bhnc_22989526-955d-49e3-9a7d-f093e8f3dbf5&idp_flow_type=login&ab_test=signup-phone%2Csignup-phone-default&s_p=apple%2Cfacebook%2Cgoogle#/")
      sleep(13)
      msg = "Find your account"
      
      comic1 = [[], [], []]
      sleep(5)
      pmg = "Welcome back"
      pmg.split()

      try:  
            sleep(2)
             
            pos = driver.find_element_by_css_selector('#EmailPage-EmailField')
            pos.clear()
            pos.send_keys(emails[k])
            sleep(3)
            
            driver.find_element_by_css_selector("#EmailForm > section.EmailPage__submit.mod-submit > div.ta-right > button").click()
            
            sleep(2)
            
            
      
            try:
          
               
                  if driver.find_element_by_css_selector('#EmailForm > section.EmailPage__email-field.form-group > label > a:nth-child(2)'):
                      cmsg = driver.find_element_by_css_selector('#EmailForm > section.EmailPage__email-field.form-group > label > a:nth-child(2)').text.split()
                      print(cmsg)
                      if cmsg[0] == msg[0]:
                            comic = str(emails[k] + ' ' + 'is not   Registered in behance')
                            comic1[0].append("not found")
                            print("behance:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
               
            except:
                  if driver.find_element_by_css_selector('#EmailForm > section.EmailPage__email-field.form-group > label'):
                      cmsg1=driver.find_element_by_css_selector('#EmailForm > section.EmailPage__email-field.form-group > label').text.split()
                      print(cmsg1)
                      if cmsg1[0]==pmg[0]:
                            flag_account_found=True
                            flag_account_source=emails[k]
                            flag_account_type="email"
                            comic = str(emails[k] + ' ' + 'is    Registered in behance')
                            comic1[0].append("account found")
                            comic1[1].append("email")
                            comic1[2].append(emails[k])
                            print("behance:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
            
                        
      except:
                 
            f = open("error.log", "a")
            f.write(msg + " " "messages are not found in behance")
            f.close()
            comic1[0].append("Not Checked")
      sleep(3)
      k=k+1


# 40 https://www.bigbasket.com/?nc=close

k=0
for i in range(len(emails)):
      driver.get("https://www.bigbasket.com/?nc=close")
      sleep(10)
      msg = "Verify Mobile Number"
      
      comic1 = [[], [], []]
      sleep(5)
      pmg = "Verify Email Address"
      pmg.split()

      try:  
            sleep(2)
            driver.find_element_by_css_selector('#headerControllerId > header > div > div > div > div > ul > li:nth-child(3) > ul > li.auth > span:nth-child(2) > a').click()
            sleep(3)
            driver.find_element_by_css_selector('#login > login > div > form > div:nth-child(2) > button:nth-child(2)')  .click()
            sleep(3)
            pos = driver.find_element_by_css_selector('#otpEmail')
            pos.send_keys(emails[k])
            sleep(3)
            
            driver.find_element_by_css_selector("#login > login > div > form > div:nth-child(2) > button.btn.btn-default.login-btn").click()

            sleep(3)
            
      

            
                 
            if driver.find_element_by_css_selector('#login > login > div > div.clearfix > div.col-md-9 > h4'):
                  cmsg = driver.find_element_by_css_selector('#login > login > div > div.clearfix > div.col-md-9 > h4').text
                  print(cmsg)
                     
                  if cmsg == msg:
                        comic = str(emails[k] + ' ' + 'is not   Registered in bigbasket')
                        comic1[0].append("not found")
                        print("bigbasket:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                              
           
               
                  if cmsg==pmg:
                        flag_account_found=True
                        flag_account_source=emails[k]
                        flag_account_type="email"
                        comic = str(emails[k] + ' ' + 'is    Registered in bigbasket')
                        comic1[0].append("account found")
                        comic1[1].append("email")
                        comic1[2].append(emails[k])
                        print("bigbasket:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
            
                        
      except:
                 
            f = open("error.log", "a")
            f.write(msg + " " "messages are not found in bigbasket")
            f.close()
            comic1[0].append("Not Checked")
      sleep(3)
      k=k+1

## 41 https://www.booking.com/

def book(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.booking.com/")
            sleep(10)
            msg = "Create password"
            
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Enter your password"
            pmg.split()

            try:  
                  sleep(2)
                  driver.find_element_by_css_selector('#b2indexPage > header > nav.bui-header__bar > div.bui-group.bui-button-group.bui-group--inline.bui-group--align-end.bui-group--vertical-align-middle > div:nth-child(6) > a').click()
                  sleep(3)
                  pos = driver.find_element_by_css_selector('#username')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_css_selector("#root > div > div > div > div.app > div.access-container.bui_font_body > div > div > div > div > div > div > form > div:nth-child(3) > button > span").click()

                  sleep(3)
                  
      
            
                  if driver.find_element_by_id('7fe2e363-c7ba-4dc6-981b-bc71da5f1ff3'):
                        cmsg = driver.find_element_by_id('7fe2e363-c7ba-4dc6-981b-bc71da5f1ff3').text.split()
                        print(cmsg)
                        if cmsg[0] == msg[0]:
                              comic = str(emails[k] + ' ' + 'is not   Registered in booking')
                              comic1[0].append("not found")
                              print("booking:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                          

                              
                              
                                    
                        cmsg1=driver.find_element_by_id('12fb4c6e-fbbf-4311-87c9-e95709a480d8').text.split()
                        print(cmsg1)
                        if cmsg1[0]==pmg[0]:
                              flag_account_found=True
                              flag_account_source=emails[k]
                              flag_account_type="email"
                              comic = str(emails[k] + ' ' + 'is    Registered in booking')
                              comic1[0].append("account found")
                              comic1[1].append("email")
                              comic1[2].append(emails[k])
                              print("booking:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                        



                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in booking")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
book(emails)

# 42 https://www.ebay.com/signin/ asking for recpacha

def ebay(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.ebay.com/signin/")
            sleep(10)
            msg = "Oops, that's not a match."
            
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Welcome"
            pmg.split()

            try:  
                  
                  sleep(3)
                  
                        
                  pos = driver.find_element_by_css_selector('#userid')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_css_selector("#signin-continue-btn").click()

                  sleep(3)
                  
            

                  try:  
                        sleep(3)
                        if driver.find_element_by_css_selector('#errormsg'):
                              cmsg = driver.find_element_by_css_selector('#errormsg').text
                              print(cmsg)
                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in ebay')
                                    comic1[0].append("not found")
                                    print("ebay:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    
                  except: 
                        
                        sleep(3)
                        if driver.find_element_by_css_selector('#root > div > div > div.RightSlideInPanel-panel-SchVCpB_.RightSlideInPanel-leveled-QJFd0yIL > div.RightSlideInPanel-content-mltRbS4a > div > div.ThankYouPanel-middleButton-ycWN1Kzq > button > span'):
                              
                              cmsg1=driver.find_element_by_css_selector('#root > div > div > div.RightSlideInPanel-panel-SchVCpB_.RightSlideInPanel-leveled-QJFd0yIL > div.RightSlideInPanel-content-mltRbS4a > div > div.ThankYouPanel-middleButton-ycWN1Kzq > button > span').text
                              print(cmsg1)
                              if cmsg1[0]==pmg[0]:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(mobile[k] + ' ' + 'is    Registered in ebay')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("ebay:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in ebay")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1

ebay(emails)

   
# 44 flipkart the msg is not detecting 

def flipkart(emails):
      k=0
      for i in range(len(emails)):
            driver.get("https://www.flipkart.com/account/login?ret=/")
            sleep(15)
            msg = "Existing User? Log in"
            msg.split()
            comic1 = [[], [], []]
            pmg = "Your username or password is incorrect"
            pmg.split()
            
            try:  
                  

                  sleep(3) 
                  
                  pos = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')
                  pos.send_keys(emails[k])
                  sleep(3)
                  pos_p = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[2]/input')
                  pos_p.send_keys(Random_password)
                  sleep(3)
                  driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div/form/div[4]/button").click()

                  sleep(1)
                  
            

            
            
                  if driver.find_element_by_css_selector('#container > div > div._2dSUjN > div > div._36HLxm.col.col-3-5 > div > form > div._1D1L_j > a > span'):
                        cmsg = driver.find_element_by_css_selector('#container > div > div._2dSUjN > div > div._36HLxm.col.col-3-5 > div > form > div._1D1L_j > a > span').text.split()
                        print(cmsg)
                  if cmsg[0] == msg[0]:
                        comic = str(emails[k] + ' ' + 'is not   Registered in flipkart')
                        comic1[0].append("not found")
                        print("flipkart:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    
      
                        
                        
                              
                  cmsg1=driver.find_element_by_css_selector('#container > div > div._2dSUjN > div > div._36HLxm.col.col-3-5 > div > form > div.IiD88i._351hSN.undefined > span._2YULOR > span').text.split()
                  print(cmsg1)
                  if cmsg1[0]==pmg[0]:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(mobile[k] + ' ' + 'is    Registered in flipkart')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("flipkart:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in flipkart")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
flipkart(emails)

#45 https://www.freshmenu.com/mumbai msg is not detecting 

def fresh(emails):
      k=0
      for i in range(len(emails)):
            driver.get("https://www.freshmenu.com/mumbai")
            sleep(10)
            msg = "Email id is not registered."
            msg.split()
            comic1 = [[], [], []]
            pmg = "OR"
            pmg.split()

            try:  
                  sleep(3)
                  driver.find_element_by_css_selector('#mainController > div.fm-top-nav-experiment > div.fm-top-nav-secondary > div.content.flex-row-center > div.action.fm-user-logged-out-dropdown-container.fm-dropdown-parent').click()
                  sleep(3)
                  driver.find_element_by_css_selector('#mainController > div.fm-top-nav-experiment > div.fm-top-nav-secondary > div.content.flex-row-center > div.action.fm-user-logged-out-dropdown-container.fm-dropdown-parent > div > ul > li:nth-child(1) > a').click()
                  sleep(3) 
            
                  pos = driver.find_element_by_css_selector('#modal-login > form > div.ng-scope > div > input')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_css_selector("#modal-login > form > div.ng-scope > button").click()

                  sleep(3)
                  
            

            
            
                  if driver.find_element_by_class_name('ng-binding'):
                        cmsg = driver.find_element_by_class_name('ng-binding').text.split()
                        print(cmsg)
                        if cmsg[0] == msg[0]:
                              comic = str(emails[k] + ' ' + 'is not   Registered in freshmenu')
                              comic1[0].append("not found")
                              print("freshmenu:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    

                        
                  
                              
                        cmsg1=driver.find_element_by_class_name('or-divider website-modal-button').text.split()
                        # print(cmsg1)
                        if cmsg1[0]==pmg[0]:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(mobile[k] + ' ' + 'is    Registered in freshmenu')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("freshmenu:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in freshmenu")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
fresh(emails)






# 48 https://www.indiaproperty.com/ not done 

def india(emails):
      k=0
      for i in range(len(emails)):
            driver.get("https://www.indiaproperty.com/")
            sleep(5)
            msg = "Invalid emailid"
            
            comic1 = [[], [], []]

            pmg = "Password reset link has been sent successfully."
            pmg.split()

            try:  
                  
                  driver.find_element_by_css_selector('#user-actions').click()
                  sleep(2)
                  driver.find_element_by_css_selector('#header_login_forgot_password > a').click()
                  sleep(2)
            
                  pos = driver.find_element_by_css_selector('#header_login_pwd_reset_email')
                  pos.send_keys(emails[k])
                  sleep(2)
                  
                  driver.find_element_by_css_selector("#header_login_pwd_reset").click()

                  sleep(2)
                  
            

                  try:  
                        sleep(3)
                        if driver.find_element_by_css_selector('#header_login_pwd_reset_credentials_err'):
                              cmsg = driver.find_element_by_css_selector('#header_login_pwd_reset_credentials_err').text
                              print(cmsg)
                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in indiaproperty')
                                    comic1[0].append("not found")
                                    print("indiaproperty:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    
                  except: 
                        
                        sleep(3)
                        if driver.find_element_by_css_selector('#header_login_pwd_link_sent > div.bce-sgnbox-tic2'):
                              
                              cmsg1=driver.find_element_by_css_selector('#header_login_pwd_link_sent > div.bce-sgnbox-tic2').text
                              print(cmsg1)
                              if cmsg1[0]==pmg[0]:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(mobile[k] + ' ' + 'is    Registered in indiaproperty')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("indiaproperty:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in indiaproperty")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1

india(emails)


#50 https://www.khelo365.com/forgot-password msg is not detecting 

def khelo(emails):
      
      k=0
      for i in range(len(mobile)):
            driver.get("https://www.khelo365.com/forgot-password")
            sleep(12)
            msg = "This phone is not registered"
            
            comic1 = [[], [], []]

            pmg = "Please verify your phone"
            pmg.split()

            try:  
                  
                  sleep(2)
            
                  pos = driver.find_element_by_css_selector('#recoverForm > div.input-group > div.input-group > input[type=tel]')
                  pos.send_keys(mobile[k])
                  sleep(4)
                  
                  driver.find_element_by_css_selector("#recoverForm > div:nth-child(3) > button").click()

                  sleep(4)
                  
            

      
                  
                  if driver.find_element_by_css_selector('#recoverForm > div.input-group > div.input-group > span'):
                        cmsg = driver.find_element_by_css_selector('#recoverForm > div.input-group > div.input-group > span').text
                        print(cmsg)
                        if cmsg == msg:
                              comic = str(mobile[k] + ' ' + 'is not   Registered in khelo365')
                              comic1[0].append("not found")
                              print("khelo365:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "mobile_id:"+mobile[k] +"\n"+'}')
                                    
      
                        
                  
                              
                              cmsg1=driver.find_element_by_css_selector('#otpModalLabel').text.split()
                              print(cmsg1)
                              if cmsg1[0]==pmg[0]:
                                    flag_account_found=True
                                    flag_account_source=mobile[k]
                                    flag_account_type="mobile"
                                    comic = str(mobile[k] + ' ' + 'is    Registered in khelo365')
                                    comic1[0].append("account found")
                                    comic1[1].append("mobile")
                                    comic1[2].append(mobile[k])
                                    print("khelo365:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in khelo365")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
khelo(emails)

## 51 https://app.lendbox.in/login

def len(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://app.lendbox.in/login")
            sleep(26)
            msg = "Email does not exist."
            msg.split()
            comic1 = [[], [], []]

            pmg = "Mail sent, please check your inbox."
            pmg.split()

            try:  
                  
                  sleep(2)
                  driver.find_element_by_css_selector('#login-form > div.form-footer > a').click()
                  sleep(4)
                  pos = driver.find_element_by_css_selector('#forgot-password > div.form-input > div > div > input')
                  pos.send_keys(emails[k])
                  sleep(4)
                  
                  driver.find_element_by_css_selector("#forgot-password > div.form-footer > button").click()

                  sleep(4)
                  
            

      
                  
                  if driver.find_element_by_css_selector('#app > div.application--wrap > div.v-snack.v-snack--active.v-snack--multi-line.v-snack--right.v-snack--top > div > div'):
                        cmsg = driver.find_element_by_css_selector('#app > div.application--wrap > div.v-snack.v-snack--active.v-snack--multi-line.v-snack--right.v-snack--top > div > div').text
                        print(cmsg)
                        if cmsg == msg:
                              comic = str(emails[k] + ' ' + 'is not   Registered in lendbox')
                              comic1[0].append("not found")
                              print("lendbox:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
      
                        
                        if cmsg[0]==pmg[0]:
                              flag_account_found=True
                              flag_account_source=emails[k]
                              flag_account_type="email"
                              comic = str(emails[k] + ' ' + 'is    Registered in lendbox')
                              comic1[0].append("account found")
                              comic1[1].append("email")
                              comic1[2].append(emails[k])
                              print("lendbox:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in lendbox")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
len(emails)

## 52 https://www.lotto247.com/en/login/forgot-password

def lotto(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.lotto247.com/en/login/forgot-password")
            sleep(10)
            msg = "We can't seem to find you. Please try again."
            msg.split()
            comic1 = [[], [], []]

            pmg = "Check your email"
            pmg.split()

            try:  
                  
                  sleep(2)
                  
                  pos = driver.find_element_by_css_selector('#mat-input-0')
                  pos.send_keys(emails[k])
                  sleep(4)
                  
                  driver.find_element_by_css_selector("#wrapper > div > div > gli-login-page > div > gli-forgot-password > div > div.left-col > div > form > div.form-control.submit-btn > gli-button > button").click()

                  sleep(4)
                  try:  
                        sleep(3)
                        if driver.find_element_by_css_selector('#wrapper > div > div > gli-login-page > div > gli-forgot-password > div > div.left-col > div > form > div.recover-password-error.ng-star-inserted > div > span'):
                              cmsg = driver.find_element_by_css_selector('#wrapper > div > div > gli-login-page > div > gli-forgot-password > div > div.left-col > div > form > div.recover-password-error.ng-star-inserted > div > span').text
                              print(cmsg)
                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in lotto247')
                                    comic1[0].append("not found")
                                    print("lotto247:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    
                  except: 
                        
                        sleep(3)
                        if driver.find_element_by_css_selector('#wrapper > div > div > gli-login-page > div > gli-forgot-password-success > div > div.left-col > h5'):
                              
                              cmsg1=driver.find_element_by_css_selector('#wrapper > div > div > gli-login-page > div > gli-forgot-password-success > div > div.left-col > h5').text
                              print(cmsg1)
                              if cmsg1[0]==pmg[0]:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(mobile[k] + ' ' + 'is    Registered in lotto247')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("lotto247:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in lotto247")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
lotto(emails)

# 52 https://www.makaan.com/

def makaan(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.makaan.com/")
            sleep(18)
            msg = "Sorry! you are not a registered user."
            msg.split()
            comic1 = [[], [], []]

            pmg = "An OTP has been sent to your registered email and mobile"
            pmg.split()

            try:  
                  
                  sleep(2)
                  driver.find_element_by_css_selector('#mod-header-1 > div.lsfix.clearfix.no-padding > div.rhs-links.clearfix.js-hideonsearch > ul > li.loginlink > div:nth-child(2)').click()
                  sleep(2)
                  driver.find_element_by_css_selector('#sociable_connect > div.mian-field-box.first-screen > div:nth-child(1)').click()
                  sleep(2)
                  driver.find_element_by_css_selector('#main_login > div.mian-field-box > div.links.js-remember-links > a').click()
                  sleep(2)
                  
                  pos = driver.find_element_by_class_name('js-email')
                  pos.send_keys(emails[k])
                  sleep(4)
                  
                  driver.find_element_by_css_selector("#forgot_password > div.mian-field-box > div.login-btn-style.send-link.max-width150").click()

                  sleep(4)
                  try:  
                        sleep(3)
                        if driver.find_element_by_css_selector('#forgot_password > div.mian-field-box > p'):
                              cmsg = driver.find_element_by_css_selector('#forgot_password > div.mian-field-box > p').text
                              print(cmsg)
                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in makaan')
                                    comic1[0].append("not found")
                                    print("makaan:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    
                  except: 
                        
                        sleep(3)
                        if driver.find_element_by_css_selector('#user-details-text > span:nth-child(4)'):
                              
                              cmsg1=driver.find_element_by_css_selector('#user-details-text > span:nth-child(4)').text
                              print(cmsg1)
                              if cmsg1[0]==pmg[0]:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(mobile[k] + ' ' + 'is    Registered in makaan')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("makaan:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in makaan")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
            
makaan(emails)

# 53 https://www.meraevents.com/login 

def meraevent(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.meraevents.com/login")
            sleep(2)
            msg = "Enter registered email id"
            msg.split()
            comic1 = [[], [], []]

            pmg ="Please check your mail"
            pmg.split()

            try:
                  
            
                  sleep(2)
                  driver.find_element_by_css_selector('#loginForm > div.checkbox > label.fwd_pass > a').click()
                  sleep(2)
                  
                  pos = driver.find_element_by_id('forgotEmail')
                  pos.send_keys(emails[k])
                  sleep(2)
                  
                  driver.find_element_by_id("ResetPassword").click()

                  sleep(2)
                  
      
                  if driver.find_element_by_css_selector('#resetPasswordForm > div > span.error.ng-binding'):
                        cmsg = driver.find_element_by_css_selector('#resetPasswordForm > div > span.error.ng-binding').text
                        print(cmsg)
                        if cmsg == msg:
                              comic = str(emails[k] + ' ' + 'is not   Registered in meraevents')
                              comic1[0].append("not found")
                              print("meraevents:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                              
                                    
                  
                        

                        cmsg1 = driver.find_element_by_css_selector('#resetPasswordForm > div > span.successmsg.ng-binding').text
                        if cmsg1 == pmg:
                              flag_account_found=True
                              flag_account_source=emails[k]
                              flag_account_type="email"
                              comic = str(mobile[k] + ' ' + 'is    Registered in meraevents')
                              comic1[0].append("account found")
                              comic1[1].append("email")
                              comic1[2].append(emails[k])
                              print("meraevents:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                              
                        else:
                              print("hello")
                  else:
                        print("excet")      
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in meraevents")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(1)
            k=k+1
meraevent(emails)

                    
                  


# 54 https://www.olx.in/ are not working 

def olx(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.olx.in/#loginemailcode")
            sleep(30)
            msg = "Enter registered email id"
            msg.split()
            comic1 = [[], [], []]

            pmg ="Enter verification code"
            pmg.split()

            try:  
                  
            
                  sleep(2)
                  driver.find_element_by_css_selector('#container > header > div > div > div._14lZ9._110yh > button > span').click()
                  sleep(2)
                  driver.find_element_by_css_selector('body > div:nth-child(24) > div > div > div > span > span').click()
                  sleep(2)
                  pos = driver.find_element_by_css_selector('#email_input_field')
                  pos.send_keys(emails[k])
                  sleep(4)
                  
                  driver.find_element_by_css_selector("body > div:nth-child(24) > div > div > form > div > button").click()

                  sleep(4)
                  
                  try:  
                        sleep(2) 
                        if driver.find_element_by_css_selector('body > div:nth-child(26) > div > div > div._2wUFI.FLgqa.C14r8._39kkL > div'):
                              cmsg = driver.find_element_by_css_selector('body > div:nth-child(26) > div > div > div._2wUFI.FLgqa.C14r8._39kkL > div').text
                              print(cmsg)
                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in olx')
                                    comic1[0].append("not found")
                                    print("olx:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                              
                                          
                        
                        
                  
                  except:
                        if driver.find_element_by_class_name('_1-x0N'):
                              
                              cmsg1=driver.find_element_by_class_name('_1-x0N').text
                              print(cmsg1)
                              if cmsg1 == pmg:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(mobile[k] + ' ' + 'is    Registered in olx')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("olx:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                              
                        
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in olx")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
olx(emails)


# 55 https://dashboard.pokerbaazi.com/login-mobile-number


def poker(emails):
      
      k=0
      for i in range(len(mobile)):
            driver.get("https://dashboard.pokerbaazi.com/login-mobile-number")
            sleep(10)
            msg = "User not found"
            msg.split()
            comic1 = [[], [], []]

            pmg ="2 Step Verification"
            pmg.split()

            try:  
                  
            
                  
                  sleep(2)
                  pos = driver.find_element_by_id('phone')
                  pos.send_keys(mobile[k])
                  sleep(4)
                  
                  driver.find_element_by_css_selector("#root > div > div.authentication__body > div > div > div.pb-container.container-login-mobile > div > form > div.pbButton > button").click()

                  sleep(2)
                  
                  try:  
                        sleep(1) 
                        if driver.find_element_by_class_name('MuiAlert-message'):
                              cmsg = driver.find_element_by_class_name('MuiAlert-message').text
                              print(cmsg)
                              if cmsg == msg:
                                    comic = str(mobile[k] + ' ' + 'is not   Registered in pokerbaazi')
                                    comic1[0].append("not found")
                                    print("pokerbaazi:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "mobile_id:"+mobile[k] +"\n"+'}')
                              
                                          
                        
                        
                  
                  except:
                        if driver.find_element_by_css_selector('#root > div > div.authentication__body > div > div > div.pb-container.container-otp > div > div.otp-header-title > span.pbText.pbText__primary.pbText__xl.pbText__lh_100.pbText__bold.otp-header-title__heading'):
                              
                              cmsg1=driver.find_element_by_css_selector('#root > div > div.authentication__body > div > div > div.pb-container.container-otp > div > div.otp-header-title > span.pbText.pbText__primary.pbText__xl.pbText__lh_100.pbText__bold.otp-header-title__heading').text
                              print(cmsg1)
                              if cmsg1 == pmg:
                                    flag_account_found=True
                                    flag_account_source=mobile[k]
                                    flag_account_type="mobile"
                                    comic = str(mobile[k] + ' ' + 'is    Registered in pokerbaazi')
                                    comic1[0].append("account found")
                                    comic1[1].append("mobile")
                                    comic1[2].append(mobile[k])
                                    print("pokerbaazi:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                              
                        
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in pokerbaazi")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
poker(emails)
 
# 56 https://www.quikr.com/

def quikr(emails):
      k=0
      for i in range(len(emails)):
            driver.get("https://www.quikr.com/")
            sleep(10)
            msg = "Sign Up On Quikr"
            msg.split()
            comic1 = [[], [], []]

            pmg ="Login On Quikr"
            pmg.split()

            try:  
                  
                  driver.find_element_by_css_selector('body > div.wpn_modal_container.wpn_modal_show > div.wpn_modal_modal > div.wpn_modal_actionButtonsContainer > button:nth-child(1)').click()
                  sleep(2)
                  driver.find_element_by_class_name('user-name').click()
                  sleep(2)
                  
                  pos = driver.find_element_by_css_selector('#newLoginSignUpModal > div > div > div > div > form > div.nls_formContainer > div > input[type=text]')
                  pos.send_keys(emails[k])
                  sleep(4)
                  
                  driver.find_element_by_class_name("nls_primaryButton").click()

                  sleep(2)
                  
            
                  
                  if driver.find_element_by_css_selector('#newLoginSignUpModal > div > div > div > header > h4'):
                        cmsg = driver.find_element_by_css_selector('#newLoginSignUpModal > div > div > div > header > h4').text
                        print(cmsg)
                        if cmsg == msg:
                              comic = str(emails[k] + ' ' + 'is not   Registered in quikr')
                              comic1[0].append("not found")
                              print("quikr:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "mobile_id:"+emails[k] +"\n"+'}')
                              
                                          
                        
                        
                  
            
                        if cmsg == pmg:
                              flag_account_found=True
                              flag_account_source=emails[k]
                              flag_account_type="emails"
                              comic = str(emails[k] + ' ' + 'is    Registered in quikr')
                              comic1[0].append("account found")
                              comic1[1].append("emails")
                              comic1[2].append(emails[k])
                              print("quikr:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                        
                  
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in quikr")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
quikr(emails)
 
# 57 https://www.raaga.com/login

def raaga(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.raaga.com/login")
            sleep(10)
            msg = "The e-mail address was not found! Please verify and try again."
            msg.split()
            comic1 = [[], [], []]

            pmg ="Your password reset link will be sent to your email address."
            pmg.split()

            try:  
                  
                  sleep(2)
                  driver.find_element_by_class_name('ac_acc').click()
                  sleep(2)
                  pos = driver.find_element_by_id('email')
                  pos.send_keys(emails[k])
                  sleep(4)
                  
                  driver.find_element_by_css_selector("#addtoplaylist_submit > aside:nth-child(1)").click()

                  sleep(2)
                  
            
                  if driver.find_element_by_class_name('alertmsg_div'):
                        cmsg = driver.find_element_by_class_name('alertmsg_div').text
                        print(cmsg)
                        if cmsg == msg:
                              comic = str(emails[k] + ' ' + 'is not   Registered in raaga')
                              comic1[0].append("not found")
                              print("raaga:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                              
                                          
                        
                        
                  
            
                        
                        if cmsg == pmg:
                              flag_account_found=True
                              flag_account_source=emails[k]
                              flag_account_type="email"
                              comic = str(mobile[k] + ' ' + 'is    Registered in raaga')
                              comic1[0].append("account found")
                              comic1[1].append("emails")
                              comic1[2].append(emails[k])
                              print("raaga:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                        
                        
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in raaga")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
raaga(emails)

# 58 https://www.realestateindia.com/login.php

def real(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.realestateindia.com/login.php")
            sleep(15)
            msg = "Incorrect Email ID"
            
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Enter Password"
            pmg.split()

            try:  
                  
                  
                  sleep(2)
                  pos = driver.find_element_by_id('user_name')
                  pos.send_keys(emails[k])
                  sleep(3)
                  
                  driver.find_element_by_css_selector("#loginMember > button").click()

                  sleep(3)
                  
            

                  try:  
                        sleep(3)
                        if driver.find_element_by_css_selector('#error_warning > p.dif.mb5px.large.fw6'):
                              cmsg = driver.find_element_by_css_selector('#error_warning > p.dif.mb5px.large.fw6').text
                              print(cmsg)
                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in realestateindia')
                                    comic1[0].append("not found")
                                    print("realestateindia:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    
                  except: 
                        
                        sleep(3)
                        if driver.find_element_by_css_selector('#loginMemberPass > p.fw6.mt10px.mb5px'):
                              
                              cmsg=driver.find_element_by_css_selector('#loginMemberPass > p.fw6.mt10px.mb5px').text
                              print(cmsg)
                              if cmsg==pmg:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in realestateindia')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("realestateindia:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in realestateindia")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
real(emails)


# 59 https://www.snapdeal.com/ not working

def snapdeal(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.snapdeal.com/")
            sleep(25)
            msg = "Create an account on Snapdeal"
            
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Login on snapdeal"
            pmg.split()

            try:  
                  
                  sleep(2)
                  driver.find_element_by_css_selector('#sdHeader > div.headerBar.reset-padding > div.topBar.top-bar-homepage.top-freeze-reference-point > div > div.col-xs-5.reset-padding.header-right.rfloat > div.myAccountTab.accountHeaderClass.col-xs-13.reset-padding > div > span.accountUserName.col-xs-12.reset-padding').click()
                  sleep(4)
                  driver.find_element_by_css_selector('#sdHeader > div.headerBar.reset-padding > div.topBar.top-bar-homepage.top-freeze-reference-point > div > div.col-xs-5.reset-padding.header-right.rfloat > div.myAccountTab.accountHeaderClass.col-xs-13.reset-padding > div > div > div.dropdownAccountNonLoggedIn > div.accountInfoNonLoggedIn > span.accountBtn.btn.rippleWhite > a').click()
                  sleep(4)
                  pos = driver.find_element_by_name('username')
                  pos.send_keys(emails[k])
                  sleep(4)
                  
                  driver.find_element_by_id("checkUser").click()

                  sleep(4)
                  
            

                  try:  
                        sleep(3)
                        if driver.find_element_by_css_selector('#login-register-modal > div > div.signup-card > div.screen1 > p'):
                              cmsg = driver.find_element_by_css_selector('#login-register-modal > div > div.signup-card > div.screen1 > p').text
                              print(cmsg)
                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in realestateindia')
                                    comic1[0].append("not found")
                                    print("realestateindia:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    
                  except: 
                        
                        sleep(3)
                        if driver.find_element_by_css_selector('#login-register-modal > div > div.loginEmailUpgrade-card > div.screen2 > header'):
                              
                              cmsg=driver.find_element_by_css_selector('#login-register-modal > div > div.loginEmailUpgrade-card > div.screen2 > header').text
                              print(cmsg)
                              if cmsg==pmg:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in realestateindia')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("realestateindia:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in realestateindia")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
snapdeal(email)

## 60 https://parimatch.in/en/

def pari(emails):
      
      k=0
      for i in range(len(mobile)):
            driver.get("https://parimatch.in/en/")
            sleep(10)
            msg = "Seems you entered incorrect data, or you're not registered"
            
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Phone verification"
            pmg.split()

            try:  
                  
                  per_login=driver.find_element_by_css_selector('#root > div._1TzeAIfhNO012CEqnBhRcV > div > div.wTtolkMw3AJ1HN-WRezK3._56KhWyTn_-Ww-wHOLgJgF > div.IJe06xkhoXrcXRZ5fewSw > a > button > span')
                  per_login.click()
                  sleep(5)
                  per_for=driver.find_element_by_class_name('rbgOJP9P_2rA0P-fLMQ97')
                  per_for.click()
                  sleep(6)
                  peri_number = driver.find_element_by_css_selector('#root > div._3eyGqokWTVf2k_vTBiSQpJ > div._2p7CwCNYgpuvkMSLc3MMLo > div > div > div._1I3H-WGKAJYxc5r_rZu2hi.Zof4D-BnjyvwQLq43subx > form > div:nth-child(1) > div > div.plZ8UNE-CuO6JdhVm1kL9 > div._2qIkKrH-04aOi3lOS4IEdW > input')
                  peri_number.clear()
                  peri_number.send_keys(mobile[k])
                  sleep(8)
                  driver.find_element_by_css_selector('#root > div._3eyGqokWTVf2k_vTBiSQpJ > div._2p7CwCNYgpuvkMSLc3MMLo > div > div > div._1I3H-WGKAJYxc5r_rZu2hi.Zof4D-BnjyvwQLq43subx > form > button').click()
                  sleep(5)
            
                  

                  try:  
                        sleep(3)
                        if driver.find_element_by_css_selector('#root > div._3eyGqokWTVf2k_vTBiSQpJ > div._2p7CwCNYgpuvkMSLc3MMLo > div > div > div._3Az03bObO_gE-WPLJ0DCQa > div'):
                              cmsg = driver.find_element_by_css_selector('#root > div._3eyGqokWTVf2k_vTBiSQpJ > div._2p7CwCNYgpuvkMSLc3MMLo > div > div > div._3Az03bObO_gE-WPLJ0DCQa > div').text
                              print(cmsg)
                              if cmsg == msg:
                                    comic = str(mobile[k] + ' ' + 'is not   Registered in parimatch.in')
                                    comic1[0].append("not found")
                                    print("parimatch.in:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "mobile_id:"+mobile[k] +"\n"+'}')
                                    
                  except: 
                        
                        sleep(3)
                        if driver.find_element_by_css_selector('#root > div:nth-child(2) > div._131YWYoqbBkZY9OKXeHJnR._3UPaBMk06f1EzhXD4X3-kH > div > div'):
                              
                              cmsg=driver.find_element_by_css_selector('#root > div:nth-child(2) > div._131YWYoqbBkZY9OKXeHJnR._3UPaBMk06f1EzhXD4X3-kH > div > div').text
                              print(cmsg)
                              if cmsg==pmg:
                                    flag_account_found=True
                                    flag_account_source=mobile[k]
                                    flag_account_type="mobile"
                                    comic = str(emails[k] + ' ' + 'is    Registered in parimatch.in')
                                    comic1[0].append("account found")
                                    comic1[1].append("mobile")
                                    comic1[2].append(mobile[k])
                                    print("parimatch.in:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in parimatch.in")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
pari(emails)

# 61 https://www.viki.com/sign-in?return_to=%2F

def viki(emails):
      
      k=0
      for i in range(len(emails)):
            driver.get("https://www.viki.com/forgot-password")
            sleep(10)
            msg = "Something went wrong"
            
            comic1 = [[], [], []]
            sleep(5)
            pmg = "Reset Password"
            pmg.split()

            try:  
                  
                  
                  peri_number = driver.find_element_by_css_selector('#__next > div.page-wrapper > main > div > div > div.sc-4zmz9t-2.gaCHgR > form > div > div > label > input')
                  peri_number.send_keys(emails[k])
                  sleep(8)
                  driver.find_element_by_css_selector('#__next > div.page-wrapper > main > div > div > div.sc-4zmz9t-2.gaCHgR > form > button').click()
                  sleep(5)
            
                  

                  try:  
                        sleep(3)
                        if driver.find_element_by_css_selector('#__next > div.page-wrapper > main > div > div.sc-gGCDDS.jAGFDm > div.sc-faUpoM.jLcQwM > div.sc-dvQaRk.ffBVjI > div > span'):
                              cmsg = driver.find_element_by_css_selector('#__next > div.page-wrapper > main > div > div.sc-gGCDDS.jAGFDm > div.sc-faUpoM.jLcQwM > div.sc-dvQaRk.ffBVjI > div > span').text
                              print(cmsg)
                              if cmsg == msg:
                                    comic = str(emails[k] + ' ' + 'is not   Registered in viki')
                                    comic1[0].append("not found")
                                    print("viki:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                                    
                  except: 
                        
                        sleep(3)
                        if driver.find_element_by_css_selector('#__next > div.page-wrapper > main > div > div > div.sc-4zmz9t-2.gaCHgR > span'):
                              
                              cmsg=driver.find_element_by_css_selector('#__next > div.page-wrapper > main > div > div > div.sc-4zmz9t-2.gaCHgR > span').text
                              print(cmsg)
                              if cmsg==pmg:
                                    flag_account_found=True
                                    flag_account_source=emails[k]
                                    flag_account_type="email"
                                    comic = str(emails[k] + ' ' + 'is    Registered in viki')
                                    comic1[0].append("account found")
                                    comic1[1].append("email")
                                    comic1[2].append(emails[k])
                                    print("viki:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                  
                              
            except:
                  
                  f = open("error.log", "a")
                  f.write(msg + " " "messages are not found in viki")
                  f.close()
                  comic1[0].append("Not Checked")
            sleep(3)
            k=k+1
viki(emails)



