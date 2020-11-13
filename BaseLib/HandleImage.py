# -*- coding: UTF-8 -*-
import datetime
import os

from BaseLib.HandleFile import file_utils
from BaseLib.LoggerConfig import logger
from BaseLib.web.SeleniumDriver import driver

'''
   整个页面截图
'''
def slm_screen(driver,img_name=None,file_path="logs/image"):
    if not img_name:
        img_name = datetime.datetime.now().strftime('%H%M%S')
    dir_patn = file_utils.location_file("{}/{}".format(file_path,  datetime.datetime.now().strftime("%Y-%m-%d")))
    if not os.path.exists(dir_patn):
        file_utils.mkdir_path(dir_patn)
    path = file_utils.location_file("{}/{}.png".format(dir_patn, img_name))
    logger.info(path)
    driver.save_screenshot(path)
    logger.info("保存截图:{}".format(path))
    return path


if __name__ == '__main__':
    driver.browser(driver.Chrome,local=True)
    driver.handle_windows(driver.Max)
    slm_screen(driver.get_web_driver())