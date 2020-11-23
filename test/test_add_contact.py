# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Harry", middlename="J", lastname="Potter", nickname="magic", title="student",
                      company="Dumbledore", address="Privet Drive 4", homephone="2244611", mobilephone="226646",
                      workphone="464651", faxphone="515151", email="harry@magic.com", email2="ron@magic.com",
                      email3="hermione@nkjn.com", homepage="www.hogwarts.com", bday="31", bmonth="July",
                      byear="1980", aday="1", amonth="January", ayear="1100", address2="Diagon Alley",
                      secondaryphone="101010", notes="969696")
    app.contact.create(contact)
    app.contact.return_to_homepage()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     app.open_home_page()
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="", lastname="")
#     app.contact.create(contact)
#     app.contact.return_to_homepage()
#     new_contacts = app.contact.get_contact_list()
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

