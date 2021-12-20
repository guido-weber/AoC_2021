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
    return (
        grid[:offset]
        + [
            "0" * offset
            + "".join(
                enhance_point(enhancement, grid, x, y + offset)
                for x in range(offset, len(row) - offset)
            )
            + "0" * offset
            for y, row in enumerate(grid[offset:-offset])
        ]
        + grid[-offset:]
    )


def print_grid(grid):
    print(
        "\n".join(
            row.translate({ord("0"): ".", ord("1"): "#"}) for row in grid[-5:]
        )
        + "\n"
    )


def part1(lines):
    enhancement, grid = parse_input(lines)
    runs = 2
    grid = blowup(grid, runs + 1)
    print_grid(grid)
    for run in range(runs):
        grid = enhance(enhancement, grid, runs - run)
        print_grid(grid)
    return sum(sum(int(c) for c in row) for row in grid)


def part2(lines):
    pass


if __name__ == "__main__":
    common.run(20, test_input, 35, test_input, 42, part1, part2)
