import os
import time

# Selenium Imports
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException


class Sling_Box(object):
    def __init__(self, profile, already_opened = [], url = 'http://www.slingbox.com'):
        self._set_profile_path(profile)
        self.skip_boxes = self._change_to_list(already_opened)
        self.url = url


    def _set_profile_path(self, profile):
        # expand profile
        profile = os.path.expanduser(profile)

        # Check if folder exists
        if os.path.isdir(profile):
            self.profile_path = profile
        else:
            raise NameError('Invalid User Profile')


    def _change_to_list(self, the_list):
        if not type(the_list) == 'list':
            return list(the_list)
        else:
            return the_list


    def _open_firefox(self):
        self._set_profile()
        self.browser = webdriver.Firefox(self.profile)


    def _set_profile(self):
        self.profile = webdriver.FirefoxProfile(self.profile_path)


    def open_slingbox_site(self):
        self._open_firefox()
        time.sleep(5)
        self.goto_url(self.url)
        self.check_login()
        self.wait_for_element(By.LINK_TEXT, 'Watch').click()
        self.wait_for_element(By.ID, 'stepsDiv', 60)
    
    def watch_slingbox(self, exclude_list = []):
        self.hover_element_id('directory_message')
        self.available_slings = self._get_sling_names('receivers_popup_wrapper')
        self.cur_sling = self._get_free_sling(exclude_list)
        if not self.cur_sling is None:
            print 'Viewing %s...' % self.cur_sling
            try:
                self.available_slings[self.cur_sling].click()
            except ElementNotVisibleException:
                self.hover_element_id('directory_message')
                self.available_slings[self.cur_sling].click()


    def hover_element_id(self, hover_element_id):
        hover_element = self.wait_for_element(By.ID, hover_element_id)
        ActionChains(self.browser).move_to_element(hover_element).perform()


    def _get_sling_names(self, menu_id):
        menu = self.browser.find_element_by_id(menu_id)
        wait_sec = 5
        list_sling = []
        while wait_sec >= 0:
            list_sling = menu.find_elements_by_tag_name('li')
            if len(list_sling)>0:
                break
            else:
                time.sleep(0.01)
                wait_sec -= 0.01
        sling_elements = {}
        for i in list_sling:
            i_element = i.find_element_by_class_name('slingboxDirectoryNameDiv')
            sling_elements[i_element.get_attribute('innerHTML')] = i_element
        del menu
        del list_sling
        del i_element
        return sling_elements

    def _get_free_sling(self, no_go_list):
        for sling in self.available_slings:
            if not sling in no_go_list:
                return sling
        return None


    def goto_url(self, url):
            self.browser.get(url)


    def wait_for_element(self, by_type, by_value, no_such_wait = 5, not_visible_wait = 5, **args):
        try:
            element = WebDriverWait(self.browser, no_such_wait).until(
                EC.presence_of_element_located((by_type, by_value)))
        except:
            raise NoSuchElementException
        if not_visible_wait > 0:
            try:
                element = WebDriverWait(self.browser, not_visible_wait).until(
                    EC.visibility_of_element_located((by_type, by_value)))
            except:
                raise ElementNotVisibleException
        return self.browser.find_element(by_type, by_value)


    def check_login(self):
        try:
            element = self.wait_for_element(By.PARTIAL_LINK_TEXT, 'Logout',10,0)
        except NoSuchElementException, ElementNotVisibleException:
            raise NameError("Please login on your %s Firefox profile, and be sure to check 'Remember Me' and try again!" % self.profile.path)


    def close(self):
        self.browser.quit()



