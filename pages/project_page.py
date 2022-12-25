from .base_page import BasePage
from .locators import ProjectsPageLocators


class ProjectPage(BasePage):
    def appereance_of_the_list_of_sectors(self):
        self.scroll_to_the_element(*ProjectsPageLocators.SCROLL_TO_SELECTION_BAR)
        self.browser.find_element(*ProjectsPageLocators.SECTOR_SELECTION_BAR).click()
        sector_menu = self.browser.find_element(*ProjectsPageLocators.SECTOR_SELECTION_BAR_STATUS_LOCATOR)
        assert "selectric-open" in sector_menu.get_attribute("class"), "Sector's menu hasn't been opened"

    def go_to_retail_sector_page(self):
        self.browser.find_element(*ProjectsPageLocators.RETAIL_SECTOR).click()
        assert self.browser.title == "Retail | Nulty | Lighting Design Consultants",\
            "Not the Retail page or page's title has been changed"


    def appereance_of_the_list_of_clients(self):
        self.scroll_to_the_element(*ProjectsPageLocators.SCROLL_TO_SELECTION_BAR)
        self.browser.find_element(*ProjectsPageLocators.CLIENT_SELECTION_BAR).click()
        client_menu = self.browser.find_element(*ProjectsPageLocators.CLIENT_SELECTION_BAR_STATUS_LOCATOR)
        assert "selectric-open" in client_menu.get_attribute("class"), "Client's menu hasn't been opened"

    def go_to_the_wildstone_page(self):
        self.browser.find_element(*ProjectsPageLocators.WILDSTONE_CLIENT).click()
        assert self.browser.title == "Wildstone | Nulty | Lighting Design Consultants",\
            "Not the Wildstone page or page's title has been changed"