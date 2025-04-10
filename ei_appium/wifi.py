import time

from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from .controller import is_device_emulator

from .utils import open_quick_settings
class WiFiError(Exception):
    def __init__(self, message="There is some issue in WiFi"):
        self.message = message
        super().__init__(self.message)


class EmulatorError(Exception):
    def __init__(self, message="Operation in emulator in not possible"):
        self.message = message
        super().__init__(self.message)


class DeviceError(Exception):
    def __init__(self, message="Device is missing"):
        self.message = message
        super().__init__(self.message)


class WiFi:
    _CONNECTION_STATUS = '<unknown ssid>'

    def open_wifi_setting(self, device):
        if device is None:
            raise DeviceError("No device has been provided")
        open_quick_settings(device)
        actions = ActionChains(device)
        wifi_btn = device.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Internet")')
        actions.click_and_hold(wifi_btn).perform()
        time.sleep(1)
        actions.release(wifi_btn)
        time.sleep(4)
    def turn_on_wifi(self, device=None):
        try:
            device.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
        except NoSuchElementException as e:
            self.open_wifi_setting(device)
        wifi_on_off_btn = device.find_element(By.ID, 'android:id/switch_widget')
        if not wifi_on_off_btn.get_attribute('checked'):
            wifi_on_off_btn.click()

    def turn_on_wifi_on_devices(self, *args):
        for device in args:
            self.turn_on_wifi(device)

    def turn_on_wifi_on_all_devices(self, devices):
        for device in devices:
            self.turn_on_wifi(device)

    def turn_off_wifi(self, device=None):
        try:
            device.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
        except NoSuchElementException as e:
            self.open_wifi_setting(device)
        wifi_on_off_btn = device.find_element(By.ID, 'android:id/switch_widget')
        if wifi_on_off_btn.get_attribute('checked'):
            wifi_on_off_btn.click()

    def turn_off_wifi_on_devices(self, *args):
        for device in args:
            self.turn_off_wifi(device)

    def turn_off_wifi_on_all_devices(self, devices):
        for device in devices:
            self.turn_off_wifi(device)

    def connect_to_wifi(self, device, wifi_name=None, wifi_password=None):
        if is_device_emulator(device):
            raise EmulatorError("Emulator devices could not be connect with real wifi network")
        if wifi_name and wifi_password:
            self.turn_on_wifi(device)
            wifi = device.find_element(By.XPATH, f'//android.widget.TextView[@resource-id="android:id/title" and @text="{wifi_name}"]')
            wifi.click()
            time.sleep(1)
            password_text_box = device.find_element(By.ID, 'com.android.settings:id/password')
            password_text_box.send_keys(wifi_password)
            device.find_element(By.ID, 'android:id/button1').click()

        else:
            if wifi_name is None and wifi_password is None:
                raise WiFiError("WiFi Name and Password must be provided")
            elif wifi_name is None:
                raise WiFiError("WiFi Name must be provided")
            else:
                raise WiFiError("WiFi Password must be provided")

    def connect_to_wifi_on_devices(self, *args, **kwargs):
        for device in args:
            self.connect_to_wifi(device, wifi_name=kwargs['wifi_name'], wifi_password=kwargs['wifi_password'])

    def connect_to_wifi_on_all_devices(self, devices, wifi_name=None, wifi_password=None):
        for device in devices:
            self.connect_to_wifi(device, wifi_name=wifi_name, wifi_password=wifi_password)

    # def is_wifi_connected(self, device=None):
    #     if device is None:
    #         raise DeviceError("No device has been provided")
    #     device.api.isWifiConnected()
    #     return device.api.isWifiConnected()
    #
    # def is_wifi_connected_on_devices(self, *args):
    #     for device in args:
    #         if not self.is_wifi_connected(device):
    #             return False
    #     else:
    #         return True
    #
    # def is_wifi_connected_on_all_devices(self, devices):
    #     for device in devices:
    #         if not self.is_wifi_connected(device):
    #             return False
    #     else:
    #         return True

    def is_wifi_connected_to(self, device=None, wifi_name=None):
        if wifi_name is None or device is None:
            if device is None:
                raise DeviceError("No device has been provided")
            else:
                raise WiFiError("WiFi Name has not been provided")
        if device.is_emulator:
            raise EmulatorError("Emulator devices could not be connect with real wifi network")
        conn_info = device.api.wifiGetConnectionInfo()
        if conn_info['SSID'] == wifi_name:
            return True
        else:
            return False

    def is_wifi_connected_to_on_devices(self, *args, **kwargs):
        for device in args:
            if not self.is_wifi_connected_to(device, kwargs['wifi_name']):
                return False
        else:
            return True

    def is_wifi_connected_to_all_devices(self, devices, wifi_name=None):
        for device in devices:
            if not self.is_wifi_connected_to(device, wifi_name):
                return False
        else:
            return True
