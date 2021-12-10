NUM_SEGMENTS_TO_NUM = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}


def construct_num_mapping(scrambled_ten: list[str]) -> list[int]:
    num_mapping: dict[int, set[str]] = {}
    five_seg_nums = []
    six_seg_nums = []
    # Get the sets for one, four, seven, eight. Build lists for 2,3,5 and 0,6,9
    for num in scrambled_ten:
        if len(num) in NUM_SEGMENTS_TO_NUM:
            num_mapping[NUM_SEGMENTS_TO_NUM[len(num)]] = set(num)
        elif len(num) == 5:
            five_seg_nums.append(set(num))
        elif len(num) == 6:
            six_seg_nums.append(set(num))
    for num_set in six_seg_nums:
        # Identify 6 as the 6 segment number that doesn't have 1 as a subset
        if not num_mapping[1].issubset(num_set):
            num_mapping[6] = num_set
        # Identify 9 as the only  6 segment number that has 4 as a subset
        elif num_mapping[4].issubset(num_set):
            num_mapping[9] = num_set
        # Identify zero as the only remaining 6 segment number
        else:
            num_mapping[0] = num_set
    for num_set in five_seg_nums:
        # Identify 3 as the 5 segment number that has 1 as a subset
        if num_mapping[1].issubset(num_set):
            num_mapping[3] = num_set
        # Identify 5 as the 5 segment number that is a subset of 6
        elif num_set.issubset(num_mapping[6]):
            num_mapping[5] = num_set
        # Identify two as the only remaining 5 segment number
        else:
            num_mapping[2] = num_set
    return [''.join(sorted(list(x))) for x in [num_mapping[x] for x in range(0, 10)]]


def part1(input_file: str) -> int:
    lines = [line.rstrip() for line in open(input_file, 'r', encoding='utf-8')]
    counter = 0
    for line in lines:
        _, last_four = line.split('|')
        last_four = last_four.split()
        for num in last_four:
            if len(num) in NUM_SEGMENTS_TO_NUM:
                counter += 1
    return counter


def part2(input_file: str) -> int:
    lines = [line.rstrip() for line in open(input_file, 'r', encoding='utf-8')]
    sum = 0
    for line in lines:
        first_ten, last_four = line.split('|')
        first_ten = first_ten.split()
        last_four = last_four.split()
        num_mapping = construct_num_mapping(first_ten)
        sum += int(''.join([str(num_mapping.index(''.join(sorted(x))))
                   for x in last_four]))
    return sum


if __name__ == '__main__':
    input = 'inputs/8.txt'
    print("On the eigth day of Christmas...")
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
