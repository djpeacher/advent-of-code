"""https://adventofcode.com/2015/day/4"""
import hashlib
from itertools import count


def part_one(data):
    for n in count(1):
        hash = hashlib.md5(str.encode(f'{data}{n}')).hexdigest()
        if hash.startswith("00000"):
            return n


def part_two(data):
    for n in count(1):
        hash = hashlib.md5(str.encode(f'{data}{n}')).hexdigest()
        if hash.startswith("000000"):
            return n


with open('input.txt') as file:
    data = file.readline()
    print(part_one(data))
    print(part_two(data))
