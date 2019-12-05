"""
Coding Challenge
Page Under Test: https://the-internet.herokuapp.com/dynamic_content
Test 1 - Assert dynamic text on page contains a word at least 10 chars in length.
Test 2 - Assert Punisher avatar does not appear on page.
Utilized Pytest and Selenium frameworks with Chromedriver. Please confirm Chromedriver path is appropriate before using.
"""

import pytest

from selenium import webdriver


@pytest.fixture
def browser():
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_paragraph_contains_word_with_10_or_more_chars(browser):
    # Make first two paragraphs static, leave third dynamic
    browser.get("https://the-internet.herokuapp.com/dynamic_content?with_content=static")

    third_paragraph = '//*[@id="content"]/div[3]/div[2]'
    paragraph_words = browser.find_element_by_xpath(third_paragraph).text
    # Create list
    words_list = paragraph_words.split()
    for word in words_list:
        print(f'{word} is {len(word)} characters long.')
        if len(word) > 9:
            over_nine_chars = word
            print(over_nine_chars)
            break

    assert over_nine_chars


def test_punisher_avatar_not_present(browser):
    # Go to full dynamic site - do not append snippet
    browser.get("https://the-internet.herokuapp.com/dynamic_content")

    punisher_xpath = "//img[@src='/img/avatars/Original-Facebook-Geek-Profile-Avatar-3.jpg']"
    punisher_is_present = len(browser.find_elements_by_xpath(punisher_xpath)) > 0
    # Assert may fail if Punisher avatar is present.
    assert punisher_is_present is False
