from selenium.webdriver.common.by import By
from common.log import Logger

logging = Logger(__name__).get_logger()

global n
def handle_black(fun):
    def run(*args, **kwargs):

        black_list = [(By.XPATH, "//input[@id='form_item_code']"), (By.XPATH, "//input[@id='form_item_new']"),
                      (By.XPATH, "//input[@id='form_item_confirm']"), (By.XPATH, "//span[text()='确 定']")]
        by_self = args[0]  #
        try:

            ele = fun(*args, **kwargs)
            return ele
        except Exception as e:
            from common.base_redis import BaseRedis
            from selenium.webdriver.remote.webelement import WebElement
            BaseRedis().set_code("18146712142")

            n = 0
            for black in black_list:
                n+=1
                logging.info(f"在黑名单中查找元素{black}")

                eles = by_self.driver.find_elements(*black)
                # 如果黑名单中的元素存在，就对该元素进行处理
                if any(eles):
                    ele: WebElement = eles[0]
                    if n == 1:
                        ele.send_keys("123456")
                    elif n == 2:
                        ele.send_keys("741852")
                    elif n == 3:
                        ele.send_keys("741852")
                    elif n == 4:
                        ele.click()

                        if ele:
                            logging.info(f"查找到黑名单元素{black}，并对该元素进行处理")
                            ele = fun(*args, **kwargs)
                            return ele
                else:
                    logging.info(f"在黑名单中元素未在页面中定位到")
            raise e

    return run
