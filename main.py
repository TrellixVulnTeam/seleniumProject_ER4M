# import traceback

from analyzersPage import AnalyzerPage
from baseSelenium import BaseSelenium
from collectionPage import CollectionPage
from dashboardPage import DashboardPage
from databasePage import DatabasePage
from graphPage import GraphPage
from servicePage import ServicePage
from loginPage import LoginPage
from queryPage import QueryPage
from supportPage import SupportPage
from userPage import UserPage
from viewsPage import ViewsPage


# from selenium.common.exceptions import TimeoutException


class Test(BaseSelenium):
    deployment = BaseSelenium.set_up_class()

    def __init__(self):
        """initial web driver setup"""
        super().__init__()
        self.created_collections_list = []  # empty 2d list

    @staticmethod
    def teardown(collection_name_list):
        """shutdown the driver"""
        # col = CollectionPage(CollectionPage.driver)  # creating collection page object
        # try:
        #     print('Deletion for collection page Started \n')
        #     # if collection_name_list[2] == 3:
        #     #     col.delete_collection(collection_name_list[1][0][0], collection_name_list[1][0][1])
        #     # else:
        #     #     col.delete_collection("TestDocRenamed", col.select_renamed_doc_collection_id)
        #     # col.delete_collection(collection_name_list[1][1][0], collection_name_list[1][1][1])
        #     # col.delete_collection(collection_name_list[1][2][0], collection_name_list[1][2][1])
        #
        #     for name, locator in collection_name_list[1]:
        #         col.delete_collection(name, locator)
        # finally:
        #     col.delete_collection("TestDocRenamed", col.select_renamed_doc_collection_id)
        #     print('Deletion for collection page Completed \n')
        #
        # log = LoginPage(LoginPage.driver)
        # log.logout_button()
        # del col
        # del log
        print('xxxxxxxxxx', collection_name_list, 'xxxxxxxxxx')
        BaseSelenium.tear_down()

    # testing login page
    def test_login(self):
        print("Starting ", self.driver.title, "\n")
        self.login = LoginPage(self.driver)
        self.login.login('root', '')
        self.login.logout_button()
        del self.login
        return 'login'

    def test_dashboard(self):
        print("---------Checking Dashboard started--------- \n")
        self.login = LoginPage(self.driver)

        if self.deployment == 2:
            self.login.select_db_opt(0)
            self.login.select_db()
        else:
            self.login.login('root', '')
        # creating object for dashboard
        self.dash = DashboardPage(self.driver)
        self.dash.check_server_package_name()
        self.dash.check_current_package_version()
        if self.deployment == 1:
            self.dash.check_current_username()
            version = self.current_package_version()
            if version == 3.9:
                self.dash.check_db_engine()
                self.dash.check_db_uptime()

        self.dash.check_current_db()
        self.dash.check_db_status()
        if self.deployment == 3:
            print('UI Responsiveness check has been disabled for CL deployment.\n')
        else:
            self.dash.check_responsiveness_for_dashboard()
        self.dash.check_authentication()

        if self.deployment == 3:
            print('Checking distribution tab \n')
            self.dash.check_distribution_tab()
            print('Checking maintenance tab \n')
            self.dash.check_maintenance_tab()
        else:
            print("\nSwitch to System Resource tab\n")
            self.dash.check_system_resource()
            print("Switch to Metrics tab\n")
            self.dash.check_system_metrics()

        print("Opening Twitter link \n")
        self.dash.click_twitter_link()
        print("Opening Slack link \n")
        self.dash.click_slack_link()
        print("Opening Stackoverflow link \n")
        self.dash.click_stackoverflow_link()
        print("Opening Google group link \n")
        self.dash.click_google_group_link()

        if self.deployment == 1:
            self.login.logout_button()
            del self.login
        print("---------Checking Dashboard Completed--------- \n")
        return 'Dashboard'

    def test_collection(self):
        print("---------Checking Collection Begin--------- \n")
        self.login = LoginPage(self.driver)
        self.login.login('root', '')
        self.col = CollectionPage(self.driver)  # creating obj for Collection

        self.created_collections_list.append(self.col.create_new_collections('TestDoc', 0, self.deployment))
        self.created_collections_list.append(self.col.create_new_collections('TestEdge', 1, self.deployment))
        self.created_collections_list.append(self.col.create_new_collections('Test', 0, self.deployment))

        print("checking Search options\n")
        print("Searching using keyword 'Doc'\n")
        self.col.checking_search_options("Doc")
        self.driver.refresh()
        print("Searching using keyword 'Edge'\n")
        self.col.checking_search_options("Edge")
        self.driver.refresh()
        print("Searching using keyword 'test'\n")
        self.col.checking_search_options("Test")
        self.driver.refresh()

        self.col.select_collection_page()

        print("Selecting Settings\n")
        self.col.select_collection_settings()
        print("Displaying system's collection\n")
        self.col.display_system_collection()
        self.col.display_system_collection()  # Doing the reverse part
        print("Displaying Document type collection\n")
        self.col.display_document_collection()
        self.col.display_document_collection()
        print("Displaying Edge type collection\n")
        self.col.display_edge_collection()
        self.col.display_edge_collection()
        print("Displaying status loaded collection\n")
        self.col.select_status_loaded()
        self.col.select_status_loaded()
        print("Displaying status unloaded collection\n")
        self.col.select_status_unloaded()
        self.col.select_status_unloaded()
        print("Sorting collections by type\n")
        self.col.sort_by_type()
        print("Sorting collections by descending\n")
        self.col.sort_descending()
        self.col.sort_descending()
        print("Sorting collections by name\n")
        self.col.sort_by_name()

        self.col.select_edge_collection_upload()
        print("Uploading file to the collection started\n")
        self.col.select_upload_btn()
        print("Uploading json file\n")
        self.col.select_choose_file_btn('C:\\Users\\rearf\\Desktop\\collections\\edges.json')
        self.col.select_confirm_upload_btn()
        self.driver.refresh()  # in order to clear the screen before fetching data
        print("Uploading " + self.col.getting_total_row_count() + " to the collection Completed\n")
        print("Selecting size of the displayed\n")

        self.driver.back()

        self.col.select_doc_collection()
        print("Uploading file to the collection started\n")
        self.col.select_upload_btn()
        print("Uploading json file\n")
        self.col.select_choose_file_btn('C:\\Users\\rearf\\Desktop\\collections\\names_100.json')
        self.col.select_confirm_upload_btn()
        self.driver.refresh()  # in order to clear the screen before fetching data
        print("Uploading " + self.col.getting_total_row_count() + " to the collection Completed\n")
        print("Selecting size of the displayed\n")

        print("Downloading Documents as JSON file\n")
        self.col.download_doc_as_json()

        print("Filter collection by '_id'\n")
        self.col.filter_documents(3)
        self.col.filter_documents(1)
        self.col.display_document_size(2)  # choosing 50 results to display
        print("Traverse back and forth search result page 1 and 2\n")
        self.col.traverse_search_pages()
        print("Selecting hand selection button\n")
        self.col.select_hand_pointer()
        print("Select Multiple item using hand pointer\n")
        self.col.select_multiple_item()
        self.col.move_btn()
        print("Multiple data moving into test collection\n")
        self.col.move_doc_textbox('Test')
        self.col.move_confirm_btn()

        print("Deleting multiple data started\n")
        self.col.select_multiple_item()
        self.col.select_collection_delete_btn()
        self.col.collection_delete_confirm_btn()
        self.col.collection_really_dlt_btn()
        print("Deleting multiple data completed\n")

        print("Selecting Index menu\n")
        self.col.select_index_menu()
        print("Create new index\n")
        version = BaseSelenium.current_package_version(self)
        self.col.create_new_index('Persistent', 1)
        self.col.create_new_index('Geo', 2)
        self.col.create_new_index('Fulltext', 3)
        self.col.create_new_index('TTL', 4)
        if version == 3.9:
            self.col.create_new_index('ZKD', 5)
            print("Deleting all index started\n")
            for i in range(4):
                self.col.delete_all_index()
            print("Deleting all index completed\n")
        else:
            print("Deleting all index started\n")
            for i in range(3):
                self.col.delete_all_index()
            print("Deleting all index completed\n")

        print("Select Info tab\n")
        self.col.select_info_tab()
        print("Selecting Schema Tab\n")
        self.col.select_schema_tab()

        print("Select Settings tab\n")
        self.col.select_settings_tab()
        if self.deployment == 3:
            print('Rename collection is not supported in Cluster deployment thus skipped \n')
        else:
            self.col.rename_collection()  # rename collection name is not allowed on other deployment mode
            print("Loading and Unloading collection\n")
            # self.col.select_settings_unload_btn()  # might be deprecated feature
            # self.col.select_settings_unload_btn()
        self.driver.refresh()
        print("Truncate collection\n")
        self.col.select_truncate_btn()
        self.driver.refresh()

        print('Deletion for collection page started. \n')
        self.col.delete_collection("TestDoc", self.col.select_doc_collection_id)
        self.col.delete_collection("TestEdge", self.col.select_edge_collection_id)
        self.col.delete_collection("Test", self.col.select_test_doc_collection_id)
        self.col.delete_collection("TestDocRenamed", self.col.select_renamed_doc_collection_id)
        print('Deletion for collection page Completed \n')

        del self.col
        self.login.logout_button()
        del self.login
        print("---------Checking Collection Completed--------- \n")

        return 'collection', self.created_collections_list, self.deployment

    def test_views(self):
        print("---------Checking Views Begin--------- \n")
        self.login = LoginPage(self.driver)
        if self.deployment == 2:
            # self.login.select_db_opt(0)
            # self.login.select_db()
            self.login.login('root', '')
        else:
            self.login.login('root', '')
        self.views = ViewsPage(self.driver)  # creating obj for viewPage

        print("Selecting Views tab\n")
        self.views.select_views_tab()

        # checking 3.9 for improved views
        version = super().current_package_version()

        if version == 3.9:
            print('Creating improved views start here \n')
            self.views.create_improved_views('improved_arangosearch_view_01', 0)
            self.views.create_improved_views('improved_arangosearch_view_02', 1)
            print('Creating improved views completed \n')

            # Checking improved views
            self.views.checking_improved_views('improved_arangosearch_view',
                                               self.views.select_improved_arangosearch_view_01, self.deployment)

            print('Deleting views started \n')
            if self.deployment == 3:
                self.views.delete_views('improved_arangosearch_view_01',
                                        self.views.select_improved_arangosearch_view_01)
            else:
                self.views.delete_views('modified_views_name', self.views.select_modified_views_name)
            self.views.delete_views('improved_arangosearch_view_02', self.views.select_improved_arangosearch_view_02)
            print('Deleting views completed \n')

        # for package version less than 3.9
        elif version <= 3.8:
            self.views.create_new_views('firstView')
            self.views.create_new_views('secondView')

            self.views.select_views_settings()

            print("Sorting views to descending\n")
            self.views.select_sorting_views()
            print("Sorting views to ascending\n")
            self.views.select_sorting_views()

            print("search views option testing\n")
            self.views.search_views("secondView", self.views.search_second_view)
            self.views.search_views("firstView", self.views.search_first_view)

            print("Selecting first Views \n")
            self.views.select_first_view()
            print("Selecting collapse button \n")
            self.views.select_collapse_btn()
            print("Selecting expand button \n")
            self.views.select_expand_btn()
            print("Selecting editor mode \n")
            self.views.select_editor_mode_btn()
            print("Switch editor mode to Code \n")
            self.views.switch_to_code_editor_mode()
            print("Switch editor mode to Compact mode Code \n")
            self.views.compact_json_data()

            print("Selecting editor mode \n")
            self.views.select_editor_mode_btn()
            print("Switch editor mode to Tree \n")
            self.views.switch_to_tree_editor_mode()

            print("Clicking on ArangoSearch documentation link \n")
            self.views.click_arangosearch_documentation_link()
            print("Selecting search option\n")
            self.views.select_inside_search("i")
            print("Traversing all results up and down \n")
            self.views.search_result_traverse_down()
            self.views.search_result_traverse_up()

            if self.deployment == 3:
                print('View rename is disabled in Cluster mode \n')
            else:
                print("Rename firstViews to thirdViews started \n")
                self.views.clicking_rename_views_btn()
                self.views.rename_views_name("thirdView")
                self.views.rename_views_name_confirm()
                print("Rename the current Views completed \n")
            self.driver.back()

            print("Deleting views started \n")
            if self.deployment == 3:
                self.views.delete_views('first_view', self.views.select_first_view_id)
            else:
                self.views.delete_views('renamed_view', self.views.select_renamed_view_id)

            self.views.delete_views('second_view', self.views.select_second_view_id)

        print("Deleting views completed\n")
        self.login.logout_button()
        del self.login
        del self.views
        print("---------Checking Views completed--------- \n")

        return 'views'

    def test_graph(self):
        print("---------Checking Graphs started--------- \n")
        self.login = LoginPage(self.driver)
        self.login.login('root', '')

        # creating multiple graph obj
        self.graph = GraphPage(self.driver)
        self.graph1 = GraphPage(self.driver)
        self.graph2 = GraphPage(self.driver)
        self.graph3 = GraphPage(self.driver)
        self.graph4 = GraphPage(self.driver)
        self.graph5 = GraphPage(self.driver)
        self.graph6 = GraphPage(self.driver)
        self.graph7 = GraphPage(self.driver)
        self.graph8 = GraphPage(self.driver)
        self.graph9 = GraphPage(self.driver)
        self.graph01 = GraphPage(self.driver)

        # print("Manual Graph creation started \n")
        # self.graph.create_manual_graph()
        self.graph.select_graph_page()
        # self.graph.adding_knows_manual_graph()
        # print("Manual Graph creation completed \n")
        # self.graph.delete_graph(9)
        # self.driver.refresh()

        print("Adding Satellite Graph started \n")
        self.graph9.adding_satellite_graph()
        print("Adding Satellite Graph started \n")

        # print("Adding Smart Graph started \n")
        # self.graph01.adding_smart_graph()
        # print("Adding Smart Graph completed \n")
        #
        # print("Adding Disjoint Smart Graph started \n")
        # self.graph01.adding_smart_graph(True)

        # print("Example Graphs creation started\n")
        # print("Creating Knows Graph\n")
        # self.graph1.select_create_graph(1)
        # self.driver.refresh()
        # print("Checking required collections created for Knows Graph\n")
        # self.graph1.checking_collection_creation(1)
        # print("Searching for 'knows' and 'persons' collections\n")
        # self.graph1.check_required_collection(1)
        # 
        # print("Creating Traversal Graph\n")
        # self.graph2.select_create_graph(2)
        # self.driver.refresh()
        # print("Checking required collections created for Traversal Graph\n")
        # self.graph2.checking_collection_creation(2)
        # print("Searching for 'circles' and 'edges' collections\n")
        # self.graph2.check_required_collection(2)
        # 
        # print("Creating K Shortest Path Graph\n")
        # self.graph3.select_create_graph(3)
        # self.driver.refresh()
        # print("Checking required collections created for K Shortest Path Graph\n")
        # self.graph3.checking_collection_creation(3)
        # print("Searching for 'connections' and 'places' collections\n")
        # self.graph3.check_required_collection(3)
        # 
        # print("Creating Mps Graph\n")
        # self.graph4.select_create_graph(4)
        # self.driver.refresh()
        # print("Checking required collections created for Mps Graph\n")
        # self.graph4.checking_collection_creation(4)
        # print("Searching for 'mps_edges' and 'mps_verts' collections\n")
        # self.graph4.check_required_collection(4)
        # 
        # print("Creating World Graph\n")
        # self.graph5.select_create_graph(5)
        # self.driver.refresh()
        # print("Checking required collections created for World Graph\n")
        # self.graph5.checking_collection_creation(5)
        # print("Searching for 'worldEdges' and 'worldvertices' collections\n")
        # self.graph5.check_required_collection(5)
        # 
        # print("Creating Social Graph\n")
        # self.graph6.select_create_graph(6)
        # self.driver.refresh()
        # print("Checking required collections created for Social Graph\n")
        # self.graph6.checking_collection_creation(6)
        # print("Searching for 'female' , 'male' and 'relation' collections\n")
        # self.graph6.check_required_collection(6)
        # 
        # print("Creating City Graph\n")
        # self.graph7.select_create_graph(7)
        # self.driver.refresh()
        # print("Checking required collections created for City Graph\n")
        # self.graph7.checking_collection_creation(7)
        # print("Searching for 'frenchCity' , 'frenchHighway' 'germanCity', 'germanHighway' & 'internationalHighway'\n")
        # self.graph7.check_required_collection(7)
        # print("Example Graphs creation Completed\n")
        # 
        # print("Sorting all graphs as descending\n")
        # self.graph.select_sort_descend()
        # 
        # print("Selecting Knows Graph for inspection\n")
        # self.graph.inspect_knows_graph()
        # print("Selecting Graphs settings menu\n")
        # self.graph.graph_setting()
        # 
        # print("Deleting created Graphs started\n")
        # self.graph1.delete_graph(1)
        # self.graph2.delete_graph(2)
        # self.graph3.delete_graph(3)
        # self.graph4.delete_graph(4)
        # self.graph5.delete_graph(5)
        # self.graph6.delete_graph(6)
        # self.graph7.delete_graph(7)
        # 
        # # print("Deleting created Graphs Completed\n")
        # del self.graph
        # del self.graph1
        # del self.graph2
        # del self.graph3
        # del self.graph4
        # del self.graph5
        # del self.graph6
        # del self.graph7
        # del self.graph8
        # del self.graph9
        # del self.graph01
        self.login.logout_button()
        del self.login
        print("---------Checking Graphs completed--------- \n")

        return 'graph'

    # testing Service page
    def test_service(self):
        print("Starting ", self.driver.title, "\n")
        self.login = LoginPage(self.driver)
        self.login.login('root', '')

        self.service = ServicePage(self.driver)
        self.service.select_service_page()
        self.service.select_add_service_button()
        self.service.service_search_option('demo')
        self.service.service_search_option('tab')
        self.service.service_search_option('grafana')
        self.service.service_category_option()
        self.service.select_category_option_from_list('connector')
        self.service.select_category_option_from_list('service')
        self.service.select_category_option_from_list('geo')
        self.service.select_category_option_from_list('demo')
        self.service.select_category_option_from_list('graphql')
        self.service.select_category_option_from_list('prometheus')
        self.service.select_category_option_from_list('monitoring')

        self.service.select_category_option_search_filter('geo')
        self.service.select_category_option_search_filter('demo')
        self.service.select_category_option_search_filter('connector')

        self.service.setup_demo_geo_s2_service()
        self.service.install_demo_geo_s2_service('/Desktop')
        self.service.check_demo_geo_s2_service_api()
        self.service.inspect_foxx_leaflet_iframe()

        self.service.delete_service('demo_geo_s2')

        del self.login
        del self.service
        return 'service'

    def test_user(self):
        print("---------User Test Begin--------- \n")
        self.login = LoginPage(self.driver)
        self.login.login('root', '')
        self.user = UserPage(self.driver)

        self.user.user_tab()

        self.user.add_new_user('tester')

        print("Allow user Read Only access only to the _system DB test started \n")
        self.user.selecting_user_tester()
        self.user.selecting_permission()
        print("Changing new user DB permission \n")
        self.user.changing_db_permission_read_only()
        self.driver.back()
        self.user.saving_user_cfg()
        print("Changing new user DB permission completed. \n")
        self.login.logout_button()
        print("Re-Login begins with new user\n")
        self.login = LoginPage(self.driver)
        self.login.login('tester', 'tester')
        print("Re-Login begins with new user completed\n")

        print("trying to create collection")
        self.user.create_sample_collection('access')
        print("Allow user Read Only access only to the current DB test completed \n")

        print("Allow user Read/Write access to the _system DB test started \n")
        print('Return back to user tab \n')

        # logout from the current user to get back to root
        self.login.logout_button()
        del self.login
        # login back with root user
        self.login = LoginPage(self.driver)
        self.login.login('root', '')

        self.user.user_tab()
        self.user.selecting_user_tester()
        self.user.selecting_permission()
        self.user.changing_db_permission_read_write()
        self.driver.back()
        self.user.saving_user_cfg()
        self.login.logout_button()
        print("Re-Login begins with new user\n")
        self.login = LoginPage(self.driver)
        self.login.login('tester', 'tester')
        print("Re-Login begins with new user completed\n")
        print("trying to create collection")
        self.user.create_sample_collection('read/write')
        print("Allow user Read/Write access to the _system DB test Completed \n")

        # logout from the current user to get back to root
        self.login.logout_button()
        del self.login
        # login back with root user
        self.login = LoginPage(self.driver)
        self.login.login('root', '')

        del self.user
        self.user = UserPage(self.driver)
        self.user.user_tab()
        self.user.selecting_new_user()
        print("Deleting created user begins\n")
        self.user.delete_user_btn()
        self.user.confirm_delete_btn()
        print("Deleting created user completed \n")
        self.login.logout_button()
        del self.login
        print("---------User Test Completed---------\n")

    def test_database(self):
        print("---------DataBase Page Test Begin--------- \n")
        login = LoginPage(self.driver)
        login.login('root', '')

        user = UserPage(self.driver)
        user.user_tab()
        user.add_new_user('tester')
        user.add_new_user('tester01')

        db = DatabasePage(self.driver)
        db.create_new_db('Sharded', 0, self.deployment)  # 0 = sharded DB
        db.create_new_db('OneShard', 1, self.deployment)  # 1 = one shard DB

        db.test_database_expected_error(self.deployment)  # testing expected error condition for database creation

        print('Checking sorting databases to ascending and descending \n')
        db.sorting_db()

        print('Checking search database functionality \n')
        db.searching_db('Sharded')
        db.searching_db('OneShard')

        db.deleting_database('Sharded')
        db.deleting_database('OneShard')

        # need to add delete created user here
        user.user_tab()
        db.deleting_user('tester')
        db.deleting_user('tester01')

        login.logout_button()
        del user
        del db
        del login
        print("---------DataBase Page Test Completed--------- \n")

        return 'database'

    def test_analyzers(self):
        print("---------Analyzers Page Test Begin--------- \n")
        login = LoginPage(self.driver)
        login.login('root', '')
        analyzers = AnalyzerPage(self.driver)

        version = analyzers.current_package_version()
        if version >= 3.9:
            analyzers.select_analyzers_page()
            analyzers.select_help_filter_btn()

            print('Showing in-built Analyzers list \n')
            analyzers.select_built_in_analyzers_open()

            print('Checking in-built identity analyzer \n')
            analyzers.select_analyzer_to_check(analyzers.identity_analyzer, analyzers.identity_analyzer_switch_view)
            print('Checking in-built text_de analyzer \n')
            analyzers.select_analyzer_to_check(analyzers.text_de, analyzers.text_de_switch_view)
            print('Checking in-built text_en analyzer \n')
            analyzers.select_analyzer_to_check(analyzers.text_en, analyzers.text_en_switch_view)
            print('Checking in-built text_es analyzer \n')
            analyzers.select_analyzer_to_check(analyzers.text_es, analyzers.text_es_switch_view)
            print('Checking in-built text_fi analyzer \n')
            analyzers.select_analyzer_to_check(analyzers.text_fi, analyzers.text_fi_switch_view)
            print('Checking in-built text_fr analyzer \n')
            analyzers.select_analyzer_to_check(analyzers.text_fr, analyzers.text_fr_switch_view)
            print('Checking in-built text_it analyzer \n')
            analyzers.select_analyzer_to_check(analyzers.text_it, analyzers.text_it_switch_view)
            print('Checking in-built text_nl analyzer \n')
            analyzers.select_analyzer_to_check(analyzers.text_nl, analyzers.text_nl_switch_view)
            print('Checking in-built text_no analyzer \n')
            analyzers.select_analyzer_to_check(analyzers.text_no, analyzers.text_no_switch_view)
            print('Checking in-built text_pt analyzer \n')
            analyzers.select_analyzer_to_check(analyzers.text_pt, analyzers.text_pt_switch_view)
            print('Checking in-built text_ru analyzer \n')
            analyzers.select_analyzer_to_check(analyzers.text_ru, analyzers.text_ru_switch_view)
            print('Checking in-built text_sv analyzer \n')
            analyzers.select_analyzer_to_check(analyzers.text_sv, analyzers.text_sv_switch_view)
            print('Checking in-built text_zh analyzer \n')
            analyzers.select_analyzer_to_check(analyzers.text_zh, analyzers.text_zh_switch_view)

            print('Hiding in-built Analyzers list \n')
            analyzers.select_built_in_analyzers_close()

            print('Adding Identity analyzer \n')
            analyzers.add_new_analyzer('My_Identity_Analyzer', 0, 12)  # 12 represents required div_id in the method

            print('Adding Delimiter analyzer \n')
            analyzers.add_new_analyzer('My_Delimiter_Analyzer', 1, 16)

            print('Adding Stem analyzer \n')
            analyzers.add_new_analyzer('My_Stem_Analyzer', 2, 20)

            print('Adding Norm analyzer \n')
            analyzers.add_new_analyzer('My_Norm_Analyzer', 3, 24)

            print('Adding N-Gram analyzer \n')
            analyzers.add_new_analyzer('My_N-Gram_Analyzer', 4, 28)

            print('Adding Text analyzer \n')
            analyzers.add_new_analyzer('My_Text_Analyzer', 5, 32)

            print('Adding AQL analyzer \n')
            analyzers.add_new_analyzer('My_AQL_Analyzer', 6, 36)

            print('Adding Stopwords analyzer \n')
            analyzers.add_new_analyzer('My_Stopwords_Analyzer', 7, 40)

            print('Adding Collation analyzer \n')
            analyzers.add_new_analyzer('My_Collation_Analyzer', 8, 44)

            print('Adding Segmentation analyzer \n')
            analyzers.add_new_analyzer('My_Segmentation_Alpha_Analyzer', 9, 48)

            print('Adding Pipeline analyzer \n')
            analyzers.add_new_analyzer('My_Pipeline_Analyzer', 10, 52)

            print('Adding GeoJSON analyzer \n')
            analyzers.add_new_analyzer('My_GeoJSON_Analyzer', 11, 56)

            print('Adding GeoJSON analyzer \n')
            analyzers.add_new_analyzer('My_GeoPoint_Analyzer', 12, 60)

            # only going to work if and only all the possible type of analyzers are done creating
            print('Checking negative scenario for the identity analyzers name \n')
            analyzers.test_analyzer_expected_error('identity_analyzer', 0, 64)
            print('Checking negative scenario for the stem analyzers locale value \n')
            analyzers.test_analyzer_expected_error('stem_analyzer', 2, 64)
            print('Checking negative scenario for the stem analyzers locale value \n')
            analyzers.test_analyzer_expected_error('n-gram_analyzer', 4, 64)
            print('Checking negative scenario for the AQL analyzers \n')
            analyzers.test_analyzer_expected_error('AQL_analyzer', 6, 64)

            print('Checking analyzer search filter options started \n')
            analyzers.checking_search_filter_option('de')
            analyzers.checking_search_filter_option('geo', False)  # false indicating builtIn option will be disabled
            print('Checking analyzer search filter options completed \n')

            # analyzers deletion start
            analyzers.delete_analyzer('My_AQL_Analyzer')
            analyzers.delete_analyzer('My_Collation_Analyzer')
            analyzers.delete_analyzer('My_Delimiter_Analyzer')
            analyzers.delete_analyzer('My_GeoJSON_Analyzer')
            analyzers.delete_analyzer('My_GeoPoint_Analyzer')
            analyzers.delete_analyzer('My_Identity_Analyzer')
            analyzers.delete_analyzer('My_N-Gram_Analyzer')
            analyzers.delete_analyzer('My_Norm_Analyzer')
            analyzers.delete_analyzer('My_Pipeline_Analyzer')
            analyzers.delete_analyzer('My_Segmentation_Alpha_Analyzer')
            analyzers.delete_analyzer('My_Stem_Analyzer')
            analyzers.delete_analyzer('My_Stopwords_Analyzer')
            analyzers.delete_analyzer('My_Text_Analyzer')

            login.logout_button()
            del login
            del analyzers
            print("---------Analyzers Page Test Completed--------- \n")
        else:
            print("Analyzer test is not available version below 3.9.0 \n")

        return 'analyzer'

    def test_query(self):
        print("---------Query Test Begin--------- \n")
        self.login = LoginPage(self.driver)
        self.login.login('root', '')

        # creating multiple query obj
        self.query = QueryPage(self.driver)
        self.query01 = QueryPage(self.driver)

        # print("Importing IMDB collections \n")
        self.query.import_collections()

        print("Selecting Query page for basic CRUD operation \n")
        self.query.selecting_query_page()

        print("Executing insert query")
        self.query.execute_insert_query()
        print("Profiling current query \n")
        self.query.profile_query()
        print("Explaining current query \n")
        self.query.explain_query()
        print("Debug packaged downloading for the current query \n")
        self.query.debug_package_download()
        print("Removing all query results \n")
        self.query.remove_query_result()
        print("Clearing query execution area \n")
        self.query.clear_query_area()

        print("Executing spot light functionality \n")
        self.query.spot_light_function('COUNT')  # can be used for search different keyword
        print('Executing read query')
        self.query01.execute_read_query()
        print('Updating documents\n')
        self.query.update_documents()
        print('Executing query with bind parameters \n')
        self.query.bind_parameters_query()

        print("Executing example graph query \n")
        self.query.world_country_graph_query()

        print('Executing K_Shortest_Paths Graph query \n')
        self.query.k_shortest_paths_graph_query()

        print('Executing City Graph query \n')
        self.query.city_graph()

        print('Importing new queries \n')
        self.query.import_queries('C:\\Users\\rearf\\Desktop\\collections\\imported_query.json')
        print("Saving Current query as custom query\n")
        self.query.custom_query()
        print('Changing the number of results from 1000 to 100\n')
        self.query.number_of_results()

        print('Deleting collections begins \n')
        self.query.delete_all_collections()
        print('Deleting collections completed \n')

        # logging out from the current user
        self.login.logout_button()
        del self.login
        del self.query
        del self.query01
        print("---------Checking Query completed--------- \n")
        return 'query_test'

    def test_support(self):
        print("---------Checking Support page started--------- \n")
        self.login = LoginPage(self.driver)
        self.login.login('root', '')

        # creating multiple support page obj
        self.support = SupportPage(self.driver)

        print('Selecting Support Page \n')
        self.support.select_support_page()

        print('Selecting documentation tab \n')
        self.support.select_documentation_support()
        print('Checking all arangodb manual link\n')
        self.support.manual_link()
        print('Checking all AQL Query Language link\n')
        self.support.aql_query_language_link()
        print('Checking all Fox Framework link \n')
        self.support.fox_framework_link()
        print('Checking all Drivers and Integration links\n')
        self.support.driver_and_integration_link()
        print('Checking Community Support tab \n')
        self.support.community_support_link()
        print('Checking Rest API tab \n')
        self.support.rest_api()

        # logging out from the current user
        self.login.logout_button()
        del self.login
        del self.support
        print("---------Checking Support page completed--------- \n")

        return 'support'


ui = Test()  # creating obj for the UI test
# test_name = ui.test_login()  # testing Login functionality
# test_name = ui.test_dashboard()  # testing Dashboard functionality
test_name = ui.test_collection()  # testing Collection tab
# test_name = ui.test_views()  # testing views functionality
# test_name = ui.test_query()  # testing query functionality **needs cluster deployment
# test_name = ui.test_graph()  # testing graph functionality **needs cluster deployment
# test_name = ui.test_service()  # testing service page
# test_name = ui.test_database()  # testing database page
# test_name = ui.test_support()  # testing support tab functionality
# ui.test_user()  # testing User functionality
# test_name = ui.test_analyzers()  # testing analyzers page  # supports only 3.9* versions

ui.teardown(test_name)  # close the driver and quit
