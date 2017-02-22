class MyListPage(object):

    def __init__(self, test):
        self.test = test

    def check_if_list_is_shared(self, list_name):
        self.test.assertIn(
            list_name,
            self.get_shared_lists()
        )

    def get_shared_lists(self):
        return self.test.browser.find_element_by_id('shared-lists')
