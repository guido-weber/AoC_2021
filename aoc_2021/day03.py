import io
from collections import Counter
from typing import Iterable


def read_input():
    with io.open("input/day03") as f:
        return f.read()


def most_common(bits: Iterable[str]):
    c = Counter(bits)
    return "0" if c["0"] > c["1"] else "1"


def least_common(bits: Iterable[str]):
    c = Counter(bits)
    return "1" if c["1"] < c["0"] else "0"


def invert(bits: str):
    return "".join("0" if b == "1" else "1" for b in bits)


def day03_1(input: str):
    lines = input.splitlines()
    gamma = "".join(most_common(bits) for bits in zip(*lines))
    epsilon = invert(gamma)
    return int(gamma, 2) * int(epsilon, 2)


def select_line(lines: list[str], crit):
    prefix = ""
    while len(lines) > 1:
        pl = len(prefix)
        prefix += crit(line[pl] for line in lines)
        lines = [line for line in lines if line.startswith(prefix)]
    return int(lines[0], 2)


def day03_2(input: str):
    lines = input.splitlines()
    oxy = select_line(lines, most_common)
    co2 = select_line(lines, least_common)
    return oxy * co2


if __name__ == "__main__":
    input = read_input()
    print(day03_1(input))
    print(day03_2(input))
