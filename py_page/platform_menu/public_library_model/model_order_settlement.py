from py_page.base_page import BasePage
from common.log import Logger

logger = Logger().get_logger()
from py_page.home_page import Home_page
class ModelOrderSettlement(BasePage):
    model_order_settlement_yamp_path=BasePage.get_yaml_path('platform_menu','model_order_settlement.yaml')
    def click_fire_coin_payment(self):
        self.run_steps(self.model_order_settlement_yamp_path,'click_fire_coin_payment')
        from py_page.platform_menu.fire_coin_model_order_mange.fire_coin_order_list import FireCoinOrderList
        return FireCoinOrderList(self.driver)
if __name__ == '__main__':
    Home_page().click_home_page_login().use_right_account_pwd_login_go_home_page().move_to_username_button().click_access_platform().click_platform_avatar().move_change_organization_ele().click_change_to_organization_316().move_to_design_design_menu().\
        click_public_library_list().click_category_of_connecting_terminal().click_category_of_connecting_terminal_and_place_order().click_fire_coin_payment()