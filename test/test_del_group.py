# -*- coding: utf-8 -*-
from model.group import Group
import random
import pytest


def test_delete_some_group(app, db, check_ui):
    if len (db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="gsdsgfsgf", footer="footer"))
    old_groups = db.get_group_list()
    with pytest.allure.step('Choice group for delete'):
        group = random.choice(old_groups)
    with pytest.allure.step('Delete random group'):
        app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()
    with pytest.allure.step('Check group is delete'):
        assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)