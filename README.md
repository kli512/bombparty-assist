# BombParty Assist

This is a python program (using selenium) to "assist" players in BombParty at jklm.fun

Uses selenium to monitor the webpage for changes in the "syllable", then generates a list of all words that contain that syllable (according to the dictionary I believe is used by bombparty). It then injects the words below the chat window in bombparty cleanly, additionally allowing sorting of the generated solutions.

## bombparty dictionary

dictionary information source: https://www.reddit.com/r/BombParty/comments/3lehxq/a_nearly_exhaustive_subset_of_the_bombparty/

dict is created by running `cat enable1.txt sowpods.txt word_list_moby_crossword.flat.txt | sort | uniq >dict.txt`

http://norvig.com/ngrams/sowpods.txt
http://norvig.com/ngrams/enable1.txt
http://pastebin.com/raw/UegdKLq8
