# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture
    
def test_add_new_contact(app):
    app.session.login(username="admin", password="secret")
    # self.add_photo(wd, upload="C//")
    app.contact.create(Contact(middlename="Iromman", firstname="Tony", lastname="Stark", nickname="ttt", title="WOW",
                               company="StarkInc", address="www", home="rock", work="worldsaver", mobile="123",
                               fax="123", email="one@home.com", email2="two@home.com", email3="three@home.com",
                               homepage="ewew", address2="leningrad", phone2="456", notes="what?", aday="5",
                               amonth="March", ayear="1987", bday="5", bmonth="March", byear="1987", ))
    app.session.logout()
