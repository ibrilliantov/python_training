from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app


    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        self.fill_contact_fields(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_home_page()

    def fill_form_date(self, field_name, date):
        wd = self.app.wd
        if date is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(date)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def fill_contact_fields(self, contact):
        wd = self.app.wd
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home)
        self.change_field_value("work", contact.work)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.fax)
        self.change_field_value("email2", contact.fax)
        self.change_field_value("email3", contact.fax)
        self.change_field_value("homepage", contact.homepage)
        # Secondary
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.address2)
        self.change_field_value("notes", contact.address2)
        # anniversary
        self.change_field_value("ayear", contact.ayear)
        # birthday
        self.change_field_value("byear", contact.ayear)

        self.fill_form_date("aday", contact.aday)
        self.fill_form_date("amonth", contact.amonth)

        self.fill_form_date("bday", contact.bday)
        self.fill_form_date("bmonth", contact.bmonth)

    def edit_first_contact_page(self, contact):
        wd = self.app.wd
        self.open_edit_first_contact_page()
        self.fill_contact_fields(contact)
        # submit contact creation
        wd.find_element_by_name("update").click()
        self.return_home_page()

    def add_photo(self, upload):
        wd = self.app.wd
        wd.find_element_by_name("photo").click()
        wd.find_element_by_name("photo").clear()
        wd.find_element_by_name("photo").send_keys(upload)

    def open_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_edit_first_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath('//*[@id="maintable"]/tbody/tr[2]/td[8]/a/img').click()

    def return_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact checkbox
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("/html/body/div/div[4]/form[2]/div[2]/input").click()
        wd.switch_to.alert.accept()

    def open_contact_home_page(self):
        wd = self.app.wd
        # wd.get("http://localhost/addressbook/index.php")
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_home_page()
        return len(wd.find_elements_by_name("selected[]"))
