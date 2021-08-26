from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.ReadSQL import Read_sql
from Config.ReadConfig import ReadConfig
from selenium.webdriver.common.by import By
from time import sleep
from Common.Logger import WebLogger


class BasePage(object):
    # 构造函数里面的参数就是类的所有参数
    def __init__(self,selenuime_driver,base_url):
        self.log = WebLogger("Base function").logger
        self.driver = selenuime_driver
        self.url = base_url

    def _open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()

    # 定义open()方法，调用_open()方法
    def open(self):
        self._open()

    def find_emelemt(self,*loc):
        try:
            # 保证元素可见
            WebDriverWait(self.driver,10,0.5).until(EC.visibility_of_all_elements_located(loc))
            return self.driver.find_element(*loc)
        except:
            self.log.info("页面中没有找到:",*loc)

    # 定义script()方法，用于执行JS脚本
    def script(self,scriptString):
        print("session_id:",self.driver.session_id)
        self.driver.execute_script(scriptString)

    # 定义页面跳转方法，比方说有的页面有frame嵌套
    def switch_frame(self,loc):
        return self.driver.switch_to_frame(loc)

    # 重新定义send_keys()方法，为了保证搜索按钮是否存在，还有有的输入框中默认有值，要清空
    def send_keys(self,loc,value,clear_first=True,click_first=True):
        try:
            # getattr方法相当于实现了self.loc
            loc = getattr(self,"_%s"%loc)
            # 是否存在搜索按钮
            if click_first:
                self.find_element(*loc).click()
            # 清空搜索框中的值，并输入需要搜索的值
            if clear_first:
                self.find_emelemt(*loc).clear()
                self.find_emelemt(*loc).send_keys(value)

        except:
            self.log.info( "页面上未找到%s元素" % loc)


    #句柄切换,切换至当前句柄
    def switch_to_handle(self):
        all_handle = self.driver.window_handles #获取所有页面得句柄
        now_handle = self.driver.current_window_handle  # 获取当前页面句柄
        for handle in all_handle:
            if handle != now_handle:
                self.driver.switch_to_window(handle)


    #scrm登录
    def _Scrm_login(self, username,
                   password,
                   ):
        userName_loc = (By.NAME, 'username')
        # 密码
        password_loc = (By.NAME, 'password')
        # 验证码
        captcha_loc = (By.NAME, 'captcha')
        # 登录按钮
        login_btn_loc = (By.XPATH, '//*[@id="app"]/div/div[2]/div/form/button/span')
        sql = "SELECT * from sys_captcha ORDER BY expire_time desc limit 1"
        baseUrl = ReadConfig()
        url = baseUrl.get_http('baseUrl')
        self.driver.get(url)
        sleep(3)
        self.find_emelemt(*userName_loc).send_keys(username)
        self.find_emelemt(*password_loc).send_keys(password)
        readSql = Read_sql(sql)
        code = readSql.sqlExecute()
        vsCode = code[0]['code']
        self.find_emelemt(*captcha_loc).send_keys(vsCode)
        # 点击登录
        self.find_emelemt(*login_btn_loc).click()




