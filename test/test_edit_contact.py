# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

#
# def test_edit_first_contact_middlename(app):
#     app.contact.edit_first_contact_page(Contact(middlename="EditIrommanEditIrommanEditIrommanEditIromman"))


def test_edit_some_contact(app):
    if app.contact.count() == 0:
        app.contact.create(
            Contact(middlename="RANDIromman", firstname="RANDTony", lastname="RANDStark", nickname="ttt", title="WOW"))
    contact = Contact(lastname="NEWEditIromman")
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
