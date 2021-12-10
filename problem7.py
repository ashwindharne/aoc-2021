from typing import Callable


def cost_to_move(current_positions: list[int], position: int, cost_fn: Callable[[int, int], int]) -> int:
    return sum([cost_fn(position, x) for x in current_positions])


def linearly_increasing_cost(a: int, b: int) -> int:
    distance = abs(a - b)
    return int((distance / 2) * (1 + distance))


def part1(input_file: str) -> int:
    line = [line.rstrip() for line in open(input_file, 'r', encoding='utf-8')]
    positions = [int(x) for x in line[0].split(',')]
    min_position = min(positions)
    max_position = max(positions)
    costs_to_move = []
    for position in range(min_position, max_position + 1):
        costs_to_move.append(cost_to_move(
            positions, position, lambda x, y: abs(x - y)))
    return min(costs_to_move)


def part2(input_file: str) -> int:
    line = [line.rstrip() for line in open(input_file, 'r', encoding='utf-8')]
    positions = [int(x) for x in line[0].split(',')]
    min_position = min(positions)
    max_position = max(positions)
    costs_to_move = []
    for position in range(min_position, max_position + 1):
        costs_to_move.append(cost_to_move(
            positions, position, linearly_increasing_cost))
    return min(costs_to_move)


if __name__ == '__main__':
    input = 'inputs/7.txt'
    print("On the seventh day of Christmas...")
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
