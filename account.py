from concurrent.futures import thread
import time
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By 
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests


global driver
driver = webdriver.Chrome(r'C:\Users\Thillak\Downloads\chromedriver_win32 (1)\chromedriver.exe')
flag_account_found = False
flag_account_source = ""
flag_account_type = ""
mobile=["98798798789", "56567587875"]
emails=["mlthillakkumar@gmail.com","sai1@gmail.com"]

#read the ignorelist and load it in vIgnoreWebSiteList
with open(r"F:\selenium project\Programs\error and ignore list\portalignorelist.txt") as f:
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
        if driver.find_element_by_class_name("cf-wrapper cf-header cf-error-overview"):
            return True
    except:
        return False
         
        
def add_portal_to_IgnoreList(websitename) :   
    lo=open(r"F:\selenium project\Programs\error and ignore list\portalignorelist.txt","w")
    lo.write(websitename)
    lo.write('\n')
    lo.close()
    #also add the websitename to vIgnoreWebSiteList variable
    return lo
    
def check_portal_in_IgnoreList(websitename):
    #if website is available in your vIgnoreWebSiteList then
    if websitename in vIgnoreWebSiteList:
        return True
    else:
       return False
def open_website(u2):
    driver.get(u2)
    ck=check_captcha(u2)
    if ck==True:
        clean_browser()
        #set_proxy()
        driver.get(u2)
        ck=check_captcha(u2)
        if ck==True:
            return False
        else:
            cq=check_website(u2)
            if cq==True:
                return True
            else:
                return False 
                print("proxy error")
                
    else:
            cq=check_website()
            if cq==True:
                return True
            else:
                return False 
                print("prixy error")            
                
                
            
def check_website():
   
    tl=driver.title
    po=tl
    try:
        if tl==po :
            return True
    except:
        return False
def debug_log(xx):
    fo=open(r"F:\selenium project\Programs\error and ignore list\error.log", "a")
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
        


 #for comikart website
def comikart():
    global url
    url="https://www.comikart.com/in/passremind"
    global flag_account_found
    kp="comikart"
    line=check_portal_in_IgnoreList(kp)
    if line==True:
        print(kp+" "+'is present in the ignore_list')
        lk="error"+ ","+ kp +"," + "email_id:" +emails[0]+","+emails[1] +" "+ "not checked as it is in ignore list"
        fk=debug_log(lk)
    else:
        if flag_account_found ==False:
            clean_browser()
            sleep(5)
            k=0         
            for i in range(len(emails)):
               #to get the website
                ow=open_website(url)
                if ow==True:
                    pos = driver.find_element_by_id("mail_input2")
                    pos.send_keys(emails[k])#sending mailid to input
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
                                comic = str(emails[k] + ' ' + 'is not Registered in comikart')
                                comic1[0].append("not found")
                                
                                print("comikart:" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                            #check for Registered mailid, Match with the pmg
                            elif cmsg==pmg:
                                comic = str(emails[k] + ' ' + 'is    Registered in comikart')
                                flag_account_found = True
                                flag_account_source = emails[k]
                                flag_account_type = "emails"
                                comic1[0].append("account found")
                                comic1[1].append("emails")
                                comic1[2].append(emails[k])
                                print("comikart :" + '{' + "\n" + "account_Status=" + comic1[0][0] + "\n" + "found_with_type=" + comic1[1][0] + "\n" + "found_with_id=" + comic1[2][0] + "\n" + '}')
                            else:
                                add_portal_to_IgnoreList("comikart")
                                print("Error, comikart, error messages have changed, pls revisit")
                   # for storing error in error.log 
                        k = k+1    
                        sleep(3)
                    except:
                        debug_log("Error, comikart, error in website, pls revisit")
                        print("Not Checked")
            flipkart()
    
def flipkart():
    global url
    url="https://www.flipkart.com/account/login?ret=/"
    global flag_account_found
    kp="flipkart"
    line=check_portal_in_IgnoreList(kp)
    if line==True:
        print(kp+" "+'is present in the ignore_list')
        lk="error"+ ","+ kp +"," + "email_id:" +emails[0]+","+emails[1] +" "+ "not checked as it is in ignore list"
        fk=debug_log(lk)
    else:
        if flag_account_found ==False:
            k=0  
            clean_browser()
            try:       
                for i in range(len(emails)):
                
                    sleep(5)
                #to get the website
                    ow=open_website(url)
                    if ow==True:
                        sleep(5)
                        pos = driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')
                        pos.send_keys(emails[k])#sending mailid to input
                        po=driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[2]/input')
                        po.send_keys("rrr")
                        lop=driver.find_element_by_xpath('/html/body/div/div/div[3]/div/div[2]/div/form/div[4]/button').click()
                        sleep(3)
                        msf='Your username or password is incorrect'
                        flipkarta = [[], [], []]#to store output
                        pmg ="You are not registered with us. Please sign up."
                    
                        #match with the messages
                        try:
                            try:
                                p=driver.find_element_by_xpath("/html/body/div/div/div[3]/div/div[2]/div/form/div[1]/span[2]/span").text
                                if p==msf:
                                    flipkart=str(emails[k] + ' ' + 'is Registered in Flipkart')
                                    flag_account_found = True
                                    flag_account_source = emails[k]
                                    flag_account_type = "emails"
                                    flipkarta[0].append("account found")
                                    flipkarta[1].append("emails")
                                    flipkarta[2].append(emails[k])
                                    print("flipkart :" + '{' + "\n" + "account_Status=" + flipkarta[0][0] + "\n" + "found_with_type=" + flipkarta[1][0] + "\n" + "found_with_id=" + flipkarta[2][0] + "\n" + '}')
                            except:
                                u=driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div/div/div[2]').text
                                if u==pmg:
                                    flipkarta[0].append("not found")

                                    print("flipkart:" + '{' + "\n" + "account_Status=" + flipkarta[0][0] + "\n" + "email_id:"+emails[k] +"\n"+'}')
                        
                                
                        except:
                                add_portal_to_IgnoreList("flipkart")
                                print("Error, flipkart, error messages have changed, pls revisit")
                        
                    # for storing error in error.log 
                    k = k+1    
                    sleep(3)
            except:
                debug_log("Error, flipkart, error in website, pls revisit")
                print("Not Checked")

comikart()



