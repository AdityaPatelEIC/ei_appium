from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from .appium_wait_and_synchronization import AppiumWaitAndSynchronization
from .appium_custom_logger import customLogger


class AppiumGestureAndTouch:
    def __init__(self):
        pass

    def swipe_up(self, device, strength_percent):
        """
        Swipes up a portion of the screen based on percent of a wider defined range.

        :param device: Appium driver instance.
        :param strength_percent: Strength of the swipe (0 to 100) relative to the swipe range.
        """
        assert 1 <= strength_percent <= 100, "strength_percent must be between 1 and 100"

        finger = PointerInput('touch', "finger")
        actions = ActionBuilder(device, mouse=finger)

        size = device.get_window_size()
        width = size['width']
        height = size['height']

        start_x = width // 2
        fixed_top = int(height * 0.2)  # 20%
        fixed_bottom = int(height * 0.8)  # 80%
        swipe_range = fixed_bottom - fixed_top

        swipe_distance = int((strength_percent / 100) * swipe_range)
        start_y = fixed_bottom
        end_y = max(start_y - swipe_distance, 10)

        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.move_to_location(start_x, end_y)
        actions.pointer_action.pointer_up()

        actions.perform()

    def swipe_down(self, device, strength_percent):
        """
        Swipes down a portion of the screen based on percent of a defined swipe range.

        :param device: Appium driver instance.
        :param strength_percent: Strength of the swipe (1 to 100) relative to the swipe range.
        """
        assert 1 <= strength_percent <= 100, "strength_percent must be between 1 and 100"

        finger = PointerInput('touch', "finger")
        actions = ActionBuilder(device, mouse=finger)

        size = device.get_window_size()
        width = size['width']
        height = size['height']

        start_x = width // 2
        fixed_top = int(height * 0.2)  # 20%
        fixed_bottom = int(height * 0.8)  # 80%
        swipe_range = fixed_bottom - fixed_top

        swipe_distance = int((strength_percent / 100) * swipe_range)
        start_y = fixed_top
        end_y = min(start_y + swipe_distance, height - 10)

        actions.pointer_action.move_to_location(start_x, start_y)
        actions.pointer_action.pointer_down()
        actions.pointer_action.move_to_location(start_x, end_y)
        actions.pointer_action.pointer_up()

        actions.perform()
