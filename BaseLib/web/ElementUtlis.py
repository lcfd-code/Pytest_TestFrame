# -*- coding: UTF-8 -*-
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, ElementNotInteractableException
from BaseLib.LoggerConfig import logger
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from BaseLib.web.WebDriverWait import WebDriverWait
from Common import local_element_config
from pykeyboard import PyKeyboard
import time


class ElementUtlis(object):

    def __init__(self, browser, configuration_file_download, local):
        self.driver = self.__open_browser(browser, configuration_file_download, local)
        self.pkb = PyKeyboard()
        self.timeout = 3
        local_element_config.change_value = None

    '''

    配置浏览器
    chrome:
        #download.default_directory：设置下载路径
        #profile.default_content_settings.popups：设置为 0 禁止弹出窗口
    firefox:
        browser.download.dir：指定下载路径
        browser.download.folderList：设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；设置成 1 表示下载到默认路径
        browser.download.manager.showWhenStarting：在开始下载时是否显示下载管理器
        browser.helperApps.neverAsk.saveToDisk：对所给出文件类型不再弹出框进行询问

    '''

    def __open_browser(self, browser, configuration_file_download, local):

        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if configuration_file_download:
                prefs = {"profile.default_content_settings.popups": 0,
                         "download.default_directory": configuration_file_download}
                options.add_experimental_option("prefs", prefs)
            if local:
                options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
            driver = webdriver.Chrome(options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if configuration_file_download:
                options.set_preference("browser.download.dir", configuration_file_download)
                options.set_preference("browser.download.folderList", "2")
                options.set_preference("browser.download.manager.showWhenStarting", False)
                options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/zip")
            driver = webdriver.Firefox(options=options)
        elif browser == "ie":
            driver = webdriver.Ie()
        elif browser == "PhantomJS":
            driver = webdriver.PhantomJS()
        else:
            driver = webdriver.edge()

        return driver

    '''
       获取windows屏幕大小
    '''

    def get_win_size(self):
        return self.driver.get_window_size()

    '''
        获取页面info元素
        @parame info 元素定位的信息
        @return 查找成功返回一个元素 element  
    '''

    def get_element(self, info):
        by, value = self.get_local_element(info)
        print(value)
        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "class":
            element = self.driver.find_element_by_class_name(value)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)
        elif by == "text":
            element = self.driver.find_element_by_link_text(value)
        else:
            element = self.driver.find_element_by_xpath(value)
        return element

    '''
        显性等待查找元素
        @parame info 定位元素的信息
    '''

    def wait_element(self, info, timeout=3):

        return WebDriverWait(self.driver, timeout).until(self.get_element, info, local_element_config.change_value)

    """
        获取页面所有info元素
        @parame info 元素定位的信息
        @return elements 返回一个列表
    """

    def get_elements(self, info):
        ele_list = []
        by, value = self.get_local_element(info)
        if by == "id":
            elements = self.driver.find_elements_by_id(value)
        elif by == "name":
            elements = self.driver.find_elements_by_name(value)
        elif by == "class":
            elements = self.driver.find_elements_by_class_name(value)
        elif by == "css":
            elements = self.driver.find_elements_by_css_selector(value)
        elif by == "text":
            return self.driver.find_elements_by_link_text(value)
        else:
            elements = self.driver.find_elements_by_xpath(value)

        return elements

    """
        显性等待获取页面所有info元素
        @parame info 元素定位的信息
        @return elements 返回一个列表
    """

    def wait_elements(self, info, timeout=12):
        return WebDriverWait(self.driver, timeout).until(self.get_elements, info)

    """
        通过当前节点定位子节点
        current_by:当前节点查找方式
        current_vlaue：当前节点元素信息
        info_by:子节点查找方式
        info_value:子节点元素信息
    """

    def get_leve_element(self, info_level, info_node):
        node_by, node_value = self.get_local_element(info_node)
        element = self.get_element(info_level)
        if element == False:
            return False
        if node_by == "id":
            node_element = element.find_element_by_id(node_value)
        elif node_by == "name":
            node_element = element.find_element_by_name(node_value)
        elif node_by == "class":
            node_element = element.find_element_by_class_name(node_value)
        elif node_by == "css":
            node_element = element.find_element_by_css_selector(node_value)
        elif node_by == "text":
            return self.driver.find_elements_by_link_text(node_value)
        else:
            node_element = element.find_element_by_xpath(node_value)
        return node_element

    """
        打开url网页     
    """

    def __get_url(self, url):
        self.driver.set_page_load_timeout(60)
        if self.driver != None:
            if 'http' in url:
                logger.info("测试线上网页:{0}".format(url))
                self.driver.get(url)
            elif 'C' or 'D' or 'E' in url:
                self.driver.get(url)
            else:
                logger.info("测试本地网页:{0}".format(url))
        else:
            logger.info("你传入的url路径有误:{0}".format(url))

        time.sleep(3)

    """
        打开url网页,并判断当前网页title_name是否符合预期   
    """

    def open_url(self, url):
        self.__get_url(url)

    '''
        判断元素是否存在页面
    '''

    def is_element_exist(self, info, timeout):
        try:
            self.wait_element(info, timeout)
        except:
            return False
        return True

    """
        输入文件路径,并按Ener
        file_path:文件路径
    """
    def __upload_file(self,file_path):
        self.pkb.type_string(file_path)
        time.sleep(2)
        self.pkb.tap_key(self.pkb.return_key)
        self.pkb.tap_key(self.pkb.return_key)

    """
        浏览器操作
    """

    def handle_windows(self, *args):
        value = len(args)
        if value == 1:
            if args[0] == "max":
                self.driver.maximize_window()
            elif args[0] == "min":
                self.driver.minimize_window()
            elif args[0] == "back":
                self.driver.back()
            elif args[0] == "go":
                self.driver.forward()
            elif args[0] == "refresh":
                self.driver.refresh()
            elif args[0] == "F5":
                ActionChains(self.driver).key_down(Keys.CONTROL).send_keys(Keys.F5).key_up(Keys.CONTROL).perform()
        elif value == 2:
            self.driver.set_window_size(args[0], args[1])
        else:
            logger.info("你传递的参数有问题")

    """
        根据传入的title_name，切换到相对应网页
    """

    def switch_web_name(self, title_name):
        hander_list = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in hander_list:
            if i != current_handle:
                self.driver.switch_to.window(i)
                if self.assert_title(title_name):
                    break

    """
        根据index，切换到相对应网页
    """

    def switch_web_index(self, index):
        hander_list = self.driver.window_handles
        if index > len(hander_list):
            logger.error("index < current_window_handle")
            raise Exception("index < current_window_handle ", index)
        self.driver.switch_to.window(hander_list[index - 1])

    """
        根据index，切换到相对应网页
    """

    def close_web_name(self, close_web_name, show_web_name):
        hander_list = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        for i in hander_list:
            if i != current_handle:
                self.driver.switch_to.window(i)
                if self.assert_title(close_web_name):
                    self.driver.close()
                    if close_web_name == show_web_name:
                        break
                    close_web_name = show_web_name
                    close_web_name(close_web_name, show_web_name)

    """
        输入值
    """

    def send_value(self, info, key):
        element = None
        try:
            element = self.wait_element(info, timeout=10)
            element.clear()
        except:
            print("元素{}查找失败".format(info))
            return
        element.send_keys(key)
        logger.info("输入值:{}".format(key))

    """
        显性等待获取到元素，并点击元素
        info:元素信息
    """

    def click_element(self, info):

        element = self.wait_element(info)
        try:
            self.driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
        except StaleElementReferenceException:
            self.click_element(info)

    """
        提交表单
        info:元素信息
    """

    def submit_from(self, info, timeout=20):
        self.wait_element(info, timeout).submit()
        logger.info("提交表单:{}".format(info))

    '''
        点击check元素
    '''

    def check_box_is_selected(self, info, check=False):
        element = self.wait_element(info)
        flag = element.is_selected()
        if check != flag:
            self.wait_element(info).click()

    '''
    通过index的值来设置 Select下拉框
    '''

    def set_selected_Index(self, info, value_index):
        selected_element = self.get_element(info)
        Select(selected_element).select_by_index(value_index)
        logger.info("设置值:{}".format(value_index))

    '''
    通过value的值来设置 Select下拉框
    '''

    def set_selected_Value(self, info, value):
        selected_element = self.get_element(info)
        Select(selected_element).select_by_value(value)
        logger.info("设置值:{}".format(info))

    '''
    通过visible_text的值来设置 Select下拉框
    '''

    def set_selected_visible_text(self, info, visible_text):
        selected_element = self.wait_element(info)
        Select(selected_element).select_by_visible_text(visible_text)
        logger.info("设置值:{}".format(visible_text))



    '''
        上传文件
        file_name:文件路径
        info:非input类型上传文件/上传按钮元素信息
        send_info:input类型上传文件/input元素信息
    '''

    def upload_file_function(self, file_name, info=None, send_info=None):
        if send_info:
            self.send_value(send_info, file_name)
        else:
            self.wait_element(info).click()
            time.sleep(5)
            self.__upload_file(file_name)

    '''
    设置日历的值
    info:日历元素元素信息
    value:需要修改的值
    '''

    def set_calendar_value(self, info, value):
        element = self.wait_element(info)
        try:
            element.get_attribute("readonly")
            self.__js_execute_calendar(info)
        except:
            print("日历中没有readonly属性，可读可写")
        element.clear()
        self.send_value(info, value)

    '''
       隐藏一个元素的样式
       info：定位元素的信息
    '''

    def js_hidden_style(self, info):
        try:
            self.driver.execute_script("arguments[0].style.display='none';", self.wait_element(info))
        except:
            logger.info("没有日历需要隐藏")

    '''
       显示一个元素的样式
       info：定位元素的信息
    '''

    def js_show_style(self, info):
        self.driver.execute_script("arguments[0].style.display='block';", self.wait_element(info))

    '''
        显示一个元素的样式
        info：定位元素的信息
     '''

    def js_update_attribute(self, info, key, value):
        print("arguments[0].{}='{}';".format(key, value))
        self.driver.execute_script("arguments[0].data-bv-result='none';", self.wait_element(info))

    '''
    将鼠标移动到一个元素上面
    info：定位元素的信息
    '''

    def moveto_element_mouse(self, info):
        element = self.wait_element(info)
        ActionChains(self.driver).move_to_element(element).perform()


    '''
    将鼠标移动到一个元素上面
    info：定位元素的信息
    '''

    def action_click(self, info):
        element = self.wait_element(info)
        ActionChains(self.driver).click(element).perform()

    '''
    将鼠标移动到一个元素上面
    info：定位元素的信息
    '''

    def moveto_element_click(self, info):
        element = self.wait_element(info)
        ActionChains(self.driver).move_to_element(element).click()

    '''
    将鼠标移动到一个元素上面
    info：定位元素的信息
    '''

    def moveto_element_send_keys(self, info, value):
        element = self.wait_element(info)
        ActionChains(self.driver).move_to_element(element).send_keys(value)

    '''
    切换iframe
    '''

    def switch_iframe(self, info):
        if info != None:
            iframe_element = self.wait_element(info)
            self.driver.switch_to_frame(iframe_element)
        else:
            self.driver.switch_to_default_content()

    '''
    点击系统弹框
    '''

    def switch_alert(self, info, value=None):
        if info == "accept":
            if value:
                self.driver.switch_to_alert().send_keys(value)
            self.driver.switch_to_alert().accept()
        else:
            self.driver.switch_to_alert().dismiss()

    '''
    滚动查找一个元素
    '''

    def scroll_element(self, info):
        js = 'document.documentElement.scrollTop=1000;'
        try:
            self.wait_element(info)
        except:
            self.driver.execute_script(js)
            pass

    '''
    得到当前网页的cookie数据
    '''

    def get_cookie(self):
        return self.driver.get_cookies()

    '''
      设置网页cookie
    '''

    def set_cookie(self, cookie):
        self.driver.delete_all_cookies()
        time.sleep(2)
        self.driver.add_cookie(cookie)

    def get_element_text(self, info):
        try:
            text = self.wait_element(info).text
            logger.info("获取的文本信息值:{}".format(text))
            return text
        except:
            return None

    def is_element_text(self, info, text):
        try:
            return text in self.get_element_text(info)
        except:
            return False

    def get_element_value_text(self, info):
        try:
            text = self.wait_element(info).get_attribute("value")
            logger.info("获取的文本信息值:{}".format(text))
            return text
        except:
            return None

    def get_element_tag_text(self, info, tag):
        if self.get_element(info) != False:
            return self.wait_element(info).get_attribute(tag)



    def get_element_attribute(self, info, tag):
        if self.get_element(info) != False:
            return self.wait_element(info).get_attribute(tag)

    '''
        设置网页加载超时
    '''

    def set_web_load_timeout(self, timeout=10):
        self.driver.set_page_load_timeout(timeout)

    '''
       关闭浏览器
    '''

    def close(self):
        self.driver.close()
        self.driver.quit()
        logger.info("关闭浏览器")

    '''
        得到本地元素信息
    '''

    def get_local_element(self, info):
        if "{}" in info:
            info = info.format(local_element_config.change_value)
        return self.parsing_content(info)

    def parsing_content(self, text_content):
        if text_content:
            return text_content.split("<")
        else:
            logger.info("传入的参数不正确")

    def save_screen(self, image_name):
        return self.driver.save_screenshot(image_name)

    def get_web_driver(self):
        return self.driver




