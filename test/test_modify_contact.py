from model.contact import Contact


def test_modify_contact_firstname(app):
    app.open_home_page()
    contact_data = Contact(firstname="Ronald")
    app.contact.modify_first_contact(contact_data)
    app.contact.return_to_homepage()


def test_modify_contact_day_month(app):
    app.open_home_page()
    contact_data = Contact(bday="8", bmonth="January", aday="3", amonth="October")
    app.contact.modify_first_contact(contact_data)
    app.contact.return_to_homepage()