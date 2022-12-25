import pytest
from .pages.project_page import ProjectPage

@pytest.mark.skip(reason="Test works")
def test_appearence_selection_menu_of_sectors(browser):
    link = "https://www.nultylighting.co.uk/projects/"
    page = ProjectPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_sectors()

@pytest.mark.skip(reason="Test works")
def test_appearence_selection_menu_of_clients(browser):
    link = "https://www.nultylighting.co.uk/projects/"
    page = ProjectPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_clients()

@pytest.mark.skip(reason="Test works")
def test_redirection_to_retail_sector_page(browser):
    link = "https://www.nultylighting.co.uk/projects/"
    page = ProjectPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_sectors()
    page.go_to_retail_sector_page()

@pytest.mark.skip(reason="Test works")

def test_redirection_to_the_wildstone_page(browser):
    link = "https://www.nultylighting.co.uk/projects/"
    page = ProjectPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_clients()
    page.go_to_the_wildstone_page()
