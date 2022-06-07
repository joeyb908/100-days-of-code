from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ----------------------------------------- Lesson with instructor ---------------------------------------------------
# setup of selenium
# chrome_driver_path = r'C:\Users\joeyb\Desktop\chromedriver.exe'
# s = Service(chrome_driver_path)
# browser = webdriver.Chrome(service=s)
# browser.get('https://en.wikipedia.org/wiki/Main_Page')
#
# # find the article count, grab the first tag which happens to be the article count!
# total_articles = browser.find_element(By.CSS_SELECTOR, '#articlecount a')
# print(total_articles.text)
#
# #  click the total number of articles
# #total_articles.click()
#
# # find the text on the page called 'Wikibooks', then click it
# wikibooks = browser.find_element(By.LINK_TEXT, 'Wikibooks')
# # wikibooks.click()
#
# # find the search field, type in python, then actually search it
# search = browser.find_element(By.NAME, 'search')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)
# # close the browser
# #browser.quit()

# ---------------------------------------------- Individual Challenge -------------------------------------------------
# Go to this link, http://secure-retreat-92358.herokuapp.com/ and fill in the first name, last name, and email address
# fields automatically, then click the "Sign Up" button

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r'C:\Users\joeyb\Desktop\chromedriver.exe'
s = Service(chrome_driver_path)
browser = webdriver.Chrome(service=s)
browser.get('http://secure-retreat-92358.herokuapp.com/')

first_name = browser.find_element(By.NAME, 'fName')
first_name.send_keys('Joey')

last_name = browser.find_element(By.NAME, 'lName')
last_name.send_keys('Ohannesian')

email = browser.find_element(By.NAME, 'email')
email.send_keys('joey@ohannesian.io')

sign_up = browser.find_element(By.CSS_SELECTOR, 'button')
sign_up.click()

browser.quit()
