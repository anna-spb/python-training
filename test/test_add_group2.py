 #-*- coding: utf-8 -*-

import pytest
from model.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(password="secret", username="admin")
    app.group.Create_group(Group(name="anechka1", header="вапап", footer="sdfg"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(password="secret", username="admin")
    app.group.Create_group(Group(name="", header="", footer=""))
    app.session.logout()