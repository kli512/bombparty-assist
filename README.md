# BombParty Assist

This is a python program (using selenium) to "assist" players in BombParty at jklm.fun

Uses selenium to monitor the webpage for changes in the "syllable", then generates a list of all words that contain that syllable (according to the dictionary I believe is used by bombparty). It then injects the words below the chat window in bombparty cleanly, additionally allowing sorting of the generated solutions.   

## Running with precompiled binaries

Find precompiled binaries at https://github.com/kli512/bombparty-assist/releases

Compilation is performed using `pyinstaller`

## Installation

Get `python3` and install the `selenium` package however you want.

### Windows Example Installation

1. Install `Python 3.7` from the Microsoft Store
2. Open a command prompt (or powershell) window and run `python3.7 -m pip install selenium`

* To compile to binary, install `pyinstaller` and run `make.bat` (for Windows).


## Usage

1. Either run the precompiled executable or open a shell, cd into `bombparty`, and run `python3.7 jklm_bombparty.py`
2. You can then choose to join an existing room or host one
  * If you want to join an existing room simply navigate to a bombparty room (make sure you enter a bombparty room - **not room selector or popsauce**)
  * If you choose to host a new room, it will simply launch chrome and you can create a bombparty room from there. Again, make sure to make a bombparty room.
4. Once you are in the game room, you can start playing as usual.
5. If you open the chat on the right side of the screen (using the arrow button at the top right), you will see that if there is a bomb with a syllable in the middle (i.e. you are in game), a word bank of solutions will appear under the chat window.



## Bombparty dictionaries

Currently, only english and french are supported.

### English dictionary

English dictionary information source: https://www.reddit.com/r/BombParty/comments/3lehxq/a_nearly_exhaustive_subset_of_the_bombparty/

dict is created by running `cat enable1.txt sowpods.txt word_list_moby_crossword.flat.txt | sort | uniq >dict.txt`

http://norvig.com/ngrams/sowpods.txt
http://norvig.com/ngrams/enable1.txt
http://pastebin.com/raw/UegdKLq8

### French dictionary

dictionary adapted from https://raw.githubusercontent.com/necrosis159/bombparty/master/fr-FR.json

Thanks to @trololol42 for pointing out this dictionary
