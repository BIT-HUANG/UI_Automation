from py_page.home_page import Home_page
from common.log import Logger
from common.screen_shot import getScreenShot
import pytest
import allure
logger = Logger().get_logger()

@allure.feature('测试登录页面')
class Test_login:
    @allure.story('测试登录功能')
    @pytest.mark.p0
    @allure.title('通过商城首页点击登录跳转到登录页面并使用正确的账号和密码登录')
    @allure.description('通过商城首页点击登录跳转到登录页面并使用正确的账号和密码登录')
    def test_use_right_account_pwd_login(self, base_driver):
        try:
            user_name = Home_page(
                base_driver).click_home_page_login().use_right_account_pwd_login_go_home_page().get_user_name()
            assert user_name == "承少"
        except AssertionError as e:
            getScreenShot(base_driver, '测试登录误')
            logger.error(f'登录错误为{e}')
            raise e

    @pytest.mark.p0
    @allure.story('测试登录功能')
    @allure.title('测试忘记密码功能')
    @allure.description('从商城页面跳转到登录页面，点击忘记密码，测试忘记密码功能，并获得操作成功信息')
    def test_reset_passwords_function(self, base_driver):
        try:
            get_reset_passwords_message = Home_page(
                base_driver).click_home_page_login().click_forgot_password().reset_passwords(
                '18146712142').get_reset_passwords_message()
            assert get_reset_passwords_message == '操作成功'
        except AssertionError as e:
            getScreenShot(base_driver, '忘记密码')
            logger.error(f'忘记密码错误为{e}')
            raise e
