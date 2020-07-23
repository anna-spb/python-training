# -*- coding: utf-8 -*-
import pytest
from Group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(password="secret", username="admin")
    app.Create_group(Group(name="anechka1", header="вапап", footer="sdfg"))
    app.logout()


def test_add_empty_group(app):
    app.login(password="secret", username="admin")
    app.Create_group(Group(name="", header="", footer=""))
    app.logout()

