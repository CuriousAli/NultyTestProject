from selenium.webdriver.common.by import By


class BasePageLocators():
    BROCHURE_FORM_REQUEST_HEADER = (By.CLASS_NAME, "brochure-stroke")
    OPENED_BROCHURE_FORM = (By.CLASS_NAME, "brochure-button-content.clearfix.open")
    CPD_LINK = (By.CLASS_NAME, "cpd-stroke")
    NEWSLETTER_FORM_REQUEST = (By.CLASS_NAME, "newsletter-stroke")
    SUCCESS_MESSAGE_OF_FOLLOWING_NEWSLETTERS = (By.CLASS_NAME, "sweet-alert.showSweetAlert.visible")
    OK_BUTTON_FOR_CLOSE_SUCCESS_MESSAGE = (By.CLASS_NAME, "confirm")
    OPENED_NEWSLETTER_FORM = (By.CLASS_NAME, "top-newsletter-enabled")
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
    FULLSCREEN_VIDEO = (By.CSS_SELECTOR, '[style="display: inline; opacity: 1;"]')
    GARRISON_PAGE_LINK = (By.CLASS_NAME, "small-12.featured-project.columns.effect-5.effect-5-small.blue.box-two-third")
    MIDTOWN_MALL_PAGE_LINK = (By.XPATH, "/html/body/section[1]/div[6]/div/div/div[1]/div/div[2]/a")
    CARTON_TOWER_PAGE_LINK = (By.XPATH, "/html/body/section[1]/div[6]/div/div/div[1]/div/div[3]/a")
    WORLD_ARCHITECTURE_FEST_PAGE_LINK = (By.XPATH, "/html/body/section[1]/div[6]/div/div/div[2]/div/div[1]/a/div[1]")
    DUBAI_DESIGN_WEEK_PAGE_LINK = (By.XPATH, "/html/body/section[1]/div[6]/div/div/div[2]/div/div[2]/a/div[1]")
    BROWNS_PAGE_LINK = (By.XPATH, "/html/body/section[1]/div[7]/div/ul/li[1]/a/img[1]")
    HAKKASAN_PAGE_LINK = (By.XPATH, "/html/body/section[1]/div[7]/div/ul/li[2]/a/img[1]")
    HARD_ROCK_PAGE_LINK = (By.XPATH, "/html/body/section[1]/div[7]/div/ul/li[3]/a/img[1]")
    NIKE_PAGE_LINK = (By.XPATH, "/html/body/section[1]/div[7]/div/ul/li[4]/a/img[1]")
    THE_RITZ_CARLTON_PAGE_LINK = (By.XPATH, "/html/body/section[1]/div[7]/div/ul/li[5]/a/img[1]")


class ProjectsPageLocators():
    SECTOR_SELECTION_BAR = (By.XPATH, "//*[@id='filtered']/div/div/div/div[1]/div[2]")
    SECTOR_SELECTION_BAR_STATUS_LOCATOR = (By.XPATH, "//*[@id='filtered']/div/div/div/div[1]")
    CLIENT_SELECTION_BAR = (By.XPATH, "//*[@id='filtered']/div/div/div/div[2]/div[2]")
    CLIENT_SELECTION_BAR_STATUS_LOCATOR = (By.XPATH, "//*[@id='filtered']/div/div/div/div[2]")
    RETAIL_SECTOR = (By.XPATH, "//*[@id='filtered']/div/div/div/div[1]/div[3]/div/ul/li[12]")
    WILDSTONE_CLIENT = (By.XPATH, "//*[@id='filtered']/div/div/div/div[2]/div[3]/div/ul/li[68]")
    SCROLL_TO_SELECTION_BAR = (By.CLASS_NAME, 'preced-grid')

class AboutPageLocators():
    COMPANY_ARTICLE_LINK = (By.CLASS_NAME, "tab-title")
    PROCESS_ARTICLE_LINK = (By.CLASS_NAME, "tab-title.process")
    AWARDS_ARTICLE_LINK = (By.CLASS_NAME, "tab-title.awards")
    CPDS_ARTICLE_LINK = (By.CLASS_NAME, "tab-title.cpds")
    COMPANY_ARTICLE_ACTIVE = (By.CLASS_NAME, "tab-title.active")
    PROCESS_ARTICLE_ACTIVE = (By.CLASS_NAME, "tab-title.process.active")
    AWARDS_ARTICLE_ACTIVE = (By.CLASS_NAME, "tab-title.awards.active")
    CPDS_ARTICLE_ACTIVE = (By.CLASS_NAME, "tab-title.cpds.active")
    SCROLL_TO_ARTICLES = (By.XPATH, "//*[@id='panel0']/div[1]/div/h3")
    NAME_CPD_FORM = (By.ID, "input_7_1")
    EMAIL_CPD_FORM = (By.ID, "input_7_2")
    PHONE_NUMBER_CPD_FORM = (By.ID, "input_7_3")
    INTERESTED_IN_TEXT_CPD_FORM = (By.ID, "input_7_12")
    CPD_SUBMIT_BUTTON = (By.ID, "gform_submit_button_7")
    SUCCESS_MESSAGE_OF_SENDED_CPD_FORM = (By.ID, "gform_confirmation_message_7")
    SCROLL_TO_CPD_FORM = (By.CLASS_NAME, "col-right")
    SCROLL_TO_SUBMIT_BUTTON = (By.CLASS_NAME, "owl-carousel")

class BlogPageLocators():
    pass


class ContactPageLocators():
    pass







