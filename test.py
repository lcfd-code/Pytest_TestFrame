#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2020/11/9 15:36 
# @Author : lcf

from xml.etree import ElementTree as ET

# 打开文件，读取XML内容，print(str_xml)则获得整个xml文件中的内容，str_xml是个字符串
str_xml = open('xo.xml', 'r').read()


# 将字符串解析成xml特殊对象，root代指xml文件的根节点，print(root)将获取根节点的内存地址，print(root.tag)可以获取根节点的名称
root = ET.XML(str_xml)

b.解析文件方式
from xml.etree import ElementTree as ET

# 直接解析xml文件
tree = ET.parse("xo.xml")

# 获取xml文件的根节点
root = tree.getroot()