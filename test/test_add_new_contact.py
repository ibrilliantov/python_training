# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string


# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
# def random_number(prefix, maxlen):
#     symbols = string.digits
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# testdata = [Contact(middlename=random_string("middlename", 10), firstname=random_string("firstname", 20), lastname=random_string("lastname", 20),
#             nickname=random_string("nickname", 20), title=random_string ("WOW",10), company=random_string ("StarkInc", 3),
#             address=random_string("www", 30), homephone=random_number ("+7", 7), workphone=random_number ("+7", 7), mobilephone=random_number("+", 7),
#                                fax=random_number ("+7", 5), email="one@home.com", email2="two@home.com", email3="three@home.com",
#                                homepage=random_string ("www", 30), address2=random_string ("www", 30), secondaryphone=random_number ("+7", 7),
#                                notes=random_string("www", 30), aday="5", amonth="March", ayear="1987", bday="5", bmonth="March", byear="1987")
#     for i in range(1)
# ]
#
#
#
#
# @pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_new_contact(app, db, check_ui, json_contacts):
    contact = json_contacts
    with pytest.allure.step('Given a contact list'):
        old_contacts = db.get_contact_list()
    with pytest.allure.step('Create contact'):
        app.contact.create(contact)
    new_contacts = db.get_contact_list()
    with pytest.allure.step('Check contacts list'):
        assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)
