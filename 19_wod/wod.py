#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import csv
import random
import io
from tabulate import tabulate


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Workout Of (the) Day (WOD)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    
    parser.add_argument('-f',
                        '--file',
                        help='CSV input file of exercises',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='inputs/exercises.csv')
    
    parser.add_argument('-s',
                        '--seed',
                        help='Random seed',
                        metavar='seed',
                        type=int,
                        default=None)

    parser.add_argument('-n',
                        '--num',
                        help='Number of exercises',
                        metavar='exercises',
                        type=int,
                        default=4)


    parser.add_argument('-e',
                        '--easy',
                        help='Halve the reps',
                        action='store_true')
    
    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    
    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)

    wod = [] # 하루 일정 (최종 결과값)

    exercises= read_csv(args.file)

    for name, low, high in random.sample(exercises, k=args.num):
        reps = random.randint(int(low), int(high)) # low ~ high 사이 난수 생성
        if args.easy:
            reps = int(reps/2)
        wod.append((name,reps))
    print(wod)
    
    print(tabulate(wod))
    

# --------------------------------------------------
def read_csv(fh): #csv 파일 읽고 운동이름, 최솟값, 최댓값 반환

    with open('inputs/exercises.csv') as fh: #filehandler
        reader= csv.DictReader(fh, delimiter=',')
        # print(list(reader))
        # records= []
        # for rec in reader:
        #     records.append(rec)
        # pprint(records)
        # records = list(reader)
        # pprint(records)
        exercises = []
        for rec in reader:
            name, reps = rec['exercise'], rec['reps']
            reee = reps.split('-')
            low = reee[0] #최솟값
            high = reee[1] #최댓값
            exercises.append((name, low, high))
        return exercises

# --------------------------------------------------
if __name__ == '__main__':
    main()
