from aoc_2021 import common

test_input = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""


def parse_input(lines: list[str]):
    tr = {ord("."): "0", ord("#"): "1"}
    enhancement = lines[0].strip().translate(tr)
    assert len(enhancement) == 512
    grid = [line.strip().translate(tr) for line in lines[2:]]
    assert len(grid) == len(grid[0])
    return enhancement, grid


def blowup(grid: list[str], by: int):
    w = len(grid[0]) + 2 * by
    return (
        ["0" * w for _ in range(by)]
        + ["0" * by + line + "0" * by for line in grid]
        + ["0" * w for _ in range(by)]
    )


def enhance_point(enhancement: str, grid: list[str], x: int, y: int):
    s = (
        grid[y - 1][x - 1 : x + 2]
        + grid[y][x - 1 : x + 2]
        + grid[y + 1][x - 1 : x + 2]
    )
    assert len(s) == 9
    idx = int(s, base=2)
    return enhancement[idx]


def enhance(enhancement: str, grid: list[str], offset: int):
    border = enhancement[0 if grid[0][0] == "0" else -1]
    return (
        [border * len(grid[0]) for _ in range(offset)]
        + [
            border * offset
            + "".join(
                enhance_point(enhancement, grid, x, y + offset)
                for x in range(offset, len(row) - offset)
            )
            + border * offset
            for y, row in enumerate(grid[offset:-offset])
        ]
        + [border * len(grid[0]) for _ in range(offset)]
    )


def doit(lines, runs):
    enhancement, grid = parse_input(lines)
    grid = blowup(grid, runs + 1)
    for run in range(runs):
        grid = enhance(enhancement, grid, runs - run)
    return sum(sum(int(c) for c in row) for row in grid)


def part1(lines):
    return doit(lines, 2)


def part2(lines):
    return doit(lines, 50)


if __name__ == "__main__":
    common.run(20, test_input, 35, test_input, 3351, part1, part2)
