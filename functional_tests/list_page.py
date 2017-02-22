from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

from .base import wait


class ListPage(object):

    def __init__(self, test):
        self.test = test

    def get_share_box(self):
        self.test.browser.find_elements_by_css_selector(
            'input[name="sharee"]'
        )


    def get_share_list(self):
        return self.test.browser.find_elements_by_css_selector(
            '.sharee-list'
        )

    def get_list_owner(self):
        return self.test.browser.find_element_by_id('list_owner').text

    def share_list_with(self, email):
        self.get_share_box().send_keys(email)
        self.get_share_box().send_keys(keys.Keys.ENTER)
        self.test.wait_for(lambda: self.test.assertIn(
            email,
            [email for email in self.get_share_list()]
        ))


    def get_table_rows(self):
        return self.test.browser.find_elements_by_css_selector('#id_list_table tr')


    @wait
    def wait_for_row_in_list_table(self, item_text, item_number):
        row_text = '{}: {}'.format(item_number, item_text)
        rows = self.get_table_rows()
        self.test.assertIn(row_text, [row.text for row in rows])


    def get_item_input_box(self):
        return self.test.browser.find_element_by_id('id_text')

    def add_list_item(self, item_text):
        new_item_no = len(self.get_table_rows()) + 1
        self.get_item_input_box().send_keys(item_text)
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table(item_text, new_item_no)
        return self