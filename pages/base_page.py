from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait

from .locators import BasePageLocators



class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)


    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def go_to_main_page(self):
        link = self.browser.find_element(*BasePageLocators.MAIN_PAGE_LINK).click()
        assert self.browser.title == "Nulty | Lighting Design Consultants", " Not a Projects page or title has been changed"

    def go_to_projects_page(self):
        link = self.browser.find_element(*BasePageLocators.PROJECTS_PAGE_LINK).click()
        assert self.browser.title == "Projects | Nulty | Lighting Design Consultants", " Not a Projects page or title has been changed"

    def go_to_clients_page(self):
        link = self.browser.find_element(*BasePageLocators.CLIENTS_PAGE_LINK).click()
        assert self.browser.title == "Clients | Nulty | Lighting Design Consultants", " Not a Clients page or title has been changed"

    def go_to_clients_page(self):
        link = self.browser.find_element(*BasePageLocators.CLIENTS_PAGE_LINK).click()
        assert self.browser.title == "Clients | Nulty | Lighting Design Consultants", " Not a Clients page or title has been changed"