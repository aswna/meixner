#!/usr/bin/env python3

"""
This tool helps the reading practice of syllables.

It takes into account the learning order of the alphabet used by the
Meixner-method.

It supports lowercase letters only.
"""

import argparse
import random
import sys

USE_TERMTABLE = True
try:
    import termtables
except ModuleNotFoundError:
    USE_TERMTABLE = False
    print('Try to install termtables for prettier output!', file=sys.stderr)

MEIXNER_VOWELS = (
    ('a', 'i', 'ó'),
    ('e', 'ú'),
    ('o', 'u'),
    ('í', 'á'),
    ('ő', 'ö'),
    ('é'),
    ('ű', 'ü'),
)

MEIXNER_CONSONANTS = (
    ('m', 't', 's'),
    ('v', 'l'),
    ('p', 'c'),
    ('k', 'f'),
    ('h', 'z'),
    ('d', 'j',),
    ('n', 'sz'),
    ('g', 'r',),
    ('b', 'gy',),
    ('cs', 'ny'),
    ('zs', 'ty'),
    ('ly', 'dz'),
    ('x', 'dzs'),
    ('y', 'w'),
    ('q'),
)


def main():
    """Start here."""
    args = parse_args()

    (consonants_pool, vowels_pool) = get_letter_pools(args)

    (max_row, max_col) = get_size(args, consonants_pool, vowels_pool)

    words = generate_words(args,
                           consonants_pool,
                           vowels_pool,
                           max_row * max_col)
    word_matrix = [
        words[i * max_col:(i + 1) * max_col]
        for i in range((len(words) + max_col - 1) // max_col)
    ]

    if USE_TERMTABLE:
        termtables.print(word_matrix)
    else:
        for row in word_matrix:
            print('\t'.join(map(str, row)))


def parse_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--number-of-letters",
                        type=int,
                        default=2,
                        help="number of letters in word")
    parser.add_argument("--level", type=int, default=0, help="level")
    parser.add_argument("--reverse", action='store_true', help="vowels first")
    parser.add_argument("--mix", action='store_true',
                        help="starting letters can be vowels and consonants, "
                             "too")
    parser.add_argument("--max-cols",
                        type=int,
                        default=0,
                        help="max number of columns")
    parser.add_argument("--max-rows",
                        type=int,
                        default=0,
                        help="max number of rows")
    args = parser.parse_args()

    if args.number_of_letters < 2 or args.number_of_letters > 3:
        print('Invalid number of letters: {args.number_of_letters}')
        sys.exit(2)

    if args.reverse and args.mix:
        print('--reverse and --mix are mutually exclusive options!')
        sys.exit(2)

    return args


def get_letter_pools(args):
    """Get already learned consonants and vowels."""
    consonants_pool = set()
    vowels_pool = set()
    if args.level <= 0:
        consonants_pool.update(
            c for level in MEIXNER_CONSONANTS for c in level)
        vowels_pool.update(v for level in MEIXNER_VOWELS for v in level)
    elif (args.level <= len(MEIXNER_CONSONANTS) or
          args.level <= len(MEIXNER_VOWELS)):
        for i in range(args.level):
            min_c = min(i, len(MEIXNER_CONSONANTS) - 1)
            consonants_pool.update(MEIXNER_CONSONANTS[min_c])
            min_v = min(i, len(MEIXNER_VOWELS) - 1)
            vowels_pool.update(MEIXNER_VOWELS[min_v])
    else:
        sys.exit('Not implemented, yet!')

    consonants_pool = list(consonants_pool)
    vowels_pool = list(vowels_pool)

    return (consonants_pool, vowels_pool)


def get_size(args, consonants_pool, vowels_pool):
    """Get number of strings to generate."""
    max_row = (min(len(consonants_pool) - 1, 5) if args.level <= 0
               else min(args.level + 1, 5))

    if args.max_rows > 0:
        max_row = min(max_row, args.max_rows)

    max_col = (min(len(vowels_pool) - 1, 5) if args.level <= 0
               else min(args.level + 2, 5))

    if args.max_cols > 0:
        max_col = min(max_col, args.max_cols)

    return (max_row, max_col)


def generate_words(args, consonants_pool, vowels_pool, size):
    """Generate words according to configuration."""
    words = []
    words_already_generated = set()

    i = 0
    while i < size:
        if args.mix:
            word = generate_mixed_word(args, consonants_pool, vowels_pool)
        elif args.reverse:
            word = generate_reversed_word(args, consonants_pool, vowels_pool)
        else:
            word = generate_word(args, consonants_pool, vowels_pool)

        if word in words_already_generated:
            continue

        words_already_generated.add(word)
        words.append(word)
        i += 1

    return words


def generate_mixed_word(args, consonants_pool, vowels_pool):
    """Generate word according to mixed rule."""
    consonant1 = random.choice(consonants_pool)
    vowel1 = random.choice(vowels_pool)
    if random.choice((True, False)):
        if args.number_of_letters == 2:
            word = f'{vowel1}{consonant1}'
        else:
            vowel2 = random.choice(vowels_pool)
            word = f'{vowel1}{consonant1}{vowel2}'
    else:
        if args.number_of_letters == 2:
            word = f'{consonant1}{vowel1}'
        else:
            consonant2 = random.choice(consonants_pool)
            word = f'{consonant1}{vowel1}{consonant2}'

    return word


def generate_reversed_word(args, consonants_pool, vowels_pool):
    """Generate word according to reverse rule."""
    consonant1 = random.choice(consonants_pool)
    vowel1 = random.choice(vowels_pool)
    if args.number_of_letters == 2:
        word = f'{vowel1}{consonant1}'
    else:
        vowel2 = random.choice(vowels_pool)
        word = f'{vowel1}{consonant1}{vowel2}'

    return word


def generate_word(args, consonants_pool, vowels_pool):
    """Generate word according to default rule."""
    consonant1 = random.choice(consonants_pool)
    vowel1 = random.choice(vowels_pool)
    if args.number_of_letters == 2:
        word = f'{consonant1}{vowel1}'
    else:
        consonant2 = random.choice(consonants_pool)
        word = f'{consonant1}{vowel1}{consonant2}'

    return word


if __name__ == '__main__':
    main()
