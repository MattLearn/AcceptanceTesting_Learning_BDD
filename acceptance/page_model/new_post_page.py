from acceptance.locators.new_post_page import NewPostPageLocators
from acceptance.page_model.base_page import BasePage
from selenium.webdriver.common.by import By


class NewPostPage(BasePage):

    @property
    def url(self):
        return super(NewPostPage, self).url + '/post'

    @property
    def form(self):
        return self.browser.find_element(*NewPostPageLocators.NEW_POST_FORM)

    @property
    def post_title(self):
        return self.browser.find_element(*NewPostPageLocators.POST_TITLE)

    @property
    def post_content(self):
        return self.browser.find_element(*NewPostPageLocators.POST_CONTENT)

    @property
    def submit_button(self):
        return self.browser.find_element(NewPostPageLocators.SUBMIT_BUTTON)

    def form_field(self, field_name):
        return self.form.find_element(By.NAME, field_name)

