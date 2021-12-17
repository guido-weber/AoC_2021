import re

from aoc_2021 import common

test_input = """target area: x=20..30, y=-10..-5
"""


def parse_input(lines: list[str]):
    m = re.match(
        r"target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)", lines[0]
    )
    assert m is not None
    xmin = min(int(m.group(1)), int(m.group(2)))
    xmax = max(int(m.group(1)), int(m.group(2)))
    ymin = min(int(m.group(3)), int(m.group(4)))
    ymax = max(int(m.group(3)), int(m.group(4)))
    return (xmin, xmax, ymin, ymax)


def part1(lines):
    """
    Assuming the target area is below y=0, and that any x velocity exixts that
    hits the area:
    - x component can be ignored completely
    - max hight is reached by having the max possible y velocity
    - downward path always has an y=0 point with y velocity = -initial_velocity
    - to hit the target area, we aim at the lower border: increasing velocity
      once again, this means velocity for this step = min y of target area
    - i.v. must therefore be abs(min y of target area) - 1
    - sum(1..N) = N * (N + 1) / 2
    """
    _, _, ymin, _ = parse_input(lines)
    return abs(ymin) * (abs(ymin) - 1) // 2


def xvelocities(xmin: int, xmax: int, max_steps: int):
    for iv in range(1, xmax + 1):
        x, v, steps = 0, iv, 0
        while steps < max_steps and x < xmax:
            steps += 1
            x += v
            if v > 0:
                v -= 1
            if x >= xmin and x <= xmax:
                yield (steps, x, iv)


def yvelocities(ymin: int, ymax: int):
    for iv in range(ymin, abs(ymin) + 1):
        y, v, steps = 0, iv, 0
        while y >= ymin:
            steps += 1
            y += v
            v -= 1
            if y >= ymin and y <= ymax:
                yield (steps, y, iv)


def part2(lines):
    xmin, xmax, ymin, ymax = parse_input(lines)
    yvs = list(yvelocities(ymin, ymax))
    max_steps = max(yv[0] for yv in yvs)
    xvs = list(xvelocities(xmin, xmax, max_steps))
    ivs = set()
    for xv in xvs:
        for yv in yvs:
            if yv[0] == xv[0]:
                ivs.add((xv[2], yv[2]))
    return len(ivs)


if __name__ == "__main__":
    common.run(17, test_input, 45, test_input, 112, part1, part2)
