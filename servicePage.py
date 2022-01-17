import time

from selenium.common.exceptions import TimeoutException

from baseSelenium import BaseSelenium
from selenium.webdriver.common.keys import Keys


class ServicePage(BaseSelenium):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.service_page = 'services'

    def select_service_page(self):
        """Selecting service page"""
        service = self.service_page
        service_sitem = BaseSelenium.locator_finder_by_id(self, service)
        service_sitem.click()
        time.sleep(2)

    def select_add_service_button(self):
        """selecting new service button"""
        add_new_service = 'addApp'
        add_new_service_stiem = BaseSelenium.locator_finder_by_id(self, add_new_service)
        add_new_service_stiem.click()
        time.sleep(2)

