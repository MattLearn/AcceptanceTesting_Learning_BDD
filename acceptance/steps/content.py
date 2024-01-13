from behave import *

from acceptance.page_model.base_page import BasePage
from acceptance.page_model.blog_page import BlogPage

use_step_matcher('re')


@then('There is a title shown on the page')
def step_impl(context):
    page = BasePage(context.browser)
    assert page.title.is_displayed()


@step('The title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.browser)
    assert page.title.text == content


@then('I can see there is a posts section on the page')
def step_impl(context):
    page = BlogPage(context.browser)

    assert page.posts_section.is_displayed()


@then('I can see there is a post with the title "(.*)" in the posts section')
def step_impl(context, post_title):
    page = BlogPage(context.browser)
    print(page.posts)
    post_list = [post for post in page.posts if post.text == post_title]
    print(post_title, post_list)
    assert (len(post_list) > 0)

    assert all([post.is_displayed() for post in post_list])

