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
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        nargs= '+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        metavar='',
                        type=str,
                        default='False')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.positional

    if args.sorted:
        sorted(items)

    # if len(items) == 1:
    #     print(f'You are bringing {items[0]}.')
    
    # elif len(items) == 2:
    #     print(f"You are bringing {items[0]} and {items[1]}.")
    
    # else:
    #     print(f"You are bringing {items[0:]}, and {items[-1]}.")

    things = ''

    num = len(items)
    bond = ', '

    if num == 1:
        things = items[0]
    elif num == 2:
        things = bond.join(items)
    else:
        items[-1] = ('and ' + items[-1])
        things = bond.join(items)

    print(f"You are bringing {things}.")



# --------------------------------------------------
if __name__ == '__main__':
    main()
