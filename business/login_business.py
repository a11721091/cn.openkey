# coding=utf-8
from handle.login_handle import LoginHandle


class LoginBusiness:
    def __init__(self, driver):
        self.handle = LoginHandle(driver)
        
    def login(self):
        try:
            # self.handle.click_in_app()
            self.handle.send_login_user()
            self.handle.send_login_pwd()
            self.handle.click_login_button()
        except AssertionError:
            pass
        
        

