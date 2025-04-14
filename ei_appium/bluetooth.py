from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from .wifi import *


class Bluetooth:
    def open_bluetooth_setting(self, device):
        if device is None:
            raise DeviceError("No device has been provided")
        open_quick_settings(device)
        actions = ActionChains(device)
        wifi_btn = device.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Bluetooth")')
        actions.click_and_hold(wifi_btn).perform()
        time.sleep(1)
        actions.release(wifi_btn)
        time.sleep(2)

    def turn_on_bluetooth(self, device=None):
        try:
            device.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Bluetooth")')
        except NoSuchElementException:
            open_quick_settings(device)
        bluetooth = device.find_element(By.XPATH, '//android.widget.Switch[@content-desc="Bluetooth."]')
        if bluetooth.get_attribute('checked') == 'false':
            bluetooth.click()

    def turn_on_bluetooth_on_devices(self, *args):
        for device in args:
            self.turn_on_bluetooth(device)

    def turn_on_bluetooth_on_all_devices(self, devices):
        for device in devices:
            self.turn_on_bluetooth(device)

    def turn_off_bluetooth(self, device=None):
        try:
            device.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Bluetooth")')
        except NoSuchElementException:
            open_quick_settings(device)
        bluetooth = device.find_element(By.XPATH, '//android.widget.Switch[@content-desc="Bluetooth."]')
        if bluetooth.get_attribute('checked') == 'true':
            bluetooth.click()

    def turn_off_bluetooth_on_devices(self, *args):
        for device in args:
            self.turn_off_bluetooth(device)

    def turn_off_bluetooth_on_all_devices(self, devices):
        for device in devices:
            self.turn_off_bluetooth(device)

    def get_bluetooth_scan_result(self, device):
        try:
            device.find_element(By.XPATH,'//android.widget.TextView[@resource-id="android:id/title" and @text="Pair new device"]')
        except NoSuchElementException:
            self.open_bluetooth_setting(device)
        pair_new_button = device.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("Pair new device")')
        pair_new_button.click()
        print("Waiting 10 seconds to load the bluetooth devices...")
        time.sleep(10)
        recycler_containing_devices = device.find_element(By.ID, 'com.android.settings:id/recycler_view')
        wifi_names = recycler_containing_devices.find_elements(By.CLASS_NAME, "android.widget.TextView")
        bluetooth_results = [wifi_name.text for wifi_name in wifi_names[3:]]
        return bluetooth_results

    def get_bluetooth_scan_result_on_devices(self, *args):
        scan_result = dict()
        for device in args:
            udid = device.capabilities.get("udid")
            scan_result[udid] = self.get_bluetooth_scan_result(device)
        return scan_result

    def get_bluetooth_scan_result_on_all_devices(self, devices):
        scan_result = dict()
        for device in devices:
            udid = device.capabilities.get("udid")
            scan_result[udid] = self.get_bluetooth_scan_result(device)
        return scan_result

    # def connect_to_wifi(self, device, wifi_name=None, wifi_password=None):
    #     if is_device_emulator(device):
    #         raise EmulatorError("Emulator devices could not be connect with real wifi network")
    #     if wifi_name and wifi_password:
    #         self.turn_on_wifi(device)
    #         wifi = device.find_element(By.XPATH,
    #                                    f'//android.widget.TextView[@resource-id="android:id/title" and @text="{wifi_name}"]')
    #         wifi.click()
    #         time.sleep(1)
    #         password_text_box = device.find_element(By.ID, 'com.android.settings:id/password')
    #         password_text_box.send_keys(wifi_password)
    #         device.find_element(By.ID, 'android:id/button1').click()
    #
    #     else:
    #         if wifi_name is None and wifi_password is None:
    #             raise WiFiError("WiFi Name and Password must be provided")
    #         elif wifi_name is None:
    #             raise WiFiError("WiFi Name must be provided")
    #         else:
    #             raise WiFiError("WiFi Password must be provided")
