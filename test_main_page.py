import allure

import pytest
from .pages.main_page import MainPage


EMAIL = "nultytestmail@gmail.com"
NAME = "John Doe"
MESSAGE = "Lorem Ipsum is simply dummy text of the printing and typesetting industry.\
          Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,  \
          when an unknown printer took a galley of type and scrambled it to make a type specimen book."



@allure.feature("Navbar menu")
@allure.story("redirection to main page via logo")
@allure.severity("blocker")
@pytest.mark.smoke
def test_redirection_to_main_page_from_about_page_via_logo_icon(browser):
    link = "https://www.nultylighting.co.uk/about/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_main_page()

@allure.feature("Navbar menu")
@allure.story("redirection to projects page")
@allure.severity("blocker")
@pytest.mark.smoke
def test_redirection_to_projects_page_via_header(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_projects_page()

@allure.feature("Navbar menu")
@allure.story("redirection to clients page")
@allure.severity("blocker")
@pytest.mark.smoke
def test_redirection_to_clients_page_via_header(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_clients_page()

@allure.feature("Navbar menu")
@allure.story("redirection to about page")
@allure.severity("blocker")
@pytest.mark.smoke
def test_redirection_to_about_page_via_header(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_about_page()

@allure.feature("Navbar menu")
@allure.story("redirection to team page")
@allure.severity("blocker")
@pytest.mark.smoke
def test_redirection_to_team_page_via_header(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_team_page()

@allure.feature("Navbar menu")
@allure.story("redirection to blog page")
@allure.severity("blocker")
@pytest.mark.smoke
def test_redirection_to_blog_page_via_header(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_blog_page()

@allure.feature("Navbar menu")
@allure.story("redirection to contact page")
@allure.severity("blocker")
@pytest.mark.smoke
def test_redirection_to_contact_page_via_header(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_contact_page()

@allure.feature("Navbar menu")
@allure.story("Open brochure form")
@allure.severity("critical")
@pytest.mark.smoke
def test_open_brochure_form_from_header(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_brochure_request_form_from_header()

@allure.feature("Navbar menu")
@allure.story("redirection to cpds article")
@allure.severity("blocker")
@pytest.mark.smoke
def test_redirection_to_cpds_article_from_header(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_cpd_article()

@allure.feature("Navbar menu")
@allure.story("open newsletter form")
@allure.severity("blocker")
@pytest.mark.smoke
def test_open_newsletter_form_from_header(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_newsletter_following_form_from_header()

@allure.feature("Footer")
@allure.story("open brochure form")
@allure.severity("blocker")
@pytest.mark.smoke
def test_open_brochure_form_from_footer(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_brochure_form_from_footer()

@allure.feature("data sending via form")
@allure.story("newsletter form")
@allure.severity("blocker")
@pytest.mark.e2e
def test_appearence_of_success_message_by_sending_newsletters_form(browser):
    link = "https://www.nultylighting.co.uk/"
    email = EMAIL
    page = MainPage(browser, link)
    page.open()
    page.should_be_newsletter_following_form_from_header()
    page.success_of_following_newsletters_mailing(email)

@allure.feature("data sending via form")
@allure.story("brochure form from navbar")
@allure.severity("blocker")
@pytest.mark.e2e
def test_appearence_of_success_message_by_sending_brochure_form_from_header(browser):
    email = EMAIL
    name = NAME
    message = MESSAGE
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_brochure_request_form_from_header()
    page.success_of_requesting_brochure_header(name, email, message)

@allure.feature("data sending via form")
@allure.story("brochure form from footer")
@allure.severity("blocker")
@pytest.mark.e2e
def test_appearence_of_success_message_by_sending_brochure_form_from_footer(browser):
    link = "https://www.nultylighting.co.uk/"
    email = EMAIL
    name = NAME
    message = MESSAGE
    page = MainPage(browser, link)
    page.open()
    page.should_be_brochure_form_from_footer()
    page.success_of_requesting_brochure_footer(name, email, message)

@allure.feature("page content")
@allure.story("video")
@allure.severity("critical")
@pytest.mark.regression
def test_playback_video(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.video_should_be_playing()

@allure.feature("page content")
@allure.story("garrison_club")
@allure.severity("critical")
@pytest.mark.regression
def test_redirection_to_garrison_club_page(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_the_garrison_club_page()

@allure.feature("page content")
@allure.story("midtown")
@allure.severity("critical")
@pytest.mark.regression
def test_redirection_to_the_midtown_mall_page(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_the_midtown_mall_page()

@allure.feature("page content")
@allure.story("carlton_tower")
@allure.severity("critical")
@pytest.mark.regression
def test_redirection_to_carlton_tower_page(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_the_carlton_tower_jumeirah_page()

@allure.feature("page content")
@allure.story("world architecture festival")
@allure.severity("critical")
@pytest.mark.regression
def test_redirection_to_world_architecture_festival_page(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_world_architecture_festival_page()

@allure.feature("page content")
@allure.story("dubai design week")
@allure.severity("critical")
@pytest.mark.regression
def test_redirection_to_dubai_design_week_page(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_the_dubai_design_week_page()

@allure.feature("page content")
@allure.story("browns")
@allure.severity("critical")
@pytest.mark.regression
def test_redirection_to_browns_page(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_browns_page()

@allure.feature("page content")
@allure.story("ghakkasan")
@allure.severity("critical")
@pytest.mark.regression
def test_redirection_to_hakkasan_page(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_hakkasan_page()

@allure.feature("page content")
@allure.story("hard rock")
@allure.severity("critical")
@pytest.mark.regression
def test_redirection_to_hard_rock_hotel_page(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_hard_rock_hotel_page()

@allure.feature("page content")
@allure.story("nike")
@allure.severity("critical")
@pytest.mark.regression
def test_redirection_to_nike_page(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_nike_page()

@allure.feature("page content")
@allure.story("the ritz-carlton")
@allure.severity("critical")
@pytest.mark.regression
def test_redirection_to_the_ritz_carlton_page(browser):
    link = "https://www.nultylighting.co.uk/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_the_ritz_carlton_page()