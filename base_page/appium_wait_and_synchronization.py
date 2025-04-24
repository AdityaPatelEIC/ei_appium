from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.ui import WebDriverWait
from .appium_custom_logger import customLogger


class AppiumWaitAndSynchronization:
    def wait_for_element(self, device, locator_type, locator_value, timeout):
        log = customLogger()
        locator_type = locator_type.lower()
        element = None

        # Dictionary mapping locator types to their corresponding AppiumBy methods
        locator_map = {
            'id': AppiumBy.ID,
            'class': AppiumBy.CLASS_NAME,
            'xpath': AppiumBy.XPATH,
            'desc': AppiumBy.ANDROID_UIAUTOMATOR,
            'text': AppiumBy.ANDROID_UIAUTOMATOR,
            'index': AppiumBy.ANDROID_UIAUTOMATOR
        }

        # Check if the locator type exists in the dictionary
        if locator_type not in locator_map:
            log.error(f"Invalid locator type: {locator_type}. Unable to find element for {locator_value}")
            return None

        # Prepare the appropriate locator strategy
        locator = locator_map[locator_type]
        # Special handling for 'desc', 'text', and 'index' that need custom expressions
        if locator_type == 'desc':
            locator_value = f'UiSelector().description("{locator_value}")'
        elif locator_type == 'text':
            locator_value = f'text("{locator_value}")'
        elif locator_type == 'index':
            locator_value = f'UiSelector().index({int(locator_value)})'

        # Wait for the element to be located
        wait = WebDriverWait(device, timeout, 1,
                             ignored_exceptions=[NoSuchElementException, ElementNotSelectableException,
                                                 ElementNotVisibleException])

        element = wait.until(lambda x: x.find_element(locator, locator_value))

        return element

    def wait_for_elements(self, device, locator_type, locator_value, timeout):
        log = customLogger()
        locator_type = locator_type.lower()
        element = None

        # Dictionary mapping locator types to their corresponding AppiumBy methods
        locator_map = {
            'id': AppiumBy.ID,
            'class': AppiumBy.CLASS_NAME,
            'xpath': AppiumBy.XPATH,
            'desc': AppiumBy.ANDROID_UIAUTOMATOR,
            'text': AppiumBy.ANDROID_UIAUTOMATOR,
            'index': AppiumBy.ANDROID_UIAUTOMATOR
        }

        # Check if the locator type exists in the dictionary
        if locator_type not in locator_map:
            log.error(f"Invalid locator type: {locator_type}. Unable to find element for {locator_value}")
            return None

        # Prepare the appropriate locator strategy
        locator = locator_map[locator_type]
        # Special handling for 'desc', 'text', and 'index' that need custom expressions
        if locator_type == 'desc':
            locator_value = f'UiSelector().description("{locator_value}")'
        elif locator_type == 'text':
            locator_value = f'text("{locator_value}")'
        elif locator_type == 'index':
            locator_value = f'UiSelector().index({int(locator_value)})'

        # Waits for the element to be located
        wait = WebDriverWait(device, timeout, 1,
                             ignored_exceptions=[NoSuchElementException, ElementNotSelectableException,
                                                 ElementNotVisibleException])

        element = wait.until(lambda x: x.find_elements(locator, locator_value))

        return element
