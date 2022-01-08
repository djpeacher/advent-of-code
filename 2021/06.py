# https://adventofcode.com/2021/day/6


def part_one(data):
    for x in range(80):
        add = 0
        for index, fish in enumerate(data):
            if fish == 0:
                add += 1
                data[index] = 6
            else:
                data[index] -= 1
        data += ([8] * add)
    return len(data)


def part_two(data):  # INCOMPLETE
    for x in range(256):
        add = 0
        for index, fish in enumerate(data):
            if fish == 0:
                add += 1
                data[index] = 6
            else:
                data[index] -= 1
        data += ([8] * add)
    return len(data)


with open('input.txt') as file:
    data = [int(x) for x in file.readline().strip().split(',')]
    print(part_one(data.copy()))
    # print(part_two(data.copy()))
    print("INCOMPLETE")
