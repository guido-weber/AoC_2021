import io


def read_input():
    with io.open("input/day01") as f:
        return [int(line) for line in f.readlines()]


def count_increasing(data_points):
    return sum(1 if a < b else 0 for a, b in zip(data_points, data_points[1:]))


def day01_1():
    return count_increasing(read_input())


def day01_2():
    measurements = read_input()
    windows = [
        a + b + c
        for a, b, c in zip(measurements, measurements[1:], measurements[2:])
    ]
    return count_increasing(windows)


if __name__ == "__main__":
    print(day01_1())
    print(day01_2())
