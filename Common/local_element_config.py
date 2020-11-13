#-*- coding: UTF-8 -*-
__author__ = 'selenium_local'
__version_ = '2020104'
'''
    url 链接 方便网页自动化快速进行测试
'''
global change_value

url = 'http://180.169.51.178:18067'
#=====================================登录模块=====================================
admin_url= "%s/login"%url

#=====================================表具管理=====================================
table_manage_url ='%s/pages/meters/info'%url               #表具信息

#=====================================用户管理=====================================
user_account_url = '%s/pages/users/account'%url            #账户管理
user_role_url = '%s/pages/users/role'%url                  #角色管理

#=====================================系统日志=====================================
logs_updatlog = '%s/pages/logs/update-log'%url             #更新日志
logs_communication = '%s/pages/logs/commu-log'%url         #通讯日志

'''
    element 定位信息
'''

#===============================================公用元素=========================================


#===============================================登录模块========================================= page 已完成
username_edt = 'xpath<//*[@id="accountNumber"]' 										#用户名输入框
password_edt = 'xpath<//*[@id="accountPassword"]' 										#密码输入框
btnLogin_but = 'xpath<//*[@id="loginBtn"]' 												#登录按钮


#===============================================首页============================================ page 已完成

header_web = 'xpath<//*[@id="header"]' 		  										    #我的首页文本

#===============================================表具信息========================================= page 已完成
'''
表具信息获取
'''
serial_number = 'xpath<//td[@class="ant-table-cell"][1]'                                    #序号
table_num = 'xpath<//td[@class="ant-table-cell"][2]'                                        #表号
last_pushtime = 'xpath<//td[@class="ant-table-cell"][3]'                                    #最后上报时间
mater_reading = 'xpath<//td[@class="ant-table-cell"][4]'                                    #表读数（m³）
module_msg = 'xpath<//td[@class="ant-table-cell"][5]'                                       #模组(imei)
data_platform = 'xpath<//td[@class="ant-table-cell"][6]'                                    #数据平台
manager = 'xpath<//td[@class="ant-table-cell"][7]'                                          #管理者
pocket_time = 'xpath<//td[@class="ant-table-cell"][8]'                                      #挂表时间
operation = 'xpath<//td[@class="ant-table-cell"][9]'                                        #操作
manage_tptal= "xpath<//div[@class='ng-star-inserted']"                                      #表具总数
no_message = 'xpath<//*[text()=" 无数据 "]'                         #无数据

'''
表具信息操作
'''
gascompang: str = "xpath<//*[@name='gasCompany']/descendant::input"                                            # 燃气公司
gass ="xpath<//*[text()='{}']"
test_platfprm = "xpath<//*[@name='testPlatform']"                                       # 通讯方式
com_status = "xpath<//*[@name='state']"                                                 # 通讯状态
search = 'xpath<//*[id="code"]'                                                         # 搜索框
start_test = 'xpath<//div[@class="ng-star-inserted"]'                                   # 开始测试
transfer = 'xpath<//div[@class="transfer "]'                                            # 转让
detail = 'xpath<//div[@class="detail"]'                                                 # 详情
delete = 'xpath<//a[@class="delete"]'                                                   # 注销
add_table = "xpath<//button[@id='addMeterBtn']"                                         # 新增
batch_adding = "xpath<//button[@id='addMetersBtn']"                                     # 批量新增
batch_delete = "xpath<//button[@id='deleteMetersBtn']"                                  # 批量注销

'''

'''