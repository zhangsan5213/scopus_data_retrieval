import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

from config import *

## initiate browser
driver = webdriver.Edge('./msedgedriver.exe')

## scopus homepage
driver.get('https://www.scopus.com/home.uri')

## scopus login
try:
    driver.find_element(By.XPATH, '//*[@id="pendo-close-guide-e0738c57"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="gh-cnt"]/micro-ui/global-header/header/div/div/div[2]/div[2]/div/div[3]/button').click()
except:
    driver.find_element(By.XPATH, '//*[@id="gh-cnt"]/micro-ui/global-header/header/div/div/div[2]/div[2]/div/div[3]/button').click()

## institution login
driver.find_element(By.XPATH, '/html/body/div/section/main/form/div[3]/div[2]/button').click()

## input institution email
driver.find_element(By.XPATH, '//*[@id="bdd-email"]').send_keys(INSTITUTION_EMAIL)
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="bdd-els-searchBtn"]').click()
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="bdd-elsPrimaryBtn3"]').click()
time.sleep(5)

## input institution info
driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(INSTITUTION_USERNAME)
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(INSTITUTION_PASSWD)
driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/form/div[5]/button').click()
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/form/div/div[2]/p[2]/input[2]').click()
time.sleep(8)

## stored search of tju
driver.find_element(By.XPATH, '//*[@id="saved-searches-tab"]/span').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="saved-searches-tab-panel"]/div/ul/li/div[1]/div[3]/div/a/span').click()
time.sleep(2)

## author name panel
driver.find_element(By.XPATH, '//*[@id="viewAllLink_AUTHOR_NAME_AND_ID"]/span').click()
time.sleep(2)

## get author names
name_containers = [
    driver.find_element(By.XPATH, '//*[@id="overlayul_AUTHOR_NAME_AND_ID1"]'),
    driver.find_element(By.XPATH, '//*[@id="overlayul_AUTHOR_NAME_AND_ID2"]'),
    driver.find_element(By.XPATH, '//*[@id="overlayul_AUTHOR_NAME_AND_ID3"]'),
    driver.find_element(By.XPATH, '//*[@id="overlayul_AUTHOR_NAME_AND_ID4"]'),
    ]

## get author blocks
name_tabs = []
for name_container in name_containers:
    kids = name_container.find_elements(By.XPATH, ".//*")
    name_tabs += kids

## get author ids
name_ids = []
for tab in name_tabs:
    temp_id = tab.get_attribute('id')
    if temp_id.startswith('li'):
        name_ids.append(temp_id)

## click author buttons
for i, name_id in enumerate(name_ids):
    print('Proceeding into', name_id)

    ## to author popout window
    driver.find_element(By.XPATH, '//*[@id="{}"]/button'.format(name_id)).click()
    time.sleep(2)

    ## to author individual page
    driver.find_element(By.XPATH, '//*[@id="cibLimit"]/span').click()
    time.sleep(2)

    ## select all
    driver.execute_script(
        'arguments[0].click();',
        driver.find_element(By.XPATH, '//*[@id="mainResults-allPageCheckBox"]'),
        )
    time.sleep(2)

    ## export
    driver.find_element(By.XPATH, '//*[@id="directExport"]').click()
    time.sleep(5)

    break

    if i != len(name_ids)-1:
        ## back to the stored search of tju
        driver.back()
        time.sleep(5)

        ## author name panel again
        driver.find_element(By.XPATH, '//*[@id="viewAllLink_AUTHOR_NAME_AND_ID"]/span').click()
        time.sleep(2)