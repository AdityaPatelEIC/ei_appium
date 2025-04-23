import time

from selenium.webdriver import ActionChains

from .wait_and_synchronization import *
from .custom_logger import customLogger


def get_element(device, locator_type, locator_value, timeout):
    log = customLogger()
    element = None
    try:
        element = wait_for_element(device, locator_type, locator_value, timeout)
        if element is None:
            return element
        log.info(f"Element found with locator type {locator_type} and locator value {locator_value}")
    except NoSuchElementException:
        log.error(f"Element not found with {locator_type} = {locator_value}")
    return element


def get_elements(device, locator_type, locator_value, timeout):
    log = customLogger()
    element = None
    try:
        element = wait_for_elements(device, locator_type, locator_value, timeout)
        if element is None:
            return element
        log.info(f"Elements found with locator type {locator_type} and locator value {locator_value}")
    except NoSuchElementException:
        log.error(f"Elements not found with {locator_type} = {locator_value}")
    return element


def click_element(device, locator_type, locator_value, timeout):
    log = customLogger()
    try:
        element = wait_for_element(device, locator_type, locator_value, timeout)
        if element:
            element.click()
            log.info(f"Clicked on element with locator type {locator_type} and locator value {locator_value}")
    except Exception as e:
        log.error(f"Element not found with {locator_type} = {locator_value}. :Error-{e}")


def long_click_element(device, locator_type, locator_value, timeout):
    log = customLogger()
    actions = ActionChains(device)
    try:
        element = wait_for_element(device, locator_type, locator_value, timeout)
        if element:
            actions.click_and_hold(element).perform()
            time.sleep(0.5)
            actions.release(element).perform()
            log.info(f"Long clicked on element with locator type {locator_type} and locator value {locator_value}")
    except Exception as e:
        log.error(f"Element not found with {locator_type} = {locator_value}. :Error-{e}")


def click_and_hold_element(device, locator_type, locator_value, hold_time, timeout):
    log = customLogger()
    actions = ActionChains(device)
    try:
        element = wait_for_element(device, locator_type, locator_value, timeout)
        if element:
            actions.click_and_hold(element).perform()
            time.sleep(hold_time)
            actions.release(element).perform()
            log.info(f"Clicked on element with locator type {locator_type} and locator value {locator_value} for {hold_time} seconds")
    except Exception as e:
        log.error(f"Element not found with {locator_type} = {locator_value}. :Error-{e}")
