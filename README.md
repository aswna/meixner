# Overview / Leírás
This tool helps the reading practice of syllables
taking into account the learning order of the alphabet
used by the Meixner-method.

Ez az eszköz a szótagolva olvasását segíti,
figyelembe vevé a Meixner-módszer ábécéjének tanulási sorrendjét.

```
usage: meixner.py [-h] [--number-of-letters NUMBER_OF_LETTERS] [--level LEVEL] [--reverse] [--mix]
                  [--max-cols MAX_COLS] [--max-rows MAX_ROWS]

options:
  -h, --help            show this help message and exit
  --number-of-letters NUMBER_OF_LETTERS
                        number of letters in word (default: 2)
  --level LEVEL         level (default: 0)
  --reverse             vowels first (default: False)
  --mix                 starting letters can be vowels and consonants, too (default: False)
  --max-cols MAX_COLS   max number of columns (default: 0)
  --max-rows MAX_ROWS   max number of rows (default: 0)
```

# Example / Példa
```
$ ./meixner.py --number-of-letters 2 --level 3 --max-cols 3 --max-rows 2
┌────┬────┬────┐
│ ve │ va │ ca │
├────┼────┼────┤
│ lo │ to │ tú │
└────┴────┴────┘

$ ./meixner.py --number-of-letters 3 --level 7 --mix --max-cols 4 --max-rows 3
┌─────┬─────┬─────┬─────┐
│ enő │ oti │ ecí │ jef │
├─────┼─────┼─────┼─────┤
│ ket │ áté │ jűc │ sáp │
├─────┼─────┼─────┼─────┤
│ nef │ hip │ ölö │ őtü │
└─────┴─────┴─────┴─────┘
```
