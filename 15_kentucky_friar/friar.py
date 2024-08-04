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
        description='Southern fry text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        type= str,
                        metavar='text',
                        help='Input text or file')
    
    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------

def fry(word):
    
    you = re.match('([yY])ou$', word) #y[Y]ou -> y[Y]'all

    ing = re.search('(.+)ing$', word) #ing -> in'

    if you:
        return you.group(1) + "'all"
    
    elif ing:
        if re.search('[aeiouy]', word[:-3]):
            return ing.group(1) + "in'"
        else:
            return word
    
    else:
        return word
    
# --------------------------------------------------

def test_fry():
    assert fry('you') == "y'all"
    assert fry('You') == "Y'all"
    assert fry('fishing') == "fishin'"
    assert fry('Aching') == "Achin'"
    assert fry('swing') == "swing"

# --------------------------------------------------

def main():
    """Make a jazz noise here"""

    args = get_args()
    for line in args.text.splitlines():
        words=[]
        for word in re.split(r'(\W+)', line.rstrip()):
            # print(word, fry(word))
            words.append(fry(word))
        print(''.join(words))

    #re.split(',', args.text) 쉼표마다 나눔
    #re.search('\W', args.text)
    #꺾쇠 기호(^)를 문자 클래스에 넣어서 보완/부정할 수 있다
    # \W: 단어, 문자가 아닌 것 찾음
    # \w: 단어 같은 문자를 찾음. 뒤에 +를 붙이면 하나 이상의 연속된 단어 문자를 찾음
    # re.split(r'(\W+)', args.text) 패턴에 일치하는 것과 일치하지 않는 것을 추출. 단어와 쉼표와 \n 나뉨
    #결과 ['Father', ', ', 'father', ', ', 'where', ' ', 'are', ' ', 'you', ' ', 'going', '?\n ', 'Oh', ' ', 'do', ' ', 'not', ' ', 'walk', ' ', 'so', ' ', 'fast', '!\n', 'Speak', ', ', 'father', ', ', 'speak', ' ', 'to', ' ', 'your', ' ', 'little', ' ', 'boy', ',\n ', 'Or', ' ', 'else', ' ', 'I', ' ', 'shall', ' ', 'be', ' ', 'lost']

    # new_word = fry(args.text)
    # print(new_word)

# --------------------------------------------------
if __name__ == '__main__':
    main()
