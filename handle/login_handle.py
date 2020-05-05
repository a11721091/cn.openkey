# coding=utf-8
from page.login_page import LoginPage

class LoginHandle:
    def __init__(self, driver):
        self.page = LoginPage(driver)
        
    def click_in_app(self):
        self.page.get_in_app().click()
        
    def send_login_user(self):
        self.page.get_login_user().clear()
        self.page.get_login_user().send_keys('15537932906')
        
    def send_login_pwd(self):
        self.page.get_login_pwd().clear()
        self.page.get_login_pwd().send_keys('666666')
        
    def click_login_button(self):
        self.page.get_login_button().click()
        
    def find_user(self):
        self.page.get_login_user()
