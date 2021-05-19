pyi-makespec jklm_bombparty.py --onefile --add-binary "drivers\*;drivers" --add-data "dictionaries\*;dictionaries" --add-data "insert_words.js;."
pyinstaller --clean jklm_bombparty.spec

move dist\jklm_bombparty.exe ..\executables
del jklm_bombparty.spec
rmdir /s /q build
rmdir dist
