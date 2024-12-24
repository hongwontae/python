import selenium.webdriver
from selenium.webdriver.common.by import By;
import selenium;


c_options = selenium.webdriver.ChromeOptions()
c_options.add_experimental_option('detach', True)

driver = selenium.webdriver.Chrome(c_options)
driver.get('https://en.wikipedia.org/wiki/Main_Page')

portal = driver.find_element(By.LINK_TEXT, value='View source')
portal.click()


