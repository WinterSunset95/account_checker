from concurrent.futures import thread
import time
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests

# captcha bypass trial

import pytesseract
import sys
import argparse
import cv2
from PIL import Image, ImageEnhance
from subprocess import check_output
def text_in_image_captcha(path):
    image = requests.get('https://secure.thefreedictionary.com/access/image-rnd.ashx?0.8241203757116862')
    file = open("captca_image.png", "wb")
    file.write(image.content)
    file.close()
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help='Captcha file path')
    ap.add_argument("-p", "--pre_processor", default="tresh", help="pre processor usage")
    args = vars(ap.parse_args())
    pth = 'captcha_image.png'
    print('Resolving Captcha')
    check_output(['convert', pth, '-resample', '600', pth])
    text = pytesseract.image_to_string(Image.open(pth))
    print(text)
    
text_in_image_captcha('https://secure.thefreedictionary.com/access/image-rnd.ashx?0.0812071932902052')    

img = Image.open('captcha_image.png')
filter = ImageEnhance.Contrast(img)
new_image = filter.enhance(3)
text = pytesseract.image_to_string(new_image)

global driver
driver = webdriver.Chrome('/home/winter/account_checker/chromedriver')
flag_account_found = False
flag_account_source = ""
flag_account_type = ""
mobile=["98798798789", "56567587875"]
emails=["mlthillakkumar@gmail.com","sai1@gmail.com","wintersunset95@gmail.com"]

#read the ignorelist and load it in vIgnoreWebSiteList
with open(r"/home/winter/account_checker/portalignorelist.txt") as f:
    vIgnoreWebSiteList = f.readlines()
    vIgnoreWebSiteList=str(vIgnoreWebSiteList)
    vIgnoreWebSiteList.split()
# def set_proxy():
#     proxy_scrape_url = "118.67.221.82:8080"
#     print(proxy_scrape_url)
#     try:
#         proxy_request = requests.get(proxy_scrape_url, Timeout=10)
#     except:
#         return False
#     proxylist = proxy_request.text.split()
#     return 'https://' + random.choice(proxylist)
#to write in  portalignorelist          
def check_captcha(u1):
    driver.get(u1)
    try:
        driver.find_element_by_class_name("cf-wrapper cf-header cf-error-overview")
        return True
    except:
        return False
         
        
def add_portal_to_IgnoreList(websitename):
    lo = open(r"./portalignorelist.txt","w")
    lo.write(websitename)
    lo.write('\n')
    lo.close()
    #also add the websitename to vIgnoreWebSiteList
    return lo
    
def check_portal_in_IgnoreList(websitename):
    #if website is available in your vIgnoreWebSiteList then
    if websitename in vIgnoreWebSiteList:
        return True
    else:
        return False
   
def open_website(u2):
    driver.get(u2)
    ck = check_captcha(u2)
    if ck == True:
        clean_browser()
        #set_proxy()
        driver.get(u2)
        ck = check_captcha(u2)
        if ck == True:
            return False
        else:
            cq = check_website(u2)
            if cq == True:
                return True
            else:
                return False 
                print("proxy error")
                
    else:
        cq = check_website()
        if cq == True:
            return True
        else:
            return False 
            print("proxy error")            
                
                
            
def check_website():
    tl = driver.title
    po = tl
    if tl == po :
        return True
    else:
        return False
    
def debug_log(xx):
    fo=open(r"./error.log", "a")
    fo.write(xx)
    fo.write('\n')
    fo.close()
            
           
# to open_chrome
def open_chrome():
    global driver
    if driver:
        if not driver.window_handles:
            return True
        else:
            return driver
    else:
        pass
open_chrome()    

def clean_browser():
    driver_len = len(driver.window_handles) #fetching the Number of Opened tabs
    print("Length of Driver = ", driver_len)
    if driver_len > 1: # Will execute if more than 1 tabs found.
        for i in range(driver_len - 1, 0, -1):
            driver.switch_to.window(driver.window_handles[i]) #will close the last tab first.
            driver.close()
            print("Closed Tab No. ", i)
        driver.switch_to.window(driver.window_handles[0]) # Switching the driver focus to First tab.
    else:
        print("Found only Single tab.")
    driver.execute_script("window.open('');")
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[-1])
    time.sleep(2)
    driver.get('chrome://settings/clearBrowserData') 
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
# do basic check to see if html is there 
        
