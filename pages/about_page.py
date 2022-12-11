from .base_page import BasePage
from .locators import AboutPageLocators



class AboutPage(BasePage):
    def should_be_process_article(self):
        self.scroll_to_the_element(*AboutPageLocators.SCROLL_TO_OBJECT)
        self.browser.find_element(*AboutPageLocators.PROCESS_ARTICLE_LINK).click()
        assert self.is_element_present(*AboutPageLocators.PROCESS_ARTICLE_ACTIVE), "Process article didn't appear"

    def should_be_awards_article(self):
        self.scroll_to_the_element(*AboutPageLocators.SCROLL_TO_OBJECT)
        self.browser.find_element(*AboutPageLocators.AWARDS_ARTICLE_LINK).click()
        assert self.is_element_present(*AboutPageLocators.AWARDS_ARTICLE_ACTIVE), "Awards article didn't appear"

    def should_be_cpds_article(self):
        self.scroll_to_the_element(*AboutPageLocators.SCROLL_TO_OBJECT)
        self.browser.find_element(*AboutPageLocators.CPDS_ARTICLE_LINK).click()
        assert self.is_element_present(*AboutPageLocators.CPDS_ARTICLE_ACTIVE), "CPDs article didn't appear"

    def should_be_company_article(self):
        self.scroll_to_the_element(*AboutPageLocators.SCROLL_TO_OBJECT)
        self.browser.find_element(*AboutPageLocators.PROCESS_ARTICLE_LINK).click()
        self.browser.find_element(*AboutPageLocators.COMPANY_ARTICLE_LINK).click()
        assert self.is_element_present(*AboutPageLocators.COMPANY_ARTICLE_ACTIVE), "Company article didn't appear"