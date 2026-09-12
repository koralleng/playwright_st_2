from time import sleep
from dotenv import load_dotenv

from playwright.sync_api import Page, Route
import re
import os

load_dotenv()

user = os.getenv("CONFIG_USER")
password = os.getenv("CONFIG_PASSWORD")

def test_request(page: Page):
    def change_request(route: Route ):
        data = route.request.post_data
        print(data)
        if data:
            data = data.replace("ER_User", user)
            print(data)
        route.continue_(post_data=data)

    page.route(re.compile('profile/authenticate'), change_request)
    page.goto("https://gymlog.ru/profile/login/")
    # sleep(1)
    page.locator("#email").fill("ER_User")
    page.locator("#password").fill(password)
    # sleep(5)
    page.get_by_role('button', name='Войти').click()
    sleep(5)
    # pytest --headed -v -s test_second.py::test_request


def test_response(page: Page):
    def change_response(route: Route):
        print()
        print('зашли в метод')
        response = route.fetch()
        data = response.text()

        data = data.replace(user, 'Alexey')
        print(f'data = {data}')
        route.fulfill(response=response, body=data)

    page.route(re.compile(r'.*/profile/412.*'), change_response)
    page.goto("https://gymlog.ru/profile/login/")
    page.locator("#email").fill(user)
    page.locator("#password").fill(password)
    page.get_by_role('button', name='Войти').click()
    page.get_by_role('link', name='Мой профиль').click()
    sleep(5)

'''
pytest --headed -v -s test_second.py::test_response
'''