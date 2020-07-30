# -*- coding: utf-8 -*-

from model.contact import Group


def test_create_contact(app):
    app.contact.create(Group(firstname="hhhhh", middlename="dddd", lastname="ddddd", nickname="ddddd",
                             title="dddd", company= "dddd", address="ggg", home="hhhhhh", mobile="jjjj", work="kkkk",
                             fax="llllll", email="aass@hhj.ru", email2="gggg@kkk.com", email3="rrrr@hh.bu",
                             homepage="http//hjhkjhj.com", bday="18",
                             bmonth="November", byear="3333", aday="18", amonth="October", ayear="2222",
                             address2="hhhhhh", phone2="lllllll", notes="ghghg"))



