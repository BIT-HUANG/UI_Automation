from py_page.base_page import BasePage
from common.log import Logger
logger = Logger().get_logger()
import time
class Home_page(BasePage):
    home_page_path = BasePage.get_yaml_path("home",'home_page.yaml')
    print(home_page_path)

    def move_to_ele_skycoresaas_shop_and_click_cabinet_series_add_cabinet_in_shop(self):
        self.run_steps(self.home_page_path, 'move_to_ele_skycoresaas_shop_and_click_cabinet_series_add_cabinet_in_shop')
        logger.info(f'执行了move_to_ele_skycoresaas_shop_and_click_cabinet_series_add_cabinet_in_shop')
        from py_page.login_page import LoginPage
        return LoginPage(self.driver)

    def click_add_shop_cart(self):
        self.run_steps(self.home_page_path, 'click_add_shop_cart')
        logger.info(f'click_add_shop_cart操作')
        return self

    def get_success_click_add_shop_cart_message(self):
        get_success_click_add_shop_cart_message_text = self.run_steps(self.home_page_path,
                                                                      'get_success_click_add_shop_cart_message').text
        logger.info(f'获取到{get_success_click_add_shop_cart_message_text}')
        return get_success_click_add_shop_cart_message_text

    def click_home_page_login(self):
        self.run_steps(self.home_page_path, 'click_home_page_login')
        from py_page.login_page import LoginPage
        return LoginPage(self.driver)

    def get_user_name(self):
        user_name = self.run_steps(self.home_page_path, 'get_user_name_ele').text
        logger.info(f'获取的用户名是{user_name}')
        return user_name

    def move_to_username_button(self):
        self.run_steps(self.home_page_path, 'move_to_username_button')
        return self

    def click_access_platform(self):
        self.run_steps(self.home_page_path, 'click_access_platform')
        from py_page.platform_menu.platform_menu import Platform
        return Platform(self.driver)


if __name__ == '__main__':
    Home_page().move_to_ele_skycoresaas_shop_and_click_cabinet_series_add_cabinet_in_shop()
