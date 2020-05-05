# coding=utf-8

import yaml


class WriteUserCommand:
    def read_data(self):
        """
        读取yaml文件
        :return:
        """
        with open("../config/user_config.yaml") as fr:
            data = yaml.load(fr)
        return data
    
    def get_value(self, key, port):
        """
        获取yaml的value
        :return:
        """
        data = self.read_data()
        value = data[key][port]
        return value
    
    def write_data(self, i, udid, bp, port):
        """
        写入数据
        :param port:
        :param bp:
        :param udid:
        :param i:
        :return:
        """
        data = self.join_data(i, udid, bp, port)
        with open("../config/user_config.yaml", "a") as fr:
            yaml.dump(data, fr)
    
    def join_data(self, i, udid, bp, port):
        """
        拼接数据
        :return:
        """
        
        # data = {'user_info_' + str(i): {'udid': udid,'bp': bp,'port': port}}
        data = {
            'user_info_' + str(i): {
                'udid': udid,
                'bp': bp,
                'port': port
            }
        }
        return data
    
    def clear_data(self):
        with open("../config/user_config.yaml", "w") as fr:
            fr.truncate()
        fr.close()


if __name__ == '__main__':
    # i=1
    # udid='4700'
    # bp='4900'
    # udid='ujidkshfjk11'
    write_file = WriteUserCommand()
    # write_file.write_data('5', 'ffoe829kas0001', '4900', '4700')
    print(write_file.get_value('user_info_0', 'port'))
