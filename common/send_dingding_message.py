import requests
import os
import requests


class SendReportMessage:

    @staticmethod
    def send_dingtalk_message(data):
        send_message_url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=fc09df8f-03c2-40e7-9320-8249477a53fe"
        params = {"text": {"content": data}, "msgtype": "text"}
        res = requests.post(url=send_message_url, json=params, ).json()

        print(res)


if __name__ == '__main__':
    url = r"https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=fc09df8f-03c2-40e7-9320-8249477a53fe&type=file"
    # skysquare_backend_url="https://skysquare_backend.skycoresaas.com"
    # UI_test_path="/skysquare/data/Test_Report/UI_Test"
    # curr_path=skysquare_backend_url+UI_test_path
    # data=requests.post(curr_path)
    # test_Report_UI_Test_path:str=data.json()["data"][-1]['file_path']
    # dir_Test_Report_UI_Test_path=test_Report_UI_Test_path.split("/",1)[0]
    # print(dir_Test_Report_UI_Test_path)
    # up_load_path="/skysquare/data-upload"
    # data_upload=skysquare_backend_url+up_load_path
    # file_path=r"C:\Users\dell\PycharmProjects\pythonProject\automated_testing\allure_report_zip\ip"
    # with open(file_path,"rb") as file:
    #     data={
    #         "file_path":up_load_path,
    #         "file":file
    #     }
    #     response=requests.post(data_upload,data=data)
    #     print(response.json())

    # project_path = os.path.dirname(os.path.dirname(__file__))
    # report_zip_path = project_path + r'\allure_report_zip\report.zip'
    # with open(report_zip_path, 'rb') as f:
    #     files = {
    #         "file": f.read()
    #     }
    #     headers = {
    #         'Content-Type': "application/zip",
    #     }
    #     res = requests.post(url=url, files=files,headers=headers).json()
    # print(res)
    # media_id = res['media_id']
    # print(media_id)
    # url1 = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=fc09df8f-03c2-40e7-9320-8249477a53fe"
    # Content_type = {
    #     "msgtype": "file",
    #     "file": {
    #         "media_id": media_id
    #     }
    # }
    # currey = requests.post(url=url1, json=Content_type,).json()
    # print(currey)
