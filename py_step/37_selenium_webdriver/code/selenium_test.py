from selenium import webdriver;
from selenium.webdriver.common.by import By;

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url='https://www.python.org/')

every_times = driver.find_elements(By.CSS_SELECTOR, '.event-widget time')
every_a = driver.find_elements(By.CSS_SELECTOR, value='.event-widget ul a')

events = {}

for n in range(len(every_times)) :
    events[n]  = {
        'time' : every_times[n].text,
        'name' : every_a[n].text
    }

print(events)

driver.quit()



