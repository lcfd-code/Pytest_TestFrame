# -*- coding: UTF-8 -*-
import time

from Common import local_element_config
from Common.webpage.page_login import *
from BaseLib.web.SeleniumDriver import driver

'''
获取表具信息
'''
class PageTableInformation():
    def __init__(self,driver):
        self.driver = driver

    def table_number(self,url=table_manage_url):
        self.driver.open_url(url)
        self.driver.click_element(gascompang)
        local_element_config.change_value = "张家港燃气"
        self.driver.click_element(gass)
        if not self.driver.is_element_exist(no_message,timeout=3):
             table_number = self.driver.get_elements(table_num)
             return table_number
        else:
            logger.info(u'该燃气公司下无表具')
        return None

if __name__ == '__main__':
    driver.browser(driver.Chrome)
    get = Pagelogin(driver)
    get.user_login()
    get_massage = PageTableInformation(driver)
    lsit_driver = get_massage.table_number()
    for i in lsit_driver:
        print(i.text)
    driver.close()


