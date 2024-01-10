import time

from py_page.base_page import BasePage
from common.log import Logger
from py_page.home_page import Home_page

logger = Logger().get_logger()


class ShoppingCart(BasePage):
    shopping_cart_yaml_path = BasePage.get_yaml_path('shopping_cart','shopping_cart.yaml')

    def click_cabinet_select_side_sliding_page(self):
        self.run_steps(self.shopping_cart_yaml_path, 'click_cabinet_select_side_sliding_page')
        return self

    def move_and_click_in_windows(self):
        self.run_steps(self.shopping_cart_yaml_path, 'move_and_click_in_windows')
        return self

    def scroll_page_in_windows(self):
        self.run_steps(self.shopping_cart_yaml_path, 'scroll_page_in_windows')
        return self

    def click_side_sliding_page_add_go_shopping(self):
        self.run_steps(self.shopping_cart_yaml_path, 'click_side_sliding_page_add_go_shopping')
        return self

    def get_add_shopping_cart_success_message(self):
        message = self.run_steps(self.shopping_cart_yaml_path, 'get_add_shopping_cart_success_message').text

        return message

    def move_by_offset_to_side_sliding(self):
        self.run_steps(self.shopping_cart_yaml_path, 'move_by_offset_to_side_sliding')
        return self

    # 在侧滑页移动鼠标滑轮，向下
    def scroll_side_sliding_down(self):
        self.run_steps(self.shopping_cart_yaml_path, 'scroll_side_sliding_down')
        return self

    def click_select_all(self):
        self.run_steps(self.shopping_cart_yaml_path, 'click_select_all')
        return self

    def get_selected_quantity(self):
        text = self.run_steps(self.shopping_cart_yaml_path, 'get_selected_quantity').text
        return text

    def click_go_to_result(self):
        self.run_steps(self.shopping_cart_yaml_path, 'click_go_to_result')
        from py_page.platform_menu.cabinet_purchase_menu.order_settlement.order_settlement import OrderSettlement
        return OrderSettlement(self.driver)


if __name__ == '__main__':
    # Home_page().click_home_page_login().use_right_account_pwd_login_go_home_page().move_to_username_button().click_access_platform().click_platform_avatar().move_change_organization_ele().click_change_organization().move_purchase_menu().move_purchase_menu().move_shopping_cart_and_click().click_select_all()
    Home_page().click_home_page_login().use_right_account_pwd_login_go_home_page().move_to_username_button().click_access_platform().click_platform_avatar() \
        .move_change_organization_ele().click_change_to_organization_316().move_to_purchase_menu().move_shopping_cart_and_click().\
        click_cabinet_select_side_sliding_page().move_by_offset_to_side_sliding().scroll_side_sliding_down().click_side_sliding_page_add_go_shopping().\
        get_add_shopping_cart_success_message()
