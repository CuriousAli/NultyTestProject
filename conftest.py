import allure
import pytest
import time
from allure_commons.types import AttachmentType
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    with allure.step("Make screenshot"):
        allure.attach(browser.get_screenshot_as_png(), name=f"{time.strftime('%m-%d-%Y,_%H:%M:%S')}", attachment_type=AttachmentType.PNG)
    browser.quit()