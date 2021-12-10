from aoc_2021 import common

test_input = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


def parse_input(lines: list[str]):
    pass


CLOSING = {")": "(", "]": "[", "}": "{", ">": "<"}
OPENING = {v: k for k, v in CLOSING.items()}


def analyze(line: str):
    POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}
    still_open = ""
    for c in line:
        if c in CLOSING:
            if len(still_open) == 0 or still_open[-1] != CLOSING[c]:
                return "", POINTS[c]
            else:
                still_open = still_open[:-1]
        else:
            still_open += c
    return still_open, 0


def part1(lines):
    return sum(analyze(line)[1] for line in lines)


def completion(chunk: str):
    POINTS = {")": 1, "]": 2, "}": 3, ">": 4}
    result = 0
    for cc in (OPENING[c] for c in reversed(chunk.strip())):
        result = 5 * result + POINTS[cc]
    return result


def part2(lines):
    scores = []
    for line in lines:
        still_open, points = analyze(line)
        if len(still_open) > 0 and points == 0:
            scores.append(completion(still_open))
    scores.sort()
    return scores[len(scores) // 2]


if __name__ == "__main__":
    common.run(10, test_input, 26397, test_input, 288957, part1, part2)
