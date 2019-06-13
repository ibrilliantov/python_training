# -*- coding: utf-8 -*-
from group import Group
import pytest
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.create_groups(Group(name="gdfgsdgdfg", header="gsdsgfsgf", footer="footer"))
    app.logout()

def test_add_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_groups(Group(name="", header="", footer=""))
    app.logout()

