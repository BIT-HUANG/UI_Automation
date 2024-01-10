from py_page.base_page import BasePage
from common.log import Logger

logger = Logger().get_logger()
from py_page.home_page import Home_page


class Platform(BasePage):
    platform_yaml_path = BasePage.get_yaml_path('platform_menu','platform.yaml')

    def move_to_purchase_menu(self):
        self.run_steps(self.platform_yaml_path, 'move_to_purchase_menu')
        logger.info("移动到机柜采购单")
        return self

    def move_shopping_cart_and_click(self):
        self.run_steps(self.platform_yaml_path, 'move_shopping_cart_and_click')
        logger.info('移动到购物车并点击')
        from py_page.platform_menu.cabinet_purchase_menu.shopping_cart import ShoppingCart
        return ShoppingCart(self.driver)

    def click_platform_avatar(self):
        self.run_steps(self.platform_yaml_path, 'click_platform_avatar')
        return self

    def move_change_organization_ele(self):
        self.run_steps(self.platform_yaml_path, 'move_change_organization_ele')
        return self

    def click_change_to_organization_316(self):
        self.run_steps(self.platform_yaml_path, 'click_change_to_organization_316')
        return self

    def get_platform_page_organization_name(self):
        get_platform_page_organization_name_text = self.run_steps(self.platform_yaml_path,
                                                                  'get_platform_page_organization_name').text
        return get_platform_page_organization_name_text
    def click_change_to_platform(self):
        self.run_steps(self.platform_yaml_path,'click_change_to_platform')
        return self
    def move_to_sell_menu(self):
        self.run_steps(self.platform_yaml_path,'move_to_sell_menu')
        logger.info("移动到销售订单菜单")
        return self
    def move_to_new_order_menu_and_click(self):
        self.run_steps(self.platform_yaml_path,'move_to_new_order_menu_and_click')
        from py_page.platform_menu.new_order.new_order import NewOrder
        return NewOrder(self.driver)
    def move_to_design_design_menu(self):
        self.run_steps(self.platform_yaml_path,'move_to_design_design_menu')
        logger.info("移动到设计菜单")
        return self
    def click_public_library_list(self):
        self.run_steps(self.platform_yaml_path,"click_public_library_list")
        logger.info('点击公库列表,跳转到公库列表页面')
        from py_page.platform_menu.public_library_model.public_library_list import PublicLibraryList
        return PublicLibraryList(self.driver)


if __name__ == '__main__':
    Home_page().click_home_page_login().use_right_account_pwd_login_go_home_page().move_to_username_button().click_access_platform().click_platform_avatar().move_change_organization_ele()\
        .click_change_to_platform().move_to_sell_menu().move_to_new_order_menu_and_click().send_customer_name_and_select_customer().click_add_cabinet_goto_cabinet_slide_page().move_by_offset_to_side_sliding().\
        scroll_side_sliding_down().click_side_sliding_page_add_go_shopping().send_total_discount_amount().click_VAT_ordinary_invoice_button().click_submit_order_button()
