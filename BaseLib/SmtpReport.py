# -*- coding: UTF-8 -*-
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header              # Header 用来构建邮件头
from BaseLib.HandleImage import *
from BaseLib.HandleFile import file_utils
from PIL import Image
import numpy as np
import smtplib



class SmtpReport:


    def __init__(self,msg_to):
        self.host = 'smtp.fiorentini.com.cn'
        self.msg_from = 'pengxz@fiorentini.com.cn' # 发送方邮箱
        self.passwd = 'SFpxz123'  # 填入发送方邮箱的授权码
        self.msg_to=msg_to


    def send_email(self,subject,image_path,report_path):

        msg = MIMEMultipart('related')
        content = MIMEText('<html><body><img src="cid:imageid" alt="imageid"></body></html>', 'html', 'utf-8')  # 正文
        msg.attach(content)
        msg['Subject'] = Header(subject)
        msg['From'] =Header(self.msg_from)
        msg['To'] =  Header(",".join(self.msg_to))
        if not os.path.exists(image_path):
            return print("图片路径不存在")
        with open(image_path, "rb") as file:
            img_data = file.read()
        file.close()
        img = MIMEImage(img_data)
        img.add_header('Content-ID', 'imageid')
        msg.attach(img)

        att1 = MIMEText(open(report_path, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename=TestReport.html'
        msg.attach(att1)

        try:
            server = smtplib.SMTP_SSL(self.host,465)
            server.login(self.msg_from, self.passwd)  # 仅smtp服务器需要验证时
            server.sendmail(self.msg_from, self.msg_to, msg.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")

    def email_image_send(self, report_path, title):
        report_png = "logs\image\\report.png"
        driver.browser(driver.Chrome)
        driver.open_url(file_utils.location_file(report_path))
        driver.handle_windows(driver.Max)
        time.sleep(2)
        web_driver = driver.get_web_driver()
        ele_list = web_driver.find_elements_by_xpath('//*[@type="case"]');
        for element in ele_list:
            web_driver.execute_script('arguments[0].setAttribute("class","hiddenRow");', element)
        time.sleep(3)
        window_height = web_driver.get_window_size()['height']  # 窗口高度
        page_height = web_driver.execute_script('return document.documentElement.scrollHeight')  # 页面高度
        image_path = slm_screen(driver.get_web_driver())
        # if page_height > window_height:
        count = page_height // window_height  # 需要滚动的次数
        base_mat = np.atleast_2d(Image.open(image_path))  # 打开截图并转为二维矩阵
        for i in range(count):
            web_driver.execute_script('document.documentElement.scrollTop={};'.format(window_height * (i + 1)))
            time.sleep(0.5)
            img_joint = slm_screen(driver.get_web_driver())
            mat = np.atleast_2d(Image.open(img_joint))  # 打开截图并转为二维矩阵
            base_mat = np.append(base_mat, mat, axis=0)  # 拼接图片的二维矩阵
            os.remove(img_joint)
        Image.fromarray(base_mat).save(file_utils.location_file(report_png))
        self.send_email(title, file_utils.location_file(report_png),report_path)
        os.remove(image_path)  # 移除截图
        os.remove(file_utils.location_file(report_png))  # 移除截图
        driver.close()
