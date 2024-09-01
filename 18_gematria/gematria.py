#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import os
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gematria',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    for line in args.text.splitlines():
        line2 = re.sub('[^A-Za-z0-9\s]', '', line) #문단을 정제된 문장으로 나눔, \s가 띄어쓰기
        print(' '.join(map(word2num, line2.split()))) #문장에 word2num 적용, 띄어쓰기 하여 단어별로 더한값을 산출

# --------------------------------------------------
def word2num(word):
    #단어 암호화 함수
    ''' filterr = re.findall('[^A-Za-z0-9]', args.text) #대소문자 알파벳, 숫자 0-9를 제외한 문자를 찾아줌
    print(filterr) '''

    vals = []
    for char in word:
        vals = map(ord, word) #입력받은 단어에 ord 함수 적용
    return str(sum(list(vals))) #vals값 map object이므로 리스트로 감싸고 sum 한 뒤 str값으로 리턴 -> 메인함수로 들어감


# --------------------------------------------------
if __name__ == '__main__':
    main()
