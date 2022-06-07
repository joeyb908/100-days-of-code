from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r'C:\Users\joeyb\Desktop\chromedriver.exe'
s = Service(chrome_driver_path)
browser = webdriver.Chrome(service=s)
browser.get("https://www.amazon.com/dp/B08LH26PFT?ref_=cm_sw_r_cp_ud_dp_AMN2XVFAN3A3C2YC53K7")
# price_whole = browser.find_element(By.CLASS_NAME, 'a-price-whole')
# print(price_whole.text)

# practice to use XPATH instead of selector
# price = browser.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[2]/span[2]')
# print(price.text)