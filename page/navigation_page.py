# coding=utf-8
from util.get_by_local import GetByLocal


class NavigationPage:
    def __init__(self, driver):
        self.get_by_local = GetByLocal(driver)
        
    def get_type_button(self):
        return self.get_by_local.get_element('type_button', 'navigation_bar')
    
    def get_home_button(self):
        return self.get_by_local.get_element('home_button', 'navigation_bar')
    
    def get_my_button(self):
        return self.get_by_local.get_element('my_button', 'navigation_bar')
    
    def get_community(self):
        return self.get_by_local.get_element('community', 'navigation_bar')
    
    def get_come_back(self):
        return self.get_by_local.get_element('come_back', 'navigation_bar')
