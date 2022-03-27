import pandas as pd
# import urllib
# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import pyautogui
import pyperclip
from openpyxl import Workbook
from webdriver_manager.chrome import ChromeDriverManager

# from selenium.webdriver.common.keys import Keys

book = Workbook()
sheet = book.active

def sales2reg():
    usr = "you@email.com"
    pwd = "Type Your Password Here"
    # searchitem = "True influence shubham varshney" 

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.linkedin.com/uas/login/")

    name_box = driver.find_element_by_id("username")
    name_box.send_keys(usr)

    pwd_box = driver.find_element_by_id("password")
    pwd_box.send_keys(pwd)

    login_button = driver.find_element_by_xpath("/html/body/div/main/div[2]/div[1]/form/div[3]/button")
    login_button.click()

    df = pd.read_excel("Data.xlsx")
    d1 = list(df['Sales URL'])

    linkedin_url = []
    for i in d1:
        if type(i) == float:
            break
        driver.get(i)
        sleep(3)

        if len(driver.find_elements_by_xpath("/html/body/main/div[1]/div[1]/div/div[2]/div[1]/div[4]/button"))>0:
            driver.find_element_by_xpath("/html/body/main/div[1]/div[1]/div/div[2]/div[1]/div[4]/button").click()
            sleep(1)
            if len(driver.find_elements_by_xpath("/html/body/main/div[1]/div[1]/div/div[2]/div[1]/div[4]/div/div/ul/li[5]/div"))>0:
                driver.find_element_by_xpath("/html/body/main/div[1]/div[1]/div/div[2]/div[1]/div[4]/div/div/ul/li[5]/div").click()
            # pyautogui.click(x=765, y=496)
                linkedin_url.append(pyperclip.paste())
            else:
                linkedin_url.append(driver.current_url)
        else:
            linkedin_url.append(driver.current_url)

    print(linkedin_url)
    


    dict = {"Linkedin URL": linkedin_url}

    df = pd.DataFrame(dict)
    # df = df.transpose()

    df.to_csv('regular_linkedin_url.csv')


    driver.close()

def revenue():
    

    df = pd.read_excel("Data.xlsx")
    d1 = list(df['Domains'])

    revenue = []
    driver = webdriver.Chrome(ChromeDriverManager().install())
    for i in d1:
        if type(i) == float:
            break
        driver.get("https://www.google.com/search?q=" + str(i) + " zoominfo")
        sleep(1)
        if len(driver.find_elements_by_class_name("D6lY4c"))>0:
            driver.find_element_by_class_name("D6lY4c").click()
        
            sleep(1)
            if len(driver.find_elements_by_xpath("/html/body/div[13]/div/div/div[5]/div/span/span/a/div/span"))>0:
                driver.find_elements_by_xpath("/html/body/div[13]/div/div/div[5]/div/span/span/a/div/span")[0].click()
            else:
                revenue.append("Not Found")
                sheet.append(list("Not Found"))
                book.save("new_revenue.xlsx")
            sleep(1)
            if len(driver.find_elements_by_xpath("/html/body/div[2]/app-root/app-company/div/div[1]/div[1]/div[1]/app-company-overview/div/div/div/div[1]/app-icon-text[5]/div/div[2]/span"))>0:
                rev = driver.find_elements_by_xpath("/html/body/div[2]/app-root/app-company/div/div[1]/div[1]/div[1]/app-company-overview/div/div/div/div[1]/app-icon-text[5]/div/div[2]/span")
                for value in rev:
                    revenue.append(value.text)
                    sheet.append(list(value.text))
                    book.save("new_revenue.xlsx")
            else:
                revenue.append("Not Found")
                sheet.append(list("Not Found"))
                book.save("new_revenue.xlsx")
        else:
            revenue.append("Not Found")
            sheet.append(list("Not Found"))
            book.save("new_revenue.xlsx")

    print(revenue)

    dict = {"Company Revenue": revenue}

    df = pd.DataFrame.from_dict(dict)
    # df = df.transpose()

    df.to_csv('revenue_extracted.csv')


    # driver.close()

