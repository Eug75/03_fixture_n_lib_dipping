import pytest
from selene import browser, be, have

def test_search_task01(browser_window_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
    assert browser.element('html').should(have.text('Об этой странице'))

    # browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
