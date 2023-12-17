# Overview / Leírás
This is a tool to practice reading syllables taking into account the alphabet learning order of the Meixner-method.

Ez egy - szótagolva olvasást segítő - eszköz, amely figyelembe veszi a Meixner-módszer ábécéjének tanulási sorrendjét.

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
