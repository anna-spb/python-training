# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest
from Group import Group
from application import Application


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.app = Application()

    def test_add_group(self):
        self.app.login(password="secret", username="admin")
        self.app.Create_group(Group(name="anechka1", header="вапап", footer="sdfg"))
        self.app.logout()

    def test_add_empty_group(self):
        self.app.login(password="secret", username="admin")
        self.app.Create_group(Group(name="", header="", footer=""))
        self.app.logout()



    #def is_element_present(self, how, what):
        #try: self.wd.find_element(by=how, value=what)
        #except NoSuchElementException as e: return False
        #return True

    #@property
    #def is_alert_present(self):
        #try: self.wd.switch_to.alert()
        #except NoAlertPresentException as e: return False
        #return True

    def tearDown(self):
        self.app.destroy()
     
if __name__ == "__main__":
    unittest.main()
