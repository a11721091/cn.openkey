# coding=utf-8
from util.get_by_local import GetByLocal

class CommunityPage:
    def __init__(self, driver):
        self.get_by_local = GetByLocal(driver)
        
    def get_community_msg(self):
        return self.get_by_local.get_element('community_msg', 'community_page')
    
    def get_visitor(self):
        return self.get_by_local.get_element('visitor', 'community_page')
    
    def get_property_number(self):
        return self.get_by_local.get_element('property_number', 'community_page')
    
    def get_door_card(self):
        return self.get_by_local.get_element('door_card', 'community_page')

    def get_city_for_windows(self):
        return self.get_by_local.get_element('city_for_windows', 'community_page')
    
    def get_mall(self):
        return self.get_by_local.get_element('mall', 'community_page')
    
    def get_bill(self):
        return self.get_by_local.get_element('bill', 'community_page')
    
    def get_member(self):
        return self.get_by_local.get_element('member', 'community_page')
    
    def get_msg_detail(self):
        return self.get_by_local.get_element('msg_detail', 'community_page')
    
    def get_visitor_first(self):
        return self.get_by_local.get_element('visitor_first', 'community_page')
    
    def get_visitor_phone(self):
        return self.get_by_local.get_element('visitor_phone', 'community_page')
    
    def get_visitor_name(self):
        return self.get_by_local.get_element('visitor_name', 'community_page')
    
    def get_visitor_share(self):
        return self.get_by_local.get_element('visitor_share', 'community_page')
    
    def get_visitor_cancel(self):
        return self.get_by_local.get_element('visitor_cancel', 'community_page')
    
    def get_property_repair(self):
        return self.get_by_local.get_element('property_repair', 'community_page')
    
    def get_property_content(self):
        return self.get_by_local.get_element('property_content', 'community_page')
    
    def get_property_address(self):
        return self.get_by_local.get_element('property_address', 'community_page')
    
    def get_property_button(self):
        return self.get_by_local.get_element('property_button', 'community_page')
    
    def get_member_management(self):
        return self.get_by_local.get_element('member_management', 'community_page')
    
    def get_add_member(self):
        return self.get_by_local.get_element('add_member', 'community_page')
    
    def get_member_name(self):
        return self.get_by_local.get_element('member_name', 'community_page')
    
    def get_member_number(self):
        return self.get_by_local.get_element('member_number', 'community_page')
    
    def get_member_identity(self):
        return self.get_by_local.get_element('member_identity', 'community_page')
    
    def get_member_relatives(self):
        return self.get_by_local.get_element('member_relatives', 'community_page')
    
    def get_member_identity_ok(self):
        return self.get_by_local.get_element('member_identity_ok', 'community_page')
    
    def get_member_data(self):
        return self.get_by_local.get_element('member_data', 'community_page')
    
    def get_member_data_forever(self):
        return self.get_by_local.get_element('member_data_forever', 'community_page')
    
    def get_member_ok(self):
        return self.get_by_local.get_element('member_ok', 'community_page')
    
    def get_property_photo(self):
        return self.get_by_local.get_element('property_photo', 'community_page')
    
    def get_property_photo_type(self):
        return self.get_by_local.get_element('property_photo_type', 'community_page')
    
    def get_property_photo_cancel(self):
        return self.get_by_local.get_element('property_photo_cancel', 'community_page')