# defines functions that are used multiple times

# click function returns boolean values
def click(name, path):
    count = 0 #counting the number of tries
    while True: #for the next 60 seconds, it'll try to click the target item
        try:
            item = driver.find_element_by_xpath(path)
            item.click()
            return True
            break
        except:
            sleep(1)
            print('trying to click item')
        count += 1
        if count > 60:
            print('timeout')
            return False
        else:
            pass
# input_data function also returns boolean values
def input_data(name, value, path):
    count = 0
    while True:
        try:
            item = driver.find_element_by_xpath(path)
            item.send_keys(value)
            return True
            break
        except:
            sleep(1)
            print('trying to find input field')
        count += 1
        if count > 60:
            print('timeout')
            return False
        else:
            pass
        

#for comikart website
def flipkart():
    url = "https://www.flipkart.com/account/login?ret=/"
    kp = "flipkart"
    line = check_portal_in_IgnoreList(kp)
    if line == True:
        print(kp+" "+'is present in the ignore_list')
        lk = "error"+ ","+ kp +"," + "email_id:" +emails[0]+","+emails[1] +" "+ "not checked as it is in ignore list"
        fk = debug_log(lk)
    else:
            clean_browser()
            try:       
                for email in emails:
                #to get the website
                    ow = open_website(url)
                    print("\n\n opened flipkart \n\n")
                    if ow == True:
                        input_data('pos', email, '//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')
                        input_data('po', 'rrr', '//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[2]/input')
                        click('lop', '/html/body/div/div/div[3]/div/div[2]/div/form/div[4]/button')
                        msf = 'Your username or password is incorrect'
                        flipkarta = [[], [], []]#to store output
                        pmg = "Looks like you're new here!"                    
                        #match with the messages
                        try:
                            count = 0
                            while count < 60:
                                sleep(1)
                                try:
                                    p = driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div/form/div[1]/span[2]/span").text
                                    if p == msf:
                                        flipkart=str(email+ ' ' + 'is Registered in Flipkart')
                                        flag_account_found = True
                                        flag_account_source = email
                                        flag_account_type = "emails"
                                        flipkarta[0].append("account found")
                                        flipkarta[1].append("emails")
                                        flipkarta[2].append(email)
                                        print("flipkart :" + '{' + "\n" + "account_Status=" + flipkarta[0][0] + "\n" + "found_with_type=" + flipkarta[1][0] + "\n" + "found_with_id=" + flipkarta[2][0] + "\n" + '}')
                                        break
                                    else:
                                        pass
                                except:
                                    u = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[1]/span/span').text
                                    if u == pmg:
                                        flipkarta[0].append("not found")
                                        print("flipkart:" + '{' + "\n" + "account_Status=" + flipkarta[0][0] + "\n" + "email_id:"+email +"\n"+'}')
                                        break
                                    else:
                                        pass
                                count += 1
                        except:
                            add_portal_to_IgnoreList("flipkart")
                            print("Error, flipkart, error messages have changed, pls revisit")                        
                    # for storing error in error.log 
                    sleep(3)
            except:
                debug_log("Error, flipkart, error in website, pls revisit")
                print("Not Checked")

