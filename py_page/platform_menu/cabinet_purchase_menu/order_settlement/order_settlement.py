from py_page.base_page import BasePage
from common.log import Logger
from py_page.home_page import Home_page
logger = Logger().get_logger()


class OrderSettlement(BasePage):
    order_settlement_path = BasePage.get_yaml_path("order_settlement","order_settlement.yaml")

    def ordinary_VAT_invoice(self):
        self.run_steps(self.order_settlement_path, 'ordinary_VAT_invoice')
        return self

    def click_submit_order(self):
        self.run_steps(self.order_settlement_path, 'click_submit_order')
        from py_page.platform_menu.cabinet_purchase_menu.order_settlement.payment_page.payment_page import Payment_page
        return Payment_page(self.driver)
if __name__ == '__main__':
    Home_page().click_home_page_login().use_right_account_pwd_login_go_home_page().move_to_username_button().click_access_platform().click_platform_avatar().move_change_organization_ele().click_change_to_organization_316().move_to_purchase_menu().move_shopping_cart_and_click().click_select_all().click_go_to_result().ordinary_VAT_invoice().click_submit_order()