def namefetch():
    df = pd.read_excel("Data.xlsx")
    d1 = list(df['Domains'])

    name = []
    driver = webdriver.Chrome(ChromeDriverManager().install())
    for i in d1:
        if type(i) == float:
            break
        driver.get("https://www.google.com/search?q=" + str(i) + " zoominfo")
        sleep(1)
        if len(driver.find_elements_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/span/div/a/span"))>0:
            driver.find_elements_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/span/div/a/span")[0].click()
        else:
            name.append("Not Found")
        sleep(1)
        if len(driver.find_elements_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/span/div/ol/li/a"))>0:
            driver.find_elements_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/span/div/ol/li/a")[0].click()
        else:
            name.append("Not Found")
        sleep(1)
        
        if len(driver.find_elements_by_xpath("/html/body/div[2]/app-root/app-company/div/div[1]/div[1]/div[1]/app-company-header/div/div[2]/h1"))>0:
            rev = driver.find_elements_by_xpath("/html/body/div[2]/app-root/app-company/div/div[1]/div[1]/div[1]/app-company-header/div/div[2]/h1")
            for value in rev:
                name.append(value.text)
        else:
            name.append("Not Found")

    print(name)

    dict = {"Company Name": name}

    df = pd.DataFrame.from_dict(dict)
    # df = df.transpose()

    df.to_csv('name_extracted.csv')


    # driver.close()

def urlfetch():
    usr = "you@email.com"
    pwd = "Type Your Password Here"
    # searchitem = "True influence shubham varshney" 

    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://www.linkedin.com/uas/login/")

    name_box = driver.find_element_by_id("username")
    name_box.send_keys(usr)

    pwd_box = driver.find_element_by_id("password")
    pwd_box.send_keys(pwd)

    login_button = driver.find_element_by_xpath("/html/body/div/main/div[2]/div[1]/form/div[3]/button")
    login_button.click()

    sleep(2)

    df = pd.read_excel("Data.xlsx")
    d1 = list(df['Search'])
    linkedin_url = [] 

    driver.get("https://www.linkedin.com/in/blank-profile-47607333/")
    sleep(2)
    # Click on Maximize
    pyautogui.click(x =895, y = 28)
    for i in d1:
        if type(i) == float:
            break
        # Click on Search Bar and Enter Query
        driver.find_element_by_xpath("/html/body/div[6]/header/div/div/div/div[1]/input").send_keys(i)
        sleep(3)
        # Click on Submit
        pyautogui.click(x =602, y = 171)
        sleep(3)
        # Click View Profile
        if len(driver.find_elements_by_xpath("/html/body/div[6]/div[3]/div/div[2]/div/div[1]/main/div/div/div[1]/div/a/div/div[2]/div[2]/a"))>0:
            driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/div[2]/div/div[1]/main/div/div/div[1]/div/a/div/div[2]/div[2]/a").click()
            sleep(3)
            new_url = driver.current_url
            linkedin_url.append(new_url)
        else:
            new_url = driver.current_url
            linkedin_url.append(new_url)

        # pyautogui.click(x =400, y = 50)
        # Fetch current_url
        driver.find_element_by_xpath("/html/body/div[6]/header/div/div/div/div[1]/input").clear()

    print(linkedin_url)

    dict = {"LinkedIn Url": linkedin_url}


    df = pd.DataFrame.from_dict(dict)
    # df = df.transpose()

    df.to_csv('linkedin_url_extracted.csv')

# driver.close()

print("1: Sales 2 Regular, 2: Revenue, 3: Company Name, 4: Fetch Profile URLs ")
value = int(input("Please enter the Number: "))
if value == 1:
    sales2reg()
elif value == 2:
    revenue()
elif value == 3:
    namefetch()
elif value == 4:
    urlfetch()
else:
    print("Plese Enter Numbers From 1 to 4 only. Thanks!")


