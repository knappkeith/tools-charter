# General Imports
import os
import sys
import time

# Import My Class
sys.path.append(os.path.abspath('../'))
from libs.sling_helper import Sling_Box

# Selenium Imports
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException


watched = []
cur_browsers = []

ff_profile = '/Users/keithknapp/Library/Application Support/Firefox/Profiles/y4042wiv.default'
cur_browser = Sling_Box(ff_profile)
cur_browser.open_slingbox_site()

while True:
	cur_browser.watch_slingbox(watched)
	if cur_browser.cur_sling is None:
		break
	watched.append(cur_browser.cur_sling)
	raw_input("next")

cur_browser.browser.quit()

















sys.exit(0)

# BELOW THIS IS OLD CODE......
fp = webdriver.FirefoxProfile('/Users/keithknapp/Library/Application Support/Firefox/Profiles/y4042wiv.default')

browser = webdriver.Firefox(fp)

browser.get('http://www.slingbox.com')

browser.find_element_by_link_text('Watch').click()

# browser.find_element_by_id('user_email').click()

# browser.find_element_by_id('menu_slingbox').click()

# slings = browser.find_elements_by_class_name('product_row')

# slings_dict = {}
# for sling in slings:
# 	slings_dict[sling.find_element_by_id('product_name').text] = sling

# print slings_dict

while True:
	try:
		print browser.find_element_by_id('stepsDiv').text
		break
	except:
		time.sleep(1)
		print 'sleep for a second'

directory = browser.find_element_by_id('directory_message')

ActionChains(browser).move_to_element(directory).perform()
menu = browser.find_element_by_id('receivers_popup_wrapper')
while True:
	list_sling = menu.find_elements_by_tag_name('li')
	if len(list_sling)>0:
		break
	else:
		time.sleep(0.01)
		print 'sleep 1/100th of sec'

list_sling[5].find_element_by_class_name('slingboxDirectoryNameDiv').click()

for sling in list_sling:
	print sling.find_element_by_class_name('slingboxDirectoryNameDiv').get_attribute('innerHTML')

iframes = browser.find_elements_by_tag_name('iframe')
count = 0.0
button_frame = 0
while count<=15:
	for i in range(0,len(iframes)):
		browser.switch_to_frame(iframes[i])
		try:
			skip_button = browser.find_element_by_class_name('videoAdUiSkipButton')
			print 'Button FOUND!!!!!'
			count = 20
			button_frame = i
		except NoSuchElementException:
			print 'Button not found in iframe #%d.' % i
		time.sleep(.5)
		count += 0.5
		browser.switch_to_default_content()
try:
	try:
		browser.switch_to_frame(iframes[button_frame])
		skip_button.click()
	except ElementNotVisibleException:
		print "Can't see button!!!"
	browser.switch_to_default_content()
except NameError:
	print 'NO Button'


time.sleep(10)
browser.close()
