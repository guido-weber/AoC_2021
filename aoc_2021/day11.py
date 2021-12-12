from aoc_2021 import common

test_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


def parse_input(lines: list[str]):
    return [[int(i) for i in line.strip()] for line in lines]


def should_flash(ng, flashed):
    return {
        (y, x)
        for y, row in enumerate(ng)
        for x, level in enumerate(row)
        if level > 9 and (y, x) not in flashed
    }


def flash(grid: list[list[int]], y: int, x: int):
    for yy in range(y - 1, y + 2):
        if yy < 0 or yy >= len(grid):
            continue
        for xx in range(x - 1, x + 2):
            if xx >= 0 and xx < len(grid[yy]) and (y != yy or x != xx):
                grid[yy][xx] += 1


def step(grid: list[list[int]]):
    ng = [[v + 1 for v in row] for row in grid]
    flashed: set[tuple[int, int]] = set()
    to_flash = should_flash(ng, flashed)
    while to_flash:
        for y, x in to_flash:
            flash(ng, y, x)
        flashed.update(to_flash)
        to_flash = should_flash(ng, flashed)
    for y, x in flashed:
        ng[y][x] = 0
    return ng, len(flashed)


def part1(lines):
    grid = parse_input(lines)
    result = 0
    for _ in range(100):
        grid, flashes = step(grid)
        result += flashes
    return result


def part2(lines):
    grid = parse_input(lines)
    num_cells = len(grid) * len(grid[0])
    count = 0
    while True:
        grid, flashes = step(grid)
        count += 1
        if flashes == num_cells:
            return count
    return -1


if __name__ == "__main__":
    common.run(11, test_input, 1656, test_input, 195, part1, part2)
