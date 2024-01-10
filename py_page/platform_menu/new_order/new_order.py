import time

from py_page.base_page import BasePage
from common.log import Logger

logger = Logger().get_logger()
from py_page.home_page import Home_page
class NewOrder(BasePage):
    new_order_page=BasePage.get_yaml_path('new_order','new_order_page.yaml')
    def send_customer_name_and_select_customer(self):
        self.run_steps(self.new_order_page,'send_customer_name_and_select_customer')
        return self
    def click_add_cabinet_goto_cabinet_slide_page(self):
        self.run_steps(self.new_order_page,'click_add_cabinet_goto_cabinet_slide_page')
        return self
    def move_by_offset_to_side_sliding(self):
        self.run_steps(self.new_order_page, 'move_by_offset_to_side_sliding')
        return self
    def click_side_sliding_page_add_go_shopping(self):
        self.run_steps(self.new_order_page, 'click_side_sliding_page_add_go_shopping')
        return self
    def click_close_side_sliding(self):
        self.run_steps(self.new_order_page,'click_close_side_sliding')
        return self
    def scroll_side_sliding_down(self):
        self.run_steps(self.new_order_page, 'scroll_side_sliding_down')
        return self
    def drag_side_sliding_width(self):
        self.run_steps(self.new_order_page,'drag_side_sliding_width')
        return self
    def choose_all_select_box(self):
        self.run_steps(self.new_order_page,'choose_all_select_box')
        return self
    def click_VAT_ordinary_invoice_button(self):
        self.run_steps(self.new_order_page,'click_VAT_ordinary_invoice_button')
        return self
    def send_total_discount_amount(self):
        self.run_steps(self.new_order_page,'send_total_discount_amount')
        return self
    def click_submit_order_button(self):
        self.run_steps(self.new_order_page,'click_submit_order_button')
        from py_page.platform_menu.order_list.order_list_page import Order_list
        return Order_list(self.driver)
if __name__ == '__main__':
    message=Home_page().click_home_page_login().use_right_account_pwd_login_go_home_page().move_to_username_button().click_access_platform().click_platform_avatar().move_change_organization_ele().click_change_to_platform().move_to_sell_menu().move_to_new_order_menu_and_click().send_customer_name_and_select_customer().\
        click_add_cabinet_goto_cabinet_slide_page().move_by_offset_to_side_sliding().scroll_side_sliding_down().click_side_sliding_page_add_go_shopping().click_close_side_sliding().choose_all_select_box().click_VAT_ordinary_invoice_button().click_submit_order_button().get_order_list_tile()
    assert message =="订单列表"