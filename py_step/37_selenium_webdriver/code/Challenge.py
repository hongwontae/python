import selenium.webdriver
from selenium.webdriver.common.by import By;
import selenium;
from selenium.webdriver.common.keys import Keys;

chrome_options = selenium.webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = selenium.webdriver.Chrome(chrome_options)
driver.get('https://secure-retreat-92358.herokuapp.com/')

form_input = driver.find_elements(By.CSS_SELECTOR, 'form input')
form_button = driver.find_element(By.XPATH, '/html/body/form/button')

form_input[0].send_keys('Hong')
form_input[1].send_keys('won tae')
form_input[2].send_keys('dnjsxoghd@naver.com')
form_button.click()
