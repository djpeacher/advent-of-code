"""https://adventofcode.com/2015/day/2"""
import math


def part_one(data):
    total = 0
    for l, w, h in data:
        s1, s2, s3 = l*w, w*h, h*l
        total += 2*(s1 + s2 + s3) + min(s1, s2, s3)
    return total


def part_two(data):
    total = 0
    for d in data:
        d = sorted(d)
        total += 2*d[0] + 2*d[1] + math.prod(d)
    return total


with open('input.txt') as file:
    data = [
        tuple(int(x) for x in line.split('x'))
        for line in file
    ]
    print(part_one(data))
    print(part_two(data))
