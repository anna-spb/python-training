# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import Select
import unittest
from Group1 import Group
from Application1 import Application

class CreateContact(unittest.TestCase):
    def setUp(self):
        self.app = Application


    def test_create_contact(self):
        self.app.Login(password="secret", username="admin")
        self.app.Create_contact(Group(firstname="hhhhh", middlename="dddd", lastname="ddddd", nickname="ddddd", title="dddd",
                            company= "dddd", address="ggg", home="hhhhhh", mobile="jjjj", work="kkkk",
                           fax="llllll", email="aass@hhj.ru", email2="gggg@kkk.com", email3="rrrr@hh.bu",
                            homepage="http//hjhkjhj.com", bday="18",
                            bmonth="November", byear="3333", aday="18", amonth="October", ayear="2222",
                            address2="hhhhhh", phone2="lllllll", notes="ghghg"))
        self.app.Logout()


        #непонятно что
        #wd.find_element_by_name("user").clear()
        #wd.find_element_by_name("user").send_keys("admin")


    def tearDown(self):
        self.app.destroy()

if __name__ == "__main__":
    unittest.main()
