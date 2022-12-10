import pytest
from .pages.main_page import MainPage


EMAIL = "nultytestmail@gmail.com"
NAME = "John Doe"
MESSAGE = "Lorem Ipsum is simply dummy text of the printing and typesetting industry.\
          Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,  \
          when an unknown printer took a galley of type and scrambled it to make a type specimen book."



def test_redirection_to_main_page_from_about_page_via_logo_icon(browser):
    link = "https://www.nultylighting.co.uk/about/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_main_page()


def test_redirection_to_projects_page_via_header(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_projects_page()


def test_redirection_to_clients_page_via_header(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_clients_page()


def test_redirection_to_about_page_via_header(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_about_page()

@pytest.mark.xfail(reason="fixing code of tests")
def test_redirection_to_team_page_via_header(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_team_page()

@pytest.mark.xfail(reason="fixing code of tests")
def test_redirection_to_blog_page_via_header(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_blog_page()


@pytest.mark.xfail(reason="fixing code of tests")
def test_redirection_to_contact_page_via_header(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_contact_page()

@pytest.mark.xfail(reason="fixing code of tests")
def test_open_brochure_form_from_header(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_brochure_request_form_from_header()


def test_open_brochure_form_from_footer(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_brochure_form_from_footer()

@pytest.mark.xfail(reason="fixing code of tests")
def test_redirection_to_cpds_article_from_header(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_cpd_article()

@pytest.mark.xfail(reason="fixing code of tests")
def test_open_newsletter_form_from_header(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_newsletter_following_form_from_header()

@pytest.mark.xfail(reason="fixing code of tests")
def test_appearence_of_success_message_by_sending_newsletters_form(browser):
    link = "https://www.nultylighting.co.uk/"
    email = EMAIL
    page = MainPage(browser, link)
    page.open()
    page.should_be_newsletter_following_form_from_header()
    page.success_of_following_newsletters_mailing(email)

@pytest.mark.xfail(reason="fixing code of tests")
def test_appearence_of_success_message_by_sending_brochure_form_from_header(browser):
    link = "https://www.nultylighting.co.uk/"
    email = EMAIL
    name = NAME
    message = MESSAGE
    page = MainPage(browser, link)
    page.open()
    page.should_be_brochure_request_form_from_header()
    page.success_of_requesting_brochure_header(name, email, message)

@pytest.mark.xfail(reason="fixing code of tests")
def test_appearence_of_success_message_by_sending_brochure_form_from_footer(browser):
    link = "https://www.nultylighting.co.uk/"
    email = EMAIL
    name = NAME
    message = MESSAGE
    page = MainPage(browser, link)
    page.open()
    page.should_be_brochure_form_from_footer()
    page.success_of_requesting_brochure_footer(name, email, message)

