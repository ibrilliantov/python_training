# -*- coding: utf-8 -*-
from model.contact import Contact

#
# def test_edit_first_contact_middlename(app):
#     app.contact.edit_first_contact_page(Contact(middlename="EditIrommanEditIrommanEditIrommanEditIromman"))


def test_edit_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(
            Contact(middlename="Iromman", firstname="Tony", lastname="Stark", nickname="ttt", title="WOW"))
    contact = Contact(middlename="EditIromman")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact_page(contact)
    new_contacts = app.contact.get_contact_list()
    assert old_contacts == new_contacts
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

