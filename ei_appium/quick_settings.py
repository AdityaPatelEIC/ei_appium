from .utils import open_quick_settings
from selenium.webdriver.common.by import By

from .wifi import *


class SelectorError(Exception):
    def __init__(self, message="There is something wrong with selector"):
        self.message = message
        super().__init__(self.message)


class ModeError(Exception):
    def __init__(self, message="There is something wrong with mode"):
        self.message = message
        super().__init__(self.message)


class QuickSettings:
    def switch_aeroplane_mode(self, device=None, selector=None, mode=None):
        open_quick_settings(device)
        if device is None or selector is None or mode is None:
            if device is None:
                raise DeviceError("No device has been provided")
            elif selector is None:
                raise SelectorError("No selector has been provided")
            else:
                raise ModeError("No mode has been provided")
        airplane_mode_button = device.find_element(By.XPATH, '//android.widget.Switch[contains(@text, "Airplane mode")]')
        curr_mode = airplane_mode_button.get_attribute('checked')
        if mode.lower() == 'on':
            if curr_mode == 'false':
                airplane_mode_button.click()
        else:
            if curr_mode == 'true':
                airplane_mode_button.click
