from selene import browser, be, have
import pytest

@pytest.fixture
def browser_window_size():
    browser.config.window_width = 1200
    browser.config.window_height = 900

def test_search_task01(browser_window_size):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('qa.guru').press_enter()
    assert browser.element('html').should(have.text('Об этой странице'))

    # browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
