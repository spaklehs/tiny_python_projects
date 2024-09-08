#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import random
import re
import string

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Password maker',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'),
                        help='Input file(s)')

    parser.add_argument('-n',
                        '--num',
                        help='Number of passwords to generate',
                        metavar='num_passwords',
                        type=int,
                        default=3)

    parser.add_argument('-m',
                        '--min_word_len',
                        help='Minimum word length',
                        metavar='minimum',
                        type=int,
                        default=3)

    parser.add_argument('-x',
                        '--max_word_len',
                        help='Maximum word length',
                        metavar='maximum',
                        type=int,
                        default=6)

    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)
    
    parser.add_argument('-l',
                        '--l33t',
                        action= 'store_true',
                        help='Obfuscate letters',
                        default= False)

    return parser.parse_args()


# --------------------------------------------------
def main():

    args = get_args()
    random.seed(args.seed)

    words= set() #단어를 중복없이 저장하기 위해    

    for fh in args.file: #파일을 하나씩 읽음
        for line in fh: #한줄씩 읽음
            for word in filter(word_len, map(clean, line.lower().split())):
            # for word in line.lower().split(): #각 줄을 소문자로 바꾼뒤 공백기준으로 단어 쪼갬
                #words[word] = 1 #value에 의미없는 값 저장 (왜냐면 key가 필요함)
                words.add(word.title())
                
    words = sorted(list(words))
    passwords = [
        ''.join(random.sample(words, args.num)) for _ in range(args.num)
    ]
    
    if args.l33t:
        passwords = ''.join(list(map(l33t, passwords)))
    
    print(passwords)

# --------------------------------------------------
def clean(word): #구두점, 기호 없애는 함수
    
    # g = word.replace('.', '')
    # print(g)
    
    return re.sub('[^a-zA-Z]', '', word)

# --------------------------------------------------
def word_len(word):
    args = get_args()
    return args.min_word_len <= len(word) <= args.max_word_len

# --------------------------------------------------
def ransom(word):
    return ''.join(map(lambda x : x.upper() if random.choice([0,1]) else x.lower(), word))

# --------------------------------------------------
def l33t(text):

    text = ransom(text)
    xform = str.maketrans({
        'a': '@', 'A': '4', 'O': '0', 't': '+', 'E': '3', 'I': '1', 'S': '5'
    }) #maketrans라는 함수가 존재
    return text.translate(xform) + random.choice(string.punctuation)

# --------------------------------------------------
if __name__ == '__main__':
    main()
