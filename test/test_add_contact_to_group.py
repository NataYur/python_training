from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_some_group(app, orm):
    if app.group.count() == 0:
        app.group.create(Group(name="group for contact"))
    group = random.choice(orm.get_group_list())
    contacts_not_from_group = orm.get_contacts_not_in_group(group)
    if len(contacts_not_from_group) == 0:
        app.contact.create(Contact(lastname="for a group"))
        contacts_not_from_group = orm.get_contacts_not_in_group(group)
    contact = random.choice(contacts_not_from_group)
    app.contact.add_contact_to_group(contact.id, group.name)
    ui_group_related_contacts = app.contact.display_group_related_contacts(group.name)
    db_group_related_contacts = orm.get_contacts_in_group(group)
    assert sorted(ui_group_related_contacts, key=Contact.id_or_max) == sorted(db_group_related_contacts,
                                                                              key=Contact.id_or_max)
