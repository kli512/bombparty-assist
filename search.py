with open('dict.txt') as f:
    s = f.read()
word_set = set(s.split('\n'))


def generate_substrings(word):
    l = len(word)
    return set(word[i:j+1] for i in range(l) for j in range(i, l))


word_substrings = {word: generate_substrings(word) for word in word_set}


def words_containing(substring, n=-1):
    words = []
    for word, substrings in word_substrings.items():
        if substring in substrings:
            words.append(word)
            if n >= 0 and len(words) >= n:
                return words

    return words


def main():
    n = int(input('Max number of words to find (-1 for all)? '))

    substring = input('Substring? ')
    words = words_containing(substring, n)

    print('\nMatched words:')
    for word in sorted(words, key=len, reverse=True):
        print(word)


if __name__ == '__main__':
    main()
