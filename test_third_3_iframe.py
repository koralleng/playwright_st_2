from time import sleep

from playwright.sync_api import Page, Route, Dialog, BrowserContext
import re

def test_iframe(page: Page, context: BrowserContext):
    page.goto(
        "https://www.qa-practice.com/elements/iframe/iframe_page",
        wait_until="networkidle",  # Ждем тишины в сети 500мс вместо полного load
        timeout=60000  # Даем 60 секунд вместо 30
    )
    page.frame_locator('iframe').locator('.navbar-toggler-icon').click()
    # page.locator('.navbar-toggler-icon').click()

    sleep(5)


'''
pytest --headed -v -s test_third_3_iframe.py::test_alert
'''