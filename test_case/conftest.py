import time
from common.send_dingding_message import SendReportMessage
import pytest
from py_page.base_page import BasePage
from common.log import Logger
import sys

logger = Logger().get_logger()


@pytest.fixture()
def base_driver():
    base = BasePage()
    driver = base.driver
    print("**********执行前置条件，进行浏览器的的初始化***************")
    yield driver  # 类似于  return
    print("**********执行后置条件，关闭浏览器***************")
    time.sleep(1)
    driver.quit()


def pytest_terminal_summary(terminalreporter):
    """收集测试结果"""
    duration = time.time() - terminalreporter._sessionstarttime
    test_result = dict(total=terminalreporter._numcollected,
                       passed=len(terminalreporter.stats.get('passed', [])),
                       failed=len(terminalreporter.stats.get('failed', [])),
                       error=len(terminalreporter.stats.get('error', [])),
                       skipped=len(terminalreporter.stats.get('skipped', [])),
                       total_time=f"{duration} seconds")
    if not sys.platform.startswith("win"):
        resport_str = f"本次测试结果：\n" \
                      f"total: {test_result.get('total')}\n" \
                      f"passed: {test_result.get('passed')}\n" \
                      f"failed: {test_result.get('failed')}\n" \
                      f"error: {test_result.get('error')}\n" \
                      f"skipped: {test_result.get('skipped')}\n" \
                      f"total_time: {test_result.get('total_time')}\n" \
                      f"测试报告网址地址:https://test-jenkins.skycoresaas.com/view/test/job/QA_automated_testing/"
    else:
        resport_str = f"本次测试结果：\n" \
                      f"total: {test_result.get('total')}\n" \
                      f"passed: {test_result.get('passed')}\n" \
                      f"failed: {test_result.get('failed')}\n" \
                      f"error: {test_result.get('error')}\n" \
                      f"skipped: {test_result.get('skipped')}\n" \
                      f"total_time: {test_result.get('total_time')}\n"

    logger.info(resport_str)
    # 发送通过钉钉发送测试简报
    SendReportMessage().send_dingtalk_message(resport_str)
