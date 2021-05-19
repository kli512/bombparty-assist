import random
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import search


def run_cheat(syllable, driver, n):
    words = search.words_containing(syllable)

    if n >= 0:
        random.shuffle(words)
        words = words[:n]

    words.sort(key=len)

    js = f'words = {str(words)};\n'
    with open('insert_words.js') as f:
        js += f.read()

    driver.switch_to.default_content()
    driver.execute_script(js)


# maybe should change it to use the normal "re-locate on call" system just incase the element becomes stale
class TextChange:
    def __init__(self, element):
        self.element = element
        self.old_text = element.text

    def __call__(self, driver):
        return self.element if self.element.text != self.old_text else False


class URLRegexMatch:
    def __init__(self, url_regex):
        self.url_regex = url_regex

    def __call__(self, driver):
        return re.match(self.url_regex, driver.current_url) is not None


def main():
    n = int(input('Max number of words to find (-1 for all)? '))

    if input('make new room [y/n]? ').lower()[0] == 'y':
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
        driver.get(f'https://jklm.fun/')

        WebDriverWait(driver, 9999).until(
            URLRegexMatch(r'.*?jklm.*?/.+')
        )
    else:
        page = input('page url/room code? ')
        room_code = page[page.rfind('/') + 1:] if '/' in page else page

        driver = webdriver.Chrome(executable_path='chromedriver.exe')
        driver.get(f'https://jklm.fun/{room_code}')

    iframe = WebDriverWait(driver, 9999).until(
        EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
    )
    assert len(driver.find_elements_by_tag_name('iframe')) == 1

    driver.switch_to.frame(iframe)

    syllable_element = WebDriverWait(driver, 9999).until(
        EC.presence_of_element_located((By.CLASS_NAME, 'syllable'))
    )

    while True:
        driver.switch_to.default_content()

        iframe = WebDriverWait(driver, 9999).until(
            EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
        )
        assert len(driver.find_elements_by_tag_name('iframe')) == 1

        driver.switch_to.frame(iframe)

        syllable_element = WebDriverWait(driver, 9999).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'syllable'))
        )
        assert len(driver.find_elements_by_class_name('syllable')) == 1

        syllable_element = WebDriverWait(driver, 9999).until(
            TextChange(syllable_element)
        )

        run_cheat(syllable_element.text.lower(), driver, n)


if __name__ == '__main__':
    main()
