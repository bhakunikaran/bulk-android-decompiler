
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os
import requests
import sys

plat = sys.argv[1:]

options = Options()
options.headless = True

try:
	if 'win' in plat[0]: 
		browser = webdriver.Chrome('chromedriver.exe', chrome_options=options)
	elif 'mac' in plat[0]:
		browser = webdriver.Chrome('mac', chrome_options=options)
	elif 'linux' in plat[0]:
		browser = webdriver.Chrome('linux', chrome_options=options)
	else:
		print('no OS argument provided. --win/--mac/--linux')
except:
	print('No argument provided or webdriver error')

apks_folder = "apks/"
code_folder = 'source_code/'

for file in os.listdir(apks_folder):
	print("decompiling " + file)
	browser.get('http://www.javadecompilers.com/apk')
	time.sleep(2)
	browser.find_element_by_id("upload_datafile").send_keys(os.getcwd()+"/" + apks_folder + file)
	# print("file uploaded")
	time.sleep(2)

	browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div/div[2]/div/form/div/div/div/div[2]/div[1]/div/button').click()

	while(True):
		try:
			element = browser.find_element_by_xpath("//*[@id='main-container']/div/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div[1]/div[2]/a")
			break
		except:
			pass

	href = element.get_attribute('href')
	r = requests.get(href, allow_redirects=True)
	open(code_folder +  file[:-4]+'.zip', 'wb').write(r.content)
	print('decompiling ' + file " completed")

browser.close()