from aoc_2021 import common

test_input = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""


def parse_input(lines: list[str]):
    points = set()
    folds = []
    for line in lines:
        x, sep, y = line.partition(",")
        if sep == ",":
            points.add((int(y), int(x)))
        elif line.startswith("fold along "):
            direction, position = line[len("fold along ") :].split("=")
            folds.append((direction, int(position)))
    return points, folds


def fold(points, direction, position):
    if direction == "x":
        return set((y, x) for y, x in points if x < position).union(
            set((y, 2 * position - x) for y, x in points if x > position)
        )
    else:
        return set((y, x) for y, x in points if y < position).union(
            set((2 * position - y, x) for y, x in points if y > position)
        )


def part1(lines):
    points, folds = parse_input(lines)
    points = fold(points, *folds[0])
    return len(points)


def part2(lines):
    points, folds = parse_input(lines)
    for direction, position in folds:
        points = fold(points, direction, position)
    width = max(x for _, x in points) + 1
    height = max(y for y, _ in points) + 1
    grid = [[" "] * width for _ in range(height)]
    for y, x in points:
        grid[y][x] = "#"
    for row in grid:
        print("".join(row))
    print("")
    return 42


if __name__ == "__main__":
    common.run(13, test_input, 17, test_input, 42, part1, part2)
