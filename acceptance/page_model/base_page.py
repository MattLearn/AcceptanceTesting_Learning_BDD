from acceptance.locators.base_page import BasePageLocators


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def url(self):
        return 'http://127.0.0.1:5000'

    @property
    def title(self):
        return self.browser.find_element(*BasePageLocators.TITLE)

    @property
    def navigation(self):
        return self.browser.find_elements(*BasePageLocators.NAV_LINKS)

    @property
    def buttons(self):
        return self.browser.find_elements(*BasePageLocators.BUTTONS)