def comikart():
    global url
    url = "https://www.comikart.com/in/passremind"
    kp = "comikart"
    line = check_portal_in_IgnoreList(kp)
    if line == True:
        print(kp+" "+'is present in the ignore_list')
        lk = "error"+ ","+ kp +"," + "email_id:" +emails[0]+","+emails[1] +" "+ "not checked as it is in ignore list"
        fk = debug_log(lk)
    else:
            clean_browser()
            for email in emails:
               #to get the website
                ow = open_website(url)
                print("\n\n opened comikart \n\n")
                if ow == True:
                    pos = driver.find_element_by_id("mail_input2")
                    pos.send_keys(email)#sending mailid to input
                    driver.find_element_by_css_selector("#box_passchange > div.innerbox > form > fieldset > div.bottombuttons > button > span").click()#To click on next 
                    msg = "There is no such e-mail address in the database."
                    comic1 = [[], [], []]#to store output
                    pmg = str("E-mail message has been sent.")
                    sleep(5)
                    #match with the messages
                    try: 
                        if driver.find_element_by_css_selector('body > div.wrap.rwd > div.container > div > div > p'):
                            cmsg = driver.find_element_by_css_selector('body > div.wrap.rwd > div.container > div > div > p').text
                            print(cmsg)
                            #check for unRegistered mailid , match with the msg
                            if cmsg == msg:
                                comic = str(email + ' ' + 'is not Registered in comikart')
                                comic1[0].append("not found")
                                
                                print("comikart:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+email +"\n"+'}')
                            #check for Registered mailid, Match with the pmg
                            elif cmsg == pmg:
                                comic = str(email + ' ' + 'is    Registered in comikart')
                                flag_account_found = True
                                flag_account_source = email
                                flag_account_type = "emails"
                                comic1[0].append("account found")
                                comic1[1].append("emails")
                                comic1[2].append(emails)
                                print("comikart :" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                            else:
                                add_portal_to_IgnoreList("comikart")
                                print("Error, comikart, error messages have changed, pls revisit")
                   # for storing error in error.log 
                        sleep(3)
                    except:
                        debug_log("Error, comikart, error in website, pls revisit")
                        print("Not Checked")
                else:
                    pass
                
def behance():
    global url
    url = "https://behance.net"
    kp = "behance"
    line = check_portal_in_IgnoreList(kp)
    if line == True:
        print(kp+" "+'is present in the ignore_list')
        lk = "error"+ ","+ kp +"," + "email_id:" +emails[0]+","+emails[1] +" "+ "not checked as it is in ignore list"
        fk = debug_log(lk)
    else:
            clean_browser()
            for email in emails:
               #to get the website
                ow = open_website(url)
                if ow == True:
                    click('login', '//*[@id="app"]/div[1]/div/div[1]/div[1]/div[2]/div[3]/ul/li[1]/div/button')
                    input_data('input', email, '//*[@id="EmailPage-EmailField"]')
                    click('continue', '//*[@id="EmailForm"]/section[2]/div[2]/button')
                    behance = [[], [], []]
                    try:
                        count = 0
                        while count < 60:
                            sleep(1)
                            try:
                                driver.find_element_by_xpath('//*[@id="EmailForm"]/section[1]/label').text
                                print("\n\n " + email + ' is not registered, please add the code for handling this \n\n')
                                # Please add code for unregistered email here
                                break
                            except:
                                print("\n\n " + email + ' is registered, add the code for handling this \n\n')
                                # code for registered email
                                break
                            count += 1
                    except:
                        debug_log("Error, behance, error in website, please revisit")
                        print("Not Checked")
                else:
                    pass
def thefreedictionary():
    global url
    url = "https://idioms.thefreedictionary.com/spice+it+up"
    kp = "behance"
    line = check_portal_in_IgnoreList(kp)
    if line == True:
        print(kp+" "+'is present in the ignore_list')
        lk = "error"+ ","+ kp +"," + "email_id:" +emails[0]+","+emails[1] +" "+ "not checked as it is in ignore list"
        fk = debug_log(lk)
    else:
            clean_browser()
            for email in emails:
               #to get the website
                ow = open_website(url)
                if ow == True:
                    click('login', '//*[@id="loginBlock"]/a[2]')
                    click('redirect', '//*[@id="login_form"]/table/tbody/tr[2]/td[2]/p/a')
                    input_data('email', 'wintersunset95@gmail.com', '//*[@id="EmailOrLogin"]')
                    thefreedictionary = [[], [], []]

# Calling the functions in this section
flipkart()
comikart()
behance()
thefreedictionary()
