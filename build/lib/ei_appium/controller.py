import os
import subprocess
import time

import requests
from appium import webdriver
from appium.options.android import UiAutomator2Options

_APPIUM_DRIVERS = None


def get_connected_devices():
    """Fetches all connected devices via adb."""
    # Run the adb devices command to get a list of connected devices
    result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = result.stdout.decode('utf-8')

    # Parse the output to extract device IDs
    devices = []
    for line in output.splitlines():
        if line.strip() and not line.startswith('List of devices'):
            device_id = line.split()[0]
            devices.append(device_id)

    return devices


def start_appium_server(port=4723):

    if os.name == 'nt':  # For Windows
        command = f'start cmd /K appium -p {port} --relaxed-security'
    elif os.name == 'posix':  # For Linux
        command = f'gnome-terminal -- bash -c "appium -p {port}; exec bash"'

    subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"Appium server started on port {port}. Check the terminal for logs.")
    wait_for_appium_server(port)


def wait_for_appium_server(port, timeout=60):
    """Waits for the Appium server to be ready to accept connections."""
    url = f'http://localhost:{port}/status'
    start_time = time.time()

    while time.time() - start_time < timeout:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                status = response.json()
                if status['value']['ready']:
                    print(f"Appium server is fully ready on port {port}.")
                    return True
        except requests.exceptions.RequestException:
            pass
        time.sleep(2)

    print(f"Appium server did not become ready on port {port} within the expected time.")
    return False


def setup_ad():
    """Sets up Appium drivers for all connected devices."""
    global _APPIUM_DRIVERS
    _APPIUM_DRIVERS = []  # Reset drivers list

    devices = get_connected_devices()
    if not devices:
        print("No devices connected.")
        return

    port = 4723
    for device in devices:
        # Set desired capabilities for each device
        desired_caps = {
            'platformName': 'Android',
            'udid': device,  # Unique device ID
            'automationName': 'UiAutomator2',
            'noReset': False,
        }
        start_appium_server(port)
        # Start a new Appium driver on a unique port for each device
        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)
        driver = webdriver.Remote(f'http://localhost:{port}', options=capabilities_options)
        driver_info = {device: driver}
        _APPIUM_DRIVERS.append(driver_info)
        print(f"Started Appium session for device {device} on port {port}")

        port += 1


def return_devices():
    """Returns the list of created Appium drivers (devices)."""
    if _APPIUM_DRIVERS:
        driver_list = []
        for item in _APPIUM_DRIVERS:
            driver_list.append(list(item.values())[0])
        return driver_list
    else:
        return None


def get_device_object(udid):
    if _APPIUM_DRIVERS:
        for item in _APPIUM_DRIVERS:
            if list(item.keys())[0] == udid:
                return list(item.values())[0]
    else:
        return None


def is_device_emulator(driver=None):
    if driver is None:
        print("No device driver has been provided")
        return
    device_udid = driver.capabilities['udid']
    if "emulator" in device_udid:
        return True
    else:
        return False


