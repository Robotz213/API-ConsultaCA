from webdriver_manager.chrome import ChromeDriverManager

# Selenium Imports
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.core.driver_cache import DriverCacheManager


import os
import pathlib
import platform
from app import app
from typing import Type

list_args = ['--ignore-ssl-errors=yes', '--ignore-certificate-errors',
             "--display=:10", "--window-size=1600,900", "--no-sandbox", "--disable-blink-features=AutomationControlled",
             '--kiosk-printing']


def DriverLauncher() -> Type[WebDriver]:

    chrome_options = Options()

    for argument in list_args:
        chrome_options.add_argument(argument)
    
    with app.app_context():
        path_chrome: str = app.config["CHROMEDRIVER_PATH"]

    driver_cache_manager = DriverCacheManager(root_dir=path_chrome)

    driverinst = ChromeDriverManager(
        cache_manager=driver_cache_manager).install()

    driverchrome = "chromedriver.exe"
    if platform.system() == "Linux":
        driverchrome = "chromedriver"

    path = os.path.join(pathlib.Path(
        driverinst).parent.resolve(), driverchrome)

    return webdriver.Chrome(service=Service(path), options=chrome_options)
