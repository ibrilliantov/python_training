# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middlename="Iromman", firstname="Tony", lastname="Stark", nickname="ttt", title="WOW" ))
    app.contact.delete_first_contact()
