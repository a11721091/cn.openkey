# coding=utf-8
from page.community_page import CommunityPage
from page.navigation_page import NavigationPage


class CommunityHandle:
    def __init__(self, driver):
        self.community_page = CommunityPage(driver)
        self.navigation_page = NavigationPage(driver)
        
    def click_type(self):
        self.navigation_page.get_type_button().click()
        
    def click_community(self):
        self.navigation_page.get_community().click()
        
    def click_back(self):
        self.navigation_page.get_come_back().click()
        
    def click_community_msg(self):
        self.community_page.get_community_msg().click()
        
    def click_msg_detail(self):
        self.community_page.get_msg_detail().click()
        
    def click_visitor(self):
        self.community_page.get_visitor().click()
        
    def click_visitor_first(self):
        self.community_page.get_visitor_first().click()
        
    def send_visitor_phone(self):
        self.community_page.get_visitor_phone().send_keys('13273714765')
        
    def send_visitor_name(self):
        self.community_page.get_visitor_name().send_keys('家属')
        
    def click_visitor_share(self):
        self.community_page.get_visitor_share().click()
        
    def click_visitor_cancel(self):
        self.community_page.get_visitor_cancel().click()
        
    def click_property_number(self):
        self.community_page.get_property_number().click()
        
    def click_property_repair(self):
        self.community_page.get_property_repair().click()
        
    def send_property_content(self):
        self.community_page.get_property_content().send_keys('水管漏水，请及时上门修理')
        
    def send_property_address(self):
        self.community_page.get_property_address().send_keys('5号楼2单元303室')
        
    def click_property_button(self):
        self.community_page.get_property_button().click()
        
    def click_bill(self):
        self.community_page.get_bill().click()
        
    def click_member(self):
        self.community_page.get_member().click()
        
    def click_member_management(self):
        self.community_page.get_member_management().click()
        
    def click_add_member(self):
        self.community_page.get_add_member().click()
        
    def send_member_name(self):
        self.community_page.get_member_name().send_keys('刘亦菲')
    
    def send_member_number(self):
        self.community_page.get_member_number().send_keys('15537996548')
        
    def click_member_identity(self):
        self.community_page.get_member_identity().click()
        
    def click_member_identity_ok(self):
        self.community_page.get_member_identity_ok().click()
        
    def click_member_data(self):
        self.community_page.get_member_data().click()
        
    def click_member_data_forever(self):
        self.community_page.get_member_data_forever().click()
        
    def click_member_ok(self):
        self.community_page.get_member_ok().click()
        
    def click_property_photo(self):
        self.community_page.get_property_photo().click()

    def click_property_photo_type(self):
        self.community_page.get_property_photo_type().click()
        
    def click_property_photo_cancel(self):
        self.community_page.get_property_photo_cancel().click()