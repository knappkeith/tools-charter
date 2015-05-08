#! /usr/bin/env python
from libs.my_login import My_Login
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import sys

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

def is_table_open(table):
    if table.get_attribute('aria-disabled') == "false":
        return False
    else:
        return True

def open_table(table):
    btn = table.find_element_by_class_name('ghx-expander')
    btn.click()

def table_issue_count(table):
    issue_cnt = table.find_element_by_class_name('ghx-issue-count').text
    count = 0
    for word in issue_cnt.split(" "):
        try:
            count = int(word)
        except:
            pass
    return count

def get_tickets(table):
    return table.find_elements_by_class_name('js-issue')

def get_infos(tickets):
    ticket_info = []
    for ticket in tickets:
        data = {}
        data['description'] = ticket.find_element_by_class_name('ghx-inner').text
        data['num'] = parse_ticket_num(ticket.find_element_by_class_name('ghx-key').text)
        data['assignee'] = ticket.find_element_by_class_name('ghx-avatar-img').get_attribute('data-tooltip')[10:]
        ticket_info.append(data)
    return ticket_info

def find_table(browser):
    my_jira.wait_for_element("class name", "ghx-backlog-container", 150)
    possible_tables = my_jira.browser.find_elements_by_class_name('ghx-backlog-container')
    for table in possible_tables:
        table_name = table.find_element_by_class_name("ghx-name")
        if table_name.text == "Bugs in Triage":
            return table

def main_puller():
    my_jira = My_Login('jira')
    my_jira.wait_for_login_element(10,10)
    my_jira.open_site('https://jira.charter.com/secure/RapidBoard.jspa?rapidView=166&view=planning.nodetail')
    my_table = find_table(my_jira)
    if not is_table_open(my_table):
        open_table(my_table)

    num_issues = table_issue_count(my_table)
    if num_issues == 0:
        print "There aren't any Bugs in Triage, YAY!!!!"
        my_jira.logout()
        my_jira.close_site()
        sys.exit()

    my_tickets = get_tickets(my_table)
    print ""
    for info in get_infos(my_tickets):
        print chr(9).join(['=hyperlink("https://jira.charter.com/browse/SPECGUIDE-%s","%s")' % (info['num'], info['num']), info['description'], info['assignee']])

    print ""
    print "There are %d tickets in the Bugs in Triage Sprint." % len(my_tickets)
    print ""
    my_jira.logout()
    my_jira.close_site()

if __name__ == '__main__':
    main_puller()