from py_page.home_page import Home_page
from common.log import Logger
from common.screen_shot import getScreenShot
from test_case.my_markers import *
import allure

logger = Logger().get_logger()


@allure.feature('测试商城首页_home_page')
class Test_Home_page:
    @allure.story('测试未登录下在商城首页操作')
    @allure.title('测试游客未登录下，购买商品跳转到登录页面，再次登录后回到商品主页并对用户进行断言')
    @p1
    def test_move_to_ele_skycoresaas_shop_and_click_cabinet_series_add_cabinet_in_shop(self, base_driver):
        try:
            with allure.step('测试游客未登录下，购买商品跳转到登录页面，再次登录后回到商品主页并对用户进行断言'):
                user_name = Home_page(
                    base_driver).move_to_ele_skycoresaas_shop_and_click_cabinet_series_add_cabinet_in_shop().use_right_account_pwd_login_go_home_page().get_user_name()
                assert user_name == "承少"


        except Exception as e:
            logger.error("测试登录功能报错了")
            getScreenShot(base_driver, __name__)
            raise e

    @allure.story('测试未登录下在商城首页操作')
    @allure.title('测试游客未登录下，购买商品跳转到登录页面，再次登录后回到商品主页并添加购物车获取操作成功信息')
    @p3
    def test_get_success_click_add_shop_cart_message(self, base_driver):
        try:
            with allure.step(
                    '测试游客未登录下，购买商品跳转到登录页面，再次登录后回到商品主页并添加购物车获取操作成功信息'):
                get_success_click_add_shop_cart_message = Home_page(
                    base_driver).move_to_ele_skycoresaas_shop_and_click_cabinet_series_add_cabinet_in_shop().use_right_account_pwd_login_go_home_page().click_add_shop_cart().get_success_click_add_shop_cart_message()
                assert get_success_click_add_shop_cart_message == "操作成功"


        except Exception as e:
            logger.error("测试登录功能报错了")
            getScreenShot(base_driver, __name__)
            raise e
