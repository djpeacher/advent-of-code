"""https://adventofcode.com/2021/day/12"""
from collections import defaultdict
from copy import deepcopy


def part_one(data):

    def count_paths(node, seen):
        if node == 'end':
            # print(node, seen, 'node was end')
            return 1
        if node == 'start' and len(seen) > 1:
            # print(node, seen, 'node was start')
            return 0
        if node.islower() and node in seen and len(seen) > 1:
            # print(node, seen, 'node seen')
            return 0
        # print(node, seen, 'new node')
        return sum(count_paths(n, [*seen, node]) for n in data[node])

    return count_paths('start', ['start'])


def part_two(data):
    def count_paths(node, seen, bonus_cave):
        if node == 'end':
            # print(node, seen, 'node was end')
            # print(",".join([*seen, node]))
            return 1
        if node == 'start' and len(seen) > 1:
            # print(node, seen, 'node was start')
            return 0
        if node.islower() and node in seen and len(seen) > 1:
            if bonus_cave:
                bonus_cave = False
            else:
                # print(node, seen, 'node seen twice')
                return 0
        # print(node, seen, 'new node')
        return sum(count_paths(n, [*seen, node], bonus_cave) for n in data[node])

    return count_paths('start', [], True)


with open('input.txt') as file:
    raw_data = [line.strip().split('-') for line in file]
    data = defaultdict(set)
    for a, b in raw_data:
        data[a].add(b)
        data[b].add(a)
    print(part_one(deepcopy(data)))
    print(part_two(deepcopy(data)))
