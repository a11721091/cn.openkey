# coding=UTF-8
import configparser


class ReadIni:
    def __init__(self, file_path=None):
        if file_path is None:
            self.file_path = '../config/Local_Element_Openkey.ini'
        else:
            self.file_path = file_path
        self.data = self.read_ini()

    # 读取ini文件
    def read_ini(self):
        read_ini = configparser.ConfigParser()
        read_ini.read(self.file_path)
        return read_ini

    # 通过参数Key获取对应value
    def get_value(self, key, section='login_element'):
        try:
            value = self.data.get(section, key)
        except:
            value = None
        return value


if __name__ == '__main__':
    read_ini = ReadIni()
    print(read_ini.get_value('login_button', 'login_element'))