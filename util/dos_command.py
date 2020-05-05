# coding=utf-8
import os

class DosCommand:
    def excute_command_result(slef, command):
        result_list = []
        result = os.popen(command).readlines()
        if len(result) == 0:
            return result
        else:
            for i in result:
                if i == '00E04C360082\n':
                    continue
                result_list.append(i.strip('\n'))
            return result_list

    def excute_command(self, command):
        # commands.getstatusoutput(command)
        os.system(command)


if __name__ == '__main__':
    dos = DosCommand()
    print(dos.excute_command_result('system_profiler SPUSBDataType | grep "Serial Number:.*" | sed s#".*Serial Number: "##'))
    # print dos.excute_command_result('lsof -i tcp:8080')