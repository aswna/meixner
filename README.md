# Overview / Leírás
This tool helps the reading practice of syllables taking into account the learning order of the alphabet used by the Meixner-method.

Ez az eszköz a szótagolva olvasását segíti, figyelembe vevé a Meixner-módszer ábécéjének tanulási sorrendjét.

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
