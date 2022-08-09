"""https://adventofcode.com/2015/day/3"""


def part_one(data):
    location = [0, 0]
    counter = {'00': True}
    for dir in data:
        update(location, dir)
        counter[f'{location[0]}{location[1]}'] = True
    return len(counter)


def part_two(data):
    santa = [0, 0]
    robot = [0, 0]
    counter = {'00': True}
    for idx, dir in enumerate(data):
        location = robot if idx % 2 else santa
        update(location, dir)
        counter[f'{location[0]}{location[1]}'] = True
    return len(counter)


def update(location, dir):
    if dir == '^':
        location[1] -= 1
    elif dir == 'v':
        location[1] += 1
    elif dir == '<':
        location[0] -= 1
    elif dir == '>':
        location[0] += 1


with open('input.txt') as file:
    data = list(file.readline())
    print(part_one(data))
    print(part_two(data))
