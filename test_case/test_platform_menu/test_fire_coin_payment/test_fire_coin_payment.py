from py_page.home_page import Home_page
from common.log import Logger
from common.screen_shot import getScreenShot
from test_case.my_markers import *
import allure

logger = Logger().get_logger()


@allure.feature('测试火币支付页面')
class TestFireCoinPayment:
    @allure.story('测试火币支付功能')
    @allure.title('测试购买物料模型并使用火币进行支付功能')
    def test_fire_coin_payment_fun(self, base_driver):
        try:
            text = Home_page(base_driver).click_home_page_login().use_right_account_pwd_login_go_home_page().move_to_username_button().click_access_platform().click_platform_avatar().move_change_organization_ele().click_change_to_organization_316().move_to_design_design_menu(). \
                click_public_library_list().click_category_of_connecting_terminal().click_category_of_connecting_terminal_and_place_order().click_fire_coin_payment().get_fire_coin_payment_success()
            assert text == "支付成功"
        except BaseException as e:
            logger.error(f'错误信息为{e}')
            getScreenShot(base_driver, __name__)
            raise e