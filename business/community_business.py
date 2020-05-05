# coding=utf-8
from handle.community_handle import CommunityHandle
import time
from util.slide.slide_direction import SlideDirection


class CommunityBusiness:
    def __init__(self, driver):
        self.community_handle = CommunityHandle(driver)
        self.slide_direction = SlideDirection(driver)
        
    def in_community(self):
        self.community_handle.click_type()
        self.community_handle.click_community()
        
    def community_msg(self):

        self.community_handle.click_community_msg()
        time.sleep(2)
        self.community_handle.click_msg_detail()
        self.community_handle.click_back()
        self.community_handle.click_back()
        
    def community_visitor(self):
        self.community_handle.click_visitor()
        self.community_handle.click_visitor_first()
        self.community_handle.send_visitor_name()
        self.community_handle.send_visitor_phone()
        self.community_handle.click_visitor_share()
        self.community_handle.click_visitor_cancel()
        self.community_handle.click_back()
        self.community_handle.click_back()
        
    def community_repair(self):
        self.community_handle.click_property_number()
        time.sleep(2)
        self.community_handle.click_property_repair()
        self.community_handle.send_property_content()
        self.slide_direction.swipe_customize(199, 205, 411, 122)
        self.community_handle.send_property_address()
        self.community_handle.click_property_photo()
        self.community_handle.click_property_photo_type()
        time.sleep(3)
        self.community_handle.click_property_photo_cancel()
        self.community_handle.click_property_button()
        time.sleep(3)
        self.community_handle.click_back()
        
    def community_member(self):
        self.community_handle.click_member()
        self.community_handle.click_member_management()
        self.community_handle.click_add_member()
        self.community_handle.send_member_name()
        self.community_handle.send_member_number()
        self.community_handle.click_member_identity()
        self.community_handle.click_member_identity_ok()
        self.community_handle.click_member_data()
        self.community_handle.click_member_data_forever()
        self.community_handle.click_member_ok()
        