from .base_page import BasePage
from .locators import ContactPageLocators



class ContactPage(BasePage):
    def should_be_success_message_after_sending_of_form_at_contact_page(self, name, email, message):
        self.scroll_to_the_element(*ContactPageLocators.CONTACT_FORM_SUBMIT_BUTTON)
        self.browser.find_element(*ContactPageLocators.CONTACT_FORM_NAME).send_keys(name)
        self.browser.find_element(*ContactPageLocators.CONTACT_FORM_EMAIL).send_keys(email)
        self.browser.find_element(*ContactPageLocators.CONTACT_FORM_MESSAGE).send_keys(message)
        self.scroll_to_the_element(*ContactPageLocators.SCROLL_FOR_PRESS_SUBMIT_BUTTON)
        self.browser.find_element(*ContactPageLocators.CONTACT_FORM_SUBMIT_BUTTON).click()
        assert self.is_element_present(*ContactPageLocators.SUCCESS_MESSAGE_OF_SENDED_CONTACT_FORM),\
            "Form hadn't been sended or success locator had been changed"
