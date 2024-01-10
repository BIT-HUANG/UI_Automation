from py_page.base_page import BasePage
from common.log import Logger

logger = Logger().get_logger()
from py_page.home_page import Home_page


class PublicLibraryList(BasePage):
    public_library_list_yaml_path = BasePage.get_yaml_path('fire_coin_project', 'public_library_list.yaml')

    def click_category_of_connecting_terminal(self):
        self.run_steps(self.public_library_list_yaml_path, 'click_category_of_connecting_terminal')
        return self

    def click_category_of_connecting_terminal_and_place_order(self):
        self.run_steps(self.public_library_list_yaml_path, 'click_category_of_connecting_terminal_and_place_order')
        from py_page.platform_menu.public_library_model.model_order_settlement import ModelOrderSettlement
        return ModelOrderSettlement(self.driver)
