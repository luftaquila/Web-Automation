import os
import sys
import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select

print('\n[' + str(datetime.datetime.now()) + '] Launching Browser\n')
chrome_options = Options()
chrome_options.binary_location = 'C:\\Users\\LUFT-AQUILA\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe'
dir = os.getcwd() + '\\chromedriver.exe'
driver = webdriver.Chrome(executable_path = dir, options = chrome_options)

print('\n[' + str(datetime.datetime.now()) + '] Attempting to log in\n')
driver.get("https://www.1365.go.kr/vols/main.do")
driver.find_element_by_xpath('//*[@id="utilMenuOpen"]').click()
driver.find_element_by_class_name('login').click()
driver.find_element_by_name('mberId').send_keys('obj512')
driver.find_element_by_name('password').send_keys('rokaF136512#')
driver.find_element_by_name('password').send_keys(Keys.ENTER)

print('[' + str(datetime.datetime.now()) + '] Specifying target\n')
driver.get("https://www.1365.go.kr/vols/P9210/partcptn/timeCptn.do")
Select(driver.find_element_by_id('searchHopeArea1')).select_by_visible_text('경기도')
Select(driver.find_element_by_id('searchHopeArea2')).select_by_visible_text('전체')
Select(driver.find_element_by_id('searchSrvcStts')).select_by_visible_text('전체')
driver.find_element_by_name('searchKeyword').send_keys('동물보호센터 돌봄')
driver.find_element_by_id('btnSearch').click()

print('[' + str(datetime.datetime.now()) + '] Waiting for targetted time\n')
target_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, 23, 59, 59, 800000)
while (target_time - datetime.datetime.now()).total_seconds() > 0 :
    print('Countdown : ' + str(target_time - datetime.datetime.now()) + ' /  Current : ' + str(datetime.datetime.now()), end='\r')
print()

driver.find_element_by_id('btnSearch').click()

"""
# wait for ticketing start time
target_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, int(sys.argv[6]), int(sys.argv[7]) - 1, 59, 800000)
while (target_time - datetime.datetime.now()).total_seconds() > 0 :
    print('Countdown : ' + str(target_time - datetime.datetime.now()), end='\r')
print()

print()
# wait for starting time
target_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, 9, 59, 59, 800000)
while (target_time - datetime.datetime.now()).total_seconds() > 0 :
    print('Targetting Start Time Countdown : ' + str(target_time - datetime.datetime.now()), end='\r')
print()

# select targetted date and time
errorTime = 0
def timeClicker():
    global errorTime
    try :
        driver.find_element_by_xpath('//*[@id="list_date"]/li[' + sys.argv[3] + ']/button').click()

    except Exception as ex:
        print('retrying... #%d' % errorTime, end='\r')
        errorTime = errorTime + 1
        timeClicker()

timeClicker()
print()
driver.find_element_by_xpath('//*[@id="list_time"]/li[' + sys.argv[4] + ']/button').click()

# set window control
main_window_handle = None
while not main_window_handle:
    main_window_handle = driver.current_window_handle

# press proceed button
driver.find_element_by_xpath('//*[@id="ticketing_process_box"]/div/div[2]/div/div[2]/button').click()

# moving to popup window
signin_window_handle = None
while not signin_window_handle:
    for handle in driver.window_handles:
        if handle != main_window_handle:
            signin_window_handle = handle
            break
driver.switch_to.window(signin_window_handle)
"""
