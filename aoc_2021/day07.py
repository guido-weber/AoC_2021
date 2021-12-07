from aoc_2021 import common

test_input = """16,1,2,0,4,2,7,1,2,14"""


def parse_input(lines: list[str]):
    return [int(i) for i in lines[0].split(",")]


def common_part(lines, costfunc):
    positions = sorted(parse_input(lines))
    best = None
    for pos in range(min(positions), max(positions) + 1):
        cost = sum(
            costfunc(abs(pos - p))
            for p in filter(lambda x: x != pos, positions)
        )
        if best is None or cost < best:
            best = cost
        elif cost > best:
            return best
    return cost


def part1(lines):
    return common_part(lines, lambda x: x)


def part2(lines):
    return common_part(lines, lambda x: x * (x + 1) // 2)


if __name__ == "__main__":
    common.run(7, test_input, 37, test_input, 168, part1, part2)
