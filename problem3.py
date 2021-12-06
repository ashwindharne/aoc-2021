def part1(input_file: str) -> int:
    lines = [line.rstrip() for line in open(input_file, 'r')]
    num_lines = len(lines)
    counters = [0] * len(lines[0])
    for line in lines:
        for idx, char in enumerate(line.rstrip()):
            if char == '1':
                counters[idx] += 1
    gamma_str = ''.join(['1' if counter > num_lines /
                        2 else '0' for counter in counters])
    gamma = int(gamma_str, 2)
    epsilon_str = ''.join(['1' if x == '0' else '0' for x in gamma_str])
    epsilon = int(epsilon_str, 2)
    return gamma * epsilon


def part2(input_file: str) -> int:
    lines = [line.rstrip() for line in open(input_file, 'r')]
    o2_indices = list(range(len(lines)))
    co2_indices = o2_indices.copy()
    position = 0
    while len(o2_indices) > 1 and len(co2_indices) > 1:
        o2_bit = most_common_bit_at_position(position, lines, o2_indices)
        o2_indices = drop_indices(position, o2_bit, o2_indices, lines)
        position += 1
    position = 0
    while len(co2_indices) > 1:
        # print(len(co2_indices))
        co2_bit = least_common_bit_at_position(position, lines, co2_indices)
        co2_indices = drop_indices(position, co2_bit, co2_indices, lines)
        position += 1
    return int(lines[o2_indices[0]], 2) * int(lines[co2_indices[0]], 2)


def most_common_bit_at_position(position, lines, indices):
    counter = 0
    for index in indices:
        if lines[index][position] == '1':
            counter += 1
    return '1' if counter >= len(indices)/2 else '0'


def least_common_bit_at_position(position, lines, indices):
    counter = 0
    for index in indices:
        if lines[index][position] == '1':
            counter += 1
    return '0' if counter >= len(indices)/2 else '1'


def drop_indices(position, criteria_bit, indices, lines):
    return list(filter(lambda x: lines[x][position] == criteria_bit, indices))


if __name__ == '__main__':
    input3 = 'inputs/3.txt'
    print("On the third day of Christmas...")
    print(f"Part 1: {part1(input3)}")
    print(f"Part 2: {part2(input3)}")
