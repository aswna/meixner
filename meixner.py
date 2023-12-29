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

    (max_rows, max_cols) = get_size(args, consonants_pool, vowels_pool)

    if args.fix:
        words = generate_fixed_words(args,
                                     consonants_pool,
                                     vowels_pool,
                                     max_rows,
                                     max_cols)
    else:
        words = generate_words(args,
                               consonants_pool,
                               vowels_pool,
                               max_rows * max_cols)
    word_matrix = [
        words[i * max_cols:(i + 1) * max_cols]
        for i in range((len(words) + max_cols - 1) // max_cols)
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
    parser.add_argument('--number-of-letters',
                        type=int,
                        default=2,
                        help='number of letters in word')
    parser.add_argument('--level',
                        type=int,
                        default=0,
                        help='level')
    parser.add_argument('--reverse', '--reversed',
                        action='store_true',
                        help='first letters will be vowels')
    parser.add_argument('--fix', '--fixed',
                        action='store_true',
                        help='print an ordered table')
    parser.add_argument('--mix', '--mixed',
                        action='store_true',
                        help='first letters can be vowels, too')
    parser.add_argument('--max-cols',
                        type=int,
                        default=0,
                        help='max number of columns')
    parser.add_argument('--max-rows',
                        type=int,
                        default=0,
                        help='max number of rows')
    args = parser.parse_args()

    if args.number_of_letters < 2 or args.number_of_letters > 3:
        sys.exit('Invalid number of letters: {args.number_of_letters}')

    if args.mix and (args.reverse or args.fix):
        sys.exit('--mix and --fix/--reverse are mutually exclusive options!')

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

    random.shuffle(consonants_pool)
    random.shuffle(vowels_pool)

    return (consonants_pool, vowels_pool)


def get_size(args, consonants_pool, vowels_pool):
    """Get number of strings to generate."""
    max_rows = min(len(consonants_pool), 7)
    if args.max_rows > 0:
        max_rows = min(max_rows, args.max_rows)

    max_cols = min(len(vowels_pool), 5)
    if args.max_cols > 0:
        max_cols = min(max_cols, args.max_cols)

    return (max_rows, max_cols)


def generate_fixed_words(args,
                         consonants_pool,
                         vowels_pool,
                         max_rows,
                         max_cols):
    """Generate words according to fixed configuration."""
    words = []
    consonants_pool2 = list(consonants_pool)
    random.shuffle(consonants_pool2)
    vowels_pool2 = list(vowels_pool)
    random.shuffle(vowels_pool2)
    for i in range(min(len(consonants_pool), max_rows)):
        for j in range(min(len(vowels_pool), max_cols)):
            if args.number_of_letters == 2:
                if args.reverse:
                    words.append(f'{vowels_pool[j]}{consonants_pool[i]}')
                else:
                    words.append(f'{consonants_pool[j]}{vowels_pool[i]}')
            else:
                if args.reverse:
                    words.append(f'{vowels_pool[j]}{consonants_pool[i]}'
                                 f'{vowels_pool2[0]}')
                else:
                    words.append(f'{consonants_pool[j]}{vowels_pool[i]}'
                                 f'{consonants_pool2[0]}')
    return words


def generate_words(args, consonants_pool, vowels_pool, size):
    """Generate words according to non-fixed configuration."""
    words = []
    words_already_generated = set()

    i = 0
    while i < size:
        random.shuffle(consonants_pool)
        random.shuffle(vowels_pool)
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
    consonant1 = consonants_pool[0]
    vowel1 = vowels_pool[0]
    if random.choice((True, False)):
        if args.number_of_letters == 2:
            word = f'{vowel1}{consonant1}'
        else:
            vowel2 = vowels_pool[1]
            word = f'{vowel1}{consonant1}{vowel2}'
    else:
        if args.number_of_letters == 2:
            word = f'{consonant1}{vowel1}'
        else:
            consonant2 = consonants_pool[1]
            word = f'{consonant1}{vowel1}{consonant2}'

    return word


def generate_reversed_word(args, consonants_pool, vowels_pool):
    """Generate word according to reverse rule."""
    consonant1 = consonants_pool[0]
    vowel1 = vowels_pool[0]
    if args.number_of_letters == 2:
        word = f'{vowel1}{consonant1}'
    else:
        vowel2 = vowels_pool[1]
        word = f'{vowel1}{consonant1}{vowel2}'

    return word


def generate_word(args, consonants_pool, vowels_pool):
    """Generate word according to default rule."""
    consonant1 = consonants_pool[0]
    vowel1 = vowels_pool[0]
    if args.number_of_letters == 2:
        word = f'{consonant1}{vowel1}'
    else:
        consonant2 = consonants_pool[1]
        word = f'{consonant1}{vowel1}{consonant2}'

    return word


if __name__ == '__main__':
    main()
