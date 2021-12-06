from enum import Enum
from dataclasses import dataclass
from collections import defaultdict


@dataclass(eq=True, frozen=True)
class Point:
    x: int
    y: int


class Orientation(Enum):
    HORIZONTAL = 1
    VERTICAL = 2
    DIAGONAL = 3


def bidirectional_range(start, stop):
    if start < stop:
        return list(range(start, stop + 1))
    return reversed(list(range(stop, start + 1)))


class VentLine:
    @classmethod
    def from_str(self, s: str):
        split_s = s.split(' ')
        a_list = [int(x) for x in split_s[0].split(',')]
        b_list = [int(x) for x in split_s[2].split(',')]
        return VentLine(Point(a_list[0], a_list[1]), Point(b_list[0], b_list[1]))

    def __init__(self, point_a: Point, point_b: Point):
        self.a: Point = point_a
        self.b: Point = point_b
        if self.a.x == self.b.x:
            self.orientation = Orientation.HORIZONTAL
        elif self.a.y == self.b.y:
            self.orientation = Orientation.VERTICAL
        else:
            self.orientation = Orientation.DIAGONAL

    def points_covered(self) -> list[Point]:
        """
        Returns a list of points that are covered by this line. Only supports horizontal and vertical lines (for now).
        """
        if self.orientation == Orientation.HORIZONTAL:
            return [Point(self.a.x, y) for y in bidirectional_range(self.a.y, self.b.y)]
        elif self.orientation == Orientation.VERTICAL:
            return [Point(x, self.a.y) for x in bidirectional_range(self.a.x, self.b.x)]
        else:
            return [Point(x, y) for x, y in list(zip(bidirectional_range(self.a.x, self.b.x), bidirectional_range(self.a.y, self.b.y)))]


class VentField:
    def __init__(self):
        self.vents: defaultdict[Point, int] = defaultdict(int)
        self.points_of_interest: set[Point] = set()

    def add_line(self, line: VentLine, include_diagonals=False):
        if line.orientation == Orientation.DIAGONAL and not include_diagonals:
            return
        for point in line.points_covered():
            self.vents[point] += 1
            if self.vents[point] >= 2:
                self.points_of_interest.add(point)


def part1(input_file: str) -> int:
    lines = [line.rstrip() for line in open(input_file, 'r', encoding='utf-8')]
    field = VentField()
    for line in lines:
        vent_line = VentLine.from_str(line)
        field.add_line(vent_line)
    return len(field.points_of_interest)


def part2(input_file: str) -> int:
    lines = [line.rstrip() for line in open(input_file, 'r')]
    field = VentField()
    for line in lines:
        vent_line = VentLine.from_str(line)
        field.add_line(vent_line, include_diagonals=True)
    return len(field.points_of_interest)


if __name__ == '__main__':
    input = 'inputs/5.txt'
    print("On the fifth day of Christmas...")
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
