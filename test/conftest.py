import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope='session')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1420,1080')
    options.add_argument('--headless=new')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-dev-shm-usage')

    binary = os.getenv('CHROME_BIN')
    if binary:
        options.binary_location = binary

    driver_path = os.getenv('CHROME_DRIVER_PATH')
    service = Service(executable_path=driver_path) if driver_path else None

    driver_ = webdriver.Chrome(service=service, options=options) if service else webdriver.Chrome(options=options)
    yield driver_
    driver_.quit()


@pytest.fixture(scope='session')
def base_url():
    return os.getenv('APP_BASE_URL', 'http://localhost:8000')