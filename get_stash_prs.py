#! /usr/bin/env python
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import sys
from libs.my_login import My_Login

def get_reviewers(table_cell):
    spans = table_cell.find_elements_by_tag_name('span')
    approved_by = []
    for span in spans:
        classes = span.get_attribute('class')
        if 'badge-hidden' not in classes and 'participant-item' in classes:
            approved_by.append(span.get_attribute('data-username'))
    if len(approved_by) > 0:
        return_string = ', '.join(approved_by)
    else:
        return_string = '--'
    return return_string


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
        return '--'


def get_table_info(table_element):
    # Set intial Variables and dictionaries
    pr_num = ''
    pr_link = ''
    pr_branch = ''
    pr_links = {}
    pr_branches = {}
    pr_ticket_links = {}
    pr_approvers = {}

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
            elif cell_class == 'reviewers':
                pr_reviewers = str(get_reviewers(cell))
        if pr_num is not '' and pr_link is not '' and pr_branch is not '':
            pr_links[pr_num] = pr_link
            pr_branches[pr_num] = pr_branch
            pr_ticket_links[pr_num] = parse_ticket_num(pr_branch)
            pr_approvers[pr_num] = pr_reviewers
    return pr_links, pr_branches, pr_ticket_links, pr_approvers


def format_pr_hyperlinks(to_format):
    for item in to_format:
        to_format[item] = '=hyperlink("%s","%s")' % (to_format[item], item)
    return to_format


def format_ticket_hyperlinks(to_format):
    for item in to_format:
        if to_format[item] != None:
            to_format[item] = '=hyperlink("https://jira.charter.com/browse/SPECGUIDE-%s","%s")' % (to_format[item], to_format[item])
        else:
            to_format[item] = '--'
    return to_format


if __name__ == "__main__":
    STASH_SITE_PR = 'http://stash.dev-charter.net/stash/projects/SG/repos/skyuisp/pull-requests'
    try:
        my_stash = My_Login('stash')
    except NoSuchElementException:
        print "Looks like you aren't on the VPN, Please Get on and try again!!!"
        my_stash.close_site()
        sys.exit()

    my_stash.wait_for_login_element(10,10)
    my_stash.open_site(STASH_SITE_PR)
    
    # Get the Table
    table = my_stash.get_element({"by":"id","name":"pull-requests-table"})

    # Get all table data
    my_prs, my_branches, my_tickets, my_reviewers = get_table_info(table)

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
        print chr(9).join([my_prs[pr], my_branches[pr], parse_ticket_type(my_branches[pr]), my_tickets[pr], my_reviewers[pr]])
    print ""
    my_stash.logout()
    my_stash.close_site()