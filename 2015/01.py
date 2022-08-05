"""https://adventofcode.com/2015/day/1"""

key = {'(': 1, ')': -1}


def part_one(data):
    return sum(key[x] for x in data)


def part_two(data):
    lvl = 0
    for idx, x in enumerate(data):
        lvl += key[x]
        if lvl == -1:
            return idx + 1


with open('input.txt') as file:
    data = file.readline()
    print(part_one(data))
    print(part_two(data))
