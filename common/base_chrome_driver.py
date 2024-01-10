import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# 创建ChromeDriver实例
def create_driver(x:int):
    driver_path_txt = os.path.expanduser('~')+"/driver_path.txt"
    try:
        with open(driver_path_txt, "r", encoding='utf-8') as file:
            path = file.readline()
            path = path if path else ChromeDriverManager().install()

        with open(driver_path_txt, "w", encoding='utf-8') as file:
            file.write(path)
            print(path)
        if x==0:
            s = Service(executable_path=path)
            d = webdriver.Chrome(service=s)
            return d
        else:
            option=webdriver.ChromeOptions()
            option.add_argument("--headless")
            option.add_argument('--window-size=2560,1440')
            s=Service(executable_path=path)
            d=webdriver.Chrome(service=s,options=option)
            return d
    except Exception as e:
        print(e)
        open(driver_path_txt, "w", encoding='utf-8').close()
        return create_driver(x)
