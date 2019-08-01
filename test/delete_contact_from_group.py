from model.contact import Contact
from model.group import Group
import random


def test_delete_contact_from_group(app, db, orm):
    if len(db.get_contact_list()) == 0:
        contact = (Contact(middlename="Iromman", firstname="Tony", lastname="Stark", nickname="ttt", title="WOW",
                           company="StarkInc", address="www", homephone="123", workphone="234", mobilephone="567",
                           fax="123", email="one@home.com", email2="two@home.com", email3="three@home.com",
                           homepage="ewew", address2="leningrad", secondaryphone="890", notes="what?", aday="5",
                           amonth="March", ayear="1987", bday="5", bmonth="March", byear="1987"))
        app.contact.create(contact)
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='group', header='2', footer='2'))
    id_group_list_with_contacts = db.get_contact_in_group_page()
    if len(id_group_list_with_contacts) == 0:
        id_contact = random.choice(db.get_contact_list()).id
        id_group = random.choice(db.get_group_list()).id
        app.contact.add_contact_to_group(id_group, id_contact)
        id_group_list_with_contacts.append(id_group)
    id_group = random.choice(id_group_list_with_contacts)
    id_contact = random.choice(orm.get_contacts_in_group(Group(id=id_group))).id
    app.contact.delete_contact_in_group(id_group, id_contact)
    assert db.get_contact_id(id_contact) not in orm.get_contacts_in_group(Group(id=id_group))
