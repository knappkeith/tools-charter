#! /usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import sys
from libs.personal_info import Personal_Info

def parse_ticket_num(pr_name):
	words = pr_name.split("-")
	for word in words:
		try:
			ticket_num = int(word)
			break
		except:
			pass
	if 'ticket_num' in vars():
		return ticket_num
	else:
		return None

def open_browser():
	browser = webdriver.Firefox()
	return browser

def goto_site(driver, url):
	driver.get(url)
	return driver

def is_logged_in(driver):
	url = driver.current_url()
	if '/login' in url:
		return False
	elif '/pull-requests' in url:
		return True
	else:
		return False

def is_on_vpn(driver):
	try:
		driver.find_element_by_id('offline-resources-1x')
		return False
	except NoSuchElementException:
		return True

def get_credits(site):
	my_info = Personal_Info()
	p_w = my_info.get_password(site)
	u_n = my_info.get_user_name(site)
	return p_w, u_n


browser = webdriver.Firefox()
browser.get('http://stash.dev-charter.net/stash/projects/SG/repos/skyuisp/pull-requests')
try:
	user = browser.find_element_by_id('j_username')
except NoSuchElementException:
	print "Are you on the VPN?  Exitting...."
	browser.close()
	sys.exit()

password = browser.find_element_by_id('j_password')
my_password, my_username = get_credits('stash')
user.send_keys(my_username)
password.send_keys(my_password + Keys.ENTER)
quit_bool = False
while not quit_bool:
	got_table = False
	while not got_table:
		try:
			table = browser.find_element_by_id('pull-requests-table')
			got_table = True
		except:
			got_table = False
			# Check for login, this is for refresh
			try:
				browser.find_element_by_id('j_password')
				print "you have been logged out, rerun. Exitting..."
				browser.quit()
				sys.exit()
			except NoSuchElementException:
				pass
	trs = table.find_elements(By.TAG_NAME, 'tr')
	pr_num = ''
	pr_link = ''
	formulas = {}
	branches = {}
	for tr in trs:
		tds = tr.find_elements(By.TAG_NAME, "td")
		for td in tds:
			td_att = td.get_attribute('class')
			if td_att == 'id':
				pr_num = td.text
			if td_att == 'title':
				pr_link = td.find_element_by_tag_name('a').get_attribute('href')
			if td_att == 'source':
				pr_branch = td.text
		if pr_num is not '' and pr_link is not '':
			formulas[int(str(pr_num[1:]))] = '=hyperlink("%s","%s")' % (str(pr_link), str(pr_num[1:]))
			branches[int(str(pr_num[1:]))] = str(pr_branch[6:])
	prs = formulas.keys()
	prs.sort()
	print "There are %d PRs in the Open Column:" % len(prs)
	print ""
	for pr in prs:
		ticket = parse_ticket_num(branches[pr])
		if ticket != None:
			print formulas[pr] + chr(9) + branches[pr] + chr(9) + '=hyperlink("https://jira.charter.com/browse/SPECGUIDE-%s","%s")' % (str(ticket), str(ticket))
		else:
			print formulas[pr] + chr(9) + branches[pr] + chr(9) + 'Parse Error'
	print ""
	if raw_input('Reload or Quit? (r/q): ') == 'r':
		browser.refresh()
		print ""
	else:
		quit_bool = True
browser.close()