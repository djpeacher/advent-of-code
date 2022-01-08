"""https://adventofcode.com/2021/day/5"""
from pprint import pprint
from collections import Counter


def part_one(data):
    board = [[0] * 1000 for _ in range(1000)]
    for start, end in data:
        x1, y1 = start
        x2, y2 = end
        if x1 != x2 and y1 != y2:
            continue
        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                board[y][x1] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                board[y1][x] += 1
    long_board = []
    for row in board:
        long_board += row

    return (1000*1000) - Counter(long_board)[0] - Counter(long_board)[1]


def part_two(data):  # INCOMPLETE
    board = [[0] * 10 for _ in range(10)]
    for start, end in data:
        x1, y1 = start
        x2, y2 = end
        if x1 != x2 and y1 != y2:
            for x, y in zip(range(min(x1, x2), max(x1, x2)+1), range(min(y1, y2), max(y1, y2)+1)):
                board[y][x] += 1
        elif x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                board[y][x1] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                board[y1][x] += 1
    pprint(board)

    long_board = []
    for row in board:
        long_board += row

    return (10*10) - Counter(long_board)[0] - Counter(long_board)[1]


with open('input.txt') as file:
    data = []
    for line in file:
        start_end = line.strip().split(' -> ')
        start = start_end[0].split(',')
        start = (int(start[0]), int(start[1]))
        end = start_end[1].split(',')
        end = (int(end[0]), int(end[1]))
        data.append([start, end])
    print(part_one(data))
    # print(part_two(data))
    print("INCOMPLETE")
