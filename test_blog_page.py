import pytest
from .pages.blog_page import BlogPage

@pytest.mark.skip(reason="Test works")
def test_appearence_selection_menu_of_categories(browser):
    link ="https://www.nultylighting.co.uk/blog/"
    page = BlogPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_categories()

@pytest.mark.skip(reason="Test works")
def test_appearence_selection_menu_of_dates(browser):
    link ="https://www.nultylighting.co.uk/blog/"
    page = BlogPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_dates()

@pytest.mark.skip(reason="Test works")
def test_appearence_selection_menu_of_authors(browser):
    link ="https://www.nultylighting.co.uk/blog/"
    page = BlogPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_authors()

@pytest.mark.skip(reason="Test works")
def test_redirection_to_video_category_page(browser):
    link ="https://www.nultylighting.co.uk/blog/"
    page = BlogPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_categories()
    page.go_to_video_category_page()

@pytest.mark.skip(reason="Test works")
def test_redirection_to_2017_year_page(browser):
    link ="https://www.nultylighting.co.uk/blog/"
    page = BlogPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_dates()
    page.go_to_2017_year_page()

@pytest.mark.skip(reason="Test works")
def test_redirection_to_mark_vowles_author_page(browser):
    link ="https://www.nultylighting.co.uk/blog/"
    page = BlogPage(browser, link)
    page.open()
    page.appereance_of_the_list_of_authors()
    page.go_to_mark_vowles_page()
