#!/usr/bin/env python3
"""
Author : Me <me@foo.com>
Date   : today
Purpose: Rock the Casbah
"""

import argparse
import re


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tic-Tac-Toe',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-b',
                        '--board',
                        metavar='board',
                        type=str,
                        help='The state of the board', #보드는 어떤 칸을 어떤 플레이어가 채웠는지 지정하는 것
                        default='.'*9) #보드의 기본 상태: 마침표 9개

    parser.add_argument('-p',
                        '--player',
                        help='player',
                        metavar='player',
                        choices='XO', #X 또는 O 지정함
                        type=str,
                        default=None)

    parser.add_argument('-c',
                        '--cell',
                        help='cell 1~9',
                        metavar='cell',
                        type=int,
                        choices= range(1, 10),
                        default=None)

    args = parser.parse_args()

    # if not re.search('^[.XO]{9}$', args.board):
    #     parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')

    if len(args.board) != 9 or any(char not in 'XO.' for char in args.board): #any는 하나만 true여도 반환
        parser.error(f'--board "{args.board}" must be 9 characters of ., X, O')


    if args.player not in {'X', 'O'}:
        parser.error("choose from 'X', 'O'")
    

    # any는 인자로 받은 자료형이 비어있는 경우 False를 반환합니다.

    if any([args.player, args.cell]) and not all([args.player,args.cell]):
        parser.error("Must provide both --player and --cell")

    if args.player and args.cell and args.board[args.cell - 1] in 'XO':
        parser.error(f'--cell "{args.cell}" already taken')

    return args

# --------------------------------------------------
def format_board(board):
    
#board가 ...XO....이면
# -------------
# | 1 | 2 | 3 |
# -------------
# | X | O | 6 |
# -------------
# | 7 | 8 | 9 |
# -------------
# 이렇게 돼야함

    lines = [board[x:x+3] for x in range(0, 9, 3)]

    # print('| {%s} | {%s} | {%s} |'%(lines[0][0], lines[0][1], lines[0][2]))
    # print('| {%s} | {%s} | {%s} |'%(lines[1][0], lines[1][1], lines[1][2]))
    # print('| {%s} | {%s} | {%s} |'%(lines[2][0], lines[2][1], lines[2][2]))
    for x in range(3):
        print('| {%s} | {%s} | {%s} |'%(lines[x][0], lines[x][1], lines[x][2]))

    # cells = 
    # bar = '-------------'
    # cells_template = '| {} | {} | {} |'

# --------------------------------------------------
def find_winner(board):

    winning_cases = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
               [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    
    for player in ['X','O']:
        for i, j, k in winning_cases:
            combo = [board[i], board[j], board[k]]
            if combo == [player, player, player]:
                return player


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    print(args.cell)
    new_board = args.board[0:args.cell-1] + args.player + args.board[args.cell:]


    format_board(new_board)
    # find_winner(new_board)
    winner = find_winner(new_board)
    print(f'{winner} has won!' if winner else 'No winner.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
