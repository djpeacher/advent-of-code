"""https://adventofcode.com/2021/day/14"""
from collections import Counter


def part_one(polymer, data):
    for i in range(10):
        # print(i, len(polymer))
        temp = ""
        for i in range(len(polymer)-1):
            pair = polymer[i:i+2]
            insert = data[pair]
            temp += f"{pair[0]}{insert}"
        temp += polymer[-1]
        polymer = temp
        # print(polymer)
    counter = Counter(polymer).most_common()
    return counter[0][1] - counter[-1][1]


def part_two(data):  # INCOMPLETE
    pass


with open('input.txt') as file:
    start = file.readline().strip()
    file.readline()
    data = {}
    for line in file:
        line = line.strip().split(' -> ')
        data[line[0]] = line[1]
    # print(start, data)
    print(part_one(start, data))
    # print(part_two(data))
    print("INCOMPLETE")
