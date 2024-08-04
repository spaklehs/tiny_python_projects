#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Twelve Days of Christmas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('-n',
                        '--num',
                        help='Number of days to sing',
                        metavar='days',
                        type=int,
                        default=12)

    parser.add_argument('-o',
                        '--outfile',
                        help='Outfile',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)
    
    args = parser.parse_args()

    if not 1 <= args.num <= 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')

    return args


# --------------------------------------------------
def verse(day):

    ordinal = [
        'first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh',
        'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth'
    ] #서수 (올려세기)

    gifts = [
        'partridge in a pear tree.',
        'Two turtle doves,',
        'Three French hens,',
        'Four calling birds,',
        'Five gold rings,',
        'Six geese a laying,',
        'Seven swans a swimming,',
        'Eight maids a milking,',
        'Nine ladies dancing,',
        'Ten lords a leaping,',
        'Eleven pipers piping,',
        'Twelve drummers drumming,',
    ] #받는 선물 (내려세기)

    lines = [
        f'On the {ordinal[day - 1]} day of Christmas,',
        'My true love gave to me,'
    ]
    
    #서수는 올려세기 고정, 이 lines에 gifts를 append

    for i in range(day, 0, -1):  #입력한 -n에 따라 gift 내려세기
        if i == 1: #첫번째 날일때
            lines.append(f'A {gifts[0]}' if day == 1 else f'And a {gifts[0]}')
        else: #첫번째 날이 아닐때
            lines.append(gifts[i-1])

    result = '\n'.join(lines)
    return result


# --------------------------------------------------
def main():
    args = get_args()
    for day in range(1, args.num + 1):
        if day == 1:
            '''
            On the first day of Christmas,
            my true love gave to me
            A partridge in a pear tree.
            '''
            print(verse(day))

        else:
            '''
            On the third day of Christmas,
            my true love gave to me
            Three French hens, # 새로 선물한거
            Two turtle doves,  # 기존에 선물한거
            And a partridge in a pear tree.
            '''
            print(verse(day))
        print()



# --------------------------------------------------
if __name__ == '__main__':
    main()
