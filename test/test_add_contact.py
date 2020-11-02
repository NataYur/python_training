# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    contact_data = Contact(firstname="Harry", middlename="J", lastname="Potter", nickname="magic", title="student",
                          company="Dumbledore", address="Privet Drive 4", home="2244611", mobile="226646", work="464651",
                          fax="515151", email="harry@magic.com", email2="ron@magic.com", email3="hermione@nkjn.com",
                          homepage="www.hogwarts.com", bday="31", bmonth="July", byear="1980", aday="1",
                          amonth="January", ayear="1100", address2="Diagon Alley", phone2="101010", notes="969696")
    app.create_contact(contact_data)
    app.return_to_homepage()
    app.logout()


def test_add_empty_contact(app):
    app.open_home_page()
    app.login(username="admin", password="secret")
    contact_data = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="",
                               home="", mobile="", work="", fax="", email="", email2="", email3="", homepage="",
                               bday="", bmonth="-", byear="", aday="", amonth="-", ayear="", address2="", phone2="",
                               notes="")
    app.create_contact(contact_data)
    app.return_to_homepage()
    app.logout()

