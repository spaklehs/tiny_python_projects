#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os
import re
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Scramble the letters of words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input text or file') #positional

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def scramble(word): #단어를 섞음
    
    middle = list(word[1:-1])
    if len(word)>3:
        random.shuffle(middle)
        word = word[0] + ''.join(middle) + word[-1]
        return word
    else:
        return word

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    random.seed(args.seed)
    splitter = re.compile("([a-zA-Z](?:[a-zA-Z']*[a-zA-Z])?)")

    for line in args.text.splitlines():
        scramble_word = map(scramble, splitter.split(line))
        print(''.join(list(scramble_word)))

# --------------------------------------------------
if __name__ == '__main__':
    main()
