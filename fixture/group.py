class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        #fill group form
        self.app.group_fill()
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        # select group
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_group_page()

    def change_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        # select group
        wd.find_element_by_name("selected[]").click()
        # edit
        wd.find_element_by_name("edit").click()
        # fill group form
        self.app.group_fill()
        # submit update
        wd.find_element_by_name("update").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
