import pytest
from .pages.about_page import AboutPage

EMAIL = "nultytestmail@gmail.com"
NAME = "John Doe"
PHONE_NUMBER = "+84 0000 00 001"
MESSAGE = "Lorem Ipsum is simply dummy text of the printing and typesetting industry.\
          Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,  \
          when an unknown printer took a galley of type and scrambled it to make a type specimen book."



@pytest.mark.skip(reason="Test works")
def test_appearence_of_process_article(browser):
    link = "https://www.nultylighting.co.uk/about/"
    page = AboutPage(browser, link)
    page.open()
    page.should_be_process_article()


@pytest.mark.skip(reason="Test works")
def test_appearence_of_awards_article(browser):
    link = "https://www.nultylighting.co.uk/about/"
    page = AboutPage(browser, link)
    page.open()
    page.should_be_awards_article()


@pytest.mark.skip(reason="Test works")
def test_appearence_of_cpds_article(browser):
    link = "https://www.nultylighting.co.uk/about/"
    page = AboutPage(browser, link)
    page.open()
    page.should_be_cpds_article()


@pytest.mark.skip(reason="Test works")
def test_appearence_of_company_article(browser):
    link = "https://www.nultylighting.co.uk/about/"
    page = AboutPage(browser, link)
    page.open()
    page.should_be_company_article()


@pytest.mark.skip(reason="Test works")
def test_appearence_of_success_message_of_sended_cpd_form(browser):
    name = NAME
    email = EMAIL
    phone_number = PHONE_NUMBER
    message = MESSAGE
    link = "https://www.nultylighting.co.uk/about/"
    page = AboutPage(browser, link)
    page.open()
    page.should_be_cpds_article()
    page.should_be_success_message_after_sending_of_cpd_form(name, email, phone_number, message)

