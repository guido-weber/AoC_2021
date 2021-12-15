import io
import os.path
import sys


def get_input(day):
    fname = os.path.join("input", "day%02d" % day)
    with io.open(fname) as f:
        return f.readlines()


def check(msg, v1, v2):
    if v1 == v2:
        print("Check %s OK: %s" % (msg, v1))
    else:
        print("Check %s failed: %s != %s" % (msg, v1, v2))
        sys.exit(1)


def run(
    day: int,
    test_input1: str,
    test_result1,
    test_input2: str,
    test_result2,
    part1,
    part2,
):
    check(1, part1(test_input1.splitlines()), test_result1)
    print("Part1: %s" % part1(get_input(day)))
    check(2, part2(test_input2.splitlines()), test_result2)
    print("Part2: %s" % part2(get_input(day)))
