import time

from selenium.common.exceptions import TimeoutException

from baseSelenium import BaseSelenium
import semver


class DashboardPage(BaseSelenium):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.check_server_package_name_id = "enterpriseLabel"
        self.check_current_package_version_id = "currentVersion"
        self.check_current_username_id = "//li[@id='userBar']//span[@class='toggle']"
        self.check_current_db_id = "//li[@id='dbStatus']/a[@class='state']"
        self.check_db_status_id = "//li[@id='healthStatus']/a[.='GOOD']"
        self.check_cluster_status_id = '//*[@id="healthStatus"]/a[2]'
        self.check_db_engine_id = "nodeattribute-Engine"
        self.check_db_uptime_id = "/html//div[@id='nodeattribute-Uptime']"
        self.check_system_resource_id = "system-statistics"
        self.check_system_metrics_id = "metrics-statistics"
        self.select_reload_btn_id = "reloadMetrics"
        self.metrics_download_id = "downloadAs"
        self.click_twitter_link_id = "//*[@id='navigationBar']/div[2]/p[1]/a"
        self.click_slack_link_id = "//*[@id='navigationBar']/div[2]/p[2]/a"
        self.click_stackoverflow_link_id = "//*[@id='navigationBar']/div[2]/p[3]/a"
        self.click_google_group_link_id = "//*[@id='navigationBar']/div[2]/p[4]/a"

    # checking server package version name
    def check_server_package_name(self):
        check_server_package_name_sitem = \
            BaseSelenium.locator_finder_by_id(self, self.check_server_package_name_id)
        print("Server Package: ", check_server_package_name_sitem.text, '\n')
        time.sleep(1)

    # checking current package version from the dashboard
    def check_current_package_version(self):
        super().current_package_version()

    # checking current username from the dashboard
    def check_current_username(self):
        check_current_username_sitem = \
            BaseSelenium.locator_finder_by_xpath(self, self.check_current_username_id).text
        print("Current User: ", check_current_username_sitem)
        time.sleep(1)

    # checking current database name from the dashboard
    def check_current_db(self):
        check_current_db = BaseSelenium.locator_finder_by_xpath(self, self.check_current_db_id).text
        print("Current DB: ", check_current_db)
        time.sleep(1)

    # checking current database status from the dashboard
    def check_db_status(self):
        try:
            check_db_status = BaseSelenium.locator_finder_by_xpath(self, self.check_db_status_id).text
            print("Current Status: ", check_db_status)
            time.sleep(1)
        except TimeoutException:
            node = BaseSelenium.locator_finder_by_xpath(self, self.check_cluster_status_id).text
            print("Cluster Health: ", node)
            time.sleep(1)

    # checking current database status from the dashboard
    def check_db_engine(self):
        check_db_engine = BaseSelenium.locator_finder_by_id(self, self.check_db_engine_id).text
        print("Current Engine: ", check_db_engine)
        time.sleep(1)

    # checking current database uptime status from the dashboard
    def check_db_uptime(self):
        check_db_uptime = BaseSelenium.locator_finder_by_xpath(self, self.check_db_uptime_id).text
        print("DB Uptime: ", check_db_uptime)
        time.sleep(1)

    def check_responsiveness_for_dashboard(self):
        """Checking LOG tab causes unresponsive UI (found in 3.8 server package)"""
        super().check_ui_responsiveness()

    def check_authentication(self):
        """This method will check for any authentication error/warning messages"""
        print('Authentication error check started \n')
        time.sleep(2)
        notification = super().handle_red_bar()
        time.sleep(3)

        if notification is not None:
            print("Warning found, Clicking on Do not show again button \n")
            button_id = '//*[@id="button3"]'
            button_id = BaseSelenium.locator_finder_by_xpath(self, button_id)
            button_id.click()

            time.sleep(3)
            print('Refreshing the page to check warning has gone for good from this page')

            dash = 'dashboard'
            dash = BaseSelenium.locator_finder_by_id(self, dash)
            dash.click()

            self.driver.refresh()
            time.sleep(5)

            print("trying to catch the warning again")
            notification = super().handle_red_bar()

            if notification is None:
                print('Warning has been gone for Good from this page.')
            else:
                raise Exception('Warning is still visible, Which is not expected.')
        print('Authentication error check completed \n')

    def check_distribution_tab(self):
        """Checking distribution tab"""
        distribution = '//*[@id="subNavigationBar"]/ul[2]/li[2]/a'
        distribution_sitem = BaseSelenium.locator_finder_by_xpath(self, distribution)
        distribution_sitem.click()
        time.sleep(3)

    def check_maintenance_tab(self):
        """Checking maintenance tab"""
        maintenance = '//*[@id="subNavigationBar"]/ul[2]/li[3]/a'
        maintenance_sitem = BaseSelenium.locator_finder_by_xpath(self, maintenance)
        maintenance_sitem.click()
        time.sleep(3)

    # checking system resource tab from the dashboard
    def check_system_resource(self):
        try:
            self.check_system_resource_id = BaseSelenium.locator_finder_by_id(self, self.check_system_resource_id)
            self.check_system_resource_id.click()
            time.sleep(1)
        except TimeoutException:
            print('FAIL: Could not find the system-statistics locator! \n')

    # checking system metrics tab from the dashboard
    def check_system_metrics(self):
        # if super().current_package_version() >= 3.8:
        if self.current_package_version() >= semver.VersionInfo.parse("3.8.0"):
            self.check_system_metrics_id = BaseSelenium.locator_finder_by_id(self, self.check_system_metrics_id)
            self.check_system_metrics_id.click()
            time.sleep(1)

            print("scrolling the current page \n")
            super().scroll()
            time.sleep(2)

            # toggle view text to table and vice-versa
            print("Changing metrics tab to table view \n")
            show_text = 'toggleView'
            text_view = BaseSelenium.locator_finder_by_id(self, show_text)
            text_view.click()
            time.sleep(3)

            print("Changing metrics tab to text view \n")
            table_view = BaseSelenium.locator_finder_by_id(self, show_text)
            table_view.click()
            time.sleep(3)

            # Reloading system metrics tab from the dashboard
            print("reloading metrics tab \n")
            self.select_reload_btn_id = BaseSelenium.locator_finder_by_id(self, self.select_reload_btn_id)
            self.select_reload_btn_id.click()
            time.sleep(2)

            # Downloading metrics from the dashboard
            if self.driver.name == "chrome":  # this will check browser name
                print("Downloading metrics has been disabled for the current browser \n")
            else:
                self.metrics_download_id = BaseSelenium.locator_finder_by_id(self, self.metrics_download_id)
                self.metrics_download_id.click()
                time.sleep(3)
                # self.clear_download_bar()
        else:
            print('Metrics Tab not supported for the current package \n')

    # Clicking on twitter link on dashboard
    def click_twitter_link(self):
        self.click_twitter_link_id = \
            BaseSelenium.locator_finder_by_xpath(self, self.click_twitter_link_id)
        title = self.switch_tab(self.click_twitter_link_id)  # this method will call switch tab and close tab
        expected_title = "arangodb (@arangodb) / Twitter"
        assert title in expected_title, f"Expected page title {expected_title} but got {title}"

    # Clicking on twitter link on dashboard
    def click_slack_link(self):
        self.click_slack_link_id = \
            BaseSelenium.locator_finder_by_xpath(self, self.click_slack_link_id)
        title = self.switch_tab(self.click_slack_link_id)
        expected_title = 'Join ArangoDB Community on Slack!'
        assert title in expected_title, f"Expected page title {expected_title} but got {title}"

    # Clicking on stack overflow link on dashboard
    def click_stackoverflow_link(self):
        self.click_stackoverflow_link_id = \
            BaseSelenium.locator_finder_by_xpath(self, self.click_stackoverflow_link_id)
        title = self.switch_tab(self.click_stackoverflow_link_id)
        expected_title = "Newest 'arangodb' Questions - Stack Overflow"
        assert title in expected_title, f"Expected page title {expected_title} but got {title}"

    # Clicking on Google group link on dashboard
    def click_google_group_link(self):
        self.click_google_group_link_id = \
            BaseSelenium.locator_finder_by_xpath(self, self.click_google_group_link_id)
        title = self.switch_tab(self.click_google_group_link_id)
        expected_title = "ArangoDB - Google Groups"
        assert title in expected_title, f"Expected page title {expected_title} but got {title}"
