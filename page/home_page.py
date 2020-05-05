# coding=utf-8
from util.get_by_local import GetByLocal


class HomePage:
    def __init__(self):
        self.get_by_local = GetByLocal()
        
    def get_home_unlock(self):
        return self.get_by_local.get_element('home_unlock', 'home_element')
        
    def get_first_room(self):
        return self.get_by_local.get_element('first_room', 'home_element')
