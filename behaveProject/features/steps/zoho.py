from behave import given, when, then
from selenium import webdriver

@given(u'Launch browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.zoho.com")


@when(u'open application')
def step_impl(context):
    raise NotImplementedError(u'STEP: When open application')


@then(u'verify login')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then verify login')


@then(u'close browser')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then close browser')
