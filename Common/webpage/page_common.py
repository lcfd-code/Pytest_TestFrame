# -*- coding: UTF-8 -*-
from Common.local_element_config import *
from BaseLib.HandleImage import *
import time

'''
    公用操作
'''

class PageCommon:

    def __init__(self,driver):
        self.driver = driver

    #输入查询输入框内容
    def send_search(self,value):
        self.loading_web()
        self.driver.send_value(search_input,value)
        logger.info("查询:{}".format(value))

    #输入原始密码
    def send_original_password(self,value):
        self.driver.send_value(original_password, value)

    #输入新密码
    def send_new_password(self,value):
        self.driver.send_value(new_password, value)

    #输入确认新密码
    def send_confirm_new_password(self,value):
        self.driver.send_value(confirm_new_password, value)

    #点击提交
    def click_submit_button(self):
        self.driver.click_element(submit_pw)
        self.loading_web()

    #点击退出
    def click_logout(self):
        self.driver.click_element(logout)
        self.loading_web()

    #点击确认退出
    def click_confirm_logout(self):
        self.driver.click_element(confirm_logout)
        self.loading_web()

    #点击查询按钮
    def click_search_button(self):
        try:
           self.driver.click_element(search_button)
        except:
            self.driver.click_element(search_button)
        time.sleep(2)
        self.loading_web()


    #获取查询结果
    def get_search_results(self):
        text = self.driver.get_element_text(search_results)
        return text


    #点击新增按钮
    def click_add_button(self):
        self.driver.click_element(add_button)
        logger.info("新增")

    # 点击删除按钮
    def click_delete_button(self):
        logger.info("删除")
        try:
            self.driver.click_element(delete_button)
        except:
            logger.info("没有数据可删除")
        self.loading_web()
    # 点击修改按钮
    def click_update(self):
        self.driver.click_element(update_button)
        self.loading_web()
        logger.info("修改")

    # 点击批量按钮
    def click_batch_button(self):
        self.driver.click_element(batch_button)
        logger.info("批量导入")


    # 点击下载模板
    def click_download_template(self):
        self.driver.click_element(download_template)

    #点击保存按钮
    def click_save_button(self):
        time.sleep(1)
        self.driver.action_click(save_button)
        time.sleep(0.5)
        logger.info("点击保存")
        self.loading_web()

    #点击保存按钮
    def click_save_button_t(self):
        self.driver.click_element(save_button_t)
        logger.info("点击保存")
        self.loading_web()

    #点击取消按钮
    def click_cancel_button(self):
        self.driver.click_element(cancel_button)

    #点击pop-up 确定按钮
    def click_pop_up_determine(self):
        self.driver.click_element(pop_up_determine)

    #点击pop-up 确认按钮
    def click_pop_up_confirm(self):
        self.driver.click_element(pop_up_confirm)

    # 点击pop-up 取消按钮
    def click_pop_up_cancel(self):
        self.driver.click_element(pop_up_cancel)

    # 点击pop-up 复制按钮`
    def click_pop_up_copy(self):
        self.driver.click_element(pop_up_copy)



    # 点击 日历确定 清空
    def click_calendar_empty(self):
        self.driver.click_element(calendar_empty)

    # 点击 左边全屏按钮
    def click_full_screen_left(self):
        self.driver.click_element(full_screen_left)

    # 点击 右边全屏按钮
    def click_full_screen_right(self):
        self.driver.click_element(full_screen_right)




    #点击显示全部
    def click_show_all(self):
        self.driver.click_element(show_all)
        time.sleep(2)

    #点击是
    def click_is_button(self):
        try:
            self.driver.click_element(is_button)
        except:
            logger.info("没有找到'是'按钮")
    #点击否
    def click_no_button(self):
        self.driver.click_element(no_button)
        try:
            self.driver.click_element(is_button)
        except:
            logger.info("没有找到'否'按钮")

    #获取toast 消息提示
    def get_pop_up_toast(self):
        toast = self.driver.get_element_text(pop_up_toast)
        logger.info("当前toast:{}".format(toast))
        #slm_screen(self.driver.get_web_driver())
        return toast

    #点击筛选
    def click_screening(self):
        self.driver.click_element(screening)



    #点击发送按钮
    def click_send_button(self):
        self.driver.click_element(send_button)

    #点击我知道了
    def click_batch_info_btn(self):
        self.driver.click_element(batch_info_btn)

    #输入密码 /批量操作密码输入框
    def send_password(self,value):
        self.driver.send_value(batch_send_password,value)

    def click_admin(self):
        self.driver.click_element(admin_web)

    def click_aboutus(self):
        self.driver.click_element(about_us)
    """
        检查页面加载
    """
    def loading_web(self):
        for i in range(30):
            results = self.driver.is_element_exist(ribbon,0.5)
            if not results:
                break
