# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import pytest


def test_delete_some_contact(app, db, check_ui):
    if len (db.get_contact_list()) == 0:
        app.contact.create(Contact(middlename="Iromman", firstname="Tony", lastname="Stark", nickname="ttt", title="WOW"))
    old_contacts = db.get_contact_list()
    with pytest.allure.step('Choice random contact for delete'):
        contact = random.choice(old_contacts)
    with pytest.allure.step('Delete random contact'):
        app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    with pytest.allure.step('Check contact is delete'):
        assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.group.get_group_list(), key=Contact.id_or_max)

