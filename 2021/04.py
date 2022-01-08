"""https://adventofcode.com/2021/day/4"""
from pprint import pprint
from copy import deepcopy


def part_one(order, boards):
    for number in order:
        for board in boards:
            for y, row in enumerate(board):
                for x, cell in enumerate(row):
                    if cell == number:
                        board[y][x] = None
                        winner = (board[y][0] == board[y][1] == board[y][2] == board[y][3] == board[y][4]) or (
                            board[0][x] == board[1][x] == board[2][x] == board[3][x] == board[4][x])
                        if winner:
                            total = 0
                            for row in board:
                                for cell in row:
                                    total += cell if cell else 0
                            return total * number


def part_two(order, boards):  # INCOMPLETE
    for number in order:
        for b, board in enumerate(boards):
            for y, row in enumerate(board):
                for x, cell in enumerate(row):
                    if cell == number:
                        board[y][x] = None
                        winner = (board[y][0] == board[y][1] == board[y][2] == board[y][3] == board[y][4]) or (
                            board[0][x] == board[1][x] == board[2][x] == board[3][x] == board[4][x])
                        if winner:
                            boards[b] = []
                            remaining = [b for b in boards if b]
                            print(len(remaining))
                            if len(remaining) == 1:
                                total = 0
                                for r in remaining[0]:
                                    for c in r:
                                        total += c if c else 0
                                print(total, number)
                                pprint(remaining[0])
                                return total * number


with open('input.txt') as file:
    order = [int(x) for x in file.readline().strip().split(',')]
    boards = []
    board = None
    for line in file:
        line = line.strip()
        if line == '':
            if board:
                boards.append(board)
            board = []
        else:
            row = [int(cell) for cell in line.split()]
            board.append(row)
    boards.append(board)
    print(part_one(order, deepcopy(boards)))
    # print(part_two(order, deepcopy(boards)))
    print("INCOMPLETE")
