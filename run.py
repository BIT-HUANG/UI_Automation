import os
from common.zip_file import zip_files
from common.send_email import SendEmail
import yaml
from common.log import Logger

logger = Logger().get_logger()


def run_case():
    source = './allure-report'
    # curr_time = time.strftime("%Y_%m_%d_%H_%M_%S")
    destin = f'./allure_report_zip/report.zip'
    zip_files(source, destin)
    with open('./py_yaml/config.yaml', mode='r', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        pytest_allure_cmd = datas['pytest_allure_cmd']
        os.system(pytest_allure_cmd['pytest_cdm'])
        os.system(pytest_allure_cmd['allure_cdm'])
    try:
        mail_data = datas['send_email']
        send_email = SendEmail(**mail_data)
        send_email.send_email_by_att(context='自动化测试报告', attachment_file_path=destin,
                                     Subject='自动化测试报告带附件')
    except Exception as e:
        logger.error('邮件发送失败')
    else:
        logger.info('邮件发送成功')


if __name__ == '__main__':
    run_case()
