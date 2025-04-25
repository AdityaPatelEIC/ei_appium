from .wifi import *
from .quick_settings import *
from .controller import *
from .bluetooth import *
from .utils import *
from controllers.appium_wifi_controller import WiFiController
from controllers.appium_bluetooth_controller import BluetoothController
from controllers.appium_quick_settings_controller import QuickSettingsController
from controllers.appium_element_interactions_controller import ElementInteractionsController


class AppiumController(WiFiController, BluetoothController, QuickSettingsController, ElementInteractionsController):
    def __init__(self):
        WiFiController.__init__(self)
        BluetoothController.__init__(self)
        QuickSettingsController.__init__(self)
        ElementInteractionsController.__init__(self)

    """ALL THE METHODS RELATED TO OPERATION WITH THE DEVICES"""

    def setup_devices(self, platform_name):
        setup_devices(platform_name)

    def get_device_object(self, device_id):
        return get_device_object(device_id)

    def return_devices(self):
        return return_devices()

    def is_device_emulator(self, device):
        return is_device_emulator(device)

    def open_application(self, device, app_package, app_activity, no_reset=True):
        open_application(device, app_package, app_activity, no_reset)
