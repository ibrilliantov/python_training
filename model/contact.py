from sys import maxsize


class Contact:
    def __init__(self, middlename=None, firstname=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, homephone=None, workphone=None, mobilephone=None, fax=None, email=None, email2=None, email3=None, homepage=None,
                 address2=None, secondaryphone=None, notes=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None, id=None,
                 all_phones_from_homepage=None, all_emails_from_homepage=None, fullname=None):
        self.all_phones_from_homepage = all_phones_from_homepage
        self.all_emails_from_homepage = all_emails_from_homepage
        self.fullname = fullname
        self.middlename = middlename
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.workphone = workphone
        self.mobilephone = mobilephone
        self.fax = fax
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.address2 = address2
        self.secondaryphone = secondaryphone
        self.notes = notes
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and (self.firstname is None or other.firstname is None or self.firstname == other.firstname) \
               and (self.lastname is None or other.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


