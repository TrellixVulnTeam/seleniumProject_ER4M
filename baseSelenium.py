import os
import time
import semver

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from webdriver_manager.utils import ChromeType


class BaseSelenium:
    browser_name = None
    deployment = None
    mode = None
    driver: WebDriver

    def __init__(self):
        self.locator = None
        self.select = None

    @classmethod
    def set_up_class(cls):
        """This method will be used for the basic driver setup"""

        deployment_list = ['1 = Single', '2 = AFO', '3 = CL', '4 = DC2DC']
        browser_list = ['1 = Chrome', '2 = Firefox', '3 = Edge', '4 = Chromium']
        deployment_mode = ['1 = Normal Mode', '2 = Headless Mode']

        print(*deployment_list, sep="\n")

        while cls.deployment not in {1, 2, 3, 4}:
            cls.deployment = int(input('Choose your deployment: '))

            if cls.deployment == 1:
                print("You have chosen: Single deployment \n")
            elif cls.deployment == 2:
                print("You have chosen: AFO deployment \n")
            elif cls.deployment == 3:
                print("You have chosen: CL deployment \n")
            elif cls.deployment == 4:
                print("You have chosen: DC2DC deployment \n")
            else:
                print("Kindly provide a specific deployment name from the list. \n")

        print(*deployment_mode, sep="\n")
        while cls.mode not in {1, 2}:
            cls.mode = int(input('Choose your browser deployment mode: '))
            if cls.mode == 1:
                print("You have chosen: Normal Mode \n")
            elif cls.mode == 2:
                print("You have chosen: Headless Mode \n")

        print(*browser_list, sep="\n")
        while cls.browser_name not in {1, 2, 3, 4}:
            cls.browser_name = int(input('Choose your browser: '))

            if cls.browser_name == 1 and cls.mode == 1:
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument("--disable-notifications")
                print("You have chosen: Chrome browser \n")
                cls.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

            elif cls.browser_name == 1 and cls.mode == 2:
                user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
                             "Chrome/91.0.4472.124 Safari/537.36 "
                options = webdriver.ChromeOptions()
                options.headless = True
                options.add_argument(f'user-agent={user_agent}')
                options.add_argument("--window-size=1920,1080")
                options.add_argument('--ignore-certificate-errors')
                options.add_argument('--allow-running-insecure-content')
                options.add_argument("--disable-extensions")
                options.add_argument("--proxy-server='direct://'")
                options.add_argument("--proxy-bypass-list=*")
                options.add_argument("--start-maximized")
                options.add_argument('--disable-gpu')
                options.add_argument('--disable-dev-shm-usage')
                options.add_argument('--no-sandbox')
                cls.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

            elif cls.browser_name == 2:
                print("You have chosen: Firefox browser \n")

                # This preference will disappear download bar for firefox
                profile = webdriver.FirefoxProfile()
                profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/json, text/csv")  # mime
                profile.set_preference("browser.download.manager.showWhenStarting", False)
                profile.set_preference("browser.download.dir", "C:\\Users\\rearf\\Downloads")
                profile.set_preference("browser.download.folderList", 2)
                profile.set_preference("pdfjs.disabled", True)

                cls.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=profile)

            elif cls.browser_name == 3:
                print("You have chosen: Edge browser \n")
                cls.driver = webdriver.Edge(EdgeChromiumDriverManager().install())
            elif cls.browser_name == 4:
                print("You have chosen: Chromium browser \n")
                cls.driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
            else:
                print("Kindly provide a specific browser name from the list. \n")

        cls.driver.set_window_size(1250, 1000)  # custom window size

        # This check the deployment and navigate the browser url accordingly
        if cls.deployment == 2:
            try:
                cls.driver.get("http://127.0.0.1:8529/_db/_system/_admin/aardvark/index.html#login")
                error = '/html/body/pre'
                error = BaseSelenium.locator_finder_by_xpath(cls, error)

                expected_text = '{"error":true,"errorNum":1496,"errorMessage":"not a leader","code":503}'
                if expected_text == error.text:
                    print('http://127.0.0.1:8529/ is not the leader moving on..\n')
                    time.sleep(3)
                    try:
                        cls.driver.get("http://127.0.0.1:8539/_db/_system/_admin/aardvark/index.html#login")
                        error01 = '/html/body/pre'
                        error01 = BaseSelenium.locator_finder_by_xpath(cls, error01)
                        if expected_text == error01.text:
                            print('http://127.0.0.1:8539/ is not the leader moving on..\n')
                            time.sleep(3)
                            try:
                                cls.driver.get("http://127.0.0.1:8549/_db/_system/_admin/aardvark/index.html#login")
                            except TimeoutException:
                                print('Error occurred!')
                        else:
                            print("Found the leader!")
                    except TimeoutException:
                        print('Error occurred!')
                else:
                    print("Found the leader!")
            except TimeoutException:
                raise Exception("No Deployment found!")
        else:
            cls.driver.get("http://127.0.0.1:8529/_db/_system/_admin/aardvark/index.html#login")

        return cls.deployment

    @classmethod
    def tear_down(cls):
        """This method will be used for teardown the driver instance"""
        time.sleep(5)
        cls.driver.close()
        print("\n--------Now Quiting--------\n")
        cls.driver.quit()

    @staticmethod
    def command(cmd):
        """This method will be used for executing console command"""
        os.system(cmd)

    def send_key_action(self, key):
        """This method will send dummy data to the textfield as necessary"""
        actions = ActionChains(self.driver)
        actions.send_keys(key)
        actions.perform()

    def switch_to_iframe(self, iframe_id):
        """This method will switch to IFrame window"""
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, iframe_id))
        time.sleep(1)

    def switch_back_to_origin_window(self):
        """This method will switch back to origin window"""
        self.driver.switch_to.default_content()
        time.sleep(1)

    def clear_all_text(self, locator=None):
        """This method will select all text and clean it"""
        if locator is not None:
            locator = locator
            locator = BaseSelenium.locator_finder_by_xpath(self, locator)

        print("Cleaning input field \n")
        actions = ActionChains(self.driver)
        actions.click(locator)
        actions.key_down(Keys.CONTROL)
        actions.send_keys('a')
        actions.send_keys(Keys.DELETE)
        actions.key_up(Keys.CONTROL)
        actions.perform()

    # checking current package version from the dashboard
    def current_package_version(self):
        """checking current package version from the dashboard"""
        package_version = "currentVersion"
        package_version = BaseSelenium.locator_finder_by_id(self, package_version).text
        print("Package Version: ", package_version)
        return semver.VersionInfo.parse(package_version)

    def check_version_is_newer(self, compare_version):
        """ check whether the version in the ui is the expected """
        ui_version_str = self.locator_finder_by_id("currentVersion").text
        print("Package Version: ", ui_version_str)
        ui_version = semver.VersionInfo.parse(ui_version_str)
        compare_version = semver.VersionInfo.parse(compare_version)
        return ui_version >= compare_version

    def check_ui_responsiveness(self):
        """Checking LOG tab causes unresponsive UI (found in 3.8 server package)"""
        print('\n')
        print("Checking UI responsiveness \n")
        print("Clicking on Log tab \n")
        log = "logs"
        log = BaseSelenium.locator_finder_by_id(self, log)
        log.click()

        print("Try to tap on Log Level drop down button \n")
        log_level = 'logLevelSelection'
        log_level = BaseSelenium.locator_finder_by_id(self, log_level)
        log_level.click()

        time.sleep(3)

        print("Close the Log Level button \n")
        log_level01 = 'closeFilter'
        log_level01 = BaseSelenium.locator_finder_by_id(self, log_level01)
        log_level01.click()

        print("Quickly tap on to Collection Tab")
        collection = "collections"
        collection = BaseSelenium.locator_finder_by_id(self, collection)
        collection.click()

        print("Waiting for few seconds \n")
        time.sleep(3)

        print("Return back to Log tab again \n")
        log01 = "logs"
        log01 = BaseSelenium.locator_finder_by_id(self, log01)
        log01.click()

        print("Trying to tap on Log Level once again \n")
        try:
            log_level = 'logLevelSelection'
            log_level = BaseSelenium.locator_finder_by_id(self, log_level)
            log_level.click()
            assert "Level" in log_level.text, "********UI become unresponsive******"
            if log_level.text == 'Level':
                print("UI is responsive and working as usual\n")
        except TimeoutException:
            print('*' * 50)
            print("Dashboard responsiveness check failed with error")
            print('*' * 50)

        time.sleep(2)
        print("UI responsiveness test completed \n")
        print("Back to Dashboard again \n")
        self.driver.refresh()
        dash = "dashboard"
        dash = BaseSelenium.locator_finder_by_id(self, dash)
        dash.click()
        time.sleep(5)

    def select_query_execution_area(self):
        """This method will select the query execution area"""
        try:
            query = '//*[@id="aqlEditor"]'
            query = \
                BaseSelenium.locator_finder_by_xpath(self, query)
            query.click()
            time.sleep(2)
        except TimeoutException:
            print("Can't find the query execution area \n")

    def query_execution_btn(self):
        """Clicking execute query button"""
        execute = 'executeQuery'
        execute = \
            BaseSelenium.locator_finder_by_id(self, execute)
        execute.click()
        time.sleep(2)

    def clear_download_bar(self):
        """This method will close the download bar from the Chrome browser"""
        pass
        # print("closing download banner from the bottom \n")
        # keyboard = Controller()
        # with keyboard.pressed(Key.ctrl):
        #     keyboard.press('j')
        #     keyboard.release('j')
        #
        # time.sleep(2)
        #
        # keyboard01 = Controller()
        # with keyboard01.pressed(Key.ctrl):
        #     keyboard01.press('w')
        #     keyboard01.release('w')

        # ActionChains(self.driver).key_down(Keys.CONTROL).send_keys("j").key_up(Keys.CONTROL).perform()
        # ActionChains(self.driver).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()

        # locator = '//*[@id="healthStatus"]/a[1]'
        # locator = BaseSelenium.locator_finder_by_xpath(self, locator)

        # actions = ActionChains(self.driver)
        # actions.click(locator)
        # actions.key_down(Keys.CONTROL)
        # actions.send_keys('j')
        # actions.key_up(Keys.CONTROL)
        #
        # actions.send_keys('w')
        # actions.perform()
        # time.sleep(5)

    # def handle_red_bar(self):
    #     """It will check for any red bar error notification"""
    #     try:
    #         notification = 'noty_body'
    #         notification = (BaseSelenium.locator_finder_by_class(self, notification))
    #         time.sleep(2)
    #         print("*" * 100)
    #         print(notification.text)
    #         print("*" * 100)
    #         # notification.click()
    #         return True, notification.text
    #     except TimeoutException:
    #         return False, ""

    def handle_red_bar(self):
        """It will check for any red bar error notification"""
        try:
            notification = 'noty_body'
            notification = (BaseSelenium.locator_finder_by_class(self, notification))
            time.sleep(2)
            print("*" * 100)
            print(notification.text)
            print("*" * 100)
            return notification.text
        except TimeoutException:
            print('No error/warning found!')
            return None

    def assert_ui_error(self, errormessage=None):
        """This method will assert the proper error"""
        ret = self.handle_red_bar()
        if not ret[0]:
            raise Exception("Expected UI error message '" + errormessage + "' but got none!")
        if not ret[1].find(errormessage=None):
            raise Exception("Expected to find the error message " + errormessage + " but only got " + ret[1] + "' !")

    def assert_no_error(self):
        ret = self.handle_red_bar()
        if ret[0]:
            raise Exception("unexpected UI error message: " + ret[1])

    def switch_tab(self, locator):
        """This method will change tab and close it and finally return to origin tab"""
        self.locator = locator
        self.locator.send_keys(Keys.CONTROL, Keys.RETURN)  # this will open new tab on top of current
        self.driver.switch_to.window(self.driver.window_handles[1])  # switch to new tab according to index value
        title = self.driver.title
        # print(title)
        time.sleep(5)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
        return title

    def scroll(self, down=0):
        """This method will be used to scroll up and down to any page"""
        self.driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.END)

        if down == 1:
            print("")
            time.sleep(3)
        else:
            time.sleep(5)
            self.driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.HOME)
        # self.driver.execute_script("window.scrollTo(0,500)")

    def locator_finder_by_id(self, locator_name):
        """This method will be used for finding all the locators by their id"""
        self.locator = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.ID, locator_name))
        )
        if self.locator is None:
            print(locator_name, " locator has not found.")
        else:
            return self.locator

    def locator_finder_by_xpath(self, locator_name):
        """This method will be used for finding all the locators by their xpath"""
        self.locator = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, locator_name))
        )
        if self.locator is None:
            print("UI-Test: ", locator_name, " locator has not found.")
        else:
            return self.locator

    def locator_finder_by_link_text(self, locator_name):
        """This method will be used for finding all the locators by their xpath"""
        self.locator = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.LINK_TEXT, locator_name))
        )
        if self.locator is None:
            print("UI-Test: ", locator_name, " locator has not found.")
        else:
            return self.locator

    def locator_finder_by_select(self, locator_name, value):
        """This method will be used for finding all the locators in drop down menu with options"""
        self.select = Select(self.driver.find_element(By.ID, locator_name))
        self.select.select_by_index(value)
        if self.select is None:
            print("UI-Test: ", locator_name, " locator has not found.")
        return self.select

    def locator_finder_by_select_using_xpath(self, locator_name, value):
        """This method will be used for finding all the locators in drop down menu with options using xpath"""
        self.select = Select(self.driver.find_element(By.XPATH, locator_name))
        self.select.select_by_index(value)
        if self.select is None:
            print("UI-Test: ", locator_name, " locator has not found.")
        return self.select

    def locator_finder_by_hover_item_id(self, locator):
        """This method will be used for finding all the locators and hover the mouse by id"""
        item = self.driver.find_element(By.ID, locator)
        action = ActionChains(self.driver)
        action.move_to_element(item).click().perform()
        time.sleep(1)
        return action

    def locator_finder_by_class(self, locator_name):
        """This method will be used for finding all the locators by their id"""
        self.locator = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CLASS_NAME, locator_name))
        )
        if self.locator is None:
            print(locator_name, " locator has not found.")
        else:
            return self.locator

    def check_expected_error_messages_for_analyzer(self,
                                                   error_input,
                                                   print_statement,
                                                   error_message,
                                                   locators_id,
                                                   error_message_id,
                                                   div_id):
        """This method will take three lists and check for expected error condition against user's inputs"""
        i = 0
        # looping through all the error scenario for test
        # print('len: ', len(name_error))
        while i < len(error_input):  # error_input list will hold a list of error inputs from the users
            print(print_statement[i])  # print_statement will hold a list of all general print statements for the test
            locators = locators_id  # locator id of the input placeholder where testing will take place
            if div_id is not None:
                locator_sitem = BaseSelenium.locator_finder_by_xpath(self, locators)
            else:
                locator_sitem = BaseSelenium.locator_finder_by_id(self, locators)

            locator_sitem.click()
            locator_sitem.clear()
            locator_sitem.send_keys(error_input[i])
            time.sleep(2)
            locator_sitem.send_keys(Keys.TAB)
            time.sleep(2)

            if div_id is not None:
                create_btn = f'/html/body/div[{div_id}]/div/div[3]/button[2]'
                create_btn_sitem = BaseSelenium.locator_finder_by_xpath(self, create_btn)
                create_btn_sitem.click()
                time.sleep(2)

            try:
                # placeholder's error message id
                error_sitem = BaseSelenium.locator_finder_by_xpath(self, error_message_id).text
                # error_message list will hold expected error messages
                assert error_sitem == error_message[i], \
                    f"FAIL: Expected error message {error_message[i]} but got {error_sitem}"

                print('x' * (len(error_sitem) + 23))
                print('OK: Expected error found: ', error_sitem)
                print('x' * (len(error_sitem) + 23), '\n')
                time.sleep(2)

            except TimeoutException:
                raise Exception('*****-->Error occurred. Manual inspection required<--***** \n')

            i = i + 1

    def check_expected_error_messages_for_database(self,
                                                   error_input,
                                                   print_statement,
                                                   error_message,
                                                   locators_id,
                                                   error_message_id,
                                                   value=False):
        """This method will take three lists and check for expected error condition against user's inputs"""
        # value represent true because cluster rf and write concern has different way to catch the error
        i = 0
        # looping through all the error scenario for test
        while i < len(error_input):  # error_input list will hold a list of error inputs from the users
            print(print_statement[i])  # print_statement will hold a list of all general print statements for the test
            locators = locators_id  # locator id of the input placeholder where testing will take place
            locator_sitem = BaseSelenium.locator_finder_by_id(self, locators)

            locator_sitem.click()
            locator_sitem.clear()
            locator_sitem.send_keys(error_input[i])
            time.sleep(2)

            if semver.VersionInfo.parse("3.8.0") <= self.current_package_version() \
                    <= semver.VersionInfo.parse("3.8.100"):
                locator_sitem.send_keys(Keys.TAB)
                time.sleep(2)
            try:
                # trying to create the db
                if value is False and self.current_package_version() >= semver.VersionInfo.parse("3.9.0"):
                    BaseSelenium.locator_finder_by_xpath(self, '//*[@id="modalButton1"]').click()
                    time.sleep(2)
                    # placeholder's error message id
                    error_sitem = BaseSelenium.locator_finder_by_xpath(self, error_message_id).text
                elif value is False and self.current_package_version() == semver.VersionInfo.parse("3.8.0"):
                    error_sitem = BaseSelenium.locator_finder_by_xpath(self, error_message_id).text
                else:
                    error_sitem = self.locator_finder_by_xpath(error_message_id).text

                # error_message list will hold expected error messages
                assert error_sitem == error_message[i], \
                    f"FAIL: Expected error message {error_message[i]} but got {error_sitem}"

                print('x' * (len(error_sitem) + 29))
                print('OK: Expected error found: ', error_sitem)
                print('x' * (len(error_sitem) + 29), '\n')
                time.sleep(2)

                # getting out from the db creation for the next check
                if value is False and self.current_package_version() == semver.VersionInfo.parse("3.9.0"):
                    self.driver.refresh()
                    BaseSelenium.locator_finder_by_id(self, 'createDatabase').click()
                    time.sleep(1)

            except TimeoutException:
                raise Exception('*****-->Error occurred. Manual inspection required<--***** \n')

            i = i + 1

    def check_expected_error_messages_for_views(self,
                                                error_input,
                                                print_statement,
                                                error_message,
                                                locators_id,
                                                error_message_id):
        """This method will take three lists and check for expected error condition against user's inputs"""
        # looping through all the error scenario for test
        i = 0
        while i < len(error_input):  # error_input list will hold a list of error inputs from the users
            print(print_statement[i])  # print_statement will hold a list of all general print statements for the test
            # locator id of the input placeholder where testing will take place
            locator_sitem = self.locator_finder_by_xpath(locators_id)
            locator_sitem.click()
            locator_sitem.clear()
            locator_sitem.send_keys(error_input[i])
            time.sleep(2)

            if self.current_package_version() >= semver.VersionInfo.parse("3.8.0"):
                locator_sitem.send_keys(Keys.TAB)
                time.sleep(2)
            try:
                # trying to create the views
                error_sitem = self.locator_finder_by_xpath(error_message_id).text

                # error_message list will hold expected error messages
                assert error_sitem == error_message[i], \
                    f"FAIL: Expected error message {error_message[i]} but got {error_sitem}"

                print('x' * (len(error_sitem) + 29))
                print('OK: Expected error found: ', error_sitem)
                print('x' * (len(error_sitem) + 29), '\n')
                time.sleep(2)

            except TimeoutException:
                raise Exception('*****-->Error occurred. Manual inspection required<--***** \n')

            i = i + 1

    def check_server_package(self):
        """This will determine the current server package type"""
        try:
            package = BaseSelenium.locator_finder_by_id(self, 'communityLabel').text
            return package
        except TimeoutException:
            print('This is not a Community server package.\n')

        try:
            package = BaseSelenium.locator_finder_by_id(self, 'enterpriseLabel').text
            return package
        except TimeoutException:
            print('This is not a Enterprise server package.\n')

    def zoom(self):
        """This method will be used for zoom in/out on any perspective window"""
        print("zooming in now\n")
        self.driver.execute_script("document.body.style.zoom='80%'")

    def locator_finder_by_hover_item(self, locator):
        """This method will be used for finding all the locators and hover the mouse by xpath"""
        item = self.driver.find_element(By.XPATH, locator)
        action = ActionChains(self.driver)
        action.move_to_element(item).click().perform()
        time.sleep(1)
        return action

    def locator_finder_by_css_selectors(self, locator_name):
        """This method will be used for finding all the locators text using CSS Selector"""
        self.locator = WebDriverWait(self.driver, 10).until(
            ec.element_to_be_clickable((By.CSS_SELECTOR, locator_name))
        )
        self.locator = self.locator.text
        if self.locator is None:
            print("UI-Test: ", locator_name, " locator has not found.")
        else:
            return self.locator
