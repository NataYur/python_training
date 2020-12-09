# -*- coding: utf-8 -*-
import random
from model.group import Group


def test_modify_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="to_modify"))
    old_groups = db.get_group_list()
    index = random.randrange(len(old_groups))
    group = Group(name="modified")
    group.id = old_groups[index].id
    app.group.modify_group_by_id(group.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(old_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_modify_group_header(app):
 #   if app.group.count() == 0:
  #      app.group.create(Group(name="to_modify"))
   # old_groups = app.group.get_group_list()
    #app.group.modify_first_group(Group(header="header50"))
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)