from selenium.webdriver.common.by import By


class BasePageLocators():
    BROCHURE_FORM_REQUEST_HEADER = (By.CLASS_NAME, "brochure-stroke")
    OPENED_BROCHURE_FORM = (By.CLASS_NAME, "brochure-button-content.clearfix.open")
    CPD_LINK = (By.CLASS_NAME, "cpd-stroke")
    NEWSLETTER_FORM_REQUEST = (By.CLASS_NAME, "newsletter-stroke")
    SUCCESS_MESSAGE_OF_FOLLOWING_NEWSLETTERS = (By.CLASS_NAME, "sweet-alert.showSweetAlert.visible")
    OK_BUTTON_FOR_CLOSE_SUCCESS_MESSAGE = (By.CLASS_NAME, "confirm")
    OPENED_NEWSLETTER_FORM = (By.CSS_SELECTOR, "[id='newsletter-popup'][style='display: block;']")
    EMAIL_FOR_NEWSLETTER = (By.ID, "newsletterpopup_email")
    NEWSLETTER_SUBMIT_BUTTON = (By.ID, "newsletterpopup_button")
    MAIN_PAGE_LINK = (By.CLASS_NAME, "title-area")
    PROJECTS_PAGE_LINK = (By.XPATH, "//*[@id='menu-main-menu-left-1']/li[2]/a")
    CLIENTS_PAGE_LINK = (By.XPATH, "//*[@id='menu-main-menu-left-1']/li[4]/a")
    ABOUT_PAGE_LINK = (By.XPATH, "//*[@id='menu-main-menu-left-1']/li[6]/a")
    TEAM_PAGE_LINK = (By.XPATH, "//*[@id='menu-main-menu-right-1']/li[2]/a")
    BLOG_PAGE_LINK = (By.XPATH, "//*[@id='menu-main-menu-right-1']/li[4]/a")
    CONTACT_PAGE_LINK = (By.XPATH, "//*[@id='menu-main-menu-right-1']/li[6]/a")
    BROCHURE_FORM_REQUEST_BUTTON_FOOTER = (By.XPATH, "/html/body/section[2]/a")
    NAME_BROCHURE_FORM = (By.ID, "input_6_1")
    EMAIL_BROCHURE_FORM = (By.ID, "input_6_2")
    MESSAGE_BROCHURE_FORM = (By.ID, "input_6_9")
    BROCHURE_SUBMIT_BUTTON = (By.ID, "gform_submit_button_6")
    SUCCESS_MESSAGE_OF_REQUESTING_BROCHURE = (By.CLASS_NAME, "gform_confirmation_message_6.gforms_confirmation_message")
    FOOTER = (By.TAG_NAME, "footer")


class MainPageLocators():
    PLAY_VIDEO_BUTTON = (By.CLASS_NAME, "play-video-button")
    FULLSCREEN_VIDEO = (By.CSS_SELECTOR, "[style='display: inline; opacity: 1;']")
    GARRISON_PAGE_LINK = (By.CLASS_NAME, "small-12.featured-project.columns.effect-5.effect-5-small.blue.box-two-third")
    MIDTOWN_MALL_PAGE_LINK = (By.XPATH, "/html/body/section[1]/div[6]/div/div/div[1]/div/div[2]/a")
    CARTON_TOWER_PAGE_LINK = (By.XPATH, "/html/body/section[1]/div[6]/div/div/div[1]/div/div[3]/a")
    WORLD_ARCHITECTURE_FEST_PAGE_LINK = (By.XPATH, "/html/body/section[1]/div[6]/div/div/div[2]/div/div[1]/a")
    DUBAI_DESIGN_WEEK_PAGE_LINK = (By.XPATH, "/html/body/section[1]/div[6]/div/div/div[2]/div/div[2]/a")
    BROWNS_PAGE_LINK = (By.XPATH, "/html/body/section[1]/div[7]/div/ul/li[1]/a")
    HAKKASAN_PAGE_LINK = (By.XPATH, "/html/body/section[1]/div[7]/div/ul/li[2]/a")
    HARD_ROCK_PAGE_LINK = (By.XPATH, "/html/body/section[1]/div[7]/div/ul/li[3]/a")
    NIKE_PAGE_LINK = (By.XPATH, "/html/body/section[1]/div[7]/div/ul/li[4]/a")
    THE_RITZ_CARLTON_PAGE_LINK = (By.XPATH, "/html/body/section[1]/div[7]/div/ul/li[5]/a")


class ProjectsPageLocators():
    pass


class AboutPageLocators():
    CPDS_ARTICLE_ACTIVE = (By.CLASS_NAME, "tab-title.cpds.active")


class BlogPageLocators():
    pass


class ContactPageLocators():
    pass







