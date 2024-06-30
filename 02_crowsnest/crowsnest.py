#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='word',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.positional

    article =''

    if word[0].lower() in 'aeiou':
        article = 'an'
    else:
        article = 'a'

    template = f'Ahoy, Captain, {article} {word} off the larboard bow!'
    print(template)


# --------------------------------------------------
if __name__ == '__main__':
    main()
