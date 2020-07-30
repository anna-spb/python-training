
from model.contact import Group


def test_delete_first_contact(app):
    if app.group.count() == 0:
        app.contact.create(Group(firstname="test"))
    app.contact.delete_first_contact()
