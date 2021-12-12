from collections import defaultdict

from aoc_2021 import common

test_input = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""


def parse_input(lines: list[str]):
    connections = defaultdict(set)
    for line in lines:
        a, b = line.strip().split("-")
        connections[a].add(b)
        connections[b].add(a)
    return connections


def continue_path(
    connections, path: tuple[str], visited: set[str], twice_allowed: bool
):
    result = []
    for node in connections[path[-1]]:
        if node == "end":
            result.append(path + (node,))
        elif node.isupper():
            result.extend(
                continue_path(
                    connections, path + (node,), visited, twice_allowed
                ),
            )
        elif node not in visited:
            result.extend(
                continue_path(
                    connections,
                    path + (node,),
                    visited.union((node,)),
                    twice_allowed,
                )
            )
        elif twice_allowed and node != "start":
            result.extend(
                continue_path(
                    connections,
                    path + (node,),
                    visited.union((node,)),
                    False,
                )
            )
    return result


def part1(lines):
    connections = parse_input(lines)
    paths = continue_path(connections, ("start",), set(["start"]), False)
    return len(paths)


def part2(lines):
    connections = parse_input(lines)
    paths = continue_path(connections, ("start",), set(["start"]), True)
    return len(paths)


if __name__ == "__main__":
    common.run(12, test_input, 226, test_input, 3509, part1, part2)
