# coding=utf-8
from util.read_init import ReadIni


class GetByLocal:
    def __init__(self, driver, file_path=None):
        self.driver = driver
        print(file_path)
        self.read_init = ReadIni(file_path)

    def get_element(self, key, section='login_page'):
        # local =xpath>//XCUIElementTypeApplication[@name="未来钥匙"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell
        local = self.read_init.get_value(key, section)
        # ['xpath', '//XCUIElementTypeApplication[@name="未来钥匙"]/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell']
        if local is not None:
            # by = xpath
            by = local.split('>')[0]
            local_by = local.split('>')[1]
            try:
                if by == 'id':
                    return self.driver.find_element_by_id(local_by)
                elif by == 'className':
                    return self.driver.find_element_by_class_name(local_by)
                elif by == 'name':
                    return self.driver.find_element_by_name(local)
                else:
                    return self.driver.find_element_by_xpath(local_by)
            except:
                return None
        else:
            return None

    def switch_to(self):
        return self.driver.switch_to.alert.accept()
    

