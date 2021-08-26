from selenium import webdriver
from Common.GetByLocal import GetByLocal
from time import sleep
import unittest
from Common.ReadSQL import Read_sql
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class Action_Method(unittest.TestCase):

    def open_browser(self,*args):
        u"""
        打开浏览器
        :param args:
        """
        browser = args[0]
        if browser == 'Chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox()
        elif browser == "Ie":
            self.driver = webdriver.Ie()
        else:
            self.driver = webdriver.Firefox()  # 默认为火狐
            # self.driver = webdriver.Remote(desired_capabilities=DesiredCapabilities.HTMLUNIT)
        self.driver.maximize_window()

    def get_url(self,*args):
        u"""
        打开url地址
        :param args:
        """
        url = args[0]
        self.driver.get(url)

    def get_element(self,*args):
        u"""
        获取element
        :param args:
        :return:
        """
        key = args[0]
        get_by_element = GetByLocal(self.driver)
        element = get_by_element.get_local_element(key)
        return element

    def element_send_keys(self,*args):
        u"""
        填写文案
        :param args:
        :return:
        """
        key, value = args[0], args[1]
        element = self.get_element(key)
        element.clear()  # 先清空文本框
        element.send_keys(value)

    def click_element(self, *args):
        u"""点击元素"""
        key = args[0]
        element = self.get_element(key)
        element.click()

    def get_element_text(self,key):
        u"""获取文本"""
        get_by_element = GetByLocal(self.driver)
        element = get_by_element.get_local_element(key)
        return element.text

    def sleep_time(self):
        u"""等待"""
        sleep(3)

    def sleep_time_custom(self,*args):
        time = args[0]
        sleep(int(time))

    def close_browser(self):
        u"""关闭浏览器"""
        self.driver.quit()

    def check_point(self,*args):
        u"""检查点"""
        key = args[0]
        expect_result = args[2]  # 期望结果
        actual_result = self.get_element_text(key)  # 实际结果
        error_des = args[3]  # 错误描述
        self.assertEqual(expect_result,actual_result,error_des)

    def get_scrm_login_vsCode(self,*args):
        u"""获取scrm登录验证码"""
        sql = "SELECT * from sys_captcha ORDER BY expire_time desc limit 1"
        readSql = Read_sql(sql, 'SCRM_DATABASE')
        code = readSql.sqlExecute()
        vsCode = code[0]['code']
        return vsCode


    def get_noah_login_vsCode(self,*args):
        u"""获取noah词库中台登录验证码"""
        sql = "SELECT * from sys_captcha ORDER BY expire_time desc limit 1"
        readSql = Read_sql(sql, 'NOAH_DATABASE')
        code = readSql.sqlExecute()
        vsCode = code[0]['code']
        return vsCode

    def switch_to_handle(self):
        u"""句柄切换,切换至当前句柄"""
        all_handle = self.driver.window_handles  # 获取所有页面得句柄
        now_handle = self.driver.current_window_handle  # 获取当前页面句柄
        for handle in all_handle:
            if handle != now_handle:
                self.driver.switch_to_window(handle)

    def go_to_frame(self,*args):
        u"""
        切换frame
        :return:
        """
        key = args[0]
        self.driver.switch_to_frame(key)



