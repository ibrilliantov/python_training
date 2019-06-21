# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    # self.add_photo(wd, upload="C//")
    app.contact.edit_first_contact_page(Contact(middlename="EditIromman", firstname="EditTony", lastname="EditStark", nickname="Editttt", title="EditWOW",
                               company="EditStarkInc", address="www", home="rock", work="worldsaver", mobile="123",
                               fax="Edit123", email="Editone@home.com", email2="Edittwo@home.com", email3="Editthree@home.com",
                               homepage="Editewew", address2="Editleningrad", phone2="Edit456", notes="Editwhat?", aday="5",
                               amonth="March", ayear="1987", bday="5", bmonth="March", byear="1987", ))
    app.session.logout()
