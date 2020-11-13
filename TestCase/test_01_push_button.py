#coding=utf-8
from Common.meter_info import *
import pytest
from BaseLib.AssertHandle import asserts

class Test_push_button:
    '''按健上报'''

    @classmethod
    def setup_class(cls):
        logger.info("$按健上报$")
        os.chdir(workpath_xml)


    @pytest.mark.usefixtures("login_web_company")
    def test_push_button(self):
         # if os.getenv("Testlogin")=="0":
             # pytest.skip(msg="登录模块测试失败,跳过此次测试")
          get_meter_mode()
          get_meter_balance()
          get_meter_status()
          get_me=get_web_pushstauts()
          if not get_me:
              pytest.skip(msg="查询无表具，跳过此次测试")
          push_s,push_t=push_count(2)
          if push_s==1:    #本地上报成功
              logger.info("本地上报成功")
              web_push=get_web_pushstauts(push_t)
              asserts.assertEqual(web_push['push_st'], 1, u'非当前上报时间，上报失败！')
              time.sleep(60)
          else:
              logger.info("表端手动上报失败")


