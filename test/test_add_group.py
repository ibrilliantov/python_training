# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_groups(Group(name="gdfgsdgdfg", header="gsdsgfsgf", footer="footer"))
    app.session.logout()

def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_groups(Group(name="", header="", footer=""))
    app.session.logout()

