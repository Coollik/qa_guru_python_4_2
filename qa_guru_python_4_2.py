import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture
def browser_open():
    browser.open('https://google.com')

@pytest.fixture()
def type_value():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()

def test_selene(browser_open, type_value):
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))