# -*- coding: utf-8 -*-
import logging
import datetime
import os

class WebLogger():
    """程序调试日志-文件和控制台输出"""

    def __init__(self, name):
        """初始化属性"""
        # 初始化日志器
        self.logger =logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        # 初始化日志输出格式器
        file_fmt='%(asctime)s,%(name)s[line:%(lineno)d],%(levelname)s,%(message)s'
        console_fmt='%(name)s[line:%(lineno)d] - %(levelname)s: %(message)s'
        file_formatter = logging.Formatter(file_fmt)
        console_formatter=logging.Formatter(console_fmt)

        #创建路径
        file_path=os.path.join(os.getcwd(),'logs')
        if not os.path.exists(file_path):
            os.mkdir(file_path)

        #初始化info文件处理器
        file_name_info=str(datetime.date.today()) + " log_info.csv"
        file_path_info=file_path+"\\"+file_name_info
        file_handler_info=logging.FileHandler(file_path_info)
        file_handler_info.setLevel(logging.INFO)
        file_handler_info.setFormatter(file_formatter)

        #初始化error文件处理器
        file_name_error=str(datetime.date.today()) + " log_error.csv"
        file_path_error=file_path+"\\"+file_name_error
        file_handler_error=logging.FileHandler(file_path_error)
        file_handler_error.setLevel(logging.ERROR)
        file_handler_error.setFormatter(file_formatter)

        #初始化日志输出流处理器
        console_handler=logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(console_formatter)

        #添加日志处理器
        self.logger.addHandler(file_handler_info)
        self.logger.addHandler(file_handler_error)
        self.logger.addHandler(console_handler)

    def get_logger(self):
        """获得自定义的日志器"""
        return self.logger

'''
DEBUG 	指定细粒度信息事件是最有用的应用程序调试
INFO 	指定能够突出在粗粒度级别的应用程序运行情况的信息的消息
WARNING 指定具有潜在危害的情况
ERROR 	错误事件可能仍然允许应用程序继续运行
FATAL 	指定非常严重的错误事件，这可能导致应用程序中止
'''