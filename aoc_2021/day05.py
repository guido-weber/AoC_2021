from collections import Counter
from dataclasses import dataclass
from typing import Iterable

from aoc_2021 import common

test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


@dataclass(frozen=True)
class Segment:
    x1: int
    y1: int
    x2: int
    y2: int

    @property
    def isHorizontal(self):
        return self.y1 == self.y2

    @property
    def isVertical(self):
        return self.x1 == self.x2

    def points(self):
        dx = 1 if self.x2 > self.x1 else (-1 if self.x1 > self.x2 else 0)
        dy = 1 if self.y2 > self.y1 else (-1 if self.y1 > self.y2 else 0)
        px, py = self.x1, self.y1
        while px != self.x2 or py != self.y2:
            yield (px, py)
            px, py = px + dx, py + dy
        yield (self.x2, self.y2)


def parse_input(lines: list[str]):
    for line in lines:
        p1, _, p2 = line.partition("->")
        yield Segment(
            *map(int, p1.strip().split(",")), *map(int, p2.strip().split(","))
        )


def filter_hv_segments(segments: Iterable[Segment]):
    return filter(lambda seg: seg.isHorizontal or seg.isVertical, segments)


def common_part(lines, filter_func):
    segments = list(filter_func(parse_input(lines)))
    cnt = Counter()
    for seg in segments:
        cnt.update(seg.points())
    return len([(k, v) for k, v in cnt.items() if v >= 2])


def part1(lines):
    return common_part(lines, filter_hv_segments)


def part2(lines):
    return common_part(lines, lambda seg: seg)


if __name__ == "__main__":
    common.run(5, test_input, 5, test_input, 12, part1, part2)
