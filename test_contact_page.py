import allure
import pytest
from .pages.contact_page import ContactPage

NAME = "John Doe"
EMAIL = "nultytestmail@gmail.com"
MESSAGE = "Lorem Ipsum is simply dummy text of the printing and typesetting industry.\
          Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,  \
          when an unknown printer took a galley of type and scrambled it to make a type specimen book."


@allure.feature("data sending via form")
@allure.story("contact form")
@allure.severity("blocker")
@pytest.mark.e2e
def test_appearence_of_success_message_of_sended_form_at_contact_page(browser):
    name = NAME
    email = EMAIL
    message = MESSAGE
    link = "https://www.nultylighting.co.uk/contact/"
    page = ContactPage(browser, link)
    page.open()
    page.should_be_success_message_after_sending_of_form_at_contact_page(name, email, message)
