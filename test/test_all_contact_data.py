from model.contact import Contact


def test_contact_data_on_homepage(app, db):
    contact_data = Contact(firstname="firstname", lastname="lastname", mobilephone="+31889977", workphone="(06)44100",
                           email="email1@email.com", email3="email3@email.com", secondaryphone="45-45-45")
    for i in range(0, 2):
        app.contact.create(contact_data)
    ui_contact_list = app.contact.get_contact_list()
    db_contact_list = db.get_contact_list()
    for contact in db_contact_list:
        contact.merge_phones_like_on_homepage()
        contact.merge_emails_like_on_homepage()
    assert sorted(ui_contact_list, key=Contact.id_or_max) == sorted(db_contact_list, key=Contact.id_or_max)
