import logging
import time
import os


class Logger:

    def __init__(self, name='mylog', logger_level='INFO', stream_level='INFO', file_level='INFO'):

        self.__logger = logging.getLogger(name)
        self.__logger.setLevel(
            logger_level)
        sh = logging.StreamHandler()
        sh.setLevel(stream_level)
        fmt = logging.Formatter('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')
        sh.setFormatter(fmt)
        curr_time = time.strftime("%Y-%m_%d")
        py_path = os.path.abspath(__file__)
        dir_common = os.path.dirname(py_path)
        dir_frame = os.path.dirname(dir_common)
        Log_path = dir_frame + "//Logs//"

        if not os.path.exists(Log_path):
            os.makedirs(Log_path)
        file_path = Log_path + curr_time + ".log"
        fh = logging.FileHandler(file_path, mode='a', encoding="utf-8")

        fh.setLevel(file_level)

        fh.setFormatter(fmt)
        if not self.__logger.handlers:
            self.__logger.addHandler(sh)
            self.__logger.addHandler(fh)

    def get_logger(self):
        return self.__logger


if __name__ == '__main__':
    Logger().get_logger().info("测试用例执行，日志记录！！！")
