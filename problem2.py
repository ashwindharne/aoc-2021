
def part1(input_file: str) -> int:
    horizontal = 0
    depth = 0
    f = open(input_file)
    instructions = [(x.split(' ')[0], int(x.split(' ')[1]))
                    for x in f.readlines()]
    for dir, val in instructions:
        if dir == 'forward':
            horizontal += val
        elif dir == 'down':
            depth += val
        elif dir == 'up':
            depth -= val
        else:
            print('panic!')
    return horizontal * depth


def part2(input_file: str) -> int:
    horizontal = 0
    depth = 0
    aim = 0
    f = open(input_file)
    instructions = [(x.split(' ')[0], int(x.split(' ')[1]))
                    for x in f.readlines()]
    for dir, val in instructions:
        if dir == 'forward':
            horizontal += val
            depth += aim * val
        elif dir == 'down':
            aim += val
        elif dir == 'up':
            aim -= val
        else:
            print('panic!')
    return horizontal * depth


if __name__ == '__main__':
    print('On the second day of Christmas...')
    input2 = 'inputs/2.txt'
    print(f"Part 1: {part1(input2)}")
    print(f"Part 2: {part2(input2)}")
