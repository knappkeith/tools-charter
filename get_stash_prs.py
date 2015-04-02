#! /usr/bin/env python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import sys
browser = webdriver.Firefox()
browser.get('http://stash.dev-charter.net/stash/projects/SG/repos/skyuisp/pull-requests')
try:
	user = browser.find_element_by_id('j_username')
except NoSuchElementException:
	print "Are you on the VPN?  Exitting...."
	browser.close()
	sys.exit(0)

password = browser.find_element_by_id('j_password')
user.send_keys('kknapp')
password.send_keys('98JRnpwWE58ELYpr' + Keys.ENTER)
quit_bool = False
while not quit_bool:
	got_table = False
	while not got_table:
		try:
			table = browser.find_element_by_id('pull-requests-table')
			got_table = True
		except:
			got_table = False
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
		print formulas[pr] + chr(9) + branches[pr]
	print ""
	if raw_input('Reload or Quit? (r/q): ') == 'r':
		browser.refresh()
		print ""
	else:
		quit_bool = True
browser.close()