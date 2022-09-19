from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

listOfEmails = []

file1 = open('rawemails2.txt', 'r')
totalines = file1.readlines()
for s in totalines:
     listOfEmails.append(s.strip())
print(listOfEmails)
driver = webdriver.Chrome('./chromedriver')
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")
for string in listOfEmails:
    driver.refresh();
    search_bar = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[1]/div/div[1]/input")
    time.sleep(1)
    search_bar.send_keys(string)
    search_bar.send_keys(Keys.RETURN)
    time.sleep(1)
    try:
        verifyemail = driver.find_element("xpath", "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[2]/div[2]/div")
    except NoSuchElementException:
        continue

    if verifyemail.text == "That username is taken. Try another.":
        print(string)
    
    
