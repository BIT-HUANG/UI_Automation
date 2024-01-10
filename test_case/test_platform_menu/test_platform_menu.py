from py_page.home_page import Home_page
from common.log import Logger
from common.screen_shot import getScreenShot
from test_case.my_markers import *
import allure

logger = Logger().get_logger()
@allure.feature('测试平台页面')
class Test_Platform:
    @allure.story('测试平台中，切换组织的功能')
    @p3
    @allure.title('游客登录成为客户切换组织的功能，并断言组织的名称')
    def test_create_new_order_fun(self, base_driver):
        try:
            platform_organization_name = Home_page(
                base_driver).click_home_page_login().use_right_account_pwd_login_go_home_page().move_to_username_button().click_access_platform().click_platform_avatar().move_change_organization_ele().click_change_to_organization_316().click_platform_avatar().get_platform_page_organization_name()
            assert platform_organization_name == "北京滴滴出行科技有限公司"
        except BaseException as e:
            logger.error(f'错误为{e}')
            getScreenShot(base_driver, '切换组织错误的截图')
            raise e
