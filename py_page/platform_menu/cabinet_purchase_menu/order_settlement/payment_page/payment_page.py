import time

from py_page.base_page import BasePage
from common.log import Logger

logger = Logger().get_logger()
from py_page.home_page import Home_page


class Payment_page(BasePage):
    payment_page = BasePage.get_yaml_path("payment_page", 'payment_page.yaml')

    def get_payment_page_title_ele(self):
        text_payment_page = self.run_steps(self.payment_page, 'get_payment_page_title_ele').text
        return text_payment_page

    def click_and_input_money(self):
        time.sleep(2)
        self.run_steps(self.payment_page, 'click_and_input_money')
        return self

    def click_balance_button_pay(self):
        self.run_steps(self.payment_page, 'click_balance_button_pay')
        return self

    def click_immediate_payment(self):
        self.run_steps(self.payment_page, 'click_immediate_payment')
        return self

    def input_payment_password(self):
        self.run_steps(self.payment_page, 'input_payment_password')
        return self

    def click_payment_confirm_button(self):
        self.run_steps(self.payment_page, 'click_payment_confirm_button')
        return self

    def get_payment_success_message(self):
        success_message = self.run_steps(self.payment_page, 'get_payment_success_message').text
        return success_message


if __name__ == '__main__':
    message = Home_page().click_home_page_login().use_right_account_pwd_login_go_home_page().move_to_username_button().click_access_platform().click_platform_avatar().move_change_organization_ele().click_change_to_organization_316().move_to_purchase_menu() \
        .move_shopping_cart_and_click().click_select_all().click_go_to_result().ordinary_VAT_invoice().click_submit_order().click_and_input_money().click_and_input_money().click_immediate_payment().input_payment_password().click_payment_confirm_button().get_payment_success_message()
    assert message == "订单支付成功"
