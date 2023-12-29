# Overview / Leírás
This tool helps the reading practice of syllables
taking into account the learning order of the alphabet
used by the Meixner-method.

Ez az eszköz -- a Meixner-módszer ábécéjének tanulási sorrendjét
figyelembe véve -- segíti a szótagolva olvasást.

```
$ ./meixner.py --help
usage: meixner.py [-h] [--number-of-letters NUMBER_OF_LETTERS] [--level LEVEL] [--reverse] [--fix]
                  [--mix] [--max-cols MAX_COLS] [--max-rows MAX_ROWS]

options:
  -h, --help            show this help message and exit
  --number-of-letters NUMBER_OF_LETTERS
                        number of letters in word (default: 2)
  --level LEVEL         level (default: 0)
  --reverse, --reversed
                        first letters will be vowels (default: False)
  --fix, --fixed        print an ordered table (default: False)
  --mix, --mixed        first letters can be vowels, too (default: False)
  --max-cols MAX_COLS   max number of columns (default: 0)
  --max-rows MAX_ROWS   max number of rows (default: 0)
```

# Example / Példa
```
$ ./meixner.py --level 2 --fix --max-cols 4 --max-rows 3
┌────┬────┬────┬────┐
│ ló │ tó │ mó │ só │
├────┼────┼────┼────┤
│ li │ ti │ mi │ si │
├────┼────┼────┼────┤
│ le │ te │ me │ se │
└────┴────┴────┴────┘

$ ./meixner.py --number-of-letters 3 --level 2 --fix --reverse --max-cols 4 --max-rows 3
┌─────┬─────┬─────┬─────┐
│ úmi │ emi │ ami │ ómi │
├─────┼─────┼─────┼─────┤
│ úti │ eti │ ati │ óti │
├─────┼─────┼─────┼─────┤
│ úli │ eli │ ali │ óli │
└─────┴─────┴─────┴─────┘

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
