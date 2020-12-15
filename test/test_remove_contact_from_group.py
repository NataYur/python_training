from fixture.orm import ORMFixture
from model.contact import Contact
from model.group import Group
import random


def test_remove_contact_from_group(app, db):
    if app.group.count() == 0:
        app.group.create(Group(name="group for contact"))
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="group contact"))
    group = random.choice(db.get_group_list())
    app.contact.filter_by_group(group.name)
    if not len(app.contact.get_contact_list()) > 0:
        contact_to_add = random.choice(db.get_contact_list())
        app.contact.add_contact_to_group(contact_to_add.id, group.name)
        app.contact.go_to_group_page(group.name)
    group_contact = random.choice(app.contact.get_contact_list())
    app.contact.remove_contact_from_group(group_contact.id)
    app.contact.go_to_group_page(group.name)
    ui_group_related_contacts = app.contact.get_contact_list()
    db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    db_group_related_contacts = db.get_contacts_in_group(group)
    assert sorted(ui_group_related_contacts, key=Contact.id_or_max) == sorted(db_group_related_contacts,
                                                                              key=Contact.id_or_max)


