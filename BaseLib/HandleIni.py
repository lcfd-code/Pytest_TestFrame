# -*- coding: UTF-8 -*-
from BaseLib.HandleFile import file_utils
import configparser



class HandleIni(object):
    file_name = "data/data.ini"

    def __init__(self):
        self.data = self.loading_ini()

    '''定位ini文件'''

    def loading_ini(self):
        file_path = file_utils.location_file(self.file_name)
        file = configparser.ConfigParser()
        file.read(file_path, encoding='UTF-8')
        return file

    def get_key(self, key, value):
        if key and value:
            return self.data.get(key, value)
        else:
            print("你输入的参数有误")

    def get_data(self):
        data_list = {}
        for key,value in self.data.items("test_data"):
            data_list[key] = value
        return data_list


handle_ini = HandleIni()
if __name__ == '__main__':

    print(handle_ini.get_data())