import os
import sys
import time
import base64
from functools import reduce

import cv2
import numpy as np
from dotenv import load_dotenv
load_dotenv()

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.touch_actions import TouchActions


print('initializing selenium...')
try:
  options = webdriver.ChromeOptions()
  if os.getenv('canary') != '0': options.binary_location = (os.getenv('canary')) # for chrome canary
  options.add_experimental_option('prefs', { 'profile.managed_default_content_settings.images': 2 }) # prevent images
  options.add_experimental_option('mobileEmulation', { 'deviceName': 'Pixel 2 XL' }) # mobile emulation
  options.add_experimental_option('w3c', False) # for touch actions
  options.add_argument('--auto-open-devtools-for-tabs') # starts with devtool
  driver = webdriver.Chrome('chromedriver.exe', options = options)
  driver.implicitly_wait(5)

except selenium.common.exceptions.WebDriverException:
  print('driver load failed.')
  sys.exit()
print('driver loaded.')

cv2.namedWindow('keys')
input('\nActivate mobile emulation and press ENTER\n\n')


print('attempting login...')
driver.get('https://login.11st.co.kr/auth/login.tmall')
driver.find_element_by_name('memId').send_keys(os.getenv('id'))
driver.find_element_by_name('memPwd').send_keys(os.getenv('pw'))
driver.find_element_by_class_name('bbtn').click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'root')))
print('  login succeeded.')


print('\nwatching product status', end='', flush=True)
driver.get(os.getenv('productURL' + os.getenv('mode')))

driver.implicitly_wait(0.1)
while True:
  try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'dt_title')))
    driver.execute_script("document.querySelector(`div.buy > button[data-log-actionid-label='buy']`).click()")
    print('\n  target found.')
    break

  except selenium.common.exceptions.JavascriptException:
    print('.', end='', flush=True)
    driver.refresh()
driver.implicitly_wait(5)
time.sleep(0.5)


print('\nprocessing options...')
opts = []
for i, opt in enumerate(driver.find_elements_by_css_selector('ul.optlst > li > a')):
  opts.append({ "index": i, "count": int(opt.get_attribute('data-stckqty')), "name": opt.get_attribute('data-optnm') })
tgt = reduce(lambda x, y: x if x['count'] > y['count'] else y, opts)
for opt in opts: print('  i:', opt['index'], ' c:', opt['count'], ' n:', opt['name'])

# tgt = opts[0] # for debugging!!!

print('\ntrying largest stock product:', tgt)
try:
  driver.execute_script("document.querySelectorAll('ul.optlst > li')[" + str(tgt['index']) + "].click()")
  time.sleep(0.5)

  print('  validating option selection...')
  try:
    driver.execute_script("document.querySelector(`div.buy > button[data-log-actionid-label='buy_now']`).click()")
    time.sleep(0.5)
    driver.execute_script("document.querySelector(`div.buy > button[data-log-actionid-label='buy_now']`).click()")

  except selenium.common.exceptions.UnexpectedAlertPresentException:
    driver.switch_to.alert.accept()
    print('  FAILED option validation. retrying from first item...')
    for opt in opts:
      print('    trying option:', opt)
      driver.execute_script("document.querySelectorAll('ul.optlst > li')[" + str(opt['index']) + "].click()")
      time.sleep(0.5)
      try:
        driver.execute_script("document.querySelector(`div.buy > button[data-log-actionid-label='buy_now']`).click()")
        time.sleep(0.5)
        driver.execute_script("document.querySelector(`div.buy > button[data-log-actionid-label='buy_now']`).click()")

      except selenium.common.exceptions.UnexpectedAlertPresentException:
        driver.switch_to.alert.accept()
        print('      failed.')
        continue
      except selenium.common.exceptions.JavascriptException: break
      break
  except selenium.common.exceptions.JavascriptException: pass
except Exception: print('  failed processing options: ignoring.')


print('\nprocessing payment...')
try:
  driver.execute_script("document.querySelector(`button#doPaySubmit`).click()")
  print('  payment click ok with javascript method.')
except selenium.common.exceptions.JavascriptException:
  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'doPaySubmit')))
  driver.find_element_by_id('doPaySubmit').click()
  print('  payment click ok with selenium method.')


print('\nprocessing sk pay...')
driver.switch_to.frame(driver.find_element_by_id('skpay-ui-frame'))
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'keypad11pay-keypad-number')))

print('  displaying key image...')
b64target = driver.find_element_by_class_name('keypad11pay-keypad-number').value_of_css_property('background-image')
b64target = b64target.replace('url("data:image/png;base64,', '').replace('")', '')

target = cv2.imdecode(np.frombuffer(base64.b64decode(b64target), np.uint8), cv2.IMREAD_UNCHANGED)
cv2.imshow('keys', target)

print('  marking keypads...')
try: driver.execute_script('for(const keypad of document.querySelectorAll(".keypad11pay-keypad")) keypad.style["border-color"] = "red";')
except Exception: pass

print('  waiting key instruction...')
blank = cv2.waitKey(0)
blank = blank - 48
print('    key:', blank)

print('  performing keypad inputs...')
touch = TouchActions(driver)
for c in os.getenv('skpaypw'):
  code = int(c)
  key = code if code > blank else code - 1
  key = str(key)
  touch.tap(driver.find_element_by_id('keypad11pay-keypad-' + key))
  print('    interpreted: keypad11pay-keypad-' + key)

if os.getenv('purchase') == '1':
  touch.perform()
  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'popup')))
  driver.find_element_by_css_selector('#popup button').click()
  WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'btn-req-auth')))
  driver.find_element_by_id('btn-req-auth').click()

driver.switch_to.default_content()
print('\nDONE.')
