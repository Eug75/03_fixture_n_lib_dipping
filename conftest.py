import pytest
from selene import browser, be, have

@pytest.fixture(scope="module")
def browser_window_size():
    browser.config.window_width = 1200
    browser.config.window_height = 900