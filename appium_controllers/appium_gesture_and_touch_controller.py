from appium_base_page.appium_gesture_and_touch import AppiumGestureAndTouch
from appium_base_page.appium_custom_logger import customLogger

class GestureAndTouchController:
    def __init__(self):
        self.gs_tch = AppiumGestureAndTouch()

    def swipe_up(self, device, strength_percent=50):
        log = customLogger()
        self.gs_tch.swipe_up(device, strength_percent)
        log.info("Successfully performed swipe up")

    def swipe_up_on_devices(self, *args, strength_percent=50):
        for device in args:
            self.swipe_up(device, strength_percent)

    def swipe_up_on_all_devices(self, devices, strength_percent=50):
        for device in devices:
            self.swipe_up(device, strength_percent)

    def swipe_down(self, device, strength_percent=50):
        log = customLogger()
        self.gs_tch.swipe_down(device, strength_percent)
        log.info('Successfully performed swipe down on device')

    def swipe_down_on_devices(self, *args, strength_percent=50):
        for device in args:
            self.swipe_down(device, strength_percent)

    def swipe_down_on_all_devices(self, devices, strength_percent=50):
        for device in devices:
            self.swipe_down(device, strength_percent)
