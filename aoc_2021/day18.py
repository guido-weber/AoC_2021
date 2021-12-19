import functools

from aoc_2021 import common

test_input = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
"""


def parse_input(lines: list[str]):
    return [eval(line.strip()) for line in lines]


@functools.singledispatch
def magnitude(num: int):
    return num


@magnitude.register
def _(num: list):
    return 3 * magnitude(num[0]) + 2 * magnitude(num[1])


@functools.singledispatch
def add_to_right(num: int, to_add: int):
    return True, num + to_add


@add_to_right.register
def _(num: list, to_add: int):
    flag, repl = add_to_right(num[0], to_add)
    if flag:
        return True, [repl, num[1]]
    flag, repl = add_to_right(num[1], to_add)
    if flag:
        return True, [num[0], repl]
    return False, num


@functools.singledispatch
def add_to_left(num: int, to_add: int):
    return True, num + to_add


@add_to_left.register
def _(num: list, to_add: int):
    flag, repl = add_to_left(num[1], to_add)
    if flag:
        return True, [num[0], repl]
    flag, repl = add_to_left(num[0], to_add)
    if flag:
        return True, [repl, num[1]]
    return False, num


@functools.singledispatch
def explode(num: int, _: int):
    return False, num, None, None


@explode.register
def _(num: list, depth: int):
    if depth == 5:
        return True, 0, num[0], num[1]
    else:
        flag, repl, left, right = explode(num[0], depth + 1)
        if flag:
            if right is None:
                return True, [repl, num[1]], left, None
            else:
                added, a_repl = add_to_right(num[1], right)
                return True, [repl, a_repl], left, None if added else right
        flag, repl, left, right = explode(num[1], depth + 1)
        if flag:
            if left is None:
                return True, [num[0], repl], None, right
            else:
                added, a_repl = add_to_left(num[0], left)
                return True, [a_repl, repl], None if added else left, right
        return False, num, None, None


@functools.singledispatch
def split(num: int):
    if num >= 10:
        left = num // 2
        return True, [left, num - left]
    return False, num


@split.register
def _(num: list):
    done, repl = split(num[0])
    if done:
        return True, [repl, num[1]]
    done, repl = split(num[1])
    if done:
        return True, [num[0], repl]
    return False, num


def sf_add(num1: list, num2: list):
    num = [num1, num2]
    done = False
    while not done:
        exploded, num, _, _ = explode(num, 1)
        if not exploded:
            splitted, num = split(num)
        done = not exploded and not splitted
    return num


def part1(lines):
    numbers = parse_input(lines)
    num = functools.reduce(sf_add, numbers)
    return magnitude(num)


def part2(lines):
    numbers = parse_input(lines)
    mm = 0
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                mm = max(mm, magnitude(sf_add(numbers[i], numbers[j])))
    return mm


if __name__ == "__main__":
    x = magnitude(
        eval("[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]")
    )
    assert x == 4140, x
    common.run(18, test_input, 4140, test_input, 3993, part1, part2)
