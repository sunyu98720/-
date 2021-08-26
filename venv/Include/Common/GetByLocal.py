from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class GetByLocal:

    def __init__(self, driver):
        self.driver = driver

    def get_local_element(self, key):
        u"""
        :param key:
        :return:
        """
        by = key.split('=')[0]
        by_value = key.split('=',1)[1]
        if by == 'id':
            return self.driver.find_element_by_id(by_value)
        elif by == 'name':
            return self.driver.find_element_by_name(by_value)
        elif by == 'className':
            return self.driver.find_element_by_class_name(by_value)
        else:
            return self.driver.find_element_by_xpath(by_value)
