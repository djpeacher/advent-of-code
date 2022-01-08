"""https://adventofcode.com/2021/day/1"""


def part_one(data):
    def compare(i): return data[i] > data[i-1]
    return len([i for i in range(1, len(data)) if compare(i)])


def part_two(data):
    def compare(i): return sum(data[i-3: i]) > sum(data[i-4: i-1])
    return len([i for i in range(3, len(data)) if compare(i)])


with open('input.txt') as file:
    data = [int(line.strip()) for line in file]
    print(part_one(data))
    print(part_two(data))
