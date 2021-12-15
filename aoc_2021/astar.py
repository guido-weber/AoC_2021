import heapq
from dataclasses import dataclass
from typing import Any

input = """1163751742
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


@dataclass(frozen=True, order=True)
class Point:
    x: int
    y: int

    def distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)


@dataclass
class Node:
    p: Point
    g: int
    h: int

    @property
    def f(self):
        return self.g + self.h


def parse_input(s: str):
    return [[int(c) for c in line] for line in s.splitlines()]


def neighbours(p: Point, grid: list[list[Any]]):
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

    """
    def best_candidate():
        result, best_score = None, None
        for p in open_set:
            score = costs[p] + p.distance(goal)
            if best_score is None or score < best_score:
                best_score = score
                result = p
        open_set.remove(p)
        return result
    """
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
                heapq.heappush(open_list, (p.distance(goal), p))


if __name__ == "__main__":
    grid = parse_input(input)
    result = find_path(
        Point(0, 0), Point(len(grid[-1]) - 1, len(grid) - 1), grid
    )
