
from model.contact import Group

def test_change_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.change_first_contact(Group(firstname=" ", middlename="     ", lastname="ddddd", nickname="ddddd",
                             title="dddd", company= "dddd", address="ggg", home="hhhhhh", mobile="jjjj", work="kkkk",
                             fax="llllll", email="aass@hhj.ru", email2="   .com", email3="rrrr@hh.bu",
                             homepage="http//hjhkjhj.com", bday="18",
                             bmonth="November", byear="3333", aday="18", amonth="October", ayear="2222",
                             address2="hhhhhh", phone2="lllllll", notes="ghghg"))
    app.session.logout()
