# -*- coding: utf-8 -*-

from model.group import Group


def test_change_first_group(app):
    app.group.change_first_group(Group(name="ddd", header="ggg", footer="asd"))

def test_modify_first_group_name(app):
    app.group.modify_first_group(Group(name="New name"))

