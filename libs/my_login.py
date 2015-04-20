from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from libs.personal_info import Personal_Info

class My_Login(object):
    SITE_JSON = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../data/site_info.json'))

    def __init__(self, site, driver=None):
        if driver == None:
            self._open_browser()
        else:
            self.browser = driver
        self.site = site
        self._get_creds()
        self._get_site_data()
        self.open_site(self._get_site_data_data('site'))
        if not self.is_login():
            self.login()
        # Get Site Details

    
    def _open_browser(self):
        self.browser = webdriver.Firefox()


    def _get_creds(self):
        my_info = Personal_Info()
        self.p_w = my_info.get_password(self.site)
        self.u_n = my_info.get_user_name(self.site)

    
    def _get_site_data(self):
        my_info = Personal_Info(self.SITE_JSON)
        self.site_data = my_info.return_category(self.site)
        if self.site_data == None:
            raise NameError('No Site Data for ' + str(self.site))


    def _get_site_data_data(self, dict_name):
        try:
            return self.site_data[dict_name]
        except KeyError:
            return None
    

    def open_site(self, url):
        self.browser.get(url)

    
    def is_login(self):
        try:
            self.get_element(self._get_site_data_data('check_login_element'))
            return True
        except NoSuchElementException:
            return False


    def login(self):
        user_element = self.get_element(self._get_site_data_data('user_name_element'))
        pw_element = self.get_element(self._get_site_data_data('password_element'))
        user_element.send_keys(self.u_n)
        pw_element.send_keys(self.p_w + Keys.ENTER)
        if self.site_data["additional_login_action"] != "None":
            self.element_action_chain(self._get_site_data_data("additional_login_action"))


    def element_action_chain(self, action_dict):
        for step in range(0, len(action_dict["by"])):
            actions = ActionChains(self.browser)
            element = self.get_element({"by":action_dict["by"][step], "name":action_dict["name"][step]})
            if action_dict["action"][step] == "click":
                actions.click(element)
            elif action_dict["action"][step] == "hover":
                actions.move_to_element(element)
            actions.perform()


    def get_element(self, elem_info):
        if type(elem_info["by"]) == list:
            return self.get_deep_element(elem_info)
        else:
            return self.browser.find_element(elem_info["by"], elem_info["name"])


    def get_deep_element(self, info_dict):
        elements = [self.browser]
        for step in range(0, len(info_dict["by"])):
            try:
                elements.append(elements[step].find_element(info_dict["by"][step], info_dict["name"][step]))
            except NoSuchElementException:
                return None
        return elements[len(elements)-1]


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


    def wait_for_login_element(self, wait_elem=5, wait_vis=5):
        return self.wait_for_element(self._get_site_data_data('check_login_element')['by'], self._get_site_data_data('check_login_element')['name'], wait_elem, wait_vis)


    def logout(self):
        self.element_action_chain(self._get_site_data_data("logout_actions"))

    
    def close_site(self):
        self.browser.close()



