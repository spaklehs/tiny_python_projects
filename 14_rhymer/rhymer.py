#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import re
import string as s

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Make rhyming "words"',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word to rhyme') #positional

    return parser.parse_args()

# --------------------------------------------------
def stemmer(word):
    # 주어진 단어를 자음 부분과 나머지 부분으로 쪼개는 함수

    word = word.lower() #모든 단어는 소문자로 변환
    
    alpha_list = list(s.ascii_lowercase)

    vowels = 'aeiou'
    consonants = ''.join([c for c in s.ascii_lowercase if c not in 'aeiou']) #자음
    # for c in s.ascii_lowercase:
    #     if c not in 'aeiou':
    #         consonants += c와 동일함

    '''
    pattern = (
        '([' + consonants + ']+)?' # capture one or more, optional 옵션
        '([' + vowels     + '])'   # capture at least one vowel 적어도 1개 이상
        '(.*)'                     # capture zero or more of anything 0개 이상
    )
    '''

    pattern = f'([{consonants}]+)?([{vowels}])(.*)'

    match = re.match(pattern, word)

    # re.match는 문자열 시작부분에서 패턴과 문자열을 비교한다
    # consonants 뒤에 오는 부분을 캡쳐하기 위해 마침표 사용
    # 패턴 뒤에 물음표 : 옵션 지정
    # 플러스 기호를 사용해서 하나 이상의 글자를 캡쳐 / (.*)으로 바꾸면 0개 이상의 값을 찾음
    # 따라서 별도의 캡쳐 그룹 구성됨 ('ch', 'air')

    if match:
        p1 = match.group(1) or '' #pattern1 or의 왼쪽은 True 분기, 오른쪽은 False
        p2 = match.group(2) or ''
        p3 = match.group(3) or ''
        return (p1, p2+p3) #앞부분과 나머지를 튜플로 반환
    else:
        return (word, '')

# --------------------------------------------------

def test_stemmer():

    assert stemmer('') == ('', '')
    assert stemmer('cake') == ('c', 'ake')
    assert stemmer('chair') == ('ch','air')
    assert stemmer('APPLE') == ('', 'apple')
    assert stemmer('RDNZL') == ('rdnzl', '')
    assert stemmer('123') == ('123', '')


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    start, rest = stemmer(args.word)
    
    prefixes = list('bcdfghjklmnpqrstvwxyz') + (
        'bl br ch cl cr dr fl fr gl gr pl pr sc '
        'sh sk sl sm sn sp st sw th tr tw thw wh wr '
        'sch scr shr sph spl spr squ str thr').split()

    if rest:
        print('\n'.join([p + rest for p in prefixes if p!=start]))
        # for p in prefixes:
            # if p != start:
                # p += rest
    else:
        print(f'cannot rhyme "{args.word}"')
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
