from py_page.base_page import BasePage
from common.log import Logger
from py_page.home_page import Home_page
from common.base_redis import BaseRedis

redis = BaseRedis()
logger = Logger().get_logger()


class LoginPage(BasePage):
    login_file_path = BasePage.get_yaml_path('login','login_page.yaml')

    def use_right_account_pwd_login_go_home_page(self):
        self.run_steps(self.login_file_path, 'use_right_account_pwd_login_go_home_page')
        logger.info(f'执行了{"use_right_account_pwd_login"}')
        return Home_page(self.driver)

    def click_forgot_password(self):
        self.run_steps(self.login_file_path, 'click_forgot_password')
        logger.info('执行了click_forgot_password操作')
        return self

    def reset_passwords(self, phone: str):
        redis.set_code(phone)
        self.run_steps(self.login_file_path, 'reset_passwords', phone=phone)
        return self

    def get_reset_passwords_message(self):
        get_reset_passwords_message_text = self.run_steps(self.login_file_path, 'get_reset_passwords_message').text
        return get_reset_passwords_message_text
#
#
if __name__ == '__main__':
    name = Home_page().click_home_page_login().click_forgot_password().reset_passwords(
        '18146712142').get_reset_passwords_message()
    assert name == "操作成功"
