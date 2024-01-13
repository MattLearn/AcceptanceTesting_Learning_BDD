from selenium.webdriver.common.by import By


class BlogPageLocators:
    TITLE = By.TAG_NAME, 'h1'
    HOME_LINK = By.ID, 'home-link'
    POSTS_SECTION = By.ID, 'posts'
    POST = By.CLASS_NAME, 'post'
    POSTS_LINK = By.ID, 'post-link'
    ADD_POST_LINK = By.ID, 'add-post-link'
