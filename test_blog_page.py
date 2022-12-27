import allure

import pytest
from .pages.blog_page import BlogPage

@allure.feature("page content")
@allure.story("categories menu")
@allure.severity("critical")
@pytest.mark.regression
def test_appearence_selection_menu_of_categories(browser):
    link ="https://www.nultylighting.co.uk/blog/"
    page = BlogPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_categories()

@allure.feature("page content")
@allure.story("date menu")
@allure.severity("critical")
@pytest.mark.regression
def test_appearence_selection_menu_of_dates(browser):
    link ="https://www.nultylighting.co.uk/blog/"
    page = BlogPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_dates()

@allure.feature("page content")
@allure.story("author menu")
@allure.severity("critical")
@pytest.mark.regression
def test_appearence_selection_menu_of_authors(browser):
    link ="https://www.nultylighting.co.uk/blog/"
    page = BlogPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_authors()

@allure.feature("page content")
@allure.story("redirection video category page")
@allure.severity("critical")
@pytest.mark.regression
def test_redirection_to_video_category_page(browser):
    link ="https://www.nultylighting.co.uk/blog/"
    page = BlogPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_categories()
    page.go_to_video_category_page()

@allure.feature("page content")
@allure.story("redirection to the date page")
@allure.severity("critical")
@pytest.mark.regression
def test_redirection_to_2017_year_page(browser):
    link ="https://www.nultylighting.co.uk/blog/"
    page = BlogPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_dates()
    page.go_to_2017_year_page()

@allure.feature("page content")
@allure.story("redirection to the author page")
@allure.severity("critical")
@pytest.mark.regression
def test_redirection_to_mark_vowles_author_page(browser):
    link ="https://www.nultylighting.co.uk/blog/"
    page = BlogPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_authors()
    page.go_to_mark_vowles_page()
