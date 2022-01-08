"""https://adventofcode.com/2021/day/11"""
from copy import copy
from pprint import pprint


def print_data(step, data):
    print()
    print('step', step)
    for row in data:
        print(''.join([str(r) for r in row]))


def part_one(data):
    count = 0
    steps = 100

    # print_data(0, data)

    for step in range(steps):
        # increment
        data = [[col+1 for col in row] for row in data]

        def increment(row, col):
            try:
                if row < 0 or col < 0:
                    return False
                data[row][col] += 1
                # print('++', row, col, data[row][col], data[row][col]+1)
                if data[row][col] > 9:
                    return True
            except:
                pass
            return False

        def flash(row, col):
            data[row][col] = None
            return any([
                increment(row-1, col-1),
                increment(row-1, col),
                increment(row-1, col+1),
                increment(row, col-1),
                increment(row, col+1),
                increment(row+1, col-1),
                increment(row+1, col),
                increment(row+1, col+1),
            ])

        # flash
        flashing = True
        while flashing:
            flashing = False
            for row in range(len(data)):
                for col in range(len(data[row])):
                    cell = data[row][col]
                    # print(row, col, cell)
                    if cell and cell > 9:
                        # print('flash!')
                        count += 1
                        cascade = flash(row, col)
                        if cascade:
                            # print("cascading")
                            flashing = True

        # reset
        data = [[0 if col == None else col for col in row] for row in data]
        # print_data(step+1, data)

    return count


def part_two(data):
    count = 0
    step = 0

    # print_data(0, data)

    while True:
        step += 1
        # increment
        data = [[col+1 for col in row] for row in data]

        def increment(row, col):
            try:
                if row < 0 or col < 0:
                    return False
                data[row][col] += 1
                # print('++', row, col, data[row][col], data[row][col]+1)
                if data[row][col] > 9:
                    return True
            except:
                pass
            return False

        def flash(row, col):
            data[row][col] = None
            return any([
                increment(row-1, col-1),
                increment(row-1, col),
                increment(row-1, col+1),
                increment(row, col-1),
                increment(row, col+1),
                increment(row+1, col-1),
                increment(row+1, col),
                increment(row+1, col+1),
            ])

        # flash
        flashing = True
        while flashing:
            flashing = False
            for row in range(len(data)):
                for col in range(len(data[row])):
                    cell = data[row][col]
                    # print(row, col, cell)
                    if cell and cell > 9:
                        # print('flash!')
                        count += 1
                        cascade = flash(row, col)
                        if cascade:
                            # print("cascading")
                            flashing = True

        # reset
        data = [[0 if col == None else col for col in row] for row in data]
        # print_data(step+1, data)

        # check
        valid = True
        for row in data:
            if sum(row) != 0:
                valid = False

        if valid:
            return step


with open('input.txt') as file:
    data = [[int(x) for x in line.strip()] for line in file]
    print(part_one(copy(data)))
    print(part_two(copy(data)))
