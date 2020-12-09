import random
from random import randrange

from model.contact import Contact


def test_modify_contact_firstname(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="to_modify"))
    old_contacts = db.get_contact_list()
    index = random.randrange(len(old_contacts))
    contact = Contact(firstname="modified", lastname="")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact.id, contact)
    app.contact.return_to_homepage()
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



# def test_modify_contact_day_month(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="to_modify"))
#     contact_data = Contact(bday="8", bmonth="January", aday="3", amonth="October")
#     app.contact.modify_first_contact(contact_data)
#     app.contact.return_to_homepage()