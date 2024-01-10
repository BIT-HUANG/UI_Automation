from py_page.home_page import Home_page
from common.log import Logger
from common.screen_shot import getScreenShot
from test_case.my_markers import *
import allure

logger = Logger().get_logger()


@allure.feature('测试新建订单页面')
class TestNewOrder:
    @allure.story('测试新建订单功能')
    @allure.title('新建订单：测试选择用户，并添加【机柜】选择发票，未选择整单优惠金额，后提交订单')
    def test_create_new_order_submit_order(self, base_driver):
        try:
            message=Home_page(base_driver).click_home_page_login().use_right_account_pwd_login_go_home_page().move_to_username_button().click_access_platform().click_platform_avatar().move_change_organization_ele().click_change_to_platform().move_to_sell_menu().move_to_new_order_menu_and_click().send_customer_name_and_select_customer(). \
                click_add_cabinet_goto_cabinet_slide_page().move_by_offset_to_side_sliding().scroll_side_sliding_down().click_side_sliding_page_add_go_shopping().click_close_side_sliding().choose_all_select_box().click_VAT_ordinary_invoice_button().click_submit_order_button().get_order_list_tile()
            assert message == "订单列表"
        except BaseException as e:
            logger.error(f'错误信息为{e}')
            getScreenShot(base_driver, '新建订单创建订单错误')
            raise e