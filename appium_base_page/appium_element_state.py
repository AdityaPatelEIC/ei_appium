from selenium.common import NoSuchElementException

from .appium_wait_and_synchronization import AppiumWaitAndSynchronization
from .appium_custom_logger import customLogger


class AppiumElementState:
    def __init__(self):
        self.wt_syn = AppiumWaitAndSynchronization()

    def get_element_attribute_state(self, device, locator_type, locator_value, attribute_name, timeout):
        log = customLogger()
        element = None
        try:
            element = self.wt_syn.wait_for_element(device, locator_type, locator_value, timeout)
            if element:
                log.info(f"Element found with locator type {locator_type} and locator value {locator_value}")
                return element.get_attribute(attribute_name)
            else:
                return element
        except NoSuchElementException:
            log.error(f"Element not found with {locator_type} = {locator_value}")
        return element
