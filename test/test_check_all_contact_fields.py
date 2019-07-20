import re
from random import randrange
from model.contact import Contact


def test_check_all_contact_fields(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middlename="Iromman", firstname="Tony", lastname="Stark", nickname="ttt", title="WOW",
            company="StarkInc", address="www", homephone="123", workphone="234", mobilephone="567",
            fax="123", email="one@home.com", email2="two@home.com", email3="three@home.com",
            homepage="ewew", address2="leningrad", secondaryphone="890", notes="what?", aday="5",
            amonth="March", ayear="1987", bday="5", bmonth="March", byear="1987"))
    contacts_list = app.contact.get_contact_list()
    index = randrange(len(contacts_list))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_homepage == merge_email_like_on_homepage(contact_from_edit_page)


def merge_email_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.email, contact.email2, contact.email3]))))

def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def clear(s):
    return re.sub("[() -]", "", s)


