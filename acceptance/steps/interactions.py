from behave import *

from acceptance.page_model.base_page import BasePage
from acceptance.page_model.new_post_page import NewPostPage

use_step_matcher('re')


@when('I click on the "(.*)" link')
def step_impl(context, link_text):
    page = BasePage(context.browser)
    links = page.navigation

    found_link = [link for link in links if link.text == link_text]
    if len(found_link) > 0:
        found_link[0].click()
    else:
        raise RuntimeError()

# This implementation assumes a fixed field
# @when('I create a post named "(.*)"')
# def step_impl(context, blog_title):
#     post = NewPostPage(context.browser)
#     post.post_title.send_keys(blog_title)


@when('I enter "(.*)" in the "(.*)" field')
def step_impl(context, field_input, field_name):
    page = NewPostPage(context.browser)
    page.form_field(field_name).send_keys(field_input)


@when('I press the "(.*)" button')
def step_impl(context, button_name):
    page = NewPostPage(context.browser)
    buttons = page.buttons
    button_list = [button for button in buttons if button.text == button_name]
    if len(button_list) > 0:
        button_list[0].click()
    else:
        raise RuntimeError()

