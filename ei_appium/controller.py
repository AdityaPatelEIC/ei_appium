import os
import re
import signal
import subprocess
import time
import json
import requests

from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.options.android import UiAutomator2Options

# Globals
_APPIUM_DRIVERS = []
_APPIUM_SERVER_PROCESS_IDS = []


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


def start_appium_server(port=4723):
    """Starts the Appium server programmatically in a new terminal."""
    global _APPIUM_SERVER_PROCESS_IDS

    if os.name == 'nt':  # For Windows
        command = f'start cmd /K appium -p {port} --relaxed-security'
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        _APPIUM_SERVER_PROCESS_IDS.append(process.pid)
    elif os.name == 'posix':
        if subprocess.run(["uname"], capture_output=True, text=True).stdout.strip() == "Darwin":
            # macOS
            appium_command = f"appium -p {port} --relaxed-security"
            command = f'tell application "Terminal" to do script "{appium_command}"'
            process = subprocess.Popen(['osascript', '-e', command])
        else:
            # Linux
            command = f'gnome-terminal -- bash -c "appium -p {port}; exec bash"'
            process = subprocess.Popen(command, shell=True)
        _APPIUM_SERVER_PROCESS_IDS.append(process.pid)

    print(f"Appium server started on port {port}. Check the terminal for logs.")
    wait_for_appium_server(port)


def get_connected_ios_devices():
    """Fetches all connected iOS simulators and real devices."""
    devices = []

    # Get simulators
    result = subprocess.run(['xcrun', 'simctl', 'list', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True)
    if result.returncode == 0:
        for line in result.stdout.strip().split('\n'):
            if "(Booted)" in line:
                match = re.search(r'\(([0-9A-Fa-f-]{36})\)', line)
                if match:
                    devices.append(match.group(1))
                else:
                    print("UDID format is not matching with regular expression. Change regular expression accordingly")
    else:
        print("Error:", result.stderr)

    # Get real devices
    result = subprocess.run(['idevice_id', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        devices += result.stdout.strip().split('\n')

    return devices


def get_connected_android_devices():
    """Fetches all connected Android devices."""
    result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    devices = []
    for line in result.stdout.splitlines():
        if line.strip() and not line.startswith('List of devices'):
            device_id = line.split()[0]
            devices.append(device_id)
    return devices


def setup_devices(platform="android"):
    """Sets up Appium drivers for all connected devices."""
    global _APPIUM_DRIVERS
    _APPIUM_DRIVERS = []

    if platform.lower() == "ios":
        devices = get_connected_ios_devices()
        driver_cls = XCUITestOptions
        default_caps = {
            "platformName": "iOS",
            "deviceName": "iPhone",
            "automationName": "XCUITest",
            "newCommandTimeout": 120
        }
        wda_local_port = 8200
    elif platform.lower() == "android":
        devices = get_connected_android_devices()
        driver_cls = UiAutomator2Options
        default_caps = {
            "platformName": "Android",
            "automationName": "UiAutomator2",
            "newCommandTimeout": 120,
            "noReset": False
        }
    else:
        print("Unsupported platform specified.")
        return

    if not devices:
        print(f"No {platform} devices connected.")
        return

    port = 4723
    for device in devices:
        print(f"Setting up device: {device}")

        desired_caps = default_caps.copy()
        desired_caps["udid"] = device
        if platform.lower() == "ios":
            desired_caps["wdaLocalPort"] = wda_local_port
            wda_local_port += 5

        start_appium_server(port)
        options = driver_cls().load_capabilities(desired_caps)
        driver = webdriver.Remote(f'http://localhost:{port}', options=options)

        _APPIUM_DRIVERS.append({device: driver})
        print(f"Started Appium session for {platform} device {device} on port {port}")
        port += 1


def return_devices():
    """Returns the list of Appium driver objects."""
    return _APPIUM_DRIVERS if _APPIUM_DRIVERS else None


def get_device_object(udid):
    """Returns Appium driver for a specific device by UDID."""
    for device_info in _APPIUM_DRIVERS:
        if udid in device_info:
            return device_info[udid]
    return None


def is_device_emulator(driver):
    """Checks if the connected Android device is an emulator."""
    if not driver:
        print("No driver provided.")
        return False
    return "emulator" in driver.capabilities.get("udid", "").lower()


def close_device_connections():
    """Closes all Appium sessions."""
    global _APPIUM_DRIVERS
    for driver_dict in _APPIUM_DRIVERS:
        list(driver_dict.values())[0].quit()
    _APPIUM_DRIVERS = []
    print("Closed all device connections.")


def stop_appium_server():
    """Stops all Appium server processes."""
    for pid in _APPIUM_SERVER_PROCESS_IDS:
        if os.name == 'nt':
            subprocess.run(['taskkill', '/F', '/PID', str(pid)])
        else:
            try:
                os.kill(pid, signal.SIGTERM)
            except OSError:
                pass
    print("Stopped all Appium servers.")
    _APPIUM_SERVER_PROCESS_IDS.clear()


# Example Usage
if __name__ == "__main__":
    # Choose your platform: "android" or "ios"
    setup_devices(platform="android")

    time.sleep(10)  # Let the sessions run for a bit

    close_device_connections()
    stop_appium_server()
