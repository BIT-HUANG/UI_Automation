import time
import os
from py_page.base_page import BasePage
from common.log import Logger

logger = Logger().get_logger()
from py_page.home_page import Home_page


class Order_list(BasePage):
    order_list_yaml_path = BasePage.get_yaml_path('order_list', 'order_list.yaml')

    def get_order_list_tile(self):
        order_list_title = self.run_steps(self.order_list_yaml_path, 'get_order_list_tile').text
        return order_list_title

    def click_cabinet_order_number(self):
        self.run_steps(self.order_list_yaml_path, 'click_cabinet_order_number')
        return self

    def upload_contract_seller(self):
        self.run_steps(self.order_list_yaml_path, 'upload_contract_seller')
        return self

    def exchange_ele_display_to_block(self):
        js = 'document.querySelector(".ant-upload input").style.display="block"'
        self.driver.execute_script(js)
        return self

    def contract_path(self):
        self.run_steps(self.order_list_yaml_path, 'contract_path')
        time.sleep(3)
        return self

    def get_upload_contract_success_mes(self):
        mes = self.run_steps(self.order_list_yaml_path, 'get_upload_contract_success_mes').text
        logger.info(f"获得添加合同的信息为:{mes}")
        return mes

    def order_return_draft_and_change_info_examine_pass(self):
        self.run_steps(self.order_list_yaml_path, 'order_return_draft_and_change_info_examine_pass')
        return self


if __name__ == '__main__':
    # 上传合同
    # Home_page().click_home_page_login().use_right_account_pwd_login_go_home_page().move_to_username_button().click_access_platform().click_platform_avatar().move_change_organization_ele().click_change_to_platform().move_to_sell_menu().move_to_new_order_menu_and_click().send_customer_name_and_select_customer(). \
    #     click_add_cabinet_goto_cabinet_slide_page().move_by_offset_to_side_sliding().scroll_side_sliding_down().click_side_sliding_page_add_go_shopping().click_close_side_sliding().choose_all_select_box().click_VAT_ordinary_invoice_button().click_submit_order_button().click_cabinet_order_number().\
    #     upload_contract_seller().exchange_ele_display_to_block().contract_path().order_return_draft_and_change_info_examine_pass()
    mes = Home_page().click_home_page_login().use_right_account_pwd_login_go_home_page().move_to_username_button().click_access_platform().click_platform_avatar().move_change_organization_ele().click_change_to_platform().move_to_sell_menu().move_to_new_order_menu_and_click().send_customer_name_and_select_customer(). \
        click_add_cabinet_goto_cabinet_slide_page().move_by_offset_to_side_sliding().scroll_side_sliding_down().click_side_sliding_page_add_go_shopping().click_close_side_sliding().choose_all_select_box().click_VAT_ordinary_invoice_button().click_submit_order_button().click_cabinet_order_number(). \
        upload_contract_seller().exchange_ele_display_to_block().contract_path().get_upload_contract_success_mes()
    assert mes == "操作成功"
