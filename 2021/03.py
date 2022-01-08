"""https://adventofcode.com/2021/day/3"""
from collections import Counter


def part_one(data):
    counts = [0] * 12
    for binary in data:
        for index, bit in enumerate(binary):
            counts[index] += 1 if bit == '1' else -1
    gamma_rate = int(''.join('1' if c > 0 else '0' for c in counts), 2)
    epsilon_rate = int(''.join('1' if c < 0 else '0' for c in counts), 2)
    return gamma_rate * epsilon_rate


def find_value(data, index, value):
    if len(data) == 1:
        return int(data[0], 2)
    common = Counter([binary[index] for binary in data]).most_common()
    equal = common[0][1] == common[1][1] if len(common) > 1 else False
    most_common = common[0][0]
    least_common = common[:0:-1][0][0] if len(common) > 1 else most_common
    filter_bit = None
    if value == 'oxygen':
        filter_bit = '1' if equal else most_common
    if value == 'co2':
        filter_bit = '0' if equal else least_common
    return find_value([b for b in data if b[index] == filter_bit], index + 1, value)


def part_two(data):
    oxygen = find_value(data, index=0, value='oxygen')
    co2 = find_value(data, index=0, value='co2')
    return oxygen * co2


with open('input.txt') as file:
    data = [line.strip() for line in file]
    print(part_one(data))
    print(part_two(data))
