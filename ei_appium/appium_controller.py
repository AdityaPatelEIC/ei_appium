from .wifi import *
from .quick_settings import *
from .controller import *
from .bluetooth import *
from .utils import *


class AppiumController:
    def __init__(self):
        self.wifi = WiFi()
        self.qs = QuickSettings()
        self.ble = Bluetooth()

    """ALL THE METHODS RELATED TO OPERATION WITH THE DEVICES"""

    def get_device_object(self, device_id):
        return get_device_object(device_id)

    def return_devices(self):
        return return_devices()

    def is_device_emulator(self, device):
        return is_device_emulator(device)

    """ALL THE METHODS RELATED TO OPERATION WITH THE Wi-Fi"""

    def turn_on_wifi(self, device):
        self.wifi.turn_on_wifi(device)

    def turn_on_wifi_on_devices(self, *args):
        self.wifi.turn_on_wifi_on_devices(*args)

    def turn_on_wifi_on_all_devices(self, devices):
        self.wifi.turn_on_wifi_on_all_devices(devices)

    def turn_off_wifi(self, device):
        self.wifi.turn_off_wifi(device)

    def turn_off_wifi_on_devices(self, *args):
        self.wifi.turn_off_wifi_on_devices(*args)

    def turn_off_wifi_on_all_devices(self, devices):
        self.wifi.turn_off_wifi_on_all_devices(devices)

    def connect_to_wifi(self, device, wifi_name, wifi_password):
        self.wifi.connect_to_wifi(device, wifi_name, wifi_password)

    def connect_to_wifi_on_devices(self, *args, wifi_name, wifi_password):
        self.wifi.connect_to_wifi_on_devices(*args, wifi_name=wifi_name, wifi_password=wifi_password)

    def connect_to_wifi_on_all_devices(self, devices, wifi_name, wifi_password):
        self.wifi.connect_to_wifi_on_all_devices(devices, wifi_name=wifi_name, wifi_password=wifi_password)

    # def is_wifi_connected(self, device):
    #     return self.wifi.is_wifi_connected(device)
    #
    # def is_wifi_connected_on_devices(self, *args):
    #     return self.wifi.is_wifi_connected_on_devices(*args)
    #
    # def is_wifi_connected_on_all_devices(self, devices):
    #     return self.wifi.is_wifi_connected_on_all_devices(devices)

    # def is_wifi_connected_to(self, device, wifi_name):
    #     return self.wifi.is_wifi_connected_to(device, wifi_name=wifi_name)
    #
    # def is_wifi_connected_to_on_devices(self, *args, wifi_name):
    #     return self.wifi.is_wifi_connected_to_on_devices(*args, wifi_name=wifi_name)
    #
    # def is_wifi_connected_to_all_devices(self, devices, wifi_name):
    #     return self.wifi.is_wifi_connected_to_all_devices(devices, wifi_name=wifi_name)
    #
    """ALL THE METHODS RELATED TO OPERATION WITH THE BLUETOOTH"""

    def turn_on_bluetooth(self, device):
        self.ble.turn_on_bluetooth(device)

    def turn_on_bluetooth_on_devices(self, *args):
        self.ble.turn_on_bluetooth_on_devices(*args)

    def turn_on_bluetooth_on_all_devices(self, devices):
        self.ble.turn_on_bluetooth_on_all_devices(devices)

    def turn_off_bluetooth(self, device):
        self.ble.turn_off_bluetooth(device)

    def turn_off_bluetooth_on_devices(self, *args):
        self.ble.turn_off_bluetooth_on_devices(*args)

    def turn_off_bluetooth_on_all_devices(self, devices):
        self.ble.turn_off_bluetooth_on_all_devices(devices)

    def get_bluetooth_scan_result(self, device):
        return self.ble.get_bluetooth_scan_result(device)

    def get_bluetooth_scan_result_on_devices(self, *args):
        return self.ble.get_bluetooth_scan_result_on_devices(*args)

    def get_bluetooth_scan_result_on_all_devices(self, devices):
        return self.ble.get_bluetooth_scan_result_on_all_devices(devices)

    """ALL THE METHODS RELATED TO QUICK SETTINGS"""

    def switch_aeroplane_mode(self, device, selector, mode):
        self.qs.switch_aeroplane_mode(device, selector, mode)

    """ALL THE METHODS RELATED TO INTERACTIONS WITH APPLICATION"""

    def open_application(self, device, app_package, app_activity, no_reset=True):
        open_application(device, app_package, app_activity, no_reset)
