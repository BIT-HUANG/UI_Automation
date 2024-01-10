from py_page.home_page import Home_page
from common.log import Logger
from common.screen_shot import getScreenShot
from test_case.my_markers import *
import allure

logger = Logger().get_logger()


@allure.feature('测试购物车页面')
class Test_ShoppingCart:
    @allure.story('测试购物车功能')
    @allure.title('测试购物车功能中的全选功能')
    def test_click_select_all_(self, base_driver):
        try:
            select_quantity_text = Home_page(
                base_driver).click_home_page_login().use_right_account_pwd_login_go_home_page().move_to_username_button().click_access_platform().click_platform_avatar().move_change_organization_ele().click_change_to_organization_316().move_to_purchase_menu().move_shopping_cart_and_click().click_select_all().get_selected_quantity()
            assert select_quantity_text != 0
        except BaseException as e:
            logger.error(f'错误信息为{e}')
            getScreenShot(base_driver, '测试购物车全选数量错误')
            raise e

    @allure.story('测试购物车功能')
    @allure.title('测试购物车功能中，机柜选型侧滑页面添加机柜')
    @p5
    def test_shopping_cart_cabinet_select_page_add_cabinet_fun(self, base_driver):
        try:
            add_success_message = Home_page(base_driver).click_home_page_login().use_right_account_pwd_login_go_home_page().move_to_username_button().click_access_platform().click_platform_avatar() \
                .move_change_organization_ele().click_change_to_organization_316().move_to_purchase_menu().move_shopping_cart_and_click().click_cabinet_select_side_sliding_page().move_by_offset_to_side_sliding().scroll_side_sliding_down().click_side_sliding_page_add_go_shopping().get_add_shopping_cart_success_message()
            assert add_success_message == "操作成功"
        except Exception as e:
            logger.error(f'错误信息是{e}')
            getScreenShot(base_driver, '测试愿望清单侧滑页添加机柜功能')
            raise e
