# -*- coding: UTF-8 -*-
import sys
from BaseLib.AssertHandle import asserts
from Common.busines.gmtp_login import Login
from Common.meter_info import *
from BaseLib.HandleIni import handle_ini

"""
    登录模块
"""

class Testlogin:



    @classmethod
    def setup_class(cls):
        logger.info("$登录模块$")
        cls.login = Login(driver)
        cls.data = handle_ini.get_data()


    # @pytest.mark.addmeter
    # @pytest.mark.flaky(reruns=2,reruns_delay=2)
    @pytest.mark.deletemeter
    @pytest.mark.usefixtures("init_web")
    def test_login(self):
        logger.info("$登录$")
        logger.info("当前运行方法=======>{}".format(sys._getframe().f_code.co_name))
        self.login.user_login(user_url, self.data["user"],  self.data["password"])


        lt = self.login.login_toast()

        asserts.assertFalse(lt, "登录模块测试失败{}:".format(lt))

        rl = self. login.login_results()
        asserts.assertTrue(rl, "登录模块测试失败:我的首页文字检查失败")


        os.environ["Testlogin"]="1"
       # web_version=self.login.get_web_version()[4:]
       # meter_version = get_meter_version()

    def teardown_class(self):
        logger.info("=================测试结束=================")


