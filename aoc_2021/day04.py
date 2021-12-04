from itertools import count

from aoc_2021 import common

test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"""


def parse_input(lines: list[str]):
    numbers = [int(i) for i in lines.pop(0).split(",")]
    boards = []
    while len(lines) > 0:
        assert lines.pop(0).strip() == ""
        board = []
        for _ in range(5):
            board.append([int(i) for i in lines.pop(0).split()])
        assert len(board) == 5
        boards.append(board)
    return numbers, boards


def check_win(marks):
    for row in marks:
        if all(row):
            return True
    for col in range(5):
        if all(row[col] for row in marks):
            return True
    return False


def draw(number, boards, markers):
    result = []
    for board, marks, idx in zip(boards, markers, count()):
        for row in range(5):
            for col in range(5):
                if board[row][col] == number:
                    marks[row][col] = True
        if check_win(marks):
            result.append(idx)
    return result


def setup(lines):
    numbers, boards = parse_input(lines)
    markers = [[[False] * 5 for _ in range(5)] for _ in range(len(boards))]
    return numbers, boards, markers


def remaining_sum(board, marks):
    result = 0
    for row in range(5):
        for col in range(5):
            if not marks[row][col]:
                result += board[row][col]
    return result


def part1(lines):
    numbers, boards, markers = setup(lines)
    for number in numbers:
        idxs = draw(number, boards, markers)
        if idxs:
            return remaining_sum(boards[idxs[0]], markers[idxs[0]]) * number


def part2(lines):
    numbers, boards, markers = setup(lines)
    for number in numbers:
        idxs = draw(number, boards, markers)
        for idx in sorted(idxs, reverse=True):
            board = boards.pop(idx)
            marks = markers.pop(idx)
            if len(boards) == 0:
                return remaining_sum(board, marks) * number


if __name__ == "__main__":
    common.run(4, test_input, 4512, test_input, 1924, part1, part2)
