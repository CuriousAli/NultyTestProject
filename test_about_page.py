import allure

import pytest
from .pages.about_page import AboutPage

EMAIL = "nultytestmail@gmail.com"
NAME = "John Doe"
PHONE_NUMBER = "+84 0000 00 001"
MESSAGE = "Lorem Ipsum is simply dummy text of the printing and typesetting industry.\
          Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,  \
          when an unknown printer took a galley of type and scrambled it to make a type specimen book."



@allure.feature("page content")
@allure.story("process article")
@allure.severity("blocker")
@pytest.mark.smoke
def test_appearence_of_process_article(browser):
    link = "https://www.nultylighting.co.uk/about/"
    page = AboutPage(browser, link)
    page.open()
    page.should_be_process_article()


@allure.feature("page content")
@allure.story("awards article")
@allure.severity("blocker")
@pytest.mark.smoke
def test_appearence_of_awards_article(browser):
    link = "https://www.nultylighting.co.uk/about/"
    page = AboutPage(browser, link)
    page.open()
    page.should_be_awards_article()


@allure.feature("page content")
@allure.story("cpds article")
@allure.severity("blocker")
@pytest.mark.smoke
def test_appearence_of_cpds_article(browser):
    link = "https://www.nultylighting.co.uk/about/"
    page = AboutPage(browser, link)
    page.open()
    page.should_be_cpds_article()


@allure.feature("page content")
@allure.story("company article")
@allure.severity("blocker")
@pytest.mark.smoke
def test_appearence_of_company_article(browser):
    link = "https://www.nultylighting.co.uk/about/"
    page = AboutPage(browser, link)
    page.open()
    page.should_be_company_article()


@allure.feature("form sending")
@allure.story("cpd form")
@allure.severity("critical")
@pytest.mark.e2e
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

