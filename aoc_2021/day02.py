import io
from dataclasses import dataclass
from functools import reduce


def read_input():
    with io.open("input/day02") as f:
        return f.read()


@dataclass(frozen=True)
class Command:
    direction: str
    units: int


@dataclass(frozen=True)
class Location1:
    position: int = 0
    depth: int = 0

    def cmd_forward(self, amount: int):
        return Location1(self.position + amount, self.depth)

    def cmd_up(self, amount: int):
        return Location1(self.position, self.depth - amount)

    def cmd_down(self, amount: int):
        return Location1(self.position, self.depth + amount)

    def __add__(self, cmd: Command):
        return getattr(self, "cmd_" + cmd.direction)(cmd.units)


@dataclass(frozen=True)
class Location2:
    position: int = 0
    depth: int = 0
    aim: int = 0

    def cmd_forward(self, amount: int):
        return Location2(
            self.position + amount, self.depth + self.aim * amount, self.aim
        )

    def cmd_up(self, amount: int):
        return Location2(self.position, self.depth, self.aim - amount)

    def cmd_down(self, amount: int):
        return Location2(self.position, self.depth, self.aim + amount)

    def __add__(self, cmd: Command):
        return getattr(self, "cmd_" + cmd.direction)(cmd.units)


def commands_from_input(input: str):
    return [
        Command(d, int(u))
        for d, u in (line.split() for line in input.splitlines())
    ]


def day02_1(input: str):
    commands = commands_from_input(input)
    final_location = reduce(lambda loc, cmd: loc + cmd, commands, Location1())
    return final_location.position * final_location.depth


def day02_2(input: str):
    commands = commands_from_input(input)
    final_location = reduce(lambda loc, cmd: loc + cmd, commands, Location2())
    return final_location.position * final_location.depth


if __name__ == "__main__":
    input = read_input()
    print(day02_1(input))
    print(day02_2(input))
