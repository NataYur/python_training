import re
from random import randrange
from model.contact import Contact


def test_contact_data_on_homepage(app):
    contact_data = Contact(firstname="firstname", lastname="lastname", mobilephone="+31889977", workphone="(06)44100",
                           email="email1@email.com", email3="email3@email.com", secondaryphone="45-45-45")
    for i in range(0, 2):
        app.contact.create(contact_data)
    contact_list = app.contact.get_contact_list()
    index = randrange(len(contact_list))
    contact_data_from_homepage = contact_list[index]
    contact_data_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_data_from_homepage.firstname == contact_data_from_edit_page.firstname
    assert contact_data_from_homepage.lastname == contact_data_from_edit_page.lastname
    assert contact_data_from_homepage.address == contact_data_from_edit_page.address
    assert contact_data_from_homepage.all_phones_from_homepage == \
           merge_phones_like_on_homepage(contact_data_from_edit_page)
    assert contact_data_from_homepage.all_emails_from_homepage == \
           merge_emails_like_on_homepage(contact_data_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [contact.homephone, contact.mobilephone,
                                                                               contact.workphone,
                                                                               contact.secondaryphone]))))


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None, [contact.email, contact.email2,
                                                                                contact.email3])))