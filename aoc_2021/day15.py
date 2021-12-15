import heapq
from dataclasses import dataclass
from functools import reduce

from aoc_2021 import common

test_input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""


def parse_input(lines: list[str]):
    return [[int(c) for c in line.strip()] for line in lines]


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


def neighbours(p: Point, grid: list[list[int]]):
    if p.y > 0:
        yield Point(p.x, p.y - 1)
    if p.x > 0:
        yield Point(p.x - 1, p.y)
    if p.y < len(grid) - 1:
        yield Point(p.x, p.y + 1)
    if p.x < len(grid[p.y]) - 1:
        yield Point(p.x + 1, p.y)


def find_path(start: Point, goal: Point, grid: list[list[int]]):
    open_list: list[tuple[int, Point]] = []
    costs: dict[Point, int] = {}

    heapq.heappush(open_list, (start.distance(goal), start))
    costs[start] = 0

    while open_list:
        _, current = heapq.heappop(open_list)
        if current == goal:
            return costs[current]

        for p in neighbours(current, grid):
            cost = costs[current] + grid[p.y][p.x]
            if p not in costs or costs[p] > cost:
                costs[p] = cost
                heapq.heappush(open_list, (cost + p.distance(goal), p))


def part1(lines):
    grid = parse_input(lines)
    return find_path(Point(0, 0), Point(len(grid[-1]) - 1, len(grid) - 1), grid)


def inc(i: int, j: int):
    x = i + j
    return x if x <= 9 else (x % 10) + 1


def extend_row(row: list[int]):
    return reduce(
        lambda a, b: a + b, [[inc(val, i) for val in row] for i in range(5)]
    )


def part2(lines):
    grid = parse_input(lines)
    grid = [extend_row(row) for row in grid]
    gg = []
    for i in range(5):
        gg.extend([inc(val, i) for val in row] for row in grid)
    return find_path(Point(0, 0), Point(len(gg[-1]) - 1, len(gg) - 1), gg)


if __name__ == "__main__":
    common.run(15, test_input, 40, test_input, 315, part1, part2)
