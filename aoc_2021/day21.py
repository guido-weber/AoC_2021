from itertools import cycle

from aoc_2021 import common

test_input = """Player 1 starting position: 4
Player 2 starting position: 8
"""


def parse_input(lines: list[str]):
    p1_start = int(lines[0].strip().split()[-1])
    p2_start = int(lines[1].strip().split()[-1])
    return [p1_start - 1, p2_start - 1]


class DeterministicDie100:
    def __init__(self) -> None:
        self.rolls = 0
        self._source = cycle(range(1, 101))

    def roll3(self):
        self.rolls += 3
        return sum(next(self._source) for _ in range(3))


def part1(lines):
    positions = parse_input(lines)
    scores = [0, 0]
    cur_player = 0
    die = DeterministicDie100()
    while True:
        steps = die.roll3()
        positions[cur_player] = (positions[cur_player] + steps) % 10
        scores[cur_player] += positions[cur_player] + 1
        if scores[cur_player] >= 1000:
            return scores[1 - cur_player] * die.rolls
        else:
            cur_player = 1 - cur_player


DiracRolls = ((3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1))


def p2_step(positions: list[int], scores: list[int], cur_player: int):
    pp = positions[:]
    ss = scores[:]
    wins = [0, 0]
    for steps, cnt in DiracRolls:
        pp[cur_player] = (positions[cur_player] + steps) % 10
        ss[cur_player] = scores[cur_player] + pp[cur_player] + 1
        if ss[cur_player] >= 21:
            wins[cur_player] += cnt
        else:
            w0, w1 = p2_step(pp, ss, 1 - cur_player)
            wins[0] += w0 * cnt
            wins[1] += w1 * cnt
    return wins


def part2(lines):
    positions = parse_input(lines)
    scores = [0, 0]
    w1, w2 = p2_step(positions, scores, 0)
    return max(w1, w2)


if __name__ == "__main__":
    common.run(
        21, test_input, 739785, test_input, 444356092776315, part1, part2
    )
