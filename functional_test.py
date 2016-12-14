from selenium import webdriver
from selenium.webdriver.common import keys
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #Edith heard there is a cool on-line to-do list app
        #She went to check the home page of that app
        self.browser.get('http://localhost:8000')

        #She noticed that both of the title and header include word "To-Do"
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #App ask her to input a to do item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        #She entered "Buy peacock feathers"
        inputbox.send_keys('Buy peacock feathers')

        #After she typed enter key, the page refreshed
        #In the to-do list table there's new item displayed as "1: Buy peacock feathers"
        inputbox.send_keys(keys.Enter)
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )
        
        #Continue to input new to-do item
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore') 


