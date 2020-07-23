# -*- coding: utf-8 -*-
import pytest
from model.contact import Group
from fixture.application1 import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Group(firstname="hhhhh", middlename="dddd", lastname="ddddd", nickname="ddddd",
                            title="dddd", company= "dddd", address="ggg", home="hhhhhh", mobile="jjjj", work="kkkk",
                            fax="llllll", email="aass@hhj.ru", email2="gggg@kkk.com", email3="rrrr@hh.bu",
                            homepage="http//hjhkjhj.com", bday="18",
                            bmonth="November", byear="3333", aday="18", amonth="October", ayear="2222",
                            address2="hhhhhh", phone2="lllllll", notes="ghghg"))
    app.logout()


