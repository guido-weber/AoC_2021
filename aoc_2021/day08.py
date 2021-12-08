from functools import reduce

from aoc_2021 import common

test_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


def parse_input(lines: list[str]):
    tpls = ((a, b) for a, _, b in (line.partition(" | ") for line in lines))
    return [(a.split(), b.split()) for a, b in tpls]


def part1(lines):
    result = 0
    for _, outputs in parse_input(lines):
        result += sum(1 if len(o) in (2, 3, 4, 7) else 0 for o in outputs)
    return result


def decode(patterns: list[frozenset[str]]):
    (cf,) = filter(lambda x: len(x) == 2, patterns)  # one
    (acf,) = filter(lambda x: len(x) == 3, patterns)  # seven
    (bcdf,) = filter(lambda x: len(x) == 4, patterns)  # four
    n6 = frozenset(filter(lambda x: len(x) == 6, patterns))
    eight = frozenset("abcdefg")
    a = acf - cf
    cde = eight - reduce(lambda p1, p2: p1 & p2, n6)
    c = cf & cde
    f = cf - c
    bf = bcdf - cde
    b = bf - f
    e = cde - bcdf
    d = cde - c - e
    g = eight - a - b - c - d - e - f
    return {
        a | b | c | e | f | g: "0",
        cf: "1",
        a | c | d | e | g: "2",
        a | c | d | f | g: "3",
        bcdf: "4",
        a | b | d | f | g: "5",
        a | b | d | e | f | g: "6",
        acf: "7",
        eight: "8",
        a | b | c | d | f | g: "9",
    }


def part2(lines):
    result = 0
    for patterns, outputs in parse_input(lines):
        codes = decode([frozenset(p) for p in patterns])
        result += int("".join([codes[frozenset(o)] for o in outputs]))
    return result


if __name__ == "__main__":
    common.run(8, test_input, 26, test_input, 61229, part1, part2)
