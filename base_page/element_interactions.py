from .wait_and_synchronization import *
from .custom_logger import customLogger


def get_element(device, locator_type, locator_value, timeout):
    log = customLogger()
    element = None
    try:
        element = wait_for_element(device, locator_type, locator_value, timeout)
        log.info(f"Element found with locator type {locator_type} and locator value {locator_value}")
    except NoSuchElementException:
        log.error(f"Element not found with {locator_type} = {locator_value}")
    return element


def get_elements(device, locator_type, locator_value, timeout):
    log = customLogger()
    element = None
    try:
        element = wait_for_elements(device, locator_type, locator_value, timeout)
        log.info(f"Elements found with locator type {locator_type} and locator value {locator_value}")
    except NoSuchElementException:
        log.error(f"Elements not found with {locator_type} = {locator_value}")
    return element
