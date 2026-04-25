import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from config.config import Config


@pytest.fixture
def driver():
    if Config.BROWSER.lower() != "chrome":
        raise ValueError(f"Unsupported browser: {Config.BROWSER}")

    options = ChromeOptions()
    options.set_capability("pageLoadStrategy", "normal")

    if os.getenv("CI") == "true" or os.getenv("GITHUB_ACTIONS") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    driver_instance = webdriver.Chrome(options=options)
    driver_instance.implicitly_wait(Config.IMPLICIT_WAIT)

    yield driver_instance

    driver_instance.quit()
