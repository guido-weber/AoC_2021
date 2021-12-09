from aoc_2021 import common

test_input = """2199943210
3987894921
9856789892
8767896789
9899965678"""


def parse_input(lines: list[str]):
    return [[int(c) for c in line.strip()] for line in lines]


def neighbours(heightmap, y, x):
    if y > 0:
        yield (y - 1, x)
    if x > 0:
        yield (y, x - 1)
    if y < (len(heightmap) - 1):
        yield (y + 1, x)
    if x < (len(heightmap[y]) - 1):
        yield (y, x + 1)


def risk_level(heightmap, y, x):
    here = heightmap[y][x]
    is_low_point = all(
        heightmap[ny][nx] > here for ny, nx in neighbours(heightmap, y, x)
    )
    return here + 1 if is_low_point else 0


def part1(lines):
    heightmap = parse_input(lines)
    result = 0
    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            result += risk_level(heightmap, y, x)
    return result


def flood(heightmap, start_y, start_x):
    basin = set()
    todo = set()
    todo.add((start_y, start_x))
    while todo:
        coord = todo.pop()
        if coord not in basin:
            basin.add(coord)
            for nb in neighbours(heightmap, coord[0], coord[1]):
                if heightmap[nb[0]][nb[1]] < 9 and nb not in basin:
                    todo.add(nb)
    return len(basin)


def part2(lines):
    heightmap = parse_input(lines)
    low_points = []
    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            if risk_level(heightmap, y, x):
                low_points.append((y, x))
    basin_sizes = []
    for y, x in low_points:
        size = flood(heightmap, y, x)
        basin_sizes.append(size)
    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


if __name__ == "__main__":
    common.run(9, test_input, 15, test_input, 1134, part1, part2)
