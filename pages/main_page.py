from .base_page import BasePage
from .locators import MainPageLocators



class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def video_should_be_playing(self):
        self.browser.find_element(*MainPageLocators.PLAY_VIDEO_BUTTON).click()
        assert self.is_element_present(*MainPageLocators.FULLSCREEN_VIDEO), "Company's video is not playing"

    def go_to_the_garrison_club_page(self):
        self.browser.find_element(*MainPageLocators.GARRISON_PAGE_LINK).click()
        assert self.browser.title == "The Garrison Club, Chelsea Barracks | Nulty | Lighting Design",\
            "Not The Garrison club page or endpoint page has been changed"

    def go_to_the_midtown_mall_page(self):
        self.browser.find_element(*MainPageLocators.MIDTOWN_MALL_PAGE_LINK).click()
        assert self.browser.title == "Midtown Mall, Riyadh | Nulty | Lighting Design Consultants",\
            "Not the Midtowns Mall page or endpoint page has been changed"

    def go_to_the_carlton_tower_jumeirah_page(self):
        self.browser.find_element(*MainPageLocators.CARTON_TOWER_PAGE_LINK).click()
        assert self.browser.title == "The Carlton Tower Jumeirah | Nulty | Hotel Lighting Design",\
            "Not the Carlton Tower Jumeirah page or endpoint page has been changed"

    def go_to_world_architecture_festival_page(self):
        self.browser.find_element(*MainPageLocators.WORLD_ARCHITECTURE_FEST_PAGE_LINK).click()
        assert self.browser.title == "World Architecture Festival 2022 | Nulty | Lighting Design Consultants",\
            "Not the World Architecture Festival 2022 page or endpoint page has been changed"

    def go_to_the_dubai_design_week_page(self):
        self.browser.find_element(*MainPageLocators.DUBAI_DESIGN_WEEK_PAGE_LINK).click()
        assert self.browser.title == "Dubai Design Week 2022 | Nulty | Lighting Design Consultants",\
            "Not the Dubai Design Week 2022 page or endpoint page has been changed"

    def go_to_browns_page(self):
        self.browser.find_element(*MainPageLocators.BROWNS_PAGE_LINK).click()
        assert self.browser.title == "Browns Brook Street, London | Nulty | Lighting Designers",\
            "Not Brown page or endpoint page has been changed"

    def go_to_hakkasan_page(self):
        self.browser.find_element(*MainPageLocators.HAKKASAN_PAGE_LINK).click()
        assert self.browser.title == "Hakkasan | Nulty | Lighting Design Consultants",\
            "Not Hakkasan page or endpoint page has been changed"

    def go_to_hard_rock_hotel_page(self):
        self.browser.find_element(*MainPageLocators.HARD_ROCK_PAGE_LINK).click()
        assert self.browser.title == "Hard Rock Hotel, London | Nulty | Lighting Design Consultants",\
            "Not Hard Rock Hotel page or endpoint page has been changed"

    def go_to_nike_page(self):
        self.browser.find_element(*MainPageLocators.NIKE_PAGE_LINK).click()
        assert self.browser.title == "Nike | Nulty | Lighting Design Consultants",\
            "Not Nike page or endpoint page has been changed"

    def go_to_the_ritz_carlton_page(self):
        self.browser.find_element(*MainPageLocators.THE_RITZ_CARLTON_PAGE_LINK).click()
        assert self.browser.title == "The Ritz-Carlton, Astana | Nulty | Lighting Design Consultants",\
            "Not The Ritz-Carlton page or endpoint page has been changed"

