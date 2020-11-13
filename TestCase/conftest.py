#-*- coding: UTF-8 -*-
import pytest,re
from BaseLib.HandleImage import *
from BaseLib.web.SeleniumDriver import driver
from  Common.local_element_config import *
from Common.busines.gmtp_login import Login
from BaseLib.HandleIni import handle_ini
data = handle_ini.get_data()


#登录模块/登录
os.environ["Testlogin"] = "0"
#燃气公司模块/新增燃气公司
os.environ["test_add_ags"] = "0"
#登录燃气公司模/登录
os.environ["test_transfer"] = "0"
#角色管理模块/新增角色
os.environ["test_add_role"] = "0"
#账号管理模块/新增账号
os.environ["test_add_account"] = "0"
#地址管理模块/新增地址
os.environ["test_add_address"] = "0"
#表具配置模块/新增表具配置
os.environ["test_add_meter_config"] = "0"
#计费配置模块/新增计费配置
os.environ["test_add_billing_config"] = "0"
#表具信息模块/新增表具
os.environ["test_add_meter"] = "0"
#开户模块/新增用户
os.environ["test_add_account"] = "0"
#挂表模块/挂表
os.environ["test_hang_table"] = "0"
#批量升级模块/批量升级
os.environ["test_upgrade_table"] = "0"
#过户模块/过户
os.environ["test_transfer_user"] = "0"
#换表模块/换表
os.environ["test_barter_table"] = "0"
#销户模块/销户
os.environ["test_account_destory"] = "0"
#批量导入/表具
os.environ["test_batch_table"] = "0"
#批量导入/开户
os.environ["test_batch_account"] = "0"






@pytest.mark.hookwrapper
def pytest_runtest_makereport():
    outcome = yield
    report = outcome.get_result()
    if "TestCase" in str(report):
        image_name = re.findall(".*TestCase/(.*)\.py.*", str(report))[0]
    else:
        image_name = re.findall(".*'(.*)\.py.*", str(report))[0]
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            fail_time = datetime.datetime.now().strftime('%H%M%S')
            try:
              slm_screen(driver.get_web_driver(),img_name="{}_{}".format(image_name,fail_time))
            except:
                logger.info("非WEB错误")

"""
    用于测登录模块
"""
@pytest.fixture(scope="function")
def init_web():
    driver.browser(driver.Chrome)
    driver.handle_windows(driver.Max)

"""
    用于测需登录之后的模块
"""



@pytest.fixture(scope="session")
def login_web_admin():
    driver.browser(driver.Chrome)
    driver.handle_windows(driver.Max)
    lg = Login(driver)
    for i in range(0,3):
        lg.user_login(user= data["admin_user"],password=data["admin_password"])
        if lg.is_home_title():
           break



@pytest.fixture(scope="session")
def login_web_company():
    driver.browser(driver.Chrome)
    driver.handle_windows(driver.Max)
    lg = Login(driver)
    for i in range(3):
        lg.user_login(user_url,data["user"], data["password"])
        if lg.is_home_title():
            break