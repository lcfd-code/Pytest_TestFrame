# -*- coding: UTF-8 -*-
from Common.local_element_config import *
from BaseLib.LoggerConfig import *
'''
    登录操作
'''

class Pagelogin():

    def __init__(self,driver):
        self.driver = driver

      #登录
    def user_login(self,url=admin_url,user='liying',password='123456'):
        self.driver.open_url(url)
        self.driver.send_value(username_edt,user)
        self.driver.send_value(password_edt,password)
        self.driver.click_element(btnLogin_but)

    def login_is_suc(self):
        if self.driver.is_element(header_web):
            logger.info(u"登录平台成功")
            return True
        else:
             logger.error(u"登录平台失败")
             return False

if __name__=='__main__':
    from BaseLib.web.SeleniumDriver import driver
    driver.browser(driver.Chrome)
    Pg=Pagelogin(driver)
    Pg.user_login()
    print(Pg.login_is_suc())
    #driver.close()


