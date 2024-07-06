#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os



# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='text',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output',
                        metavar='str',
                        type=str,
                        default='')
    
    args = parser.parse_args()
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.outfile
    pos_arg = args.positional

    # out_fh = open(args.positional, 'wt')
    # out_fh.write(args.positional.upper())
    # out_fh.close()

    
    if os.path.isfile(args.positional):
        pf = open(args.positional, 'r').read().rstrip() #포지셔널파일
        ret = pf.upper()
        print(ret)


# --------------------------------------------------
if __name__ == '__main__':
    main()
