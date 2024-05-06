# Encapsulation of core APIs of Selenium WebDriver for
# controlling the behavior of web browsers. Each browser is
# backed by a specific WebDriver implementation, called a
# driver. The driver is the component responsible for
# delegating down to the browser, and handles communication
# to and from Selenium and the browser.

import os

from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


class BaseKey:

    def __init__(self, driver):
        self.driver = driver[0]
        self.config = driver[1]
        self._wait = WebDriverWait(self.driver, self.config.timeout())

    def open(self, url):
        self.driver.get(self.config.base_url() + url)

    def quit(self):
        self.driver.quit()

    def _find(self, locator):
        return self.driver.find_element(**locator)

    def enter(self, locator, values):
        el = self._find(locator)
        el.clear()
        el.send_keys(values)

    def click(self, locator):
        self._find(locator).click()

    def wait_for(self, locator):
        return self._wait.until(lambda el: self._find(locator))

    def take_screenshot(self):
        self.driver.get_screenshot_as_png()

    def file_upload(self, locator, path):
        file_input = self._find(locator)
        # Absolute path converted
        upload_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', path))
        file_input.send_keys(upload_file)

    def scroll_to(self, locator):
        el = self._find(locator)
        ActionChains(self.driver).scroll_to_element(el).perform()
        return el

    def select_list_el(self, select_loc, option_loc):
        """
        Select an option from a select list element
        :param select_loc: Locator of select list
        :param option_loc: Locator of option
        :return:
        """
        self.click(select_loc)
        self.wait_for(option_loc)
        self.scroll_to(option_loc)
        self.wait_for(option_loc)
        self.click(option_loc)

    def mouse_hover(self, locator):
        el = self._find(locator)
        ActionChains(self.driver).move_to_element(el).perform()
        return el

    def switch_to_iframe(self, frame_loc):
        self.driver.switch_to.frame(frame_loc)

    def switch_to_default(self):
        self.driver.switch_to.default_content()
