import time

from selenium.webdriver import ActionChains

from .appium_wait_and_synchronization import *
from .appium_custom_logger import customLogger


class AppiumElementInteractions:
    def __init__(self):
        self.wt_syn = AppiumWaitAndSynchronization()

    def get_element(self, device, locator_type, locator_value, timeout):
        log = customLogger()
        element = None
        try:
            element = self.wt_syn.wait_for_element(device, locator_type, locator_value, timeout)
            if element is None:
                return element
            log.info(f"Element found with locator type {locator_type} and locator value {locator_value}")
        except NoSuchElementException:
            log.error(f"Element not found with {locator_type} = {locator_value}")
        return element

    def get_elements(self, device, locator_type, locator_value, timeout):
        log = customLogger()
        element = None
        try:
            element = self.wt_syn.wait_for_elements(device, locator_type, locator_value, timeout)
            if element is None:
                return element
            log.info(f"Elements found with locator type {locator_type} and locator value {locator_value}")
        except NoSuchElementException:
            log.error(f"Elements not found with {locator_type} = {locator_value}")
        return element

    def click_element(self, device, locator_type, locator_value, timeout):
        log = customLogger()
        try:
            element = self.wt_syn.wait_for_element(device, locator_type, locator_value, timeout)
            if element:
                element.click()
                log.info(f"Clicked on element with locator type {locator_type} and locator value {locator_value}")
            else:
                log.error(
                    f"Failed to click on element with locator type {locator_type} and locator value {locator_value}")
        except Exception as e:
            log.error(f"Element not found with {locator_type} = {locator_value}. :Error-{e}")

    def click_element_on_devices(self, *args, locator_type, locator_value, timeout):
        for device in args:
            self.click_element(device, locator_type, locator_value, timeout)

    def click_element_on_all_devices(self, devices, locator_type, locator_value, timeout):
        for device in devices:
            self.click_element(device, locator_type, locator_value, timeout)

    def long_click_element(self, device, locator_type, locator_value, timeout):
        log = customLogger()
        actions = ActionChains(device)
        try:
            element = self.wt_syn.wait_for_element(device, locator_type, locator_value, timeout)
            if element:
                actions.click_and_hold(element).perform()
                time.sleep(0.5)
                actions.release(element).perform()
                log.info(f"Long clicked on element with locator type {locator_type} and locator value {locator_value}")
            else:
                log.error(
                    f"Failed to long click on element with locator type {locator_type} and locator value {locator_value}")
        except Exception as e:
            log.error(f"Element not found with {locator_type} = {locator_value}. :Error-{e}")

    def long_click_element_on_devices(self, *args, locator_type, locator_value, timeout):
        for device in args:
            self.long_click_element(device, locator_type, locator_value, timeout)

    def long_click_element_on_all_devices(self, devices, locator_type, locator_value, timeout):
        for device in devices:
            self.long_click_element(device, locator_type, locator_value, timeout)

    def click_and_hold_element(self, device, locator_type, locator_value, hold_time, timeout):
        log = customLogger()
        actions = ActionChains(device)
        try:
            element = self.wt_syn.wait_for_element(device, locator_type, locator_value, timeout)
            if element:
                actions.click_and_hold(element).perform()
                time.sleep(hold_time)
                actions.release(element).perform()
                log.info(
                    f"Clicked on element with locator type {locator_type} and locator value {locator_value} for {hold_time} seconds")
            else:
                log.error(
                    f"Failed to click and hold on element with locator type {locator_type} and locator value {locator_value}")
        except Exception as e:
            log.error(f"Element not found with {locator_type} = {locator_value}. :Error-{e}")

    def click_element_n_times(self, device, locator_type, locator_value, n, timeout):
        log = customLogger()
        try:
            element = self.wt_syn.wait_for_element(device, locator_type, locator_value, timeout)
            if element:
                for _ in range(n):
                    element.click()
                else:
                    log.info(f"Successfully clicked on element {n} times with locator type {locator_type} and locator value {locator_value}")
            else:
                log.error(f"Failed to click {n} times on element with locator type {locator_type} and locator value {locator_value}")

        except Exception as e:
            log.error(f"Element not found with {locator_type} = {locator_value}. :Error-{e}")

    def click_element_n_times_on_devices(self, *args, locator_type, locator_value, n, timeout):
        for device in args:
            self.click_element_n_times(device, locator_type, locator_value, n, timeout)

    def click_element_n_times_on_all_devices(self, devices, locator_type, locator_value, n, timeout):
        for device in devices:
            self.click_element_n_times(device, locator_type, locator_value, n, timeout)

    def click_and_hold_element_on_devices(self, *args, locator_type, locator_value, hold_time, timeout):
        for device in args:
            self.click_and_hold_element(device, locator_type, locator_value, hold_time, timeout)

    def click_and_hold_element_on_all_devices(self, devices, locator_type, locator_value, hold_time, timeout):
        for device in devices:
            self.click_and_hold_element(device, locator_type, locator_value, hold_time, timeout)

    def set_element_text(self, device, locator_type, locator_value, text, timeout):
        log = customLogger()
        try:
            element = self.wt_syn.wait_for_element(device, locator_type, locator_value, timeout)
            if element:
                element.send_keys(text)
                log.info(
                    f"Set text = \"{text}\" on element with locator type {locator_type} and locator value {locator_value}")
            else:
                log.error(
                    f"Failed to set text \"{text}\" on element with locator type {locator_type} and locator value {locator_value}")
        except Exception as e:
            log.error(f"Element not found with {locator_type} = {locator_value}. :Error-{e}")

    def set_element_text_on_devices(self, *args, locator_type, locator_value, text, timeout):
        for device in args:
            self.set_element_text(device, locator_type, locator_value, text, timeout)

    def set_element_text_on_all_devices(self, devices, locator_type, locator_value, text, timeout):
        for device in devices:
            self.set_element_text(device, locator_type, locator_value, text, timeout)

    def clear_element_text(self, device, locator_type, locator_value, timeout):
        log = customLogger()
        try:
            element = self.wt_syn.wait_for_element(device, locator_type, locator_value, timeout)
            if element:
                if element.clear():
                    log.info(f"Cleared existing text from the element with locator type {locator_type} and locator "
                             f"value {locator_value}")
                else:
                    log.error(f"Failed to clear existing text from the element with locator type {locator_type} and "
                              f"locator value {locator_value}")
        except Exception as e:
            log.error(f"Element not found with {locator_type} = {locator_value}. :Error-{e}")

    def clear_element_text_on_devices(self, *args, locator_type, locator_value, timeout):
        for device in args:
            self.clear_element_text(device, locator_type, locator_value, timeout)

    def clear_element_text_on_all_devices(self, devices, locator_type, locator_value, timeout):
        for device in devices:
            self.clear_element_text(device, locator_type, locator_value, timeout)
