from .base_page import BasePage
from .locators import AboutPageLocators



class AboutPage(BasePage):
    def should_be_process_article(self):
        self.scroll_to_the_element(*AboutPageLocators.SCROLL_TO_ARTICLES)
        self.browser.find_element(*AboutPageLocators.PROCESS_ARTICLE_LINK).click()
        assert self.is_element_present(*AboutPageLocators.PROCESS_ARTICLE_ACTIVE), "Process article didn't appear"

    def should_be_awards_article(self):
        self.scroll_to_the_element(*AboutPageLocators.SCROLL_TO_ARTICLES)
        self.browser.find_element(*AboutPageLocators.AWARDS_ARTICLE_LINK).click()
        assert self.is_element_present(*AboutPageLocators.AWARDS_ARTICLE_ACTIVE), "Awards article didn't appear"

    def should_be_cpds_article(self):
        self.scroll_to_the_element(*AboutPageLocators.SCROLL_TO_ARTICLES)
        self.browser.find_element(*AboutPageLocators.CPDS_ARTICLE_LINK).click()
        assert self.is_element_present(*AboutPageLocators.CPDS_ARTICLE_ACTIVE), "CPDs article didn't appear"

    def should_be_company_article(self):
        self.scroll_to_the_element(*AboutPageLocators.SCROLL_TO_ARTICLES)
        self.browser.find_element(*AboutPageLocators.PROCESS_ARTICLE_LINK).click()
        self.browser.find_element(*AboutPageLocators.COMPANY_ARTICLE_LINK).click()
        assert self.is_element_present(*AboutPageLocators.COMPANY_ARTICLE_ACTIVE), "Company article didn't appear"

    def should_be_success_message_after_sending_of_cpd_form(self, name, email, phone_number, message):
        self.scroll_to_the_element(*AboutPageLocators.SCROLL_TO_CPD_FORM)
        self.browser.find_element(*AboutPageLocators.NAME_CPD_FORM).send_keys(name)
        self.browser.find_element(*AboutPageLocators.EMAIL_CPD_FORM).send_keys(email)
        self.browser.find_element(*AboutPageLocators.PHONE_NUMBER_CPD_FORM).send_keys(phone_number)
        self.browser.find_element(*AboutPageLocators.INTERESTED_IN_TEXT_CPD_FORM).send_keys(message)
        self.scroll_to_the_element(*AboutPageLocators.SCROLL_TO_SUBMIT_BUTTON)
        self.browser.find_element(*AboutPageLocators.CPD_SUBMIT_BUTTON).click()
        assert self.is_element_present(*AboutPageLocators.SUCCESS_MESSAGE_OF_SENDED_CPD_FORM), "Form hadn't been sended or success locator had been changed"