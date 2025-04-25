from base_page.appium_element_interactions import AppiumElementInteractions


class ElementInteractionsController:
    def __init__(self):
        self.ele_interaction = AppiumElementInteractions()

    def get_element(self, device, locator_type, locator_value, timeout=15):
        return self.ele_interaction.get_element(device, locator_type, locator_value, timeout)

    def get_elements(self, device, locator_type, locator_value, timeout=15):
        return self.ele_interaction.get_elements(device, locator_type, locator_value, timeout)

    def click_element(self, device, locator_type, locator_value, timeout=15):
        self.ele_interaction.click_element(device, locator_type, locator_value, timeout)

    def long_click_element(self, device, locator_type, locator_value, timeout=15):
        self.ele_interaction.long_click_element(device, locator_type, locator_value, timeout)

    def click_and_hold_element(self, device, locator_type, locator_value, hold_time=2, timeout=15):
        self.ele_interaction.click_and_hold_element(device, locator_type, locator_value, hold_time, timeout)
