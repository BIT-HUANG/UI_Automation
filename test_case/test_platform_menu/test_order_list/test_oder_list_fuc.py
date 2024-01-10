from py_page.home_page import Home_page
from common.log import Logger
from common.screen_shot import getScreenShot
from test_case.my_markers import *
import allure

logger = Logger().get_logger()


@allure.feature('测试订单列表页面')
class TestOrderList:
    @allure.story('测试订单编辑功能')
    @allure.title('测试创建新的手工单后，并上传纸质合同')
    def test_get_upload_contract_success_mes(self, base_driver):
        try:
            mes = Home_page(base_driver).click_home_page_login().use_right_account_pwd_login_go_home_page().move_to_username_button().click_access_platform().click_platform_avatar().move_change_organization_ele().click_change_to_platform().move_to_sell_menu().move_to_new_order_menu_and_click().send_customer_name_and_select_customer(). \
                click_add_cabinet_goto_cabinet_slide_page().move_by_offset_to_side_sliding().scroll_side_sliding_down().click_side_sliding_page_add_go_shopping().click_close_side_sliding().choose_all_select_box().click_VAT_ordinary_invoice_button().click_submit_order_button().click_cabinet_order_number(). \
                upload_contract_seller().exchange_ele_display_to_block().contract_path().get_upload_contract_success_mes()
            assert mes == "操作成功"

        except BaseException as e:
            logger.error(f'错误信息为{e}')
            getScreenShot(base_driver, __name__)
            raise e
