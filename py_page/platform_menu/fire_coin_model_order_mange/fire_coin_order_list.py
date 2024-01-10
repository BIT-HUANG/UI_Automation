from py_page.base_page import BasePage
from common.log import Logger

logger = Logger().get_logger()
from py_page.home_page import Home_page
class FireCoinOrderList(BasePage):
    model_order_list_path=BasePage.get_yaml_path('fire_coin_project','model_order_list.yaml')
    def get_fire_coin_payment_success(self):
        payment_success_text=self.run_steps(self.model_order_list_path,'get_fire_coin_payment_success').text
        return payment_success_text
if __name__ == '__main__':
    text=Home_page().click_home_page_login().use_right_account_pwd_login_go_home_page().move_to_username_button().click_access_platform().click_platform_avatar().move_change_organization_ele().click_change_to_organization_316().move_to_design_design_menu().\
        click_public_library_list().click_category_of_connecting_terminal().click_category_of_connecting_terminal_and_place_order().click_fire_coin_payment().get_fire_coin_payment_success()
    assert text =="支付成功",f'断言错误，{text}不等于支付成'