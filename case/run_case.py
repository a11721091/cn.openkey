# coding=utf-8
import sys
import os
curPath = os.path.abspath(os.path.dirname('/Users/llc/PycharmProjects/cn.openkey'))
rootPath = os.path.split(curPath)[0]
PathProject = os.path.split(rootPath)[0]
sys.path.append(rootPath)
sys.path.append(PathProject)
import unittest
from imp import reload
from business.login_business import LoginBusiness
from business.base_driver import BaseDriver
from business.community_business import CommunityBusiness
from util.slide.slide_direction import SlideDirection
from util.HTMLTestRunner import HTMLTestRunner
import time


class CaseTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        reload(sys)
        cls.base_driver = BaseDriver()
        cls.driver = cls.base_driver.ios_driver()
        cls.slide_direction = SlideDirection(cls.driver)
        cls.login_business = LoginBusiness(cls.driver)
        cls.community = CommunityBusiness(cls.driver)
        
    def slide_guide_pages(self):
        """
        引导页滑动
        :return:
        """
        self.driver.switch_to.alert.accept()
        self.slide_direction.swipe_on('left')
        self.slide_direction.swipe_on('left')

    def login_case(self):
        '''登陆操作'''
        self.login_business.login()
        time.sleep(1)
    
    def in_community(self):
        '''进入社区列表'''
        self.community.in_community()
        pass
    
    def community_msg(self):
        '''社区通告'''
        # self.community.community_msg()
        pass
    def community_visitor(self):
        '''访客邀请'''
        # self.community.community_visitor()
        pass
    def community_repair(self):
        '''账单管理'''
        # self.community.community_repair()
        pass
    def community_member(self):
        '''添加成员用例'''
        # self.community.community_member()
        pass
    @classmethod
    def tearDownClass(cls):
        time.sleep(5)
        cls.driver.quit()


def get_suite():
    suite = unittest.TestSuite()
    # suite.addTest(CaseTest('slide_guide_pages'))
    suite.addTest(CaseTest('login_case'))
    suite.addTest(CaseTest('in_community'))
    suite.addTest(CaseTest('community_msg'))
    suite.addTest(CaseTest('community_visitor'))
    suite.addTest(CaseTest('community_repair'))
    suite.addTest(CaseTest('community_member'))
    html_file = '../report.html'
    fp = open(html_file, "wb")
    HTMLTestRunner(fp, title='未来钥匙测试用例', description='这是用例描述').run(suite)
    fp.close()


if __name__ == '__main__':
    get_suite()