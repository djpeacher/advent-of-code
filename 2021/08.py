"""https://adventofcode.com/2021/day/8"""


def part_one(data):
    count = 0
    for entry in data:
        for digit in entry:
            if len(digit) in [2, 4, 3, 7]:
                count += 1
    return count


def part_two(data):  # INCOMPLETE
    pass


with open('input.txt') as file:
    data = [line.strip().split(' | ')[1].split() for line in file]
    print(part_one(data))
    # print(part_two(data))
    print("INCOMPLETE")
