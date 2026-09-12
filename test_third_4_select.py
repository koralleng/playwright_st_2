from time import sleep

from playwright.sync_api import Page
import re

def test_select(page: Page):
    # page.goto("https://magento.softwaretestingboard.com/men/tops-men.html")
    page.goto("https://the-internet.herokuapp.com/dropdown")
    page.locator('#dropdown').first.select_option('Option 1')
    sleep(3)
    page.locator('#dropdown').first.select_option('Option 2')
    # page.locator('.navbar-toggler-icon').click()

    sleep(3)

