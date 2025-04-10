import time

from .wifi import *


def open_quick_settings(driver):
    driver.open_notifications()
    device_size = driver.get_window_size()
    height = device_size['height']
    width = device_size['width']
    driver.swipe(int(height * .2), int(width * 0.2), int(height * 0.2), int(width * 0.9))
    time.sleep(2)


def open_application(device=None, app_package=None, app_activity=None, no_reset=True):
    if device is None:
        raise DeviceError("No device has been provided")
    if app_package is None or app_activity is None:
        raise DeviceError("App package or App Acitivity has not been provided")
    if not no_reset:
        print('Clearing app data...')
        result_clear = device.execute_script('mobile: shell', {
            'command': 'pm',
            'args': ['clear', app_package]  # Replace with the app's package name
        })
        print(result_clear)
    print('Starting the app...')
    # Start the app with the desired activity using ADB command
    result_start = device.execute_script('mobile: shell', {
        'command': 'am',
        'args': ['start', '-n', app_package + '/' + app_activity]
    })

    print(result_start)
