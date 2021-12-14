from collections import Counter

from aoc_2021 import common

test_input = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""


def parse_input(lines: list[str]):
    rules = {}
    for line in lines[2:]:
        a, b = line.strip().split(" -> ")
        rules[a] = b
    return lines[0].strip(), rules


rules: dict[str, str] = {}
cache: dict[tuple[str, int], Counter[str]] = {}
empty: Counter[str] = Counter()


def expand(pattern: str, cycles: int):
    global rules, cache, empty
    repl = rules.get(pattern)
    if repl is None:
        return empty
    key = (pattern, cycles)
    cnt = cache.get(key)
    if cnt is not None:
        return cnt
    cnt = Counter({repl: 1})
    if cycles > 1:
        cnt += expand(pattern[0] + repl, cycles - 1)
        cnt += expand(repl + pattern[1], cycles - 1)
    cache[key] = cnt
    return cnt


def common_part(lines, cycles):
    global rules, cache
    polymer, rules = parse_input(lines)
    cache = {}
    cnt = Counter(polymer)
    while len(polymer) >= 2:
        cnt += expand(polymer[0:2], cycles)
        polymer = polymer[1:]
    counts = cnt.most_common()
    return counts[0][1] - counts[-1][1]


def part1(lines):
    return common_part(lines, 10)


def part2(lines):
    return common_part(lines, 40)


if __name__ == "__main__":
    common.run(14, test_input, 1588, test_input, 2188189693529, part1, part2)
