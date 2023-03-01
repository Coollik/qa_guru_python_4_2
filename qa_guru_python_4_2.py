import pytest
from selene.support.shared import browser
from selene import be, have

def test_selene(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_failed(browser_open):
    browser.element('[name="q"]').should(be.blank).type('ratamahata').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
