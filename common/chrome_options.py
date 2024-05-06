"""
    options settings for Chrome browser
"""
from selenium import webdriver


def chrome_options():
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'

    # options.add_argument()
    # options.add_experimental_option()

    # Maximize window
    options.add_argument('start-maximized')
    # options.add_argument('window-position=500,500')
    # options.add_argument('window-size=3000,2000')

    # Remove automation warning
    options.add_experimental_option('excludeSwitches', ['enable-automation', 'enable-logging'])

    # options.add_argument('--headless')

    # Login popup handle
    prefs = {
        'credentials_enable_service': False,
        'profile.password_manager_enable': False
    }
    options.add_experimental_option('prefs', prefs)

    # Loading cache of browser. Make sure all browser closed before launch to avoid error.
    # options.add_argument(r'--user-data-dir=C:\Users\15414\AppData\Local\Google\Chrome\User Data')

    # Open browser in incognito mode
    # options.add_argument('incognito')

    # Remove redundant logging info in console
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # Remove redundant info in console
    options.add_argument('--log_level=3')
    options.add_argument('--disable-gpu')
    options.add_argument('--ignore-certificate-errors')

    return options
