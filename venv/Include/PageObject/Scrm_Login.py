from Public.BasePage import BasePage
from selenium.webdriver.common.by import By
from Common.Logger import WebLogger


class Login(BasePage):
    log = WebLogger("登录测试用例").logger
    #用户名
    userName_loc = (By.NAME,'username')
    #密码
    password_loc = (By.NAME,'password')
    #验证码
    captcha_loc = (By.NAME,'captcha')
    #登录按钮
    login_btn_loc = (By.XPATH,'//*[@id="app"]/div/div[2]/div/form/button/span')
    #错误提示
    error_alert_loc = (By.XPATH,'/html/body/div[2]/p')
    #冒烟测试检查点
    home_check_text_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[1]')

    # # 重写父类的open()方法
    # def open(self):
    #     self._open(self.base_url)


    def userName_send_keys(self, content):
        userName = self.find_emelemt(*self.userName_loc)
        userName.send_keys(content)
        self.log.info("username输入框输入:" + content)

    def password_send_keys(self, content):
        password = self.find_emelemt(*self.password_loc)
        password.send_keys(content)
        self.log.info("password输入框输入:" + content)

    def vsCode_send_keys(self, content):
        vsCode = self.find_emelemt(*self.captcha_loc)
        vsCode.send_keys(content)
        self.log.info("验证码输入框输入:" + content)

    def login_btn_lick(self):
        self.find_emelemt(*self.login_btn_loc).click()
        self.log.info("点击登录按钮")

    def login_btn_text(self):
        login_text = self.find_emelemt(*self.login_btn_loc).text
        self.log.info("登录按钮值为:" + login_text)
        return login_text

    def error_alert_loc_text(self):
        error_text = self.find_emelemt(*self.error_alert_loc).text
        self.log.info("错误提示为:" + error_text)
        return error_text

    def home_check_text(self):
        home_check = self.find_emelemt(*self.home_check_text_loc).text
        self.log.info("登录检查点:" + home_check)
        return home_check

    # def property_init(self,location_mode,location_value):
    #     u"""
    #     路径驱动
    #     :param location_mode:定位方式
    #     :param location_value:定位值
    #     :return:
    #     """
    #     if location_mode != None:
    #         if location_mode == 'NAME':
    #             location_value = (By.NAME, location_value)
    #         elif location_mode == 'XPATH':
    #             location_value = (By.XPATH, location_value)
    #         elif location_mode == 'LINK_TEXT':
    #             location_value = (By.LINK_TEXT, location_value)
    #         elif location_mode == 'ID':
    #             location_value = (By.ID, location_value)
    #         elif location_mode == 'PARTIAL_LINK_TEXT':
    #             location_value = (By.PARTIAL_LINK_TEXT, location_value)
    #         elif location_mode == 'TAG_NAME':
    #             location_value = (By.TAG_NAME, location_value)
    #         elif location_mode == 'CLASS_NAME':
    #             location_value = (By.CLASS_NAME, location_value)
    #         elif location_mode == 'CSS_SELECTOR':
    #             location_value = (By.CSS_SELECTOR, location_value)
    #         return location_value
    #
    # def incident_init(self,incident,input_value,log_record):
    #     u"""
    #     事件驱动
    #     :param incident: 事件
    #     :param input_value: 需要输入的值
    #     :param describe:日志描述
    #     :return:
    #     """
    #     self.location_value = self.property_init()
    #     if incident != None:
    #         if incident == 'text':
    #             text_value = self.find_emelemt(*self.location_value).text
    #             self.log.info(log_record)
    #             return text_value
    #         elif incident == 'click':
    #             self.find_emelemt(*self.location_value).click()
    #             self.log.info(log_record)
    #         elif incident == 'clear':
    #             self.find_emelemt(*self.location_value).clear()
    #             self.log.info(log_record)
    #         elif incident == 'send_keys':
    #             self.find_emelemt(*self.location_value).send_keys(input_value)
    #             self.log.info(log_record)
    #         elif incident == 'get_attribute':
    #             self.find_emelemt(*self.location_value).get_attribute(input_value)
    #             self.log.info(log_record)










