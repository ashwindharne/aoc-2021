
class BingoBoard:
    def __init__(self, list_of_rows: list[str]):
        self.done = False
        int_rows = [[int(x) for x in row.split()] for row in list_of_rows]
        self.sum = sum([sum(row) for row in int_rows])
        self.rows = [set(nums) for nums in int_rows]
        self.cols = [set() for _ in range(len(int_rows[0]))]
        for row in int_rows:
            for idx, num in enumerate(row):
                self.cols[idx].add(num)
        
    def mark_num(self, num: int) -> bool:
        """
        Marks the given number on the board. Returns whether the board is "done" or not.
        """
        for row in self.rows:
            if num in row:
                row.remove(num)
                self.sum -= num
                if not len(row):
                    self.done = True
        for col in self.cols:
            if num in col:
                col.remove(num)
                if not len(col):
                    self.done = True
        return self.done
    
    def unmarked_sum(self) -> int:
        """
        Returns the sum of all the unmarked numbers on the board
        """
        return self.sum

def construct_boards(lines: list[str]) -> list[BingoBoard]:
    """
    Constructs a list of BingoBoards from the given lines. The first line must contain numbers.
    """
    line_buf = []
    boards = []
    for line in lines:
        if line != '':
            line_buf.append(line)
        else:
            boards.append(BingoBoard(line_buf))
            line_buf.clear()
    return boards


def part1(input_file: str) -> int:
    lines = [line.rstrip() for line in open(input_file, 'r').readlines()]
    numbers_drawn = [int(x) for x in lines[0].split(',')]
    bingo_boards = construct_boards(lines[2:])
    for num in numbers_drawn:
        for board in bingo_boards:
            if board.mark_num(num):
                return num * board.unmarked_sum()
    return 0


def part2(input_file: str) -> int:
    lines = [line.rstrip() for line in open(input_file, 'r').readlines()]
    numbers_drawn = [int(x) for x in lines[0].split(',')]
    bingo_boards = construct_boards(lines[2:])
    last_score = 0
    for num in numbers_drawn:
        for idx, board in enumerate(bingo_boards):
            if board.mark_num(num):
                last_score = num * board.unmarked_sum()
        bingo_boards = [board for board in bingo_boards if not board.done]
    return last_score
        

if __name__ == '__main__':
    input = 'inputs/4.txt'
    print("On the fourth day of Christmas...")
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")