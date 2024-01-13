from selenium.webdriver.common.by import By


class NewPostPageLocators:
    TITLE = By.TAG_NAME, 'h1'
    NEW_POST_FORM = By.ID, 'post-form'
    RETURN_TO_BLOG = By.ID, 'blog-link'
    POST_TITLE = By.NAME, 'title'
    POST_CONTENT = By.NAME, 'content'
    SUBMIT_BUTTON = By.ID, 'create-post'
