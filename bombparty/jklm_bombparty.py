import glob
import os
import re
import sys
import time

from selenium import webdriver
from selenium.common.exceptions import SessionNotCreatedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import search


LANGUAGE_CODE = {
    'English': 'en',
    'French': 'fr',
    'French with proper nouns': 'fr'
}

def resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)


def run_cheat(language, syllable, driver, n):
    words = search.words_containing(language, syllable, n)

    js = f'var smartWords = {str(words)};\n'
    with open(resource_path('insert_words.js'), encoding='utf-8') as f:
        js += f.read()

    driver.switch_to.default_content()
    driver.execute_script(js)


# maybe should change it to use the normal "re-locate on call" system just incase the element becomes stale
class TextChange:
    def __init__(self, element):
        self.element = element
        self.old_text = element.text

    def __call__(self, _):
        return self.element if self.element.text != self.old_text else False


class URLRegexMatch:
    def __init__(self, url_regex):
        self.url_regex = url_regex

    def __call__(self, driver):
        return re.match(self.url_regex, driver.current_url) is not None


def main():
    try:
        driver_paths = glob.glob(resource_path('drivers/*.exe'))
        for driver_path in driver_paths:
            try:
                driver = webdriver.Chrome(executable_path=driver_path)
            except SessionNotCreatedException:
                continue
            break
        else:
            raise Exception('No chrome version 88/89/90/91 found.')

        driver.get(f'https://jklm.fun/')

        WebDriverWait(driver, 99999).until(
            URLRegexMatch(r'.*?jklm\.fun.*?/.+')
        )

        while True:
            driver.switch_to.default_content()

            iframe = WebDriverWait(driver, 99999).until(
                EC.presence_of_element_located((By.TAG_NAME, 'iframe'))
            )
            assert len(driver.find_elements_by_tag_name('iframe')) == 1

            driver.switch_to.frame(iframe)

            syllable_element = WebDriverWait(driver, 99999).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'syllable'))
            )
            assert len(driver.find_elements_by_class_name('syllable')) == 1

            syllable_element = WebDriverWait(driver, 99999).until(
                TextChange(syllable_element)
            )

            dictionary_element = WebDriverWait(driver, 99999).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'dictionary'))
            )
            assert len(driver.find_elements_by_class_name('dictionary')) == 1
            language = dictionary_element.get_attribute('innerText')

            try:
                lang_code = LANGUAGE_CODE[language]
            except KeyError:
                raise KeyError(f'Language {language} not supported')

            run_cheat(lang_code, syllable_element.text.lower(), driver, 500)

    except Exception as e:
        print(e)
        time.sleep(5)

    exit(0)


if __name__ == '__main__':
    main()
