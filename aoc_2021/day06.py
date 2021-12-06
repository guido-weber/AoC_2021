from collections import Counter, defaultdict

from aoc_2021 import common

test_input = """3,4,3,1,2"""


def parse_input(lines: list[str]):
    return dict(Counter(int(i) for i in lines[0].split(",")))


def cycle(cur):
    next = defaultdict(int)
    for i in range(1, 9):
        next[i - 1] = cur[i] if i in cur else 0
    if 0 in cur:
        next[8] += cur[0]
        next[6] += cur[0]
    return next


def do_generations(lines, generations):
    population = parse_input(lines)
    for _ in range(generations):
        population = cycle(population)
    return sum(population.values())


def part1(lines):
    return do_generations(lines, 80)


def part2(lines):
    return do_generations(lines, 256)


if __name__ == "__main__":
    common.run(6, test_input, 5934, test_input, 26984457539, part1, part2)
