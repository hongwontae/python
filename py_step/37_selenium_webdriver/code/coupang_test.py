from selenium import webdriver
import selenium
import selenium.webdriver
from selenium.webdriver.common.by import By
import time

c_options = webdriver.ChromeOptions()
c_options.add_experimental_option('detach', True)

driver = selenium.webdriver.Chrome(options=c_options)
driver.maximize_window()
driver.get(url='https://www.saramin.co.kr/zf_user/')
saram_in = driver.find_element(By.XPATH, '//*[@id="btn_search"]')

saram_in.click()
time.sleep(1)

saram_in_input = driver.find_element(By.XPATH, '//*[@id="ipt_keyword_recruit"]')
saram_in_input.send_keys('프론트엔드 신입')
time.sleep(1)

saram_area_button = driver.find_element(By.XPATH, '//*[@id="ipt_area_recruit"]')
driver.execute_script('arguments[0].click();', saram_area_button)
time.sleep(2)

saram_in_areas = driver.find_elements(By.CSS_SELECTOR, '.overview ul li')
saram_in_areas[0].click()
saram_in_areas[2].click()
saram_in_areas[1].click()
saram_in_area_detail = driver.find_elements(By.CSS_SELECTOR, '.viewport .overview ul li label span')
cc = []
for siad in saram_in_area_detail :
    cc.append(siad.text)

print(cc)


# saram_beginer_button = driver.find_element(By.XPATH, '//*[@id="sp_main_wrapper"]/div[1]/div[1]/button')
# saram_beginer_right_button = driver.find_element(By.XPATH, '//*[@id="sp_main_wrapper"]/div[1]/div[1]/div/div[1]/div[1]/label')


# saram_beginer_button.click()
# time.sleep(1)
# saram_beginer_right_button.click()

# time.sleep(4)

# saram_in_re_button = driver.find_element(By.XPATH, '//*[@id="search_btn"]')
# saram_in_re_button.click()









