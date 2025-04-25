from ei_appium.quick_settings import QuickSettings


class QuickSettingsController:
    def __init__(self):
        self.qs = QuickSettings()

    def switch_aeroplane_mode(self, device, selector, mode):
        self.qs.switch_aeroplane_mode(device, selector, mode)
