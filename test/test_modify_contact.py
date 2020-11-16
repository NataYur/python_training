from model.contact import Contact


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="to_modify"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ronald", lastname="")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    app.contact.return_to_homepage()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)



# def test_modify_contact_day_month(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="to_modify"))
#     contact_data = Contact(bday="8", bmonth="January", aday="3", amonth="October")
#     app.contact.modify_first_contact(contact_data)
#     app.contact.return_to_homepage()