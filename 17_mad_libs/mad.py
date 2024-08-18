#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import re
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Mad Libs',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        help='Input file') #위치 인수로 파일을 받는다

    parser.add_argument('-i',
                        '--inputs',
                        help='Inputs (for testing)',
                        metavar='input',
                        type=str,
                        nargs = '*',
                        default= None)
    
    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    inputs = args.inputs
    text = args.file.read().rstrip()

    matches = re.findall('(<([^<>]+)>)', text)

    inputs = []

    for placeholder, name in matches:
        article = 'an' if name[0] in 'aeiou' else 'a' #관사
        value = input(f'Give me {article} {name}: ')
        inputs.append(value)
    
    print(inputs)

    text_word_list = text.split()
    index = 0
    for i, word in enumerate(text_word_list):
        if len(word) > 2 and word[-2] == ">" and word[-1] == ",":
            text_word_list[i] = ","
        if word[-1] == ">":
            text_word_list[i] = ""
        if word[0] == "<":
            text_word_list[i] = inputs[index]
            index += 1
    print(' '.join(text_word_list)+"." if text[-1] == "." else ' '.join(text_word_list))


    # print(inputs) input 받은 단어들이 저장된 리스트. 이걸 이제 직접 바꿔야 한다.


    if not matches:
        print('This is an error!', file= sys.stderr)
        sys.exit(1)


# --------------------------------------------------
if __name__ == '__main__':
    main()
