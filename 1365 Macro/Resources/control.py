import os
import sys
import ntplib
import datetime
import selenium
from time import sleep
from selenium import webdriver
from colorama import init, Fore, Back, Style
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

init(autoreset = True)
id = input(' [+] ID 입력 : ')
pwd = input(' [+] PW 입력 : ')
ch = input(' [+] 요일 선택 : ')

print(Style.BRIGHT + '\n [' + str(datetime.datetime.now()) + '] Launching Browser...')
dir = os.getcwd() + '\\chromedriver.exe'
chrome_options = Options()
#chrome_options.binary_location = 'C:\\Users\\LUFT-AQUILA\\AppData\\Local\\Google\\Chrome SxS\\Application\\chrome.exe'
try:
    driver = webdriver.Chrome(executable_path = dir, options = chrome_options)
except selenium.common.exceptions.WebDriverException:
    print(Fore.RED + Style.BRIGHT + ' ERROR_chrome_not_installed\n')
    sys.exit()

print(Style.BRIGHT + '\n [' + str(datetime.datetime.now()) + '] Attempting to logging in...', end='')
try:
    driver.get("https://www.1365.go.kr/vols/main.do")
    popupClose()
    driver.find_element_by_xpath('//*[@id="utilMenuOpen"]').click()
    driver.find_element_by_class_name('login').click()
except selenium.common.exceptions.ElementNotVisibleException:
    print(Fore.RED + Style.BRIGHT + ' ERROR_login_failure_not_visible\n')
    print(' [' + str(datetime.datetime.now()) + '] ' + Fore.YELLOW + Style.BRIGHT + 'Retrying...', end='')
    driver.find_element_by_xpath('//*[contains(@class, "login")]/a').click()
try:
    driver.find_element_by_name('mberId').send_keys(id)
    driver.find_element_by_name('password').send_keys(pwd)
    driver.find_element_by_name('password').send_keys(Keys.ENTER)
    driver.get("https://www.1365.go.kr/vols/P9210/partcptn/timeCptn.do")
    popupClose()
except selenium.common.exceptions.UnexpectedAlertPresentException:
    print(Fore.RED + Style.BRIGHT + ' ERROR_login_failure_wrong_info\n')
    print(' [' + str(datetime.datetime.now()) + '] ' + Fore.YELLOW + Style.BRIGHT + 'Restarting...\n')
    os.system('control.exe')
    sys.exit()
print(Fore.GREEN + ' SUCCESS\n')

print(Style.BRIGHT + ' [' + str(datetime.datetime.now()) + '] Specifying target...', end='')
Select(driver.find_element_by_id('searchHopeArea1')).select_by_visible_text('경기도')
Select(driver.find_element_by_id('searchHopeArea2')).select_by_visible_text('전체')
Select(driver.find_element_by_id('searchSrvcStts')).select_by_visible_text('전체')
driver.find_element_by_name('searchKeyword').send_keys('동물보호센터 돌봄')
driver.find_element_by_id('btnSearch').click()
print(Fore.GREEN + ' SUCCESS\n')

print(Style.BRIGHT + ' [' + str(datetime.datetime.now()) + '] Synchronizing time with NTP Server kr.pool.ntp.org...', end='')
try:
    ntpTM, lclTM = datetime.datetime.fromtimestamp(ntplib.NTPClient().request('kr.pool.ntp.org', version = 3).tx_time), datetime.datetime.now()
except ntplib.NTPException:
    print(Fore.RED + Style.BRIGHT + ' ERROR_NTP_Server_not_responding\n')
    print(Style.BRIGHT + ' [' + str(datetime.datetime.now()) + '] Retrying with time.google.com...', end='')
    ntpTM, lclTM = datetime.datetime.fromtimestamp(ntplib.NTPClient().request('time.google.com', version = 3).tx_time), datetime.datetime.now()
print(Fore.GREEN + ' SUCCESS\n')

print(Style.BRIGHT + ' [' + str(datetime.datetime.now()) + '] Waiting for targetted time...\n')
target_time = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, 23, 59, 59, 800000)
while (target_time - (ntpTM + (datetime.datetime.now() - lclTM))).total_seconds() > 0 :
    print(Fore.YELLOW + Style.BRIGHT + ' Countdown : ' + Fore.RESET + str(target_time - (ntpTM + (datetime.datetime.now() - lclTM))) + Fore.YELLOW + '    Current : ' + Fore.RESET + str(ntpTM + (datetime.datetime.now() - lclTM)), end='\r')

print(Style.BRIGHT + '\n\n [' + str(datetime.datetime.now()) + '] Waiting 1 sec for request safety\n')
sleep(1)
startTime1 = datetime.datetime.now()

print(Style.BRIGHT + ' [' + str(datetime.datetime.now()) + '] Refreshing list...', end='')
Select(driver.find_element_by_id('searchSrvcStts')).select_by_visible_text('모집중')
driver.find_element_by_id('btnSearch').click()
print(Fore.GREEN + ' SUCCESS\n')

print(Style.BRIGHT + ' [' + str(datetime.datetime.now()) + '] Selecting target...', end='')
try:
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[contains(@class, "service_part")][2]/div[contains(@class, "data_middle")]/ul/li[1]/a')))
    element.click()
    startTime2 = datetime.datetime.now()
except selenium.common.exceptions.TimeoutException:
    print(Fore.RED + Style.BRIGHT + ' ERROR_no_result')
    sys.exit()
print(Fore.GREEN + ' SUCCESS\n')

print(Style.BRIGHT + ' [' + str(datetime.datetime.now()) + '] Attempting to apply...', end='')
try:
    driver.find_element_by_xpath('//button[@id="btnReqst"]').click()
except selenium.common.exceptions.NoSuchElementException:
    print(Fore.RED + Style.BRIGHT + ' ERROR_not_appliable')
    sys.exit()
print(Fore.GREEN + ' SUCCESS\n')

print(Style.BRIGHT + ' [' + str(datetime.datetime.now()) + '] Attempting to select date...', end='')
try:
    driver.find_element_by_xpath('//*[contains(@class, "pc_only")]//span[text()="모집중"][' + ch + ']').click()
except selenium.common.exceptions.NoSuchElementException:
    print(Fore.RED + Style.BRIGHT + ' ERROR_no_available_date')
    sys.exit()
print(Fore.GREEN + ' SUCCESS\n')

print(Style.BRIGHT + ' [' + str(datetime.datetime.now()) + '] Selecting checkbox...', end='')
driver.find_element_by_id('agreeYn').click()
print(Fore.GREEN + ' SUCCESS\n')

print(Style.BRIGHT + ' [' + str(datetime.datetime.now()) + '] Final apply...', end='')
driver.find_element_by_id('btnRequest').click()
driver.switch_to.alert.accept()
print(Fore.GREEN + ' SUCCESS\n')

print(Style.BRIGHT + ' [' + str(datetime.datetime.now()) + '] Terminating Program.')
print(Fore.YELLOW + Style.BRIGHT + '\n Request Time : ' + Fore.RESET + str(datetime.datetime.now() - startTime1) + Fore.YELLOW + '    Working Time : ' + Fore.RESET + str(datetime.datetime.now() - startTime2))
sys.exit()
