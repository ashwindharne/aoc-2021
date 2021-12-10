from collections import deque
import itertools

Point = tuple[int, int]


class HeightMap:
    def __init__(self, input_lines: list[str]):
        self.map = input_lines
        self.max_row = len(self.map) - 1
        self.max_col = len(self.map[0]) - 1

    def is_lowest(self, point: Point) -> bool:
        return all(self.get_height(adj) > self.get_height(point) for adj in self.get_adjacent_points(point))

    def get_height(self, point: Point) -> int:
        return int(self.map[point[0]][point[1]])

    def get_points_in_basin(self, point: Point) -> set[tuple[int, int]]:
        total_basin = set()
        frontier = set()
        frontier.add(point)
        while len(frontier):
            current_point = frontier.pop()
            total_basin.add(current_point)
            for adj_point in self.get_adjacent_points(current_point):
                if self.get_height(adj_point) != 9:
                    if adj_point not in total_basin and adj_point not in frontier:
                        frontier.add(adj_point)
        return total_basin

    def get_adjacent_points(self, point: Point) -> list[tuple[int, int]]:
        adjacent_coords = [
            (point[0] + 1, point[1]),
            (point[0] - 1, point[1]),
            (point[0], point[1] + 1),
            (point[0], point[1] - 1)]
        return list(filter(self.is_valid_point, adjacent_coords))

    def is_valid_point(self, point: Point) -> bool:
        return 0 <= point[0] <= self.max_row and 0 <= point[1] <= self.max_col

    def get_all_basin_points(self) -> set[tuple[int, int]]:
        point_set = set()
        for point in itertools.product(
                list(range(0, self.max_row + 1)),
                list(range(0, self.max_col + 1))):
            if self.get_height(point) != 9:
                point_set.add(point)
        return point_set


def part1(input_file: str) -> int:
    lines = [line.rstrip() for line in open(input_file, 'r', encoding='utf-8')]
    map = HeightMap(lines)
    sum = 0
    for point in itertools.product(
            list(range(0, map.max_row + 1)),
            list(range(0, map.max_col + 1))):
        if map.is_lowest(point):
            sum += 1 + map.get_height(point)
    return sum


def part2(input_file: str) -> int:
    lines = [line.rstrip() for line in open(input_file, 'r', encoding='utf-8')]
    map = HeightMap(lines)
    points_to_flood = map.get_all_basin_points()
    basin_sizes = []
    while len(points_to_flood):
        basin_points = map.get_points_in_basin(points_to_flood.pop())
        basin_sizes.append(len(basin_points))
        points_to_flood -= basin_points
    sorted_basin_sizes = list(sorted(basin_sizes, reverse=True))
    return sorted_basin_sizes[0] * sorted_basin_sizes[1] * sorted_basin_sizes[2]


if __name__ == '__main__':
    input = 'inputs/9.txt'
    print("On the ninth day of Christmas...")
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
