 #-*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(password="secret", username="admin")
    app.group.create(Group(name="anechka1", header="вапап", footer="sdfg"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(password="secret", username="admin")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()