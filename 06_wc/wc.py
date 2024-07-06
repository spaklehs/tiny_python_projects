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
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)


    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        type=argparse.FileType('r'),
                        default=[sys.stdin],
                        help='Input file(s)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    total_lines, total_word, total_byte = 0, 0, 0     #총 줄, 단어, 바이트 수
    for argsfh in args.file:
        num_lines, num_word, num_byte = 0, 0, 0
        f= open(argsfh.name)

        for line in f:
            # print("line : ", line)
            num_lines += 1
            num_word += len(line.split(' '))
            num_byte += len(line)
        
        total_lines += num_lines
        total_word += num_word
        total_byte += num_byte

        print(f'{num_lines}  {num_word}  {num_byte}  {argsfh.name}')
        # print('file_arg = "{}"'.format(argsfh.name if file_arg else ''))
    
    if len(args.file) > 1:  #파일이 두 개 이상일 때부터 total 값 출력
        print(f'{total_lines}  {total_word}  {total_byte}  total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
