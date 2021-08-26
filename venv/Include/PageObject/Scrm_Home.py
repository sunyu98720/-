from Public.BasePage import BasePage
from selenium.webdriver.common.by import By


class Home(BasePage):
    HomePage_info_loc = (By.XPATH,'//*[@id="app"]/section/div[1]/div[1]')


    def login_btn_text(self):
        return self.find_emelemt(*self.HomePage_info_loc).text

    def cut_handle(self):
        self.switch_to_handle()