# Overview / Leírás
This tool helps the reading practice of syllables taking into account the learning order of the alphabet used by the Meixner-method.

Ez az eszköz a szótagolva olvasását segíti, figyelembe vevé a Meixner-módszer ábécéjének tanulási sorrendjét.

```
$ ./meixner.py --help
usage: meixner.py [-h] [--number-of-letters NUMBER_OF_LETTERS] [--level LEVEL] [--reverse] [--mixed]
                  [--max-cols MAX_COLS] [--max-rows MAX_ROWS]

options:
  -h, --help            show this help message and exit
  --number-of-letters NUMBER_OF_LETTERS
                        number of letters in word
  --level LEVEL         level
  --reverse             reverse
  --mixed               mixed
  --max-cols MAX_COLS   max number of columns
  --max-rows MAX_ROWS   max number of rows
```

# Example / Példa
```
$ ./meixner.py --number-of-letters 2 --level 3 --max-cols 3 --max-rows 2
┌────┬────┬────┐
│ ve │ va │ ca │
├────┼────┼────┤
│ lo │ to │ tú │
└────┴────┴────┘

$ ./meixner.py --number-of-letters 3 --level 7 --mixed --max-cols 4 --max-rows 3
┌─────┬─────┬─────┬─────┐
│ enő │ oti │ ecí │ jef │
├─────┼─────┼─────┼─────┤
│ ket │ áté │ jűc │ sáp │
├─────┼─────┼─────┼─────┤
│ nef │ hip │ ölö │ őtü │
└─────┴─────┴─────┴─────┘
```
