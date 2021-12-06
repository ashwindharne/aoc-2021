def part1(input_file: str) -> int:
    counter = 0
    prev = float('inf')
    with open(input_file, 'r') as f:
        for line in f:
            curr = int(line)
            if curr > prev:
                counter += 1
            prev = curr
    return counter


def part2(input_file: str) -> int:
    counter = 0
    with open(input_file, 'r') as f:
        lines = f.readlines()
        window = [int(x) for x in lines[0:3]]
        window_sum = sum(window)
        for line in lines[3:]:
            new_val = int(line)
            new_sum = window_sum - window[0] + new_val
            if new_sum > window_sum:
                counter += 1
            window.pop(0)
            window.append(new_val)
    return counter


if __name__ == '__main__':
    input1 = 'inputs/1.txt'
    print("On the first day of Christmas...")
    print(f"Part 1: {part1(input1)}")
    print(f"Part 2: {part2(input1)}")
