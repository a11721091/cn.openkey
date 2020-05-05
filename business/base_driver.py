import time
from appium import webdriver
from util.write_user_command import WriteUserCommand
from util.sever import Sever


class BaseDriver:
    # def __init__(self):
        # self.s = Sever()
        # self.s.main()
        
    def ios_driver(self, app_path='/Users/llc/Desktop/App/Payload01/OpenkeyHomestay.app'):
        # udid
        # port
        write_file = WriteUserCommand()
        udid = write_file.get_value('user_info_0', 'udid')
        port = write_file.get_value('user_info_0', 'port')
        capabilities = {
            "platformName": "ios",
            "platformVersion": "12.0",
            # "udid": udid,
            "udid": "70836918dd5df3141ebe3ee81a5791daa4254de5",
            "deviceName": "iPhone",
            "automationName": "XCUITest",
            "bundleId": "cn.openkeychina.openkeyapp",
            # "app": app_path,
            "newCommandTimeout": "60"
        }
        # driver = webdriver.Remote("http://127.0.0.1:" + port + "/wd/hub", capabilities)
        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", capabilities)
        time.sleep(10)
        return driver
    
    
if __name__ =='__main__':
    a = BaseDriver()
    a.ios_driver()