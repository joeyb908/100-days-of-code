from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# basic selenium setup
chrome_driver_path = r'C:\Users\joeyb\Desktop\chromedriver.exe'
s = Service(chrome_driver_path)
browser = webdriver.Chrome(service=s)
browser.get("https://www.python.org/")

# set up upcoming events dictionary
upcoming_event_dict = {}
upcoming_events = browser.find_elements(By.CSS_SELECTOR, '.medium-widget.event-widget.last')

# my solution
# for each element in upcoming events
for element in upcoming_events:
    # dictionary count set to 0
    count = 0

    # grab the date & date
    date_and_name = element.find_elements(By.CSS_SELECTOR, 'li')
    # for each date_and_time combo, split the data into 2 parts. One holding the date, one holding the title
    for option in date_and_name:
        info_list = option.text
        date = info_list[:5]
        title = info_list[6:]

        # the date and title of the event into a dictionary
        upcoming_event_dict[count] = {'time': date, 'name': title}

        # increase dictionary location by 1
        count += 1

# teacher solution
# grab the event times and names
event_times = browser.find_elements(By.CSS_SELECTOR, '.event-widget time')
event_names = browser.find_elements(By.CSS_SELECTOR, '.event-widget li a')

# in the range of 0 to the length of the list, update the dictionary to hold the time and name for each entry
events = {}
for n in range(0, len(event_times)):
    events[n] = {
        'time': event_times[n].text,
        'name': event_names[n].text
    }
print(events)
print(upcoming_event_dict)

browser.quit()
