from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


from .locators import BasePageLocators, AboutPageLocators



class BasePage():
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    def is_not_element_present(self, how, what, timeout=15):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def scroll_to_the_element(self, how, what):
        self.element = self.browser.find_element(how, what)
        self.actions = ActionChains(self.browser)
        self.actions.move_to_element(self.element).perform()



    def go_to_main_page(self):
        link = self.browser.find_element(*BasePageLocators.MAIN_PAGE_LINK).click()
        assert self.browser.title == "Nulty | Lighting Design Consultants", " Not a Projects page or title has been changed"

    def go_to_projects_page(self):
        link = self.browser.find_element(*BasePageLocators.PROJECTS_PAGE_LINK).click()
        assert self.browser.title == "Projects | Nulty | Lighting Design Consultants", " Not a Projects page or title has been changed"

    def go_to_clients_page(self):
        link = self.browser.find_element(*BasePageLocators.CLIENTS_PAGE_LINK).click()
        assert self.browser.title == "Clients | Nulty | Lighting Design Consultants", " Not a Clients page or title has been changed"

    def go_to_about_page(self):
        link = self.browser.find_element(*BasePageLocators.ABOUT_PAGE_LINK).click()
        assert self.browser.title == "About | Nulty | Lighting Design Consultants", " Not a About page or title has been changed"

    def go_to_team_page(self):
        link = self.browser.find_element(*BasePageLocators.TEAM_PAGE_LINK).click()
        assert self.browser.title == "Team | Nulty | Lighting Design Consultants", " Not a Team page or title has been changed"

    def go_to_blog_page(self):
        link = self.browser.find_element(*BasePageLocators.BLOG_PAGE_LINK).click()
        assert self.browser.title == "Blog | Nulty | Lighting Design Consultants", " Not a Blog page or title has been changed"

    def go_to_contact_page(self):
        link = self.browser.find_element(*BasePageLocators.CONTACT_PAGE_LINK).click()
        assert self.browser.title == "Contact | Nulty | Lighting Design Consultants", " Not a Contact page or title has been changed"


    def should_be_brochure_request_form_from_header(self):
        self.browser.find_element(*BasePageLocators.BROCHURE_FORM_REQUEST_HEADER).click()
        assert self.is_element_present(*BasePageLocators.OPENED_BROCHURE_FORM), "Brochure form didn't appear"

    def go_to_cpd_article(self):
        self.browser.find_element(*BasePageLocators.CPD_LINK).click()
        assert self.is_element_present(*AboutPageLocators.CPDS_ARTICLE_ACTIVE), "Page has no article about cpd"

    def should_be_newsletter_following_form_from_header(self):
        self.browser.find_element(*BasePageLocators.NEWSLETTER_FORM_REQUEST).click()
        assert self.is_element_present(*BasePageLocators.OPENED_NEWSLETTER_FORM), "Newsletter following form didn't appear"

    def success_of_following_newsletters_mailing(self, email):
        self.browser.find_element(*BasePageLocators.EMAIL_FOR_NEWSLETTER).send_keys(email)
        self.browser.find_element(*BasePageLocators.NEWSLETTER_SUBMIT_BUTTON).click()
        assert self.is_element_present(*BasePageLocators.SUCCESS_MESSAGE_OF_FOLLOWING_NEWSLETTERS), "Success message of Following of newsletters not appear"

    def should_be_brochure_form_from_footer(self):
        self.scroll_to_the_element(*BasePageLocators.FOOTER)
        self.browser.find_element(*BasePageLocators.BROCHURE_FORM_REQUEST_BUTTON_FOOTER).click()
        assert self.is_element_present(*BasePageLocators.OPENED_BROCHURE_FORM), "Brochure form didn't appear"

    def success_of_requesting_brochure_footer(self, name, email, message):
        self.browser.find_element(*BasePageLocators.BROCHURE_FORM_REQUEST_BUTTON_FOOTER).click()
        self.browser.find_element(*BasePageLocators.NAME_BROCHURE_FORM).send_keys(name)
        self.browser.find_element(*BasePageLocators.EMAIL_BROCHURE_FORM).send_keys(email)
        self.browser.find_element(*BasePageLocators.MESSAGE_BROCHURE_FORM).send_keys(message)
        self.browser.find_element(*BasePageLocators.BROCHURE_SUBMIT_BUTTON).click()
        assert self.is_element_present(*BasePageLocators.SUCCESS_MESSAGE_OF_REQUESTING_BROCHURE)

    def success_of_requesting_brochure_header(self, name, email, message):
        self.browser.find_element(*BasePageLocators.BROCHURE_FORM_REQUEST_HEADER).click()
        self.browser.find_element(*BasePageLocators.NAME_BROCHURE_FORM).send_keys(name)
        self.browser.find_element(*BasePageLocators.EMAIL_BROCHURE_FORM).send_keys(email)
        self.browser.find_element(*BasePageLocators.MESSAGE_BROCHURE_FORM).send_keys(message)
        self.browser.find_element(*BasePageLocators.BROCHURE_SUBMIT_BUTTON).click()
        assert self.is_element_present(*BasePageLocators.SUCCESS_MESSAGE_OF_REQUESTING_BROCHURE)

