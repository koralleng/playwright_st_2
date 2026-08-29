from time import sleep

from playwright.sync_api import Page, BrowserContext

'''
    pytest --headed -v -s test_third_2_tabs.py::test_tabs
'''

'''Работа с вкладками'''
def test_tabs(page: Page, context: BrowserContext):
    page.goto("https://nomads.com/")
    sleep(2)
    # page.get_by_alt_text('Get insured').click()

    # page.get_by_role('button', name='Get covered now').click()
    # page.get_by_test_id("ni-landing-sign-me-up-button").click()

    with context.expect_page() as new_tab_event:
        page.get_by_alt_text('Get insured').click()
        new_tab = new_tab_event.value
    # new_tab.get_by_role('link', name='Get covered now').click()
    sleep(4)
    # new_tab.get_by_role('button', name='Get covered now').click()
    new_tab.get_by_test_id("ni-landing-sign-me-up-button").click()


    sleep(5)