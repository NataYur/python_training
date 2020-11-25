# -*- coding: utf-8 -*-
import random
import string
import pytest
import calendar
from model.contact import Contact


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_string_year():
    return str(random.randrange(1900, 2021))


def random_string_month():
    return calendar.month_name[random.randrange(1, 13)]


def random_string_day():
    return str(random.randrange(1, 32))


testdata = [Contact(firstname="", lastname="")] + [
    Contact(firstname=random_string("firstname", 15), middlename=random_string("middlename", 10),
            lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
            title=random_string("title", 15), company=random_string("company", 15), address=random_string("address", 10),
            homephone="2244611", mobilephone="226646", workphone="464651", faxphone="515151", email="harry@magic.com",
            email2="ron@magic.com", email3="hermione@nkjn.com", homepage="www.hogwarts.com", bday=random_string_day(),
            bmonth=random_string_month(), byear=random_string_year(), aday=random_string_day(),
            amonth=random_string_month(), ayear=random_string_year(), address2=random_string("address2", 10),
            secondaryphone="101010", notes=random_string("notes", 10))
    for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    app.contact.return_to_homepage()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)