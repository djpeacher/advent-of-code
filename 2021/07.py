# https://adventofcode.com/2021/day/7


def part_one(data):
    def calc_move(p, c): return abs(p-c)
    fuel = [sum(calc_move(p, c) for c in data) for p in range(len(data))]
    return min(fuel)


def part_two(data):
    def calc_move(p, c): return sum(range(1, abs(p-c)+1))
    fuel = [sum(calc_move(p, c) for c in data) for p in range(len(data))]
    return min(fuel)


with open('input.txt') as file:
    data = [int(x) for x in file.readline().strip().split(',')]
    print(part_one(data))
    print(part_two(data))
