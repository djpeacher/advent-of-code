"""https://adventofcode.com/2021/day/2"""


def part_one(data):
    position, depth = 0, 0
    for command, value in data:
        if command == 'forward':
            position += value
        elif command == 'up':
            depth -= value
        elif command == 'down':
            depth += value
    return position * depth


def part_two(data):
    position, depth, aim = 0, 0, 0
    for command, value in data:
        if command == 'forward':
            position += value
            depth += aim * value
        elif command == 'up':
            aim -= value
        elif command == 'down':
            aim += value
    return position * depth


with open('input.txt') as file:
    def format(x): return (x[0], int(x[1]))
    data = [format(line.strip().split()) for line in file]
    print(part_one(data))
    print(part_two(data))
