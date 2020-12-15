from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group for contact"))
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="group contact"))
    all_ui_contacts = app.contact.get_contact_list()
    contact = random.choice(all_ui_contacts)
    ui_groups = app.group.get_group_list()
    group = random.choice(ui_groups)
    app.contact.add_contact_to_group(contact.id, group.name)
    ui_group_related_contacts = app.contact.display_group_related_contacts(group.name)
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    db_group_related_contacts = db.get_contacts_in_group(group)
    assert sorted(ui_group_related_contacts, key=Contact.id_or_max) == sorted(db_group_related_contacts,
                                                                              key=Contact.id_or_max)
