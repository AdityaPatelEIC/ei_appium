from ei_appium.bluetooth import Bluetooth


class BluetoothController:
    def __init__(self):
        self.ble = Bluetooth()

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
