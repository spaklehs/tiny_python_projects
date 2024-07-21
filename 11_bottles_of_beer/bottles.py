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
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--number',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)


    args = parser.parse_args()

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for i in range(args.number, 0, -1):
        print(verse(i)) #step을 -1로 지정해서 내려 세기


# --------------------------------------------------

def verse(bottle):

    next_bottle = bottle-1

    if bottle == 1:
        return '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,','No more bottles of beer on the wall!'])
    
    elif next_bottle == 1:
        return '\n'.join([
            f'{bottle} bottles of beer on the wall,', f'{bottle} bottles of beer,',
            f'Take one down, pass it around,',f'{next_bottle} bottle of beer on the wall!'])
    
    else:
        return '\n'.join([
            f'{bottle} bottles of beer on the wall,', f'{bottle} bottles of beer,',
            f'Take one down, pass it around,',f'{next_bottle} bottles of beer on the wall!'])



def test_verse():
    last_verse = verse(1) #bottle이 1개 남았을때가 마지막
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,','No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,','1 bottle of beer on the wall!'
    ])
    

    


# --------------------------------------------------
if __name__ == '__main__':
    main()
