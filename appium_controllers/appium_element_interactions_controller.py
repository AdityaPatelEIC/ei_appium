from appium_base_page.appium_element_interactions import AppiumElementInteractions


class ElementInteractionsController:
    def __init__(self):
        self.ele_interaction = AppiumElementInteractions()

    def get_element(self, device, locator_type, locator_value, timeout=15):
        return self.ele_interaction.get_element(device, locator_type, locator_value, timeout)

    def get_elements(self, device, locator_type, locator_value, timeout=15):
        return self.ele_interaction.get_elements(device, locator_type, locator_value, timeout)

    def click_element(self, device, locator_type, locator_value, timeout=15):
        self.ele_interaction.click_element(device, locator_type, locator_value, timeout)

    def click_element_on_devices(self, *args, locator_type, locator_value, timeout=15):
        self.ele_interaction.click_element_on_devices(*args, locator_type=locator_type, locator_value=locator_value,
                                                      timeout=timeout)

    def click_element_on_all_devices(self, devices, locator_type, locator_value, timeout=15):
        self.ele_interaction.click_element_on_all_devices(devices, locator_type,
                                                          locator_value, timeout)

    def long_click_element(self, device, locator_type, locator_value, timeout=15):
        self.ele_interaction.long_click_element(device, locator_type, locator_value, timeout)

    def long_click_element_on_devices(self, *args, locator_type, locator_value, timeout=15):
        self.ele_interaction.long_click_element_on_devices(*args, locator_type=locator_type,
                                                           locator_value=locator_value, timeout=timeout)

    def long_click_element_on_all_devices(self, devices, locator_type, locator_value, timeout=15):
        self.ele_interaction.long_click_element_on_all_devices(devices, locator_type,
                                                               locator_value, timeout)

    def click_and_hold_element(self, device, locator_type, locator_value, hold_time=2, timeout=15):
        self.ele_interaction.click_and_hold_element(device, locator_type, locator_value, hold_time, timeout)

    def click_and_hold_element_on_devices(self, *args, locator_type, locator_value, hold_time=2, timeout=15):
        self.ele_interaction.click_and_hold_element_on_devices(*args, locator_type=locator_type,
                                                               locator_value=locator_value, hold_time=hold_time,
                                                               timeout=timeout)

    def click_and_hold_element_on_all_devices(self, devices, locator_type, locator_value, hold_time=2, timeout=15):
        self.ele_interaction.click_and_hold_element_on_all_devices(devices, locator_type, locator_value, hold_time,
                                                                   timeout)

    def click_element_n_times(self, device, locator_type, locator_value, n=2, timeout=15):
        self.ele_interaction.click_element_n_times(device, locator_type, locator_value, n, timeout)

    def click_element_n_times_on_devices(self, *args, locator_type, locator_value, n=2, timeout=15):
        self.ele_interaction.click_element_n_times_on_devices(*args, locator_type=locator_type,
                                                              locator_value=locator_value, n=n,
                                                              timeout=timeout)

    def click_element_n_times_on_all_devices(self, devices, locator_type, locator_value, n=2, timeout=15):
        self.ele_interaction.click_element_n_times_on_all_devices(devices, locator_type, locator_value, n, timeout)

    def set_element_text(self, device, locator_type, locator_value, text, timeout=15):
        self.ele_interaction.set_element_text(device, locator_type, locator_value, text, timeout)

    def set_element_text_on_devices(self, *args, locator_type, locator_value, text, timeout=15):
        self.ele_interaction.set_element_text_on_devices(*args, locator_type=locator_type, locator_value=locator_value,
                                                         text=text, timeout=timeout)

    def set_element_text_on_all_devices(self, devices, locator_type, locator_value, text, timeout=15):
        self.ele_interaction.set_element_text_on_all_devices(devices, locator_type, locator_value, text, timeout)

    def clear_element_text(self, device, locator_type, locator_value, timeout=15):
        self.ele_interaction.clear_element_text(device, locator_type, locator_value, timeout)

    def clear_element_text_on_devices(self, *args, locator_type, locator_value, timeout=15):
        self.ele_interaction.clear_element_text_on_devices(*args, locator_type=locator_type,
                                                           locator_value=locator_value, timeout=timeout)

    def clear_element_text_on_all_devices(self, devices, locator_type, locator_value, timeout=15):
        self.ele_interaction.clear_element_text_on_all_devices(devices, locator_type, locator_value, timeout)
