# coding=utf-8

from util.dos_command import DosCommand
from util.port import Port
from util.write_user_command import WriteUserCommand
import time


class Sever:
    def __init__(self):
        self.dos = DosCommand()
        self.udid_list = self.get_udid()
        self.write_file = WriteUserCommand()

    def get_udid(self):
        """
        获取设备信息
        """

        devices_list = []
        result_list = self.dos.excute_command_result(
            'system_profiler SPUSBDataType | grep "Serial Number:.*" | sed s#".*Serial Number: "##')
        if result_list is not None:
            for i in result_list:
                devices_info = i
                devices_list.append(devices_info)
            return devices_list

    def create_port_list(self, start_port):
        """
        创建可用端口
        :return:
        """
        port = Port()
        port_list = []
        port_list = port.create_port_list(start_port, self.udid_list)
        return port_list

    def create_command_list(self, i):
        """
        appium -p 4700 -bp 4701 -U "udid"
        生成命令

        :return:
        """

        command_list = []
        appium_port_list = self.create_port_list(4700)
        bootstrap_port_list = self.create_port_list(4900)
        command = "appium -p " + str(appium_port_list[i]) + " --webdriveragent-port " + str(bootstrap_port_list[i]) + " -U " + \
                  self.udid_list[i] + " --session-override"
        # --no-reset 不重新安装app
        print(command)
        command_list.append(command)
        self.write_file.write_data(i, self.udid_list[i], str(bootstrap_port_list[i]), str(appium_port_list[i]))
        return command_list

    def start_sever(self, i):
        """
        启动Appium服务
        :param i:
        :return:
        """
        self.start_list = self.create_command_list(i)
        self.dos.excute_command('pwd')
        self.dos.excute_command(self.start_list[i]+" &")

    def killall_sever(self):
        self.dos.excute_command('killall -9 node')
        self.dos.excute_command('killall -9 iproxy')

    def main(self):
        self.killall_sever()
        self.write_file.clear_data()
        self.start_sever(0)
        time.sleep(10)


if __name__ == '__main__':
    sever = Sever()
    print(sever.get_udid())
