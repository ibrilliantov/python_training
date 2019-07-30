# -*- coding: utf-8 -*-
from model.group import Group
import random

# def test_edit_some_group(app, db, check_ui):
#     if app.group.count() == 0:
#         app.group.create(Group(name="gdfgsdgdfg", header="gsdsgfsgf", footer="footer"))
#     old_groups = db.get_group_list()
#     group = random.choice(old_groups)
#     group = Group(name="New group")
#     group.id = old_groups[index].id
#     app.group.edit_group_by_index(index, group)
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
#     old_groups[index] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_random_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='gdfgsdgdfg', header='gdfgsdgdfg', footer='gdfgsdgdfg'))
    old_groups = db.get_group_list()
    id = random.choice(old_groups).id
    old_group_data = db.get_group_by_id(id)
    old_groups.remove(old_group_data)
    group = Group(name='New group', id=id)
    app.group.edit_group_by_id(id, group)
    old_groups.append(group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

# def test_edit_first_group_header(app):
#     old_groups = app.group.get_group_list()
#     if app.group.count() == 0:
#         app.group.create(Group(name="gdfgsdgdfg", header="gsdsgfsgf", footer="footer"))
#     app.group.edit_first_group(Group(header="New Header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
