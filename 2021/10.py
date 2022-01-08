"""https://adventofcode.com/2021/day/10"""
from collections import deque


def part_one(data):
    illegal_char_count = {
        ')': 0,
        ']': 0,
        '}': 0,
        '>': 0
    }
    for line in data:
        stack = deque()

        for character in line:
            if character in '([{<':
                stack.append(character)
                continue
            left = stack.pop()
            expected_right = {
                '(': ')',
                '[': ']',
                '{': '}',
                '<': '>'
            }[left]
            if character != expected_right:
                illegal_char_count[character] += 1
                break
    return illegal_char_count[')'] * 3 + \
        illegal_char_count[']'] * 57 + \
        illegal_char_count['}'] * 1197 + \
        illegal_char_count['>'] * 25137


def part_two(data):
    illegal_char_count = {
        ')': 0,
        ']': 0,
        '}': 0,
        '>': 0
    }
    scores = []
    for line in data:
        stack = deque()

        for character in line:
            if character in '([{<':
                stack.append(character)
                continue
            left = stack.pop()
            expected_right = {
                '(': ')',
                '[': ']',
                '{': '}',
                '<': '>'
            }[left]
            if character != expected_right:
                stack = None
                break
        if stack:
            remainder = list(reversed(stack))
            end = ''
            for character in remainder:
                end += {
                    '(': ')',
                    '[': ']',
                    '{': '}',
                    '<': '>'
                }[character]
            score = 0
            for character in end:
                score *= 5
                score += {
                    ')': 1,
                    ']': 2,
                    '}': 3,
                    '>': 4
                }[character]
            scores.append(score)
    scores.sort()
    return scores[int(len(scores)/2)]


with open('input.txt') as file:
    data = [list(line.strip()) for line in file]
    print(part_one(data))
    print(part_two(data))
