from selenium import webdriver

from common.chrome_options import chrome_options
from common.config_factory import ConfigFactory


class DriverFactory:

    def __init__(self):
        self.config = ConfigFactory()

    def _set_driver(self, driver):
        driver.implicitly_wait(self.config.timeout())
        return driver

    def get_driver(self):
        browser = self.config.browser()
        if browser == 'chrome':
            driver = webdriver.Chrome(options=chrome_options())
        else:
            try:
                driver = getattr(webdriver, browser.capitalize())()
            except Exception(f'Invalid Browser Setting: {browser}'):
                raise
        return driver
