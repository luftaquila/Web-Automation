import os
import sys
import datetime
import selenium
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def popupClose():
    # set window control
    main_window_handle = None
    while not main_window_handle:
        main_window_handle = driver.current_window_handle

    # moving to popup window
    signin_window_handle = None
    while not signin_window_handle:
        for handle in driver.window_handles:
            if handle != main_window_handle:
                signin_window_handle = handle
                break
    driver.switch_to.window(signin_window_handle)
    driver.close()
    driver.switch_to.window(main_window_handle)

id = input('ID 입력 : ')
pwd = input('PW 입력 : ')
ch = input('요일 선택 : ')

print('\n[' + str(datetime.datetime.now()) + '] Launching Browser')
dir = os.getcwd() + '\\chromedriver.exe'
chrome_options = Options()
#chrome_options.binary_location = 'C:\\Users\\LUFT-AQUILA\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe'
driver = webdriver.Chrome(executable_path = dir, options = chrome_options)

print('\n[' + str(datetime.datetime.now()) + '] Attempting to logging in\n')
try:
    driver.get("https://www.1365.go.kr/vols/main.do")
    popupClose()
    driver.find_element_by_xpath('//*[@id="utilMenuOpen"]').click()
    driver.find_element_by_class_name('login').click()
    driver.find_element_by_name('mberId').send_keys(id)
    driver.find_element_by_name('password').send_keys(pwd)
    driver.find_element_by_name('password').send_keys(Keys.ENTER)
    popupClose()
except selenium.common.exceptions.UnexpectedAlertPresentException:
    print('error_login_failure\n')
    print('Restarting...\n')
    os.system('python control.py')
    sys.exit()

print('[' + str(datetime.datetime.now()) + '] Specifying target\n')
driver.get("https://www.1365.go.kr/vols/P9210/partcptn/timeCptn.do")
Select(driver.find_element_by_id('searchHopeArea1')).select_by_visible_text('경기도')
Select(driver.find_element_by_id('searchHopeArea2')).select_by_visible_text('전체')
Select(driver.find_element_by_id('searchSrvcStts')).select_by_visible_text('전체')
driver.find_element_by_name('searchKeyword').send_keys('동물보호센터 돌봄')
driver.find_element_by_id('btnSearch').click()
sleep(1)

print('[' + str(datetime.datetime.now()) + '] Waiting for targetted time\n')
target_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, 23, 59, 59, 800000)
while (target_time - datetime.datetime.now()).total_seconds() > 0 :
    print('Countdown : ' + str(target_time - datetime.datetime.now()) + ' /  Current : ' + str(datetime.datetime.now()), end='\r')
print()

print('[' + str(datetime.datetime.now()) + '] Refreshing list\n')
Select(driver.find_element_by_id('searchSrvcStts')).select_by_visible_text('모집중')
driver.find_element_by_id('btnSearch').click()

print('[' + str(datetime.datetime.now()) + '] Selecting target\n')
try:
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "service_part")][2]/div[contains(@class, "data_middle")]/ul/li[1]/a')))
    element.click()
except selenium.common.exceptions.NoSuchElementException:
    print('error_no_result')
    sys.exit()
except selenium.common.exceptions.StaleElementReferenceException:
    print('error_no_result')
    sys.exit()

print('[' + str(datetime.datetime.now()) + '] Attempting to apply\n')
try:
    driver.find_element_by_xpath('//button[@id="btnReqst"]').click()
except selenium.common.exceptions.NoSuchElementException:
    print('error_not_appliable')
    sys.exit()
except selenium.common.exceptions.StaleElementReferenceException:
    print('error_not_appliable')
    sys.exit()

print('[' + str(datetime.datetime.now()) + '] Attempting to select date\n')
try:
    driver.find_element_by_xpath('//*[contains(@class, "pc_only")]//span[text()="모집중"][' + ch + ']').click()
except selenium.common.exceptions.NoSuchElementException:
    print('error_no_available_date')
    sys.exit()
except selenium.common.exceptions.StaleElementReferenceException:
    print('error_no_available_date')
    sys.exit()

print('[' + str(datetime.datetime.now()) + '] Selecting checkbox\n')
driver.find_element_by_id('agreeYn').click()

print('[' + str(datetime.datetime.now()) + '] Final apply\n')
driver.find_element_by_id('btnRequest').click()
driver.switch_to.alert.accept()
sys.exit()
