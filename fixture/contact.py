from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len( wd.find_elements_by_link_text("add new")) > 0):
            wd.find_element_by_link_text("home").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, group):
        wd = self.app.wd
        self.change_field_value("firstname", group.firstname)
        self.change_field_value("middlename", group.middlename)
        self.change_field_value("lastname", group.lastname)
        self.change_field_value ("nickname", group.nickname)
        self.change_field_value ("title", group.title)
        self.change_field_value ("company", group.company)
        self.change_field_value ("address", group.address)
        self.change_field_value ("home" ,group.home)
        self.change_field_value ("mobile", group.mobile)
        self.change_field_value ("work", group.work)
        self.change_field_value ("fax", group.fax)
        self.change_field_value ("email", group.email)
        self.change_field_value ("email2", group.email2)
        self.change_field_value ("email3", group.email3)
        self.change_field_value ("homepage", group.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(group.bday)
        wd.find_element_by_xpath("//option[@value='18']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(group.bmonth)
        wd.find_element_by_xpath("//option[@value='November']").click()
        self.change_field_value ("byear", group.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(group.aday)
        wd.find_element_by_xpath("(//option[@value='18'])[2]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(group.amonth)
        wd.find_element_by_xpath("(//option[@value='October'])[2]").click()
        self.change_field_value ("ayear", group.ayear)
        self.change_field_value ("address2", group.address2)
        self.change_field_value ("phone2", group.phone2)
        self.change_field_value ("notes", group.notes)

    def create(self, group):
        self.return_to_home_page()
        wd = self.app.wd
        # init new contact
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(group)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()

    def change_first_contact(self, group):
        wd = self.app.wd
        self.return_to_home_page()
        self.select_first_contact()
        # select edit contact
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(group)
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))
