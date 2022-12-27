import allure

import pytest
from .pages.project_page import ProjectPage

@allure.feature("page content")
@allure.story("sectors menu")
@allure.severity("critical")
@pytest.mark.regression
def test_appearence_selection_menu_of_sectors(browser):
    link = "https://www.nultylighting.co.uk/projects/"
    page = ProjectPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_sectors()

@allure.feature("page content")
@allure.story("client menu")
@allure.severity("critical")
@pytest.mark.regression
def test_appearence_selection_menu_of_clients(browser):
    link = "https://www.nultylighting.co.uk/projects/"
    page = ProjectPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_clients()

@allure.feature("page content")
@allure.story("retail")
@allure.severity("critical")
@pytest.mark.regression
def test_redirection_to_retail_sector_page(browser):
    link = "https://www.nultylighting.co.uk/projects/"
    page = ProjectPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_sectors()
    page.go_to_retail_sector_page()

@allure.feature("page content")
@allure.story("wildstone")
@allure.severity("critical")
@pytest.mark.regression
def test_redirection_to_the_wildstone_page(browser):
    link = "https://www.nultylighting.co.uk/projects/"
    page = ProjectPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_clients()
    page.go_to_the_wildstone_page()
