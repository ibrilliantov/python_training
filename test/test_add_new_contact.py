# -*- coding: utf-8 -*-
from model.contact import Contact

    
def test_add_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact (middlename="Iromman", firstname="Tony", lastname="Stark", nickname="ttt", title="WOW",
                               company="StarkInc", address="www", homephone="123", workphone="234", mobilephone="567",
                               fax="123", email="one@home.com", email2="two@home.com", email3="three@home.com",
                               homepage="ewew", address2="leningrad", secondaryphone="890", notes="what?", aday="5",
                               amonth="March", ayear="1987", bday="5", bmonth="March", byear="1987")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

