# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd)
        self.create_contact(wd)
        self.return_to_homepage(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_homepage(self, wd):
        wd.find_element_by_link_text("home").click()

    def create_contact(self, wd):
        # init new contact creation
        wd.find_element_by_link_text("add new").click()
        # fill in new contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("dd")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("ddc")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("d")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("dfdfc")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("koko")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("joijoij")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("kjojoi")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("2266466")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("44611")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("46465131")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("515151")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("yuiuiu@nkjn.com")
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").click()
        # ERROR: Caught exception [ERROR: Unsupported command [doubleClick | name=email | ]]
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("yuiuiu@nkjn.com")
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("yuiuiu@nkjn.com")
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("www.fjvbfdbv.com")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("18")
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1515")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("15")
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("February")
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("1222")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("lkmflksdm")
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("efvfedv")
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("vefbebe")
        # submit group creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def login(self, wd):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_id("LoginForm").submit()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
