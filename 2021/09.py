"""https://adventofcode.com/2021/day/9"""


def part_one(data):
    low_points = []

    def is_low_point(x, y):
        point = data[y][x]
        # print(point)
        try:
            if point < data[y+1][x]:
                pass
            else:
                return False
        except:
            pass
        try:
            if point < data[y-1][x]:
                pass
            else:
                return False
        except:
            pass
        try:
            if point < data[y][x+1]:
                pass
            else:
                return False
        except:
            pass
        try:
            if point < data[y][x-1]:
                pass
            else:
                return False
        except:
            pass
        return True
    for y in range(len(data)):
        for x in range(len(data[y])):
            if is_low_point(x, y):
                low_points.append(data[y][x])
    # print(low_points)
    return sum(low_points) + len(low_points)


def part_two(data):  # INCOMPLETE
    pass


with open('input.txt') as file:
    data = [[int(x) for x in row.strip()] for row in file]
    print(part_one(data))
    print("INCOMPLETE")
