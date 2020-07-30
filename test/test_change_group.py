# -*- coding: utf-8 -*-

from model.group import Group


def test_change_first_group(app):
    app.group.change_first_group(Group(name="ddd", header="ggg", footer="asd"))

