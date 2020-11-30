import json
import calendar
from model.contact import Contact
import random
import string
import os.path
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
    for i in range(n)
]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))