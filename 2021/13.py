"""https://adventofcode.com/2021/day/13"""
from pprint import pprint
from copy import deepcopy


def part_one(grid, folds):  # INCOMPLETE
    dir, pos = folds[0]

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if row
            new_row
    for dir, pos in folds:
        new_pos =
        pass
        # print(dir, pos)
        # y
        # pos - (y - pos)
        # pprint(grid)


def part_two(grid, folds):  # INCOMPLETE
    pass


with open('input.txt') as file:
    data = [line.strip() for line in file]
    sep = data.index('')
    points = [(int(p.split(',')[0]), int(p.split(',')[1]))
              for p in data[0:sep]]
    max_x = max(p[0] for p in points) + 1
    max_y = max(p[1] for p in points) + 1
    grid = [[0 for col in range(max_x)] for row in range(max_y)]
    for x, y in points:
        grid[y][x] = 1
    folds = [(x.split(' ')[-1].split('=')[0], int(x.split(' ')[-1].split('=')[1]))
             for x in data[sep+1:len(data)]]
    # print(points)
    # print(folds)
    print(max_x, max_y)
    # pprint(grid)
    print(part_one(deepcopy(grid), folds))
    print(part_two(deepcopy(grid), folds))
