# coding=utf-8
import time


class SlideDirection:
    def __init__(self, driver):
        self.driver = driver

    def get_size(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        return width, height

    def swipe_left(self):
        x1 = self.get_size()[0] / 10 * 9
        y = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": 0.5, "element": None, "fromX": x1, "fromY": y, "toX": x, "toY": y})
        time.sleep(0.2)

    def swipe_right(self):
        x1 = self.get_size()[0] / 10 * 9
        y = self.get_size()[1] / 2
        x = self.get_size()[0] / 10
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": 0.5, "element": None, "fromX": x, "fromY": y, "toX": x1, "toY": y})
        time.sleep(0.2)

    def swipe_up(self):
        y1 = self.get_size()[1] / 10 * 9
        y = self.get_size()[1] / 10
        x = self.get_size()[0] / 2
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": 0.5, "element": None, "fromX": x, "fromY": y1, "toX": x, "toY": y})
        time.sleep(0.2)

    def swipe_down(self):
        y1 = self.get_size()[1] / 10
        y = self.get_size()[1]
        x = self.get_size()[0] / 10 * 9
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": 0.5, "element": None, "fromX": x, "fromY": y, "toX": x, "toY": y1})
        time.sleep(0.2)

    def swipe_time(self):
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": 0.5, "element": None, "fromX": 277, "fromY": 654, "toX": 277, "toY": 700})

    def swipe_customize(self, x1, x2, y1, y2):
        self.driver.execute_script("mobile:dragFromToForDuration",
                                   {"duration": 2, "element": None, "fromX": x1, "fromY": y1, "toX": x2, "toY": y2})

    def stop_key(self):
        # self.driver.hide_keyboard()
        self.driver.hide_keyboard(key_name='UIKeyboardTypeDefault')
        # self.driver.hide_keyboard()
        # self.driver.hide_keyboard()
        # self.driver.hide_keyboard()
        # self.driver.hide_keyboard()
        # self.driver.hide_keyboard()

    def tap_space(self):
        self.driver.tap([(223, 411)], 100)
        # self.driver.hide_keyboard(key_name='UIKeyboardTypeDefault')

    def swipe_on(self, direction):
        if direction == 'left':
            self.swipe_left()
        elif direction == 'right':
            self.swipe_right()
        elif direction == 'up':
            self.swipe_up()
        elif direction == 'down':
            self.swipe_up()
        else:
            raise ImportError('参数错误:\'left\'or\'right\'or\'up\'or\'down\'')

