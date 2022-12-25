from .base_page import BasePage
from .locators import BlogPageLocators


class BlogPage(BasePage):
    def appereance_of_the_list_of_categories(self):
        self.scroll_to_the_element(*BlogPageLocators.SCROLL_TO_SELECTION_BLOG_BAR)
        self.browser.find_element(*BlogPageLocators.CATEGORY_SELECTION_BAR).click()
        category_menu = self.browser.find_element(*BlogPageLocators.CATEGORY_STATUS_LOCATOR)
        assert "selectric-open" in category_menu.get_attribute("class"), "Sector's menu hasn't been opened"

    def go_to_video_category_page(self):
        self.browser.find_element(*BlogPageLocators.VIDEO_CATEGORY).click()
        assert self.browser.title == "Video | Nulty | Lighting Design Consultants",\
            "Not the Video page or page's title has been changed"

    def appereance_of_the_list_of_dates(self):
        self.scroll_to_the_element(*BlogPageLocators.SCROLL_TO_SELECTION_BLOG_BAR)
        self.browser.find_element(*BlogPageLocators.DATE_SELECTION_BAR).click()
        category_menu = self.browser.find_element(*BlogPageLocators.DATE_STATUS_LOCATOR)
        assert "selectric-open" in category_menu.get_attribute("class"), "Sector's menu hasn't been opened"

    def go_to_2017_year_page(self):
        self.browser.find_element(*BlogPageLocators.DATE).click()
        assert self.browser.title == "2017 | Nulty | Lighting Design Consultants",\
            "Not the page of 2017 or page's title has been changed"

    def appereance_of_the_list_of_authors(self):
        self.scroll_to_the_element(*BlogPageLocators.SCROLL_TO_SELECTION_BLOG_BAR)
        self.browser.find_element(*BlogPageLocators.AUTHOR_SELECTION_BAR).click()
        category_menu = self.browser.find_element(*BlogPageLocators.AUTHOR_STATUS_LOCATOR)
        assert "selectric-open" in category_menu.get_attribute("class"), "Sector's menu hasn't been opened"

    def go_to_mark_vowles_page(self):
        self.browser.find_element(*BlogPageLocators.AUTHOR).click()
        assert self.browser.current_url == "https://www.nultylighting.co.uk/blog/?a=33#filtered",\
            "Not the Mark's Vowles page or page's title has been changed"
