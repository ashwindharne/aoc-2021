from collections import deque

END_BRACKET_SCORES = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

COMPLETION_SCORES = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

BRACKET_MATCHES = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

def corruption_score(chunk: str) -> int:
    stack = deque()
    for bracket in chunk:
        if bracket in BRACKET_MATCHES:
            stack.append(bracket)
        elif BRACKET_MATCHES[stack.pop()] != bracket:
            return END_BRACKET_SCORES[bracket]
    return 0

def completion_score(chunk: str) -> int:
    stack = deque()
    for bracket in chunk:
        if bracket in BRACKET_MATCHES:
            stack.append(bracket)
        else:
            stack.pop()
    score = 0
    while len(stack):
        score *= 5
        score += COMPLETION_SCORES[BRACKET_MATCHES[stack.pop()]]
    return score

def part1(input_file: str) -> int:
    chunks = [line.rstrip() for line in open(input_file, 'r', encoding='utf-8')]
    return sum(corruption_score(chunk) for chunk in chunks)


def part2(input_file: str) -> int:
    chunks = [line.rstrip() for line in open(input_file, 'r', encoding='utf-8')]
    valid_chunks = list(filter(lambda chunk: not corruption_score(chunk), chunks))
    completion_scores = list(sorted([completion_score(chunk) for chunk in valid_chunks]))
    return completion_scores[len(completion_scores)//2]


if __name__ == '__main__':
    input = 'inputs/10.txt'
    print("On the tenth day of Christmas...")
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
