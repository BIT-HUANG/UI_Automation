import os.path

from typing import List

from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
import yaml
from common.log import Logger
from string import Template
from selenium import webdriver
from common.handle_black import handle_black
from common.base_chrome_driver import create_driver
import sys
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random

logger = Logger().get_logger()


class BasePage:

    def __init__(self, driver: WebDriver = None):
        if not driver:
            if sys.platform.startswith("win"):
                self.driver = create_driver(0)
            else:
                self.options = webdriver.ChromeOptions()
                self.options.add_argument('--headless')
                self.options.add_argument('window-size=2560x1440')
                self.driver = webdriver.Remote(command_executor="http://192.168.0.45:4455/wd/hub",
                                               options=self.options)

            self.driver.implicitly_wait(10)
            self.driver.get("https://qa.skycoresaas.com/#/home")
            self.driver.maximize_window()
            time.sleep(1)
        else:
            self.driver = driver

    @handle_black
    def find(self, by: str, locator) -> WebElement:
        by = by.lower()
        by_locator = ""
        if by == "xpath":
            by_locator = (By.XPATH, locator)
        elif by == "css":
            by_locator = (By.CSS_SELECTOR, locator)
        ele = WebDriverWait(self.driver, 10, 0.5).until(ec.visibility_of_element_located(by_locator))
        return ele

    @handle_black
    def finds(self, by: str, locator) -> List[WebElement]:
        by = by.lower()
        by_locator = ""
        if by == "xpath":
            by_locator = (By.XPATH, locator)
        elif by == "css":
            by_locator = (By.CSS_SELECTOR, locator)
        eles = WebDriverWait(self.driver, 10, 0.5).until(ec.visibility_of_all_elements_located(by_locator))
        return eles

    @handle_black
    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    @handle_black
    def finds_and_click(self, by, locator, index):
        self.finds(by, locator)[index].click()

    @handle_black
    def find_and_send(self, by, locator, text):
        textS = str(text)
        for text in textS:
            self.find(by, locator).send_keys(text)
            time.sleep(random.randint(0, 1) / 10)

    @handle_black
    def finds_and_send(self, by, locator, index, text: str):
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        text = str(text)
        if "project_path" in text:
            text = text.replace("project_path", path)

        self.finds(by, locator)[index].send_keys(text)

    def keyboard_backspace(self, by, locator, text):
        text = int(text)
        for i in range(text):
            self.find(by, locator).send_keys(Keys.BACK_SPACE)

    @handle_black
    def find_and_clear(self, by, locator):
        self.find(by, locator).clear()

    @handle_black
    def finds_and_clear(self, by, locator, index):
        self.finds(by, locator)[index].clear()

    @handle_black
    def move_to_ele(self, by, locator, index=None):
        if not index:
            ele = self.find(by, locator)
        else:
            ele = self.finds(by, locator)[index]
        ActionChains(self.driver).move_to_element(ele).perform()

    def scroll_page(self, x, y, t=0):  # x为正 代表向右滑动，y为正向下滑动
        ActionChains(self.driver).scroll_by_amount(x, y).pause(t).perform()

    def scroll_page2(self, by, locator, x, y):
        ele = self.find(by, locator)
        so = ScrollOrigin.from_element(ele)
        ActionChains(self.driver).scroll_from_origin(so, x, y).perform()

    def move_by_offset(self, x, y, t=0):  # 光标移动
        ActionChains(self.driver).move_by_offset(x, y).pause(t).perform()

    @handle_black
    def switch_alert_and_action(self, yes_or_not=None, text=None):
        alert = self.driver.switch_to.alert
        if text:
            alert.send_keys(text)

        if yes_or_not == 1:
            alert.accept()
        else:
            alert.dismiss()

    @staticmethod
    def get_yaml_path(dir_path, yaml_file_name):
        path = os.path.abspath(__file__)
        project_path = os.path.dirname(os.path.dirname(path))
        dir_abd_path = project_path + fr'/py_yaml/{dir_path}'
        if not os.path.exists(dir_abd_path):
            os.makedirs(dir_abd_path)
        yaml_file_name = project_path + fr'/py_yaml/{dir_path}/{yaml_file_name}'
        return yaml_file_name

    def run_steps(self, yaml_path, page_function, **kwargs):
        with open(yaml_path, mode="r", encoding="utf-8") as f:
            yaml_data = yaml.safe_load(f)
        steps = yaml_data[page_function]
        for k, v in kwargs.items():  # {"tel":'"13012312300"'}
            if isinstance(v, str):
                kwargs[k] = f"'{v}'"
        logger.info(f'**********执行了页面类里面的{page_function}方法*****************,yaml文件的路径是{yaml_path}')
        for step in steps:
            try:
                step = yaml.dump(step)
                data2 = Template(step).substitute(kwargs)
                step = yaml.safe_load(data2)
                sleep_time = step.get('sleep')
                if sleep_time:
                    time.sleep(sleep_time)
                method = getattr(self, step["action"])
                if step["action"] == "find_and_click":
                    method(*step["locator"])
                    logger.info(f'调用了{step["action"]}操作')
                elif step["action"] == "finds_and_click":
                    method(*step["locator"], step["index"])
                    logger.info(f'调用了{step["action"]},下标为{step["index"]}')
                elif step["action"] == "find_and_send":
                    method(*step["locator"], step["text"])
                    logger.info(f'调用了{step["action"]},输入的文本{step["text"]}')
                elif step["action"] == "finds_and_send":
                    method(*step["locator"], step["index"], step["text"])
                    logger.info(f'调用了{step["action"]},传入的索引是{step["index"]}:输入的文本{step["text"]}')
                elif step["action"] == "find_and_clear":
                    method(*step["locator"])
                    logger.info(f'调用了{step["action"]}操作')
                elif step["action"] == "finds_and_clear":
                    method(*step["locator"], step["index"])
                    logger.info(f'调用了{step["action"]}操作，索引是{step["index"]}')
                elif step["action"] == "move_to_ele":
                    method(*step["locator"], index=step["index"])
                    logger.info(f'调用了{step["action"]}操作，索引是{step["index"]}')
                elif step["action"] == "scroll_page":
                    method(*step["index"])
                    logger.info(f'调用了{step["action"]}操作，索引是{step["index"]}')
                elif step["action"] == "move_by_offset":
                    method(*step["index"])
                    logger.info(f'调用了{step["action"]}操作，索引是{step["index"]}')
                elif step["action"] == "find":
                    ele = method(*step["locator"])
                    logger.info(f'调用了{step["action"]}操作')
                    return ele
                elif step["action"] == "finds":
                    eles = self.finds(*step["locator"])
                    logger.info(f'调用了{step["action"]}操作')
                    return eles
                elif step["action"] == "click_alert_yes":
                    self.switch_alert_and_action(step['index'], step['text'])
                    logger.info(f'调用了{step["action"]}操作')
                    return self
                elif step["action"] == "scroll_page2":
                    method(*step["locator"], *step["index"])
                    logger.info(f'调用了{step["action"]}操作')
                elif step["action"] == "keyboard_backspace":
                    method(*step["locator"], step["text"])
                    logger.info(f'调用了{step["action"]}操作,次数为{step["text"]}')

                else:
                    raise AttributeError("方法错误，请检查")
            except Exception as e:
                logger.error(
                    f'元素定位交互异常，传入的参数是{step["action"]},传入的参数是{step["locator"]}::下标为{step["index"]}::等待时间为{step["sleep"]}')
                logger.error(f'报错信息是{e}')
                raise e
