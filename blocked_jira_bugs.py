#! /usr/bin/env python
from libs.my_login import My_Login
from selenium.common.exceptions import NoSuchElementException

HYPERLINK_TEXT='=hyperlink("https://inspirato.atlassian.net/browse/WOODII-%s","%s")'
# HYPERLINK_TEXT='=hyperlink("https://jira.charter.com/browse/SPECGUIDE-%s","%s")'

def parse_ticket(stuff):
    words = stuff.split("-")
    for word in words:
        try:
            ticket_num = int(word)
            break
        except:
            pass
    if 'ticket_num' in vars():
        return ticket_num
    else:
        return 'None'

def get_tickets(driver):
    ticket_dict = {}
    try:
        mainlist = driver.get_element({"by":"class name","name":'issue-list'})
    except NoSuchElementException:
        return []
    try:
        list_elem = list(mainlist.find_elements_by_tag_name('li'))
    except:
        return None
    for item in list_elem:
        try:
            b = item.get_attribute('data-key')
            ticket_link = HYPERLINK_TEXT % (parse_ticket(b), parse_ticket(b))
            c = item.get_attribute('title')
        except:
            return None
        ticket_dict[ticket_link] = c
    return ticket_dict

def main_puller():
    my_jira = My_Login('jira-inspirato')
    my_jira.wait_for_login_element(10,10)
    tk_cnt = 0
    filters = {
        "Keith":"https://inspirato.atlassian.net/browse/WOODII-925?filter=18100"
        }

    print ""
    for name in filters:
        my_jira.open_site(filters[name])
        tickets = get_tickets(my_jira)
        while tickets == None:
            tickets = get_tickets(my_jira)

        for ticket in tickets:
            print chr(9).join([ticket, tickets[ticket]])
            tk_cnt += 1

    print ""
    print "There are %d tickets for %s." % (tk_cnt, ", ".join([x for x in filters]))
    print ""
    my_jira.logout()
    my_jira.close_site()

if __name__ == "__main__":
    main_puller()