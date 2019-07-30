# -*- coding: utf-8 -*-
from model.contact import Contact
import random

#
# def test_edit_first_contact_middlename(app):
#     app.contact.edit_first_contact_page(Contact(middlename="EditIrommanEditIrommanEditIrommanEditIromman"))

#
# def test_edit_some_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(
#             Contact(middlename="RANDIromman", firstname="RANDTony", lastname="RANDStark", nickname="ttt", title="WOW"))
#     contact = Contact(lastname="NEWEditIromman")
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact.id = old_contacts[index].id
#     app.contact.edit_contact_by_index(index, contact)
#     assert len(old_contacts) == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts[index] = contact
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_edit_random_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname='RANDIromman', middlename='RANDTony', lastname='RANDStark', nickname='tert', address='newyork', mobile='+7129837', email='home@mail.com'))
    old_contacts = db.get_contact_list()
    id = random.choice(old_contacts).id
    old_contacts_data = db.get_contact_id(id)
    old_contacts.remove(old_contacts_data)
    contact = Contact(firstname='Максим', id=id)
    app.contact.edit_contact_by_id(id, contact)
    old_contacts.append(contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)