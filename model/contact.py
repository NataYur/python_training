import re
from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, mobilephone=None, workphone=None, faxphone=None, email=None, email2=None,
                 email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None,
                 address2=None, secondaryphone=None, notes=None, id=None, all_phones_from_homepage=None,
                 all_emails_from_homepage=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.faxphone = faxphone
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.id = id
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage

    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname,
                                      self.address, self.all_emails_from_homepage, self.all_phones_from_homepage)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.firstname == other.firstname \
               and self.lastname == other.lastname \
               and self.address == other.address \
               and self.all_emails_from_homepage == other.all_emails_from_homepage \
               and self.all_phones_from_homepage == other.all_phones_from_homepage

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

    def merge_phones_like_on_homepage(self):
        def clear(s):
            return re.sub("[() -]", "", s)

        self.all_phones_from_homepage = "\n".join(
            filter(lambda x: x != "", map(lambda x: clear(x),
                                          filter(lambda x: x is not None, [self.homephone, self.mobilephone,
                                                                           self.workphone, self.secondaryphone]))))

    def merge_emails_like_on_homepage(self):
        self.all_emails_from_homepage = "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                                                                   [self.email, self.email2,
                                                                                    self.email3])))