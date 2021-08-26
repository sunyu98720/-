from Public.BasePage import BasePage
from selenium.webdriver.common.by import By
from Common.Logger import WebLogger

class PersonageUser(BasePage):
    log = WebLogger("个号用户测试用例").logger
    #微信号/用户名输入框
    Wx_number_input_loc = (By.XPATH,'//*[@id="app"]/section/div[2]/section/div/form/div[1]/div[1]/div/div/div/input')

    #性别选择
    sex_select_loc = (By.XPATH,'//*[@id="app"]/section/div[2]/section/div/form/div[1]/div[2]/div/div/div/div/input')
    #性别男
    sex_select_man_loc = (By.XPATH,'/html/body/div[8]/div[1]/div[1]/ul/li[1]')
    #性别女
    sex_select_woman_loc = (By.XPATH,'/html/body/div[8]/div[1]/div[1]/ul/li[2]')
    #未知
    sex_select_unknown_loc = (By.XPATH,'/html/body/div[8]/div[1]/div[1]/ul/li[2]')

    #地区选择
    area_select_loc = (By.XPATH,'//*[@id="app"]/section/div[2]/section/div/form/div[1]/div[3]/div/div/div/div[1]/input')

    #标签选择
    label_select_loc = (By.XPATH,'//*[@id="app"]/section/div[2]/section/div/form/div[2]/div[1]/div/div/div/div/div')
    #清空标签
    label_clear_loc = (By.XPATH,'//*[@id="app"]/section/div[2]/section/div/form/div[2]/div[1]/div/div/div/div/button/span')
    #标签输入
    label_input_loc = (By.XPATH,'/html/body/div[2]/div[1]/div/input')
    #标签查询
    label_select_btn_loc = (By.XPATH,'/html/body/div[2]/div[1]/button')
    #标签选中
    label_check_first_loc = (By.XPATH,'/html/body/div[2]/div[2]/div[1]/div[1]/span[2]')

    #查询
    select_btn_loc = (By.XPATH,'//*[@id="app"]/section/div[2]/section/div/form/div[2]/div[3]/div/div/button')

    #微信查询检查点:四月一日君寻
    check_name_loc = (By.XPATH,'//*[@id="app"]/section/div[2]/section/div/div[1]/div[3]/table/tbody/tr[1]/td[2]/div')

    #查询过后的列表
    select_after_list_loc = (By.XPATH,'//*[@id="app"]/section/div[2]/section/div/div[1]/div[3]/table/tbody')



    def login_smoking(self):
        self._Scrm_login("jiao",'1')

    def Wx_number_input_loc_send_keys(self,content):
        self.find_emelemt(*self.Wx_number_input_loc).send_keys(content)
        self.log.info("微信号/用户名输入框:" + content)
    def Wx_number_input_loc_clear(self):
        self.find_emelemt(*self.Wx_number_input_loc).clear()
        self.log.info("清空微信号/用户名输入框")

    def select_btn_loc_click(self):
        self.find_emelemt(*self.select_btn_loc).click()
        self.log.info("点击查询按钮")

    def check_name_loc_text(self):
        check_text = self.find_emelemt(*self.check_name_loc).text
        self.log.info("检查点的值为:" + check_text)
        return check_text

    def label_select_loc_click(self):
        self.find_emelemt(*self.label_select_loc).click()
        self.log.info("点击标签选择")

    def label_input_loc_send_keys(self,content):
        self.find_emelemt(*self.label_input_loc).send_keys(content)
        self.log.info("标签查询框输入:" + content)

    def label_select_btn_loc_click(self):
        self.find_emelemt(*self.label_select_btn_loc).click()
        self.log.info("点击标签查询")

    def label_check_first_loc_click(self):
        self.find_emelemt(*self.label_check_first_loc).click()
        self.log.info("点击选择第一个标签")

    def select_after_list_loc_tr_list_rows(self):
        select_result = self.find_emelemt(*self.select_after_list_loc)
        rows = select_result.find_elements_by_tag_name('tr')
        self.log.info("查询结果为:" + str(len(rows)))
        return str(len(rows))

    def sex_select_loc_click(self):
        self.find_emelemt(*self.sex_select_loc).click()
        self.log.info("点击性别选择框")

    def sex_select_man_loc_click(self):
        self.find_emelemt(*self.sex_select_man_loc).click()
        self.log.info("选择性别男")





