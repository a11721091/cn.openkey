# coding=utf-8
from util.dos_command import DosCommand


class Port:
    def port_is_used(self, port_num):
        """
        判断端口是否被占用
        :param port_num:
        :return:
        """
        self.dos = DosCommand()
        result = self.dos.excute_command_result('lsof -i tcp:' + str(port_num))
        if len(result) > 0:
            flag = True
        else:
            flag = False
        return flag

    def create_port_list(self, start_port, udid_list):
        """
        生成可用端口
        :param start_port:
        :param udid_list:
        :return:
        """
        port_list = []
        if udid_list is not None:
            while len(port_list) != len(udid_list):
                if not self.port_is_used(start_port):
                    port_list.append(start_port)
                start_port = start_port + 1
            return port_list
        else:
            print('生成可用端口失败')
            return None


if __name__ == '__main__':
    port = Port()
    li = [1, 2, 3, 4, 5]
    # print port.port_is_used('4723')
    print(port.create_port_list(4723, li))
