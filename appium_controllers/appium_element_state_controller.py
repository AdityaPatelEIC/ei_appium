from appium_base_page.appium_element_state import AppiumElementState
from appium_base_page.appium_custom_logger import customLogger


class ElementStateController:
    def __init__(self):
        self.ele_state = AppiumElementState()

    def get_element_attribute_state(self, device, locator_type, locator_value, attribute_name, timeout=15):
        self.ele_state.get_element_attribute_state(device, locator_type, locator_value, attribute_name, timeout)

    def get_element_attribute_state_on_devices(self, *args, locator_type, locator_value, attribute_name, timeout=15):
        log = customLogger()
        element_states = []
        for device in args:
            element_states.append(
                self.ele_state.get_element_attribute_state(device, locator_type, locator_value, attribute_name,
                                                           timeout))
        first = element_states[0]
        if all(state == first for state in element_states):
            log.info(f'{attribute_name} has same state across all devices')
            return first
        log.warning(f'{attribute_name} state on all the device is not same')
        return None

    def get_element_attribute_state_on_all_devices(self, devices, locator_type, locator_value, attribute_name, timeout=15):
        log = customLogger()
        element_states = []
        for device in devices:
            element_states.append(
                self.ele_state.get_element_attribute_state(device, locator_type, locator_value, attribute_name,
                                                           timeout))
        first = element_states[0]
        if all(state == first for state in element_states):
            log.info(f'{attribute_name} has same state across all devices')
            return first
        log.warning(f'{attribute_name} state on all the device is not same')
        return None
