# -*- coding: utf-8 -*-

#rom model.group import Group


def test_change_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.change_first_group(name="ddd", header="ggg", footer="asd")
    app.session.logout()
