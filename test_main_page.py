import pytest
from .pages.main_page import MainPage


def test_redirection_to_main_page_from_about_page_via_logo_icon(browser):
    link = "https://www.nultylighting.co.uk/about/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_main_page()