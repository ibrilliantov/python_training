import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DBfixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
             cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
             for row in cursor:
                 (id, name, header, footer) = row
                 list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_group_by_id(self, id_in):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list WHERE group_id='%s'"
                           % id_in)
            (id, name, header, footer) = cursor.fetchone()
            group_return = Group(id=str(id), name=name, header=header, footer=footer)
        finally:
            cursor.close()
        return group_return

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
             cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
             for row in cursor:
                 (id, firstname, lastname) = row
                 list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_contact_id(self, id_in):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT id, firstname, lastname from addressbook WHERE id='%s'"
                           % id_in)
            (id, firstname, lastname) = cursor.fetchone()
            contact_return = Contact(id=str(id), firstname=firstname, lastname=lastname)
        finally:
            cursor.close()
        return contact_return

    def destroy(self):
        self.connection.close()
