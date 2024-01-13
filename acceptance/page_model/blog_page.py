from acceptance.locators.blog_page import BlogPageLocators
from acceptance.page_model.base_page import BasePage


class BlogPage(BasePage):

    @property
    def url(self):
        return super(BlogPage, self).url + '/blog'

    @property
    def posts(self):
        return self.browser.find_elements(*BlogPageLocators.POST)

    @property
    def posts_section(self):
        return self.browser.find_element(*BlogPageLocators.POSTS_SECTION)

    @property
    def add_posts_link(self):
        return self.browser.find_element(*BlogPageLocators.ADD_POST_LINK)
