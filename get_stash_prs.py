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


def parse_ticket_type(pr_branch):
	words = pr_branch.split('/')
	if len(words) > 1:
		return words[0]
	else:
		return 'None'


def open_browser():
	browser = webdriver.Firefox()
	return browser


def goto_site(driver, url):
	driver.get(url)
	return driver


def is_logged_in(driver):
	my_password, my_username = get_credits('stash')
	try:
		user_dropdown = driver.find_element_by_id('current-user')
		cur_user = user_dropdown.get_attribute('data-username')
		if my_username == cur_user:
			return True
		else:
			print "Different User logged in: %s instead of %s" % (cur_user, my_username)
			return True
	except NoSuchElementException:
		return False


def is_on_vpn(driver):
	try:
		driver.find_element_by_id('errorPageContainer')
		return False
	except NoSuchElementException:
		return True


def get_credits(site):
	my_info = Personal_Info()
	p_w = my_info.get_password(site)
	u_n = my_info.get_user_name(site)
	return p_w, u_n


def log_in(driver, url):
	driver.get(url)
	user_element = driver.find_element_by_id('j_username')
	password_element = driver.find_element_by_id('j_password')
	my_password, my_username = get_credits('stash')
	user_element.send_keys(my_username)
	password_element.send_keys(my_password + Keys.ENTER)


def ensure_page(driver, url):
	if driver.current_url != url:
		goto_site(driver, url)
		assert driver.current_url == url, 'Cannot go to url, %s current url is %s' % (url, driver.current_url)


def get_table(driver, pr_url, login_url):
	while True:
		try:
			return_table = driver.find_element_by_id('pull-requests-table')
			return return_table
		except NoSuchElementException:
			if is_logged_in(driver):
				pass
			else:
				log_in(driver, login_url)
				ensure_page(driver, pr_url)


def close_browser(driver):
	try:
		driver.close()
		driver.quit()
	except:
		pass


def get_table_info(table_element):
	# Set intial Variables and dictionaries
	pr_num = ''
	pr_link = ''
	pr_branch = ''
	pr_links = {}
	pr_branches = {}
	pr_ticket_links = {}

	# Get Table Rows
	table_rows = table_element.find_elements(By.TAG_NAME, 'tr')
	for table_row in table_rows:

		# Get Cells in a Row
		cells = table_row.find_elements(By.TAG_NAME, "td")
		for cell in cells:

			# Parse based on cell class
			cell_class = cell.get_attribute('class')
			if cell_class == 'id':
				pr_num = int(str(cell.text[1:]))
				pr_link = str(cell.find_element_by_tag_name('a').get_attribute('href'))
			elif cell_class == 'source':
				pr_branch = str(cell.text)
		if pr_num is not '' and pr_link is not '' and pr_branch is not '':
			pr_links[pr_num] = pr_link
			pr_branches[pr_num] = pr_branch
			pr_ticket_links[pr_num] = parse_ticket_num(pr_branch)
	return pr_links, pr_branches, pr_ticket_links


def format_pr_hyperlinks(to_format):
	for item in to_format:
		to_format[item] = '=hyperlink("%s","%s")' % (to_format[item], item)
	return to_format

def format_ticket_hyperlinks(to_format):
	for item in to_format:
		if to_format[item] != None:
			to_format[item] = '=hyperlink("https://jira.charter.com/browse/SPECGUIDE-%s","%s")' % (to_format[item], to_format[item])
		else:
			to_format[item] = 'None'
	return to_format

if __name__ == "__main__":
	STASH_SITE_PR = 'http://stash.dev-charter.net/stash/projects/SG/repos/skyuisp/pull-requests'
	STASH_SITE_LOGIN = 'http://stash.dev-charter.net/stash/login'

	# Open Browser and Site for Stash
	browser = open_browser()
	goto_site(browser, STASH_SITE_PR)

	# Check if on VPN
	if not is_on_vpn(browser):
		print "Looks like you aren't on the VPN, Please Get on and try again!!!"
		close_browser(browser)
		sys.exit()

	# Check if logged in
	if not is_logged_in(browser):
		log_in(browser, STASH_SITE_LOGIN)

	# Ensure on PR Page
	ensure_page(browser, STASH_SITE_PR)

	quit_bool = False
	while not quit_bool:
		
		# Get the Table
		table = get_table(browser, STASH_SITE_PR, STASH_SITE_LOGIN)

		# Get all table data
		my_prs, my_branches, my_tickets = get_table_info(table)

		# formatt data for google docs
		my_prs = format_pr_hyperlinks(my_prs)
		my_tickets = format_ticket_hyperlinks(my_tickets)

		# Print everything out, sorted by prs
		prs = my_prs.keys()
		prs.sort()
		print ""
		print "There are %d PRs in the Open Column:" % len(prs)
		print ""
		for pr in prs:
			print chr(9).join([my_prs[pr], my_branches[pr], parse_ticket_type(my_branches[pr]), my_tickets[pr]])
		print ""
		if raw_input('Reload or Quit? (r/q): ') == 'r':
			browser.refresh()
			print ""
		else:
			quit_bool = True
	browser.close()