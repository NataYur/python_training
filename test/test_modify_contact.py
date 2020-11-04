from model.contact import Contact


def test_modify_first_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    contact_data = Contact(firstname="Ronald", lastname="Weasley")
    app.contact.modify_first_contact(contact_data)
    app.contact.return_to_homepage()
    app.session.logout()
