import dataclasses
import functools

from aoc_2021 import common

test_input = """8A004A801A8002F478
620080001611562C8802118E34
C0015000016115A2E0802F182340
A0016C880162017C3686B18A3D4780
"""


@dataclasses.dataclass
class Packet:
    version: int
    typeID: int

    def version_sum(self):
        return self.version

    def read_from_string(self, s: str):
        raise NotImplementedError()

    def compute_value(self):
        raise NotImplementedError()


@dataclasses.dataclass
class LiteralPacket(Packet):
    value: int = 0

    def compute_value(self):
        return self.value

    def read_from_string(self, s: str):
        done = False
        binstr = ""
        while not done:
            binstr += s[1:5]
            done = s.startswith("0")
            s = s[5:]
        self.value = int(binstr, base=2)
        return s


@dataclasses.dataclass
class OperatorPacket(Packet):
    sub_packets: list[Packet] = dataclasses.field(default_factory=list)

    def version_sum(self):
        return self.version + sum(
            pkg.version_sum() for pkg in self.sub_packets
        )

    def compute_value(self):
        sub_values = (p.compute_value() for p in self.sub_packets)
        if self.typeID == 0:
            return sum(sub_values)
        elif self.typeID == 1:
            return functools.reduce(lambda a, b: a * b, sub_values)
        elif self.typeID == 2:
            return min(sub_values)
        elif self.typeID == 3:
            return max(sub_values)
        elif self.typeID == 5:
            i, j = list(sub_values)
            return 1 if i > j else 0
        elif self.typeID == 6:
            i, j = list(sub_values)
            return 1 if i < j else 0
        elif self.typeID == 7:
            i, j = list(sub_values)
            return 1 if i == j else 0

    def read_from_string(self, s: str):
        # length type ID
        if s.startswith("0"):
            bit_length = int(s[1:16], 2)
            s = s[16:]
            remaining_length = len(s) - bit_length
            while len(s) > remaining_length:
                pkg, s = packet_from_string(s)
                self.sub_packets.append(pkg)
        else:
            num_sub_pkgs = int(s[1:12], 2)
            s = s[12:]
            for _ in range(num_sub_pkgs):
                pkg, s = packet_from_string(s)
                self.sub_packets.append(pkg)
        return s


def packet_from_string(s: str):
    version = int(s[0:3], base=2)
    typeID = int(s[3:6], base=2)
    packet_cls = LiteralPacket if typeID == 4 else OperatorPacket
    packet = packet_cls(version, typeID)
    rest = packet.read_from_string(s[6:])
    return packet, rest


def parse_input(lines: list[str]):
    binary = [
        "".join("{0:04b}".format(int(c, base=16)) for c in line.strip())
        for line in lines
    ]
    return [packet_from_string(binstr)[0] for binstr in binary]


def part1(lines):
    packets = parse_input(lines)
    return sum(pkg.version_sum() for pkg in packets)


def part2(lines):
    packets = parse_input(lines)
    return sum(pkg.compute_value() for pkg in packets)


if __name__ == "__main__":
    common.run(16, test_input, 16 + 12 + 23 + 31, test_input, 161, part1, part2)
