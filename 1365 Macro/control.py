import os
import sys
import datetime
from time import sleep
from selenium import webdriver
from pynput.keyboard import Key, Controller

#dir = os.getcwd() + '\\IEDriverServer.exe'
dir = os.getcwd() + '\\chromedriver.exe'
driver = webdriver.Chrome(dir)

driver.get("http://sugang.ajou.ac.kr")
"""
# attempt to logging in
driver.get('https://ticket.melon.com/concert/index.htm')
driver.find_element_by_xpath('//a[@class="btn_gnb btn_g_login"]').click()
driver.find_element_by_name('id').send_keys(sys.argv[1])
driver.find_element_by_name('pwd').send_keys(sys.argv[2])
driver.find_element_by_id('btnLogin').click()
driver.get('https://ticket.melon.com/performance/index.htm?prodId=' + sys.argv[5])
print()

# force display box_ticketing_process div
driver.execute_script("document.getElementsByClassName('box_ticketing_process')[0].style.display = 'block';")

# wait for ticketing start time
target_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, int(sys.argv[6]), int(sys.argv[7]) - 1, 59, 800000)
while (target_time - datetime.datetime.now()).total_seconds() > 0 :
    print('Countdown : ' + str(target_time - datetime.datetime.now()), end='\r')
print()
"""
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
