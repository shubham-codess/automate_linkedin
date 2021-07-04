import pandas as pd
# import urllib
# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import pyautogui
import pyperclip
# from selenium.webdriver.common.keys import Keys

def sales2reg():
    usr = "you@email.com"
    pwd = "Type Your Password Here"
    # searchitem = "True influence shubham varshney" 

    driver = webdriver.Chrome()
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
    title = []
    location = []
    name =[]
    current =[]
    for i in d1:
        driver.get(i)
        sleep(3)

        if len(driver.find_elements_by_xpath("/html/body/main/div[1]/div[1]/div/div[2]/div[1]/div[3]/button"))>0:
            driver.find_element_by_xpath("/html/body/main/div[1]/div[1]/div/div[2]/div[1]/div[3]/button").click()
            sleep(2)
            pyautogui.click(x =784, y = 453)
            linkedin_url.append(pyperclip.paste())
            job_title = driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/div/div[1]/section[1]/div/ul/li[1]/dl/dt")
            title.append(job_title.text)

            company_name = driver.find_element_by_xpath("/html/body/main/div[2]/div[1]/div/div[1]/section[1]/div/ul/li[1]/dl/dd[1]/span[2]/a")
            name.append(company_name.text)

            company_location = driver.find_element_by_xpath("/html/body/main/div[1]/div[1]/div/div[1]/div[1]/div/dl/dd[3]/div[1]")
            location.append(company_location.text)

            employment = driver.find_element_by_xpath("/html/body/main/div[1]/div[1]/div/div[1]/div[2]/dl/dt[1]/button/span/span[1]")
            if employment.text == "Current":
                current.append("Yes")
            else:
                current.append("No")
        else:
            linkedin_url.append("None")
            title.append("None")
            name.append("None")
            location.append("None")
            current.append("None")

    print(linkedin_url)
    print(name)
    print(title)
    print(location)
    print(current)


    dict = {"Linkedin URL": linkedin_url, "Job Title": title, "Company Name": name, "Emp Location": location, "Current": current}

    df = pd.DataFrame.from_dict(dict)
    # df = df.transpose()

    df.to_csv('regular_linkedin_url.csv')


    driver.close()

def revenue():

    df = pd.read_excel("Data.xlsx")
    d1 = list(df['Domains'])

    revenue = []
    driver = webdriver.Chrome()
    for i in d1:
        if type(i) == float:
            break
        driver.get("https://www.google.com/search?q=" + str(i) + " zoominfo")
        sleep(1)
        if len(driver.find_elements_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/span/div/a/span"))>0:
            driver.find_elements_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/span/div/a/span")[0].click()
        else:
            revenue.append("Not Found")
        sleep(1)
        if len(driver.find_elements_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/span/div/ol/li/a"))>0:
            driver.find_elements_by_xpath("/html/body/div[7]/div/div[9]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/span/div/ol/li/a")[0].click()
        else:
            revenue.append("Not Found")
        sleep(1)
        if len(driver.find_elements_by_xpath("/html/body/div[2]/app-root/app-company/div/div[1]/div[1]/div[1]/app-company-overview/div/div/div/div[1]/app-icon-text[5]/div/div[2]/span"))>0:
            rev = driver.find_elements_by_xpath("/html/body/div[2]/app-root/app-company/div/div[1]/div[1]/div[1]/app-company-overview/div/div/div/div[1]/app-icon-text[5]/div/div[2]/span")
            for value in rev:
                revenue.append(value.text)
        else:
            revenue.append("Not Found")

    print(revenue)

    dict = {"Company Revenue": revenue}

    df = pd.DataFrame.from_dict(dict)
    # df = df.transpose()

    df.to_csv('revenue_extracted.csv')

    driver.close()

def namefetch():
    df = pd.read_excel("Data.xlsx")
    d1 = list(df['Domains'])

    name = []
    driver = webdriver.Chrome()
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


    driver.close()

def urlfetch():
    usr = "you@email.com"
    pwd = "Type Your Password Here"
    # searchitem = "True influence shubham varshney" 

    driver = webdriver.Chrome()
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
        driver.find_element_by_xpath("/html/body/div[6]/header/div/div/div/div[1]/div[2]/input").send_keys(i)
        sleep(3)
        # Click on Submit
        pyautogui.click(x =602, y = 171)
        sleep(3)
        # pyautogui.click(x =400, y = 50)
        # Fetch current_url
        new_url = driver.current_url
        linkedin_url.append(new_url)
        driver.find_element_by_xpath("/html/body/div[6]/header/div/div/div/div[1]/div[2]/input").clear()

    print(linkedin_url)

    dict = {"LinkedIn Url": linkedin_url}

    df = pd.DataFrame.from_dict(dict)
    # df = df.transpose()

    df.to_csv('linkedin_url_extracted.csv')

    driver.close()

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


