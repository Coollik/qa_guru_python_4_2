import pytest
from selene.support.shared import browser
from selene import be, have


@pytest.fixture(scope="function") # Со скоупом "function" фикстура будет заново запускаться при каждом вызове функции "clear_field"
def clear_field():
    yield
    browser.element('[name="q"]').clear()

@pytest.fixture(scope="session")  # Со скоупом "session" фикстура запустится один раз на всю сессию при вызове функции "browser_open"
def browser_open():
    browser.config.window_height = 640
    browser.config.window_width = 480
    browser.open('https://google.com')
