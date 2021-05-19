import os
import sys
import glob
import random
from progressbar import progressbar

def resource_path(relative_path: str) -> str:
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.dirname(__file__)
    return os.path.join(base_path, relative_path)

def generate_substrings(word):
    l = len(word)
    return set(word[i:j+1] for i in range(l) for j in range(i, l))

dictionary_paths = glob.glob(resource_path('dictionaries/*.txt'))

word_substrings = {}

for dictionary_path in dictionary_paths:
    language = os.path.basename(dictionary_path)[:-4]
    print(f'Loading {language} dictionary...')
    with open(dictionary_path) as f:
        s = f.read()
    words = s.split('\n')
    random.shuffle(words)

    # word_substrings[language] = {word: generate_substrings(word) for word in words}

    word_substrings[language] = {}
    for word in progressbar(words):
        word_substrings[language][word] = generate_substrings(word)


def words_containing(language, substring, n=-1):
    words = []
    for word, substrings in word_substrings[language].items():
        if substring in substrings:
            words.append(word)
            if n >= 0 and len(words) >= n:
                return words

    return words


def main():
    n = int(input('Max number of words to find (-1 for all)? '))
    language = input('language (en/fr)? ')

    substring = input('Substring? ')
    words = words_containing(language, substring, n)

    print('\nMatched words:')
    for word in sorted(words, key=len, reverse=True):
        print(word)


if __name__ == '__main__':
    main()
