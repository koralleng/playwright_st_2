from time import sleep

from playwright.sync_api import Page
import re

def test_select(page: Page):
    page.goto("https://magento.softwaretestingboard.com/men/tops-men.html")
    page.locator('#sorter').first.select_option('Price')
    sleep(3)
    page.locator('#sorter').first.select_option('Product Name')
    # page.locator('.navbar-toggler-icon').click()

    sleep(3)

