#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os
import random
import math
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if not 0 <= args.mutations <=1:
        parser.error(f'--mutations "{args.mutations} must be between 0 and 1')
    
    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    print(f'You said: "{args.text}"')

    num_mutations = math.floor(len(args.text)*args.mutations) #문장에서 몇 글자를 바꿀 것인지
    indexes = random.sample(range(len(args.text)), num_mutations) #문장에서 바꿀 글자의 인덱스
    alpha = string.ascii_letters + string.punctuation

    changed_char = list(args.text) #리스트로 묶음

    for i in indexes:
        changed_char[i] = random.choice(alpha)
        changed_text = ''.join(changed_char)
        
    print(f'I heard: "{changed_text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
