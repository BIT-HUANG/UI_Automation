from py_page.home_page import Home_page
from common.log import Logger
from common.screen_shot import getScreenShot
from test_case.my_markers import *
import allure

logger = Logger().get_logger()


@allure.feature('测试支付页面')
class Test_payment_page:
    @allure.story('测试点击【提交订单】后,是否成功生成订单')
    @allure.title('测试点击【提交订单】后，跳转到支付页面，并获取支付页面的标题')
    def test_get_payment_page_title_ele(self, base_driver):
        try:
            pay_page_title = Home_page(
                base_driver).click_home_page_login().use_right_account_pwd_login_go_home_page().move_to_username_button().click_access_platform().click_platform_avatar().move_change_organization_ele().click_change_to_organization_316().move_to_purchase_menu().move_shopping_cart_and_click().click_select_all().click_go_to_result().ordinary_VAT_invoice().click_submit_order().get_payment_page_title_ele()
            assert pay_page_title == "支付页面"
        except BaseException as e:
            logger.error(f'错误信息为{e}')
            getScreenShot(base_driver, '获取错误标题页面的截图')
            raise e
    @p4
    @allure.story('测试点击【提交订单】后,并输入金额，校验能否正在支付')
    @allure.title('测试点击【提交订单】后，跳转到支付页面，输入支付金额和【正确的支付密码】，得到【支付成功的信息】')
    def test_input_password_and_amount_and_get_success_message(self, base_driver):
        try:
            message = Home_page(base_driver).click_home_page_login().use_right_account_pwd_login_go_home_page().move_to_username_button().click_access_platform().click_platform_avatar().move_change_organization_ele().click_change_to_organization_316().move_to_purchase_menu() \
                .move_shopping_cart_and_click().click_select_all().click_go_to_result().ordinary_VAT_invoice().click_submit_order().click_and_input_money().click_and_input_money().click_immediate_payment().input_payment_password().click_payment_confirm_button().get_payment_success_message()
            assert message == "订单支付成功"

        except BaseException as e:
            logger.error(f'错误信息为{e}')
            getScreenShot(base_driver, '生成订单并支付失败的截图')
            raise e
