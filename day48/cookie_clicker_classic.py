import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


def click_cookie():
    # find the cookie, then click it
    cookie = browser.find_element(By.ID, 'cookie')
    cookie.click()


def determine_item_costs():
    store = browser.find_elements(By.CSS_SELECTOR, '#store b')[:8]
    purchase_cost = {}

    for n in range(0, len(store)):
        split_text = store[n].text.split('-')
        if split_text == ['']:
            pass
        else:
            purchase_cost[n] = {
                "item": split_text[0].strip(),
                "cost": int(split_text[1].strip().replace(',', ''))
            }

    return purchase_cost


def make_purchase():
    for x in range(7, 0, -1):
        total_cookies = browser.find_element(By.ID, 'money').text
        if ',' in total_cookies:
            total_cookies = total_cookies.replace(',', '')
            total_cookies = int(total_cookies)
        else:
            total_cookies = int(total_cookies)
        if total_cookies > store_dict[x]['cost']:
            try:
                browser.find_element(By.ID, f'buy{store_dict[x]["item"]}').click()
            except selenium.common.exceptions.StaleElementReferenceException:
                pass


def reset_purchase_timeout():
    return time.time() + 5


# set time to purchase items and end the game (5 seconds and 5 minutes respectively)
purchase_timeout = time.time() + 5
gametime = time.time() + 300

# basic selenium setup to open cookie clicker website
chrome_driver_path = r'C:\Users\joeyb\Desktop\chromedriver.exe'
s = Service(chrome_driver_path)
browser = webdriver.Chrome(service=s)
browser.get("https://orteil.dashnet.org/experiments/cookie/")

store_dict = determine_item_costs()

# set loop to click the big cookie
while time.time() < gametime:
    click_cookie()

    # if purchase_timeout has come, make the purchase
    if time.time() > purchase_timeout:
        make_purchase()
        purchase_timeout = reset_purchase_timeout()

browser.quit()