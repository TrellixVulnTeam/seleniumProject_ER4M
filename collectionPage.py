import time
from baseSelenium import BaseSelenium
from selenium.common.exceptions import TimeoutException
import traceback


class CollectionPage(BaseSelenium):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.select_collection_page_id = "collections"
        self.select_create_collection_id = "createCollection"
        self.select_new_collection_name_id = "new-collection-name"
        self.select_collection_type_id = "new-collection-type"
        # fixme
        # self.select_advance_option_id = "/html//div[@id='accordion2']//a[@href='#collapseOne']"
        self.select_advance_option_id = '//*[@id="accordion2"]/div/div[1]/a/span[2]/b'
        self.wait_for_sync_id = "new-collection-sync"
        self.create_new_collection_btn_id = "modalButton1"
        self.select_collection_settings_id = "collectionsToggle"
        self.display_system_collection_id = "//div[@id='collectionsDropdown']" \
                                            "/ul[1]/li[2]/a/label[@class='checkbox checkboxLabel']"
        self.display_document_collection_id = "//div[@id='collectionsDropdown']" \
                                              "/ul[1]/li[3]/a/label[@class='checkbox checkboxLabel']"
        self.display_edge_collection_id = "//div[@id='collectionsDropdown']" \
                                          "/ul[1]/li[4]/a/label[@class='checkbox checkboxLabel']"
        self.select_status_loaded_id = "//div[@id='collectionsDropdown']" \
                                       "/ul[2]/li[2]/a[@href='#']/label[@class='checkbox checkboxLabel']"
        self.select_status_unloaded_id = "//div[@id='collectionsDropdown']" \
                                         "/ul[2]/li[3]/a[@href='#']/label[@class='checkbox checkboxLabel']"
        self.sort_by_name_id = '//*[@id="collectionsDropdown"]/ul[2]/li[2]/a/label/i'
        self.sort_by_type_id = '//*[@id="collectionsDropdown"]/ul[2]/li[3]/a/label/i'
        self.sort_descending_id = '//*[@id="collectionsDropdown"]/ul[2]/li[4]/a/label/i'
        self.sort_descending_id = '//*[@id="collectionsDropdown"]/ul[3]/li[4]/a/label'

        self.select_doc_collection_id = "//div[@id='collection_TestDoc']//h5[@class='collectionName']"

        self.select_upload_btn_id = "/html//a[@id='importCollection']"

        self.select_choose_file_btn_id = "/html//input[@id='importDocuments']"
        self.select_confirm_upload_btn_id = "confirmDocImport"
        self.getting_total_row_count_id = "/html//a[@id='totalDocuments']"
        self.display_document_size_id = "documentSize"
        self.move_first_page_id = "//div[@id='documentsToolbarF']/ul[@class='arango-pagination']//a[.='1']"
        self.move_second_page_id = "//div[@id='documentsToolbarF']/ul[@class='arango-pagination']//a[.='2']"

        self.select_collection_setting_id = "//div[@id='subNavigationBar']/ul[2]//a[.='Settings']"
        self.select_hand_pointer_id = "/html//a[@id='markDocuments']"

        self.row1_id = "//div[@id='docPureTable']/div[2]/div[1]"
        self.row2_id = "//div[@id='docPureTable']/div[2]/div[3]"
        self.row3_id = "//div[@id='docPureTable']/div[2]/div[5]"
        self.row4_id = "//div[@id='docPureTable']/div[2]/div[7]"
        self.move_btn_id = "/html//button[@id='moveSelected']"
        self.move_doc_textbox_id = "move-documents-to"
        self.move_confirm_btn_id = "modalButton1"
        self.select_collection_delete_btn_id = "deleteSelected"
        self.collection_delete_confirm_btn_id = "//*[@id='modalButton1']"
        self.collection_really_dlt_btn_id = "/html//button[@id='modal-confirm-delete']"
        self.select_index_menu_id = "//*[@id='subNavigationBar']/ul[2]/li[2]/a"
        self.create_new_index_btn_id = "addIndex"
        self.select_index_type_id = "newIndexType"

        self.select_geo_fields_id = "newGeoFields"
        self.select_geo_name_id = "newGeoName"
        self.select_geo_json_id = "newGeoJson"
        self.select_geo_background_id = "newGeoBackground"

        self.select_create_index_btn_id = "createIndex"

        self.select_persistent_fields_id = "newPersistentFields"
        self.select_persistent_name_id = "newPersistentName"
        self.select_persistent_unique_id = "newPersistentUnique"
        self.select_persistent_sparse_id = "newPersistentSparse"
        self.select_persistent_duplicate_id = "newPersistentDeduplicate"
        self.select_persistent_background_id = "newPersistentBackground"

        self.select_fulltext_field_id = "newFulltextFields"
        self.select_fulltext_name_id = "newFulltextName"
        self.select_fulltext_length_id = "newFulltextMinLength"
        self.select_fulltext_background_id = "newFulltextBackground"

        self.select_ttl_field_id = "newTtlFields"
        self.select_ttl_name_id = "newTtlName"
        self.select_ttl_expiry_id = "newTtlExpireAfter"
        self.select_ttl_background_id = "newTtlBackground"

        self.select_index_for_delete_id = "/html//table[@id='collectionEditIndexTable']" \
                                          "/tbody/tr[2]/th[9]/span[@title='Delete index']"
        self.select_index_confirm_delete = "indexConfirmDelete"
        self.select_info_tab_id = "//*[@id='subNavigationBar']/ul[2]/li[3]/a"

        self.select_schema_tab_id = "//*[@id='subNavigationBar']/ul[2]/li[5]/a"

        self.select_settings_tab_id = "//*[@id='subNavigationBar']/ul[2]/li[4]/a"

        # fixme found two elements with this id for the version 3.8.5e
        # self.select_settings_name_textbox_id = "change-collection-name"

        self.select_settings_name_textbox_id = '/html/body/div[2]/div/div[2]/div[2]/div/div[1]/div/' \
                                               'div[1]/table/tbody/tr[1]/th[2]/input'

        self.select_settings_wait_type_id = "change-collection-sync"
        # fixme modalbutton get changed to modalbutton5 in 3.8.5e
        # self.select_new_settings_save_btn_id = "modalButton4"
        self.select_new_settings_save_btn_id = "modalButton4"

        self.select_load_index_into_memory_id = "//*[@id='modalButton2']"
        self.select_settings_unload_btn_id = "//*[@id='modalButton3']"
        self.select_truncate_btn_id = "//*[@id='modalButton1']"
        self.select_truncate_confirm_btn_id = "//*[@id='modal-confirm-delete']"
        self.delete_collection_id = "//*[@id='modalButton0']"
        self.delete_collection_confirm_id = "//*[@id='modal-confirm-delete']"

        self.select_edge_collection_upload_id = "//*[@id='collection_TestEdge']/div/h5"
        self.select_edge_collection_id = "//*[@id='collection_TestEdge']/div/h5"
        self.select_edge_settings_id = "//*[@id='subNavigationBar']/ul[2]/li[4]/a"
        self.select_test_doc_settings_id = "//*[@id='subNavigationBar']/ul[2]/li[4]/a"

        self.select_test_doc_collection_id = "//div[@id='collection_Test']//h5[@class='collectionName']"
        self.select_collection_search_id = "//*[@id='searchInput']"

        self.select_export_doc_as_jason_id = "//*[@id='exportCollection']/span/i"
        self.select_export_doc_confirm_btn_id = "exportDocuments"

        self.select_filter_collection_id = "//*[@id='filterCollection']/span/i"
        self.select_filter_input_id = "attribute_name0"
        self.select_filter_operator_id = "operator0"
        self.select_filter_attribute_value_id = "attribute_value0"
        self.select_filter_btn_id = "//*[@id='filterSend']"
        self.select_row4_id = "//div[@id='docPureTable']/div[2]/div[5]"
        self.document_id = "document-id"
        self.select_filter_reset_btn_id = "/html//button[@id='resetView']"
        self.select_renamed_doc_collection_id = '//*[@id="collection_testDocRenamed"]/div/h5'

    # selecting collection tab
    def select_collection_page(self):
        """selecting collection tab"""
        select_collection_page_sitem = BaseSelenium.locator_finder_by_id(self, self.select_collection_page_id)
        select_collection_page_sitem.click()
        time.sleep(1)

    def select_create_collection(self):
        """Clicking on create new collection box"""
        select_create_collection_sitem = BaseSelenium.locator_finder_by_id(self, self.select_create_collection_id)
        select_create_collection_sitem.click()
        time.sleep(1)

    def select_new_collection_name(self, name):
        """Providing new collection name"""
        select_new_collection_name_sitem = BaseSelenium.locator_finder_by_id(self, self.select_new_collection_name_id)
        select_new_collection_name_sitem.click()
        select_new_collection_name_sitem.send_keys(name)
        time.sleep(1)

    def select_collection_type(self, value):
        """Selecting collection Document type where # '2' = Document, '3' = Edge"""
        BaseSelenium.locator_finder_by_select(self, self.select_collection_type_id, value)
        time.sleep(1)

    def select_number_of_shards(self, shard_value):
        """selecting number of shards for the collection"""
        shards = 'new-collection-shards'
        shards_sitem = BaseSelenium.locator_finder_by_id(self, shards)
        shards_sitem.click()
        shards_sitem.clear()
        shards_sitem.send_keys(shard_value)
        time.sleep(2)

    def select_replication_factor(self, rf_value):
        """selecting number of replication factor for the collection"""
        rf = 'new-replication-factor'
        rf_sitem = BaseSelenium.locator_finder_by_id(self, rf)
        rf_sitem.click()
        rf_sitem.clear()
        rf_sitem.send_keys(rf_value)
        time.sleep(2)

    def select_advance_option(self):
        """Selecting collection advance options"""
        select_advance_option_sitem = BaseSelenium.locator_finder_by_xpath(self, self.select_advance_option_id)
        select_advance_option_sitem.click()
        time.sleep(1)

    def wait_for_sync(self, value):
        """Selecting collection wait type where value # 0 = YES, '1' = NO"""
        BaseSelenium.locator_finder_by_select(self, self.wait_for_sync_id, value)
        time.sleep(1)

    def create_new_collection_btn(self):
        """Select create new collection button"""
        create_new_collection_btn_sitem = BaseSelenium.locator_finder_by_id(self, self.create_new_collection_btn_id)
        create_new_collection_btn_sitem.click()
        time.sleep(3)
        self.driver.refresh()

    # ------------------------------------------------------------------------------------------ #
    def create_new_collections(self, name, doc_type, cluster_status):
        print('selecting collection tab \n')
        select_collection_page_sitem = BaseSelenium.locator_finder_by_id(self, self.select_collection_page_id)
        select_collection_page_sitem.click()
        time.sleep(1)

        print('Clicking on create new collection box \n')
        select_create_collection_sitem = BaseSelenium.locator_finder_by_id(self, self.select_create_collection_id)
        select_create_collection_sitem.click()
        time.sleep(1)

        print('Selecting new collection name \n')
        select_new_collection_name_sitem = BaseSelenium.locator_finder_by_id(self, self.select_new_collection_name_id)
        select_new_collection_name_sitem.click()
        select_new_collection_name_sitem.send_keys(name)
        time.sleep(1)

        print(f'Selecting collection type for {name} \n')  # collection Document type where # '2' = Document, '3' = Edge
        BaseSelenium.locator_finder_by_select(self, self.select_collection_type_id, doc_type)
        time.sleep(1)

        if cluster_status == 3:
            print(f'selecting number of Shards for the {name} \n')
            shards = 'new-collection-shards'
            shards_sitem = BaseSelenium.locator_finder_by_id(self, shards)
            shards_sitem.click()
            shards_sitem.clear()
            shards_sitem.send_keys(9)
            time.sleep(2)

            print(f'selecting number of replication factor for {name} \n')
            rf = 'new-replication-factor'
            rf_sitem = BaseSelenium.locator_finder_by_id(self, rf)
            rf_sitem.click()
            rf_sitem.clear()
            rf_sitem.send_keys(3)
            time.sleep(2)

        print(f'Selecting collection advance options for {name} \n')
        select_advance_option_sitem = BaseSelenium.locator_finder_by_xpath(self, self.select_advance_option_id)
        select_advance_option_sitem.click()
        time.sleep(1)

        # Selecting collection wait type where value # 0 = YES, '1' = NO)
        BaseSelenium.locator_finder_by_select(self, self.wait_for_sync_id, 0)
        time.sleep(1)

        print(f'Selecting create button for {name} \n')
        create_new_collection_btn_sitem = BaseSelenium.locator_finder_by_id(self, self.create_new_collection_btn_id)
        create_new_collection_btn_sitem.click()
        time.sleep(3)
        self.driver.refresh()

        if name == 'TestDoc':
            return [name, self.select_doc_collection_id]
        elif name == 'TestEdge':
            return [name, self.select_edge_collection_id]
        elif name == 'Test':
            return [name, self.select_test_doc_collection_id]
        else:
            print('Collection is not existed!! \n')

        if cluster_status == 3:
            return ['TestDocRenamed', self.select_renamed_doc_collection_id]

    # ---------------------------------------------------------------------------#

    def checking_search_options(self, search):
        """Checking search functionality"""
        select_collection_search_sitem = BaseSelenium.locator_finder_by_xpath(self, self.select_collection_search_id)
        select_collection_search_sitem.click()
        select_collection_search_sitem.clear()
        select_collection_search_sitem.send_keys(search)
        time.sleep(2)

    def select_collection_settings(self):
        """selecting collection settings icon"""
        select_collection_settings_sitem = BaseSelenium.locator_finder_by_id(self, self.select_collection_settings_id)
        select_collection_settings_sitem.click()
        time.sleep(1)

    def display_system_collection(self):
        """Displaying system's collection"""
        display_system_collection_sitem = BaseSelenium.locator_finder_by_xpath(self, self.display_system_collection_id)
        display_system_collection_sitem.click()
        time.sleep(2)

    def display_document_collection(self):
        """Displaying Document type collection"""
        display_document_collection_sitem = \
            BaseSelenium.locator_finder_by_xpath(self, self.display_document_collection_id)
        display_document_collection_sitem.click()
        time.sleep(2)

    def display_edge_collection(self):
        """Displaying Edge type collection"""
        display_edge_collection_sitem = BaseSelenium.locator_finder_by_xpath(self, self.display_edge_collection_id)
        display_edge_collection_sitem.click()
        time.sleep(2)

    def select_status_loaded(self):
        """Displaying status loaded collection"""
        select_status_loaded_sitem = BaseSelenium.locator_finder_by_xpath(self, self.select_status_loaded_id)
        select_status_loaded_sitem.click()
        time.sleep(2)

    def select_status_unloaded(self):
        """Displaying status unloaded collection"""
        select_status_unloaded_sitem = BaseSelenium.locator_finder_by_xpath(self, self.select_status_unloaded_id)
        select_status_unloaded_sitem.click()
        time.sleep(2)

    # Sorting collection by type
    def sort_by_type(self):
        version = super().current_package_version()
        if version == 3.8:
            sort_by_type = '//*[@id="collectionsDropdown"]/ul[3]/li[3]/a/label'
            sort_by_type_sitem = BaseSelenium.locator_finder_by_xpath(self, sort_by_type)
        else:
            sort_by_type_sitem = BaseSelenium.locator_finder_by_xpath(self, self.sort_by_type_id)

        sort_by_type_sitem.click()
        time.sleep(2)

    def sort_descending(self):
        """Sorting collection by descending"""
        sort_by_descending = '//*[@id="collectionsDropdown"]/ul[3]/li[4]/a/label/i'
        version = super().current_package_version()
        if version == 3.8:
            sort_by_descending = '//*[@id="collectionsDropdown"]/ul[3]/li[4]/a/label/i'
            sort_descending_sitem = BaseSelenium.locator_finder_by_xpath(self, sort_by_descending)
        else:
            sort_descending_sitem = BaseSelenium.locator_finder_by_xpath(self, self.sort_descending_id)
        sort_descending_sitem.click()
        time.sleep(2)

    def sort_by_name(self):
        """Sorting collection by name"""
        version = super().current_package_version()
        if version == 3.8:
            name = '//*[@id="collectionsDropdown"]/ul[3]/li[2]/a/label'
            sort_by_name_sitem = BaseSelenium.locator_finder_by_xpath(self, name)
        else:
            sort_by_name_sitem = BaseSelenium.locator_finder_by_xpath(self, self.sort_by_name_id)
        sort_by_name_sitem.click()
        time.sleep(2)

    # selecting TestDoc Collection
    def select_doc_collection(self):
        print('Selecting TestDoc Collection \n')
        select_doc_collection_sitem = BaseSelenium.locator_finder_by_xpath(self, self.select_doc_collection_id)
        select_doc_collection_sitem.click()
        time.sleep(1)

    def select_upload_btn(self):
        """selecting collection upload btn"""
        select_upload_btn_sitem = BaseSelenium.locator_finder_by_xpath(self, self.select_upload_btn_id)
        select_upload_btn_sitem.click()
        time.sleep(3)

    def select_choose_file_btn(self, path):
        """This method will upload the file with the file path given"""
        select_choose_file_btn_sitem = BaseSelenium.locator_finder_by_xpath(self, self.select_choose_file_btn_id)
        time.sleep(2)
        select_choose_file_btn_sitem.send_keys(path)
        time.sleep(1)

    def select_confirm_upload_btn(self):
        """Confirm file upload btn"""
        select_confirm_upload_btn_sitem = BaseSelenium.locator_finder_by_id(self, self.select_confirm_upload_btn_id)
        select_confirm_upload_btn_sitem.click()
        time.sleep(1)

    def getting_total_row_count(self):
        """getting_total_row_count"""
        getting_total_row_count_sitem = BaseSelenium.locator_finder_by_xpath(self, self.getting_total_row_count_id)
        return getting_total_row_count_sitem.text

    # Exporting documents as JSON file from the collection
    def download_doc_as_json(self):
        if self.driver.name == "chrome":  # this will check browser name
            print("Download has been disabled for the Chrome browser \n")
        else:
            select_export_doc_as_jason_sitem = \
                BaseSelenium.locator_finder_by_xpath(self, self.select_export_doc_as_jason_id)
            select_export_doc_as_jason_sitem.click()
            time.sleep(1)
            select_export_doc_confirm_btn_sitem = \
                BaseSelenium.locator_finder_by_id(self, self.select_export_doc_confirm_btn_id)
            select_export_doc_confirm_btn_sitem.click()
            time.sleep(2)
            # super().clear_download_bar()

    # Checking Filter functionality
    def filter_documents(self, value):
        select_filter_collection_sitem = BaseSelenium.locator_finder_by_xpath(self, self.select_filter_collection_id)
        select_filter_collection_sitem.click()
        time.sleep(1)

        select_row4_sitem = BaseSelenium.locator_finder_by_xpath(self, self.select_row4_id)
        select_row4_sitem.click()
        time.sleep(1)
        document_id_sitem = BaseSelenium.locator_finder_by_id(self, self.document_id)
        string = document_id_sitem.text
        self.driver.back()
        time.sleep(1)

        select_filter_input_sitem = BaseSelenium.locator_finder_by_id(self, self.select_filter_input_id)
        select_filter_input_sitem.click()
        select_filter_input_sitem.clear()
        select_filter_input_sitem.send_keys("_id")
        time.sleep(1)

        BaseSelenium.locator_finder_by_select(self, self.select_filter_operator_id, value)
        time.sleep(1)

        select_filter_attribute_value_sitem = \
            BaseSelenium.locator_finder_by_id(self, self.select_filter_attribute_value_id)
        select_filter_attribute_value_sitem.click()
        select_filter_attribute_value_sitem.clear()
        select_filter_attribute_value_sitem.send_keys(string)
        time.sleep(1)

        select_filter_btn_sitem = BaseSelenium.locator_finder_by_xpath(self, self.select_filter_btn_id)
        select_filter_btn_sitem.click()
        time.sleep(3)

        select_filter_reset_btn_sitem = \
            BaseSelenium.locator_finder_by_xpath(self, self.select_filter_reset_btn_id)
        select_filter_reset_btn_sitem.click()
        time.sleep(2)

    def display_document_size(self, value):
        """Choose how many rows of docs will be display"""
        BaseSelenium.locator_finder_by_select(self, self.display_document_size_id, value)
        time.sleep(2)

    def traverse_search_pages(self):
        """After changing the document display size checking everything loads"""
        BaseSelenium.locator_finder_by_hover_item(self, self.move_second_page_id)
        time.sleep(2)
        BaseSelenium.locator_finder_by_hover_item(self, self.move_first_page_id)
        time.sleep(2)

    def select_hand_pointer(self):
        """Selecting Hand selection button"""
        BaseSelenium.locator_finder_by_hover_item(self, self.select_hand_pointer_id)

    def select_multiple_item(self):
        """selecting multiple document rows from the current collection"""
        time.sleep(2)
        BaseSelenium.locator_finder_by_hover_item(self, self.row1_id)
        BaseSelenium.locator_finder_by_hover_item(self, self.row2_id)
        BaseSelenium.locator_finder_by_hover_item(self, self.row3_id)
        BaseSelenium.locator_finder_by_hover_item(self, self.row4_id)
        time.sleep(1)

    def move_btn(self):
        """selecting collection move button after selecting"""
        BaseSelenium.locator_finder_by_hover_item(self, self.move_btn_id)
        time.sleep(1)

    def move_doc_textbox(self, collection):
        """selecting Collection to move the selected data"""
        move_doc_textbox_sitem = BaseSelenium.locator_finder_by_id(self, self.move_doc_textbox_id)
        move_doc_textbox_sitem.click()
        move_doc_textbox_sitem.send_keys(collection)

    def move_confirm_btn(self):
        """Confirming move data to the Collection"""
        move_confirm_btn_sitem = BaseSelenium.locator_finder_by_id(self, self.move_confirm_btn_id)
        move_confirm_btn_sitem.click()
        time.sleep(1)

    # Selecting delete button for selected data
    def select_collection_delete_btn(self):
        select_collection_delete_btn_sitem = \
            BaseSelenium.locator_finder_by_id(self, self.select_collection_delete_btn_id)
        select_collection_delete_btn_sitem.click()
        time.sleep(1)

    # Selecting delete button for selected data
    def collection_delete_confirm_btn(self):
        collection_delete_confirm_btn_sitem = \
            BaseSelenium.locator_finder_by_xpath(self, self.collection_delete_confirm_btn_id)
        collection_delete_confirm_btn_sitem.click()
        time.sleep(1)

    def collection_really_dlt_btn(self):
        """Selecting really delete button for selected data"""
        collection_really_dlt_btn_sitem = BaseSelenium.locator_finder_by_xpath(self, self.collection_really_dlt_btn_id)
        collection_really_dlt_btn_sitem.click()
        self.driver.refresh()
        time.sleep(1)

    def select_index_menu(self):
        """Selecting index menu from collection"""
        select_index_menu_sitem = BaseSelenium.locator_finder_by_xpath(self, self.select_index_menu_id)
        select_index_menu_sitem.click()
        time.sleep(1)

    def create_new_index(self, index_name, value):
        print(f"Creating {index_name} index started \n")
        create_new_index_btn_sitem = BaseSelenium.locator_finder_by_id(self, self.create_new_index_btn_id)
        create_new_index_btn_sitem.click()
        time.sleep(2)

        print(f"selecting {index_name} from the list\n")
        BaseSelenium.locator_finder_by_select(self, self.select_index_type_id, value)

        if index_name == 'Persistent':
            select_persistent_fields_sitem = \
                BaseSelenium.locator_finder_by_hover_item_id(self, self.select_persistent_fields_id)
            time.sleep(1)
            select_persistent_fields_sitem.send_keys("pfields").perform()
            select_persistent_name_sitem = \
                BaseSelenium.locator_finder_by_hover_item_id(self, self.select_persistent_name_id)
            select_persistent_name_sitem.send_keys("pname").perform()
            time.sleep(1)

            if self.deployment <= 2:
                BaseSelenium.locator_finder_by_hover_item_id(self, self.select_persistent_unique_id)

            BaseSelenium.locator_finder_by_hover_item_id(self, self.select_persistent_sparse_id)

            BaseSelenium.locator_finder_by_hover_item_id(self, self.select_persistent_duplicate_id)

            BaseSelenium.locator_finder_by_hover_item_id(self, self.select_persistent_background_id)
            time.sleep(1)

        elif index_name == 'Geo':
            select_geo_fields_sitem = BaseSelenium.locator_finder_by_hover_item_id(self, self.select_geo_fields_id)
            select_geo_fields_sitem.send_keys("gfields").perform()
            time.sleep(1)
            select_geo_name_sitem = BaseSelenium.locator_finder_by_hover_item_id(self, self.select_geo_name_id)
            select_geo_name_sitem.send_keys("gname").perform()
            time.sleep(1)

            BaseSelenium.locator_finder_by_hover_item_id(self, self.select_geo_json_id)
            time.sleep(1)
            BaseSelenium.locator_finder_by_hover_item_id(self, self.select_geo_background_id)
            time.sleep(1)

        elif index_name == 'Fulltext':
            select_fulltext_field_sitem = \
                BaseSelenium.locator_finder_by_hover_item_id(self, self.select_fulltext_field_id)
            select_fulltext_field_sitem.send_keys("ffields").perform()
            time.sleep(1)
            select_fulltext_name_sitem = \
                BaseSelenium.locator_finder_by_hover_item_id(self, self.select_fulltext_name_id)
            select_fulltext_name_sitem.send_keys("fname").perform()
            time.sleep(1)
            select_fulltext_length_sitem = \
                BaseSelenium.locator_finder_by_hover_item_id(self, self.select_fulltext_length_id)
            select_fulltext_length_sitem.send_keys(100)

            BaseSelenium.locator_finder_by_hover_item_id(self, self.select_fulltext_background_id)
            time.sleep(1)

        elif index_name == 'TTL':
            select_ttl_field_sitem = BaseSelenium.locator_finder_by_hover_item_id(self, self.select_ttl_field_id)
            select_ttl_field_sitem.send_keys("tfields").perform()
            time.sleep(1)
            select_ttl_name_sitem = BaseSelenium.locator_finder_by_hover_item_id(self, self.select_ttl_name_id)
            select_ttl_name_sitem.send_keys("tname").perform()
            time.sleep(1)
            select_ttl_expiry_sitem = BaseSelenium.locator_finder_by_hover_item_id(self, self.select_ttl_expiry_id)
            select_ttl_expiry_sitem.send_keys(1000)

            BaseSelenium.locator_finder_by_hover_item_id(self, self.select_ttl_background_id)
            time.sleep(1)

        elif index_name == 'ZKD':
            select_zkd_field_sitem = BaseSelenium.locator_finder_by_id(self, 'newZkdFields')
            select_zkd_field_sitem.click()
            select_zkd_field_sitem.clear()
            select_zkd_field_sitem.send_keys('zkdfileds')

            select_zkd_name_sitem = BaseSelenium.locator_finder_by_id(self, 'newZkdName')
            select_zkd_name_sitem.click()
            select_zkd_name_sitem.clear()
            select_zkd_name_sitem.send_keys('zkdname')

        select_create_index_btn_sitem = BaseSelenium.locator_finder_by_id(self, self.select_create_index_btn_id)
        select_create_index_btn_sitem.click()
        time.sleep(10)

        print(f"Creating {index_name} index completed \n")

    def delete_all_index(self):
        """this method will delete all the indexes one by one"""
        try:
            select_index_for_delete_sitem = BaseSelenium.locator_finder_by_xpath(self, self.select_index_for_delete_id)
            select_index_for_delete_sitem.click()
            time.sleep(2)

            select_index_confirm_delete_sitem = BaseSelenium.locator_finder_by_id(self,
                                                                                  self.select_index_confirm_delete)
            select_index_confirm_delete_sitem.click()
            self.driver.refresh()
        except TimeoutException as e:
            print('Something went wrong', e, '\n')

    def select_info_tab(self):
        """Selecting info tab from the collection submenu"""
        self.select_info_tab_id = \
            BaseSelenium.locator_finder_by_xpath(self, self.select_info_tab_id)
        self.select_info_tab_id.click()
        time.sleep(2)

    def select_schema_tab(self):
        """Selecting Schema tab from the collection submenu"""
        if super().current_package_version() >= 3.8:
            select_schema_tab_sitem = BaseSelenium.locator_finder_by_xpath(self, self.select_schema_tab_id)
            select_schema_tab_sitem.click()
            time.sleep(2)
        else:
            print('Schema check not supported for the current package version \n')
        time.sleep(2)

    def select_settings_tab(self):
        """Selecting settings tab from the collection submenu"""
        select_settings_tab_sitem = BaseSelenium.locator_finder_by_xpath(self, self.select_settings_tab_id)
        select_settings_tab_sitem.click()
        time.sleep(1)

    # Selecting settings tab from the collection submenu
    def rename_collection(self):
        select_settings_name_textbox_sitem = \
            BaseSelenium.locator_finder_by_xpath(self, self.select_settings_name_textbox_id)
        select_settings_name_textbox_sitem.click()
        select_settings_name_textbox_sitem.clear()
        select_settings_name_textbox_sitem.send_keys("testDocRenamed")
        time.sleep(1)

        BaseSelenium.locator_finder_by_select(self, self.select_settings_wait_type_id, 0)
        select_new_settings_save_btn_sitem = \
            BaseSelenium.locator_finder_by_id(self, self.select_new_settings_save_btn_id)
        select_new_settings_save_btn_sitem.click()
        time.sleep(2)
        print("Loading Index into memory\n")
        select_load_index_into_memory_sitem = \
            BaseSelenium.locator_finder_by_xpath(self, self.select_load_index_into_memory_id)
        select_load_index_into_memory_sitem.click()
        time.sleep(2)

    # # Loading and Unloading collection (deprecated)
    # def select_settings_unload_btn(self):
    #     self.select_settings_unload_btn_id = \
    #         BaseSelenium.locator_finder_by_xpath(self, self.select_settings_unload_btn_id)
    #     self.select_settings_unload_btn_id.click()
    #     time.sleep(2)

    def select_truncate_btn(self):
        """Loading and Unloading collection"""
        select_truncate_btn_sitem = BaseSelenium.locator_finder_by_xpath(self, self.select_truncate_btn_id)
        select_truncate_btn_sitem.click()
        time.sleep(1)

        select_truncate_confirm_btn_sitem = \
            BaseSelenium.locator_finder_by_xpath(self, self.select_truncate_confirm_btn_id)
        select_truncate_confirm_btn_sitem.click()
        time.sleep(2)

    def select_delete_collection(self):
        """Deleting Collection from settings tab"""
        delete_collection_sitem = BaseSelenium.locator_finder_by_xpath(self, self.delete_collection_id)
        delete_collection_sitem.click()
        time.sleep(1)

        delete_collection_confirm_sitem = BaseSelenium.locator_finder_by_xpath(self, self.delete_collection_confirm_id)
        delete_collection_confirm_sitem.click()
        time.sleep(1)

    # selecting Edge collection for data uploading
    def select_edge_collection_upload(self):
        select_edge_collection_upload_sitem = \
            BaseSelenium.locator_finder_by_xpath(self, self.select_edge_collection_upload_id)
        select_edge_collection_upload_sitem.click()
        time.sleep(1)

    # selecting TestEdge Collection
    def select_edge_collection(self):
        select_edge_collection_sitem = BaseSelenium.locator_finder_by_xpath(self, self.select_edge_collection_id)
        select_edge_collection_sitem.click()
        time.sleep(1)

        select_edge_settings_sitem = BaseSelenium.locator_finder_by_xpath(self, self.select_edge_settings_id)
        select_edge_settings_sitem.click()
        time.sleep(1)

    # selecting TestEdge Collection
    def select_test_collection(self):
        select_test_doc_collection_sitem = \
            BaseSelenium.locator_finder_by_xpath(self, self.select_test_doc_collection_id)
        select_test_doc_collection_sitem.click()
        time.sleep(2)

    def delete_collection(self, collection_name, collection_locator):
        """This method will delete all the collection"""
        print(f'Deleting {collection_name} collection started \n')
        self.select_collection_page()

        try:
            BaseSelenium.locator_finder_by_xpath(self, collection_locator).click()

            self.select_settings_tab()
            self.select_delete_collection()

            print(f'Deleting {collection_name} collection Completed \n')
            self.driver.refresh()
        except TimeoutException:
            print('TimeoutException occurred! \n')
            print('Info: Collection has already been deleted or never created. \n')
        except Exception:
            traceback.print_exc()
            raise Exception('Critical Error occurred and need manual inspection!! \n')
