import time

from selenium.common.exceptions import TimeoutException
from baseSelenium import BaseSelenium


class UserPage(BaseSelenium):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.select_user_tab_id = "users"
        self.add_new_user_id = "createUser"
        self.enter_new_user_name_id = "newUsername"
        self.enter_new_name_id = "newName"
        self.enter_new_password_id = "newPassword"
        self.create_user_btn_id = "modalButton1"
        self.selecting_user_tester_id = "tester"
        self.permission_link_id = "//*[@id='subNavigationBar']/ul[2]/li[2]/a"
        self.db_permission_read_only = "//*[@id='*-db']/div[3]/input"
        self.db_permission_read_write = '//*[@id="*-db"]/div[2]/input'
        self.saving_user_cfg_id = "modalButton3"
        self.select_user_delete_btn = "modalButton0"
        self.select_confirm_delete_btn = "modal-confirm-delete"
        self.select_collection_page_id = "collections"
        self.select_create_collection_id = "createCollection"
        self.select_new_collection_name_id = "new-collection-name"

    # selecting user tab
    def user_tab(self):
        user_tab = self.select_user_tab_id
        user_tab_sitem = BaseSelenium.locator_finder_by_id(self, user_tab)
        user_tab_sitem.click()

    # User page selecting add new user
    def add_new_user(self, tester):
        print(f"New user {tester} creation begins \n")
        new_user = self.add_new_user_id
        add_new_user_id_sitem = BaseSelenium.locator_finder_by_id(self, new_user)
        add_new_user_id_sitem.click()

        # entering new user name
        new_user_name = self.enter_new_user_name_id
        enter_new_user_name_id_sitem = BaseSelenium.locator_finder_by_id(self, new_user_name)
        enter_new_user_name_id_sitem.click()
        enter_new_user_name_id_sitem.send_keys(tester)
        time.sleep(3)

        # providing new user name
        new_name = self.enter_new_name_id
        enter_new_name_id_sitem = BaseSelenium.locator_finder_by_id(self, new_name)
        enter_new_name_id_sitem.click()
        enter_new_name_id_sitem.send_keys(tester)

        # entering new user pass
        new_password = self.enter_new_password_id
        enter_new_password_id_sitem = BaseSelenium.locator_finder_by_id(self, new_password)
        enter_new_password_id_sitem.click()
        enter_new_password_id_sitem.send_keys(tester)

        # User page selecting add new user
        create_user = self.create_user_btn_id
        create_user_btn_id_sitem = BaseSelenium.locator_finder_by_id(self, create_user)
        create_user_btn_id_sitem.click()
        time.sleep(3)
        print(f"New user {tester} creation completed \n")

    # selecting newly created user
    def selecting_user_tester(self):
        new_user = self.selecting_user_tester_id
        new_user = BaseSelenium.locator_finder_by_id(self, new_user)
        new_user.click()

    # selecting newly created user
    def selecting_permission(self):
        permission = self.permission_link_id
        permission = BaseSelenium.locator_finder_by_xpath(self, permission)
        permission.click()

    def changing_db_permission_read_only(self):
        """changing permission for the new user"""
        db_permission = self.db_permission_read_only
        db_permission = BaseSelenium.locator_finder_by_xpath(self, db_permission)
        db_permission.click()

    def changing_db_permission_read_write(self):
        """changing permission for the new user"""
        db_permission = self.db_permission_read_write
        db_permission = BaseSelenium.locator_finder_by_xpath(self, db_permission)
        db_permission.click()

    # saving new settings for new user
    def saving_user_cfg(self):
        save_button = self.saving_user_cfg_id
        save_button = BaseSelenium.locator_finder_by_id(self, save_button)
        save_button.click()
        time.sleep(3)

    def selecting_new_user(self):
        tester = '//*[@id="userManagementThumbnailsIn"]/div[3]/div/h5'
        tester = BaseSelenium.locator_finder_by_xpath(self, tester)
        tester.click()
        time.sleep(4)

    def create_sample_collection(self, test_name):
        # selecting collection tab
        try:
            collection_page = self.select_collection_page_id
            collection_page = \
                BaseSelenium.locator_finder_by_id(self, collection_page)
            collection_page.click()

            # Clicking on create new collection box
            create_collection = self.select_create_collection_id
            create_collection = \
                BaseSelenium.locator_finder_by_id(self, create_collection)
            create_collection.click()
            time.sleep(2)

            # Providing new collection name
            collection_name = self.select_new_collection_name_id
            collection_name = \
                BaseSelenium.locator_finder_by_id(self, collection_name)
            collection_name.click()
            collection_name.send_keys("testDoc")

            # creating collection by tapping on save button
            save = 'modalButton1'
            save = BaseSelenium.locator_finder_by_id(self, save)
            save.click()

            try:
                notification = 'noty_body'
                notification = (BaseSelenium.locator_finder_by_class(self, notification))
                time.sleep(1)
                expected_text = 'Collection: Collection "testDoc" successfully created.'
                assert notification.text == expected_text, f"Expected text{expected_text} but got {notification.text}"

                try:
                    print('Deleting testDoc collection \n')

                    select_test_doc_collection_id = '//*[@id="collection_testDoc"]/div/h5'
                    select_collection_settings_id = "//*[@id='subNavigationBar']/ul[2]/li[4]/a"
                    select_test_doc_collection_id = \
                        BaseSelenium.locator_finder_by_xpath(self, select_test_doc_collection_id)
                    select_test_doc_collection_id.click()

                    time.sleep(4)
                    select_test_doc_settings_id = \
                        BaseSelenium.locator_finder_by_xpath(self, select_collection_settings_id)
                    select_test_doc_settings_id.click()

                    delete_collection_id = "//*[@id='modalButton0']"
                    delete_collection_confirm_id = "//*[@id='modal-confirm-delete']"

                    delete_collection_id = \
                        BaseSelenium.locator_finder_by_xpath(self, delete_collection_id)
                    delete_collection_id.click()
                    time.sleep(4)
                    delete_collection_confirm_id = \
                        BaseSelenium.locator_finder_by_xpath(self, delete_collection_confirm_id)
                    delete_collection_confirm_id.click()

                    print('Deleting testDoc collection completed\n')
                except TimeoutException:
                    print('Deleting testDoc collection failed \n')

            except TimeoutException:
                print('FAIL: Unexpected error occurred!')

        except TimeoutException:
            if test_name == 'access':
                print("Collection creation failed, which is expected")
            if test_name == 'read/write':
                raise Exception("FAIL: Unexpected error occurred!")

    # deleting user
    def delete_user_btn(self):
        self.select_user_delete_btn = BaseSelenium.locator_finder_by_id(self, self.select_user_delete_btn)
        self.select_user_delete_btn.click()

    # confirming delete user
    def confirm_delete_btn(self):
        self.select_confirm_delete_btn = BaseSelenium.locator_finder_by_id(self, self.select_confirm_delete_btn)
        self.select_confirm_delete_btn.click()
        time.sleep(3)
