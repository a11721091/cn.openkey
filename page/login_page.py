# coding=utf-8
from util.get_by_local import GetByLocal

class LoginPage:
    def __init__(self, driver):
        self.get_by_local = GetByLocal(driver)
        
    def get_in_app(self):
        return self.get_by_local.get_element('in_app', 'login_element')
        
    def get_login_user(self):
        return self.get_by_local.get_element('login_user', 'login_element')
        
    def get_login_pwd(self):
        return self.get_by_local.get_element('login_pwd', 'login_element')
    
    def get_login_button(self):
        return self.get_by_local.get_element('login_button', 'login_element')
    

