# -*- coding: utf-8 -*-
from model.contact import Contact

#
# def test_edit_first_contact_middlename(app):
#     app.session.login(username="admin", password="secret")
#     app.contact.edit_first_contact_page(Contact(middlename="EditIrommanEditIrommanEditIrommanEditIromman"))
#     app.session.logout()


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact_page(Contact(middlename="EditIromman", firstname="EditTony", lastname="EditStark", nickname="Editttt", title="EditWOW",
                               company="EditStarkInc", address="www", home="rock", work="worldsaver", mobile="123",
                               fax="Edit123", email="Editone@home.com", email2="Edittwo@home.com", email3="Editthree@home.com",
                               homepage="Editewew", address2="Editleningrad", phone2="Edit456", notes="Editwhat?", aday="6",
                               amonth="June", ayear="1988", bday="6", bmonth="June", byear="1988", ))
    app.session.logout()

# def test_edit_first_amonth(app):
#     app.session.login(username="admin", password="secret")
#     app.contact.edit_first_contact_page(Contact(amonth="May"))
#     app.session.logout()
