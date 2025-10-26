from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I open the product page')
def step_impl(context):
    context.driver = webdriver.Chrome()  # or Firefox
    context.driver.get("http://localhost:8000/products")

@then('I should see the message "{message}"')
def step_impl(context, message):
    body_text = context.driver.find_element(By.TAG_NAME, "body").text
    assert message in body_text

@then('I should not see the text "{text}"')
def step_impl(context, text):
    body_text = context.driver.find_element(By.TAG_NAME, "body").text
    assert text not in body_text

@then('I should see the text "{text}"')
def step_impl(context, text):
    body_text = context.driver.find_element(By.TAG_NAME, "body").text
    assert text in body_text

@when('I click the "{button_name}" button')
def step_impl(context, button_name):
    button = context.driver.find_element(By.XPATH, f"//button[text()='{button_name}']")
    button.click()
