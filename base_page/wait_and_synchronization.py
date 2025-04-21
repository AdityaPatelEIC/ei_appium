from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .custom_logger import *


def wait_for_element(driver, locator_type, locator_value, timeout=15):
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
    wait = WebDriverWait(driver, timeout, 1,
                         ignored_exceptions=[NoSuchElementException, ElementNotSelectableException, ElementNotVisibleException])

    try:
        # Using EC.presence_of_element_located with the locator
        element = wait.until(lambda x: x.find_element(locator_type, locator_value))
        log.info(f"Found element by {locator_type}: {locator_value}")
    except NoSuchElementException:
        log.error(f"Element not found with {locator_type} = {locator_value}")

    return element
