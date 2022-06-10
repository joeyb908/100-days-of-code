from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# set twitter username, password, promised up and down speeds, as well as timeout for the speedtest
TWITTER_USERNAME = 'johannesian'
TWITTER_PASSWORD = '@G7%ZQ4jVgZywZ'
PROMISED_UP = 500
PROMISED_DOWN = 500
timeout = 60
PROVIDER = '@ATT'

class TwitterBot:
    def __init__(self):
        # set upload speed, twitter username and pass
        self.upload_speed = None
        self.download_speed = None
        self.TWITTER_USERNAME = TWITTER_USERNAME
        self.TWITTER_PASSWORD = TWITTER_PASSWORD

        # basic selenium setup
        chrome_driver_path = r'C:\Users\joeyb\Desktop\chromedriver.exe'
        s = Service(chrome_driver_path)
        self.driver = webdriver.Chrome(service=s)
        self.driver.get('https://www.speedtest.net/')

        # set the upload and download speeds promised by the provider
        self.up = PROMISED_UP
        self.down = PROMISED_DOWN

        # set the wait condition default for the browser
        self.wait = WebDriverWait(self.driver, 50)

        # set the default provider's handle
        self.PROVIDER = PROVIDER

    def get_internet_speed(self):
        """Go to the provided website and grab the current upload and download speed"""

        # find the start button and click it
        self.driver.find_element(By.CLASS_NAME, "start-text").click()

        # wait until done
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'result-label')))

        # grab the download and upload speeds
        self.download_speed = float(self.driver.find_element(By.CLASS_NAME, "download-speed").text)
        self.upload_speed = float(self.driver.find_element(By.CLASS_NAME, "upload-speed").text)

        # if either the download speed is below promised or the upload is below, tweet
        if (self.download_speed < self.down) or (self.upload_speed < self.up):
            self.tweet_at_provider()

        # otherwise, let the user know everything is peachy
        else:
            print("All good!")

    def tweet_at_provider(self):
        """Send a tweet to the provider letting them know you're not getting what you pay for"""

        # go to twitter login
        self.driver.get('https://twitter.com/i/flow/login')

        # wait for the page to load
        self.wait = WebDriverWait(self.driver, 5)

        # wait until the text box to put in the username is available, then enter the username and hit enter
        self.wait.until(EC.visibility_of_element_located((By.NAME, 'text')))
        enter_username = self.driver.find_element(By.NAME, 'text')
        enter_username.send_keys(TWITTER_USERNAME)
        enter_username.send_keys(Keys.ENTER)

        # wait until the password field is available, then enter the password and hit enter
        self.wait.until(EC.visibility_of_element_located((By.NAME, 'password')))
        enter_password = self.driver.find_element(By.NAME, 'password')
        enter_password.send_keys(TWITTER_PASSWORD)
        enter_password.send_keys(Keys.ENTER)

        # wait until the tweet box is available, then post your tweet!
        self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')))
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/'
                                           'div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/'
                                           'div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/'
                                           'div').send_keys(f"Hey {self.PROVIDER}, what's up? I have {self.download_speed} Mbps "
                                                            f"when I was promised {self.down} Mbps and {self.upload_speed} Mbps "
                                                            f"when I was promised {self.up} Mbps!")
