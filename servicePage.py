import time
from baseSelenium import BaseSelenium


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

    def service_search_option(self, search_keyword):
        """checking service page search options"""
        search = 'foxxSearch'
        service_search_stiem = BaseSelenium.locator_finder_by_id(self, search)
        service_search_stiem.click()
        service_search_stiem.clear()
        time.sleep(2)

        print(f'Searching for {search_keyword} \n')
        service_search_stiem.send_keys(search_keyword)
        time.sleep(1)

        # checking search find the correct demo services
        if search_keyword == 'demo':
            search_item = '//*[@id="availableFoxxes"]/div[2]/div/div[1]/p[1]/span'
            expected_text = 'demo-graphql'
            demo_graphql_stiem = BaseSelenium.locator_finder_by_xpath(self, search_item)
            # print(f'{demo_graphql_stiem}')
            assert demo_graphql_stiem.text == expected_text, f"Expected text{expected_text} " \
                                                             f"but got {demo_graphql_stiem.text}"
        if search_keyword == 'tab':
            search_item = '//*[@id="availableFoxxes"]/div[7]/div/div[1]/p[1]/span'
            expected_text = 'tableau-connector'
            demo_graphql_stiem = BaseSelenium.locator_finder_by_xpath(self, search_item)
            # print(f'{demo_graphql_stiem}')
            assert demo_graphql_stiem.text == expected_text, f"Expected text{expected_text} " \
                                                             f"but got {demo_graphql_stiem.text}"
        if search_keyword == 'grafana':
            search_item = '//*[@id="availableFoxxes"]/div[3]/div/div[1]/p[1]/span'
            expected_text = 'grafana-connector'
            demo_graphql_stiem = BaseSelenium.locator_finder_by_xpath(self, search_item)
            # print(f'{demo_graphql_stiem}')
            assert demo_graphql_stiem.text == expected_text, f"Expected text{expected_text} " \
                                                             f"but got {demo_graphql_stiem.text}"

    def service_category_option(self):
        """checking service page category options"""
        category = 'categorySelection'

        print('Selecting category options \n')
        select_service_category_sitem = BaseSelenium.locator_finder_by_id(self, category)
        select_service_category_sitem.click()
        time.sleep(1)

    def service_filter_category_option(self):
        """selecting category search option"""
        filter_option = 'Category-filter'
        filter_option_stiem = BaseSelenium.locator_finder_by_xpath(self, filter_option)
        filter_option_stiem.click()
        filter_option_stiem.clear()
        time.sleep(1)

    def select_category_option_from_list(self, category):
        """checking service page category options"""
        if category == 'connector':
            print(f'Selecting {category} category from the drop-down menu \n')
            connector_name = '//*[@id="connector-option"]/span[3]'
            connector_stiem = BaseSelenium.locator_finder_by_xpath(self, connector_name)
            connector_stiem.click()
            time.sleep(1)
            connector_stiem.click()

        if category == 'service':
            print(f'Selecting {category} category from the drop-down menu \n')
            connector_name = '//*[@id="service-option"]/span[3]'
            connector_stiem = BaseSelenium.locator_finder_by_xpath(self, connector_name)
            connector_stiem.click()
            time.sleep(1)
            connector_stiem.click()

        if category == 'geo':
            print(f'Selecting {category} category from the drop-down menu \n')
            connector_name = '//*[@id="geo-option"]/span[3]'
            connector_stiem = BaseSelenium.locator_finder_by_xpath(self, connector_name)
            connector_stiem.click()
            time.sleep(1)
            connector_stiem.click()

        if category == 'demo':
            print(f'Selecting {category} category from the drop-down menu \n')
            connector_name = '//*[@id="demo-option"]/span[3]'
            connector_stiem = BaseSelenium.locator_finder_by_xpath(self, connector_name)
            connector_stiem.click()
            time.sleep(1)
            connector_stiem.click()

        if category == 'graphql':
            print(f'Selecting {category} category from the drop-down menu \n')
            connector_name = '//*[@id="graphql-option"]/span[3]'
            connector_stiem = BaseSelenium.locator_finder_by_xpath(self, connector_name)
            connector_stiem.click()
            time.sleep(1)
            connector_stiem.click()

        if category == 'prometheus':
            print(f'Selecting {category} category from the drop-down menu \n')
            connector_name = '//*[@id="prometheus-option"]/span[3]'
            connector_stiem = BaseSelenium.locator_finder_by_xpath(self, connector_name)
            connector_stiem.click()
            time.sleep(1)
            connector_stiem.click()

        if category == 'monitoring':
            print(f'Selecting {category} category from the drop-down menu \n')
            connector_name = '//*[@id="monitoring-option"]/span[3]'
            connector_stiem = BaseSelenium.locator_finder_by_xpath(self, connector_name)
            connector_stiem.click()
            time.sleep(1)
            connector_stiem.click()