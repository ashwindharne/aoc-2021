import itertools
OctoLocation = tuple[int, int]

class FlashyOctoGrid:
    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        self.num_rows = len(self.grid)
        self.num_cols = len(self.grid[0])
    
    @classmethod
    def from_lines(self, lines: list[str]):
        grid = [[int(e) for e in line] for line in lines]
        return FlashyOctoGrid(grid)

    def step(self):
        all_locs = itertools.product(range(0, len(self.grid)), range(0, len(self.grid[0])))
        flashed = set()
        to_flash = set()
        # Increase the energy levels of all the octopi by 1.
        for loc in all_locs:
            if self.increment_energy(loc):
                to_flash.add(loc)
        flash_counter = 0
        while to_flash:
            flash_loc = to_flash.pop()
            adjacent_octopi = self.get_adjacent_octopi(flash_loc)
            self.flash(flash_loc)
            for adj in adjacent_octopi:
                if adj not in flashed and adj not in to_flash:
                    if self.increment_energy(adj):
                        to_flash.add(adj)
            flashed.add(flash_loc)
            flash_counter += 1
        return flash_counter

    def increment_energy(self, loc: OctoLocation) -> bool:
        """
        Increments the energy of the octopus at `loc`. Returns whether or not the 
        Octopus should flash this step.
        """
        self.grid[loc[0]][loc[1]] += 1
        return self.grid[loc[0]][loc[1]] > 9

    def flash(self, loc: OctoLocation):
        self.grid[loc[0]][loc[1]] = 0
    
    def get_adjacent_octopi(self, loc: OctoLocation) -> set[OctoLocation]:
        adjacent_locs = [
            (loc[0] - 1, loc[1] - 1),
            (loc[0] - 1, loc[1]),
            (loc[0] - 1, loc[1] + 1),
            (loc[0], loc[1] + 1),
            (loc[0] + 1, loc[1] + 1),
            (loc[0] + 1, loc[1]),
            (loc[0] + 1, loc[1] -1),
            (loc[0], loc[1] - 1)]
        return set(loc for loc in adjacent_locs if self.is_valid_loc(loc))

    def is_valid_loc(self, loc: OctoLocation):
        return 0 <= loc[0] < self.num_rows and 0 <= loc[1] < self.num_cols
        


def part1(input_file: str) -> int:
    lines = [line.rstrip() for line in open(input_file, 'r', encoding='utf-8')]
    grid = FlashyOctoGrid.from_lines(lines)
    return sum([grid.step() for _ in range(100)])


def part2(input_file: str) -> int:
    lines = [line.rstrip() for line in open(input_file, 'r', encoding='utf-8')]
    grid = FlashyOctoGrid.from_lines(lines)
    for i in itertools.count(start=1):
        if grid.step() == grid.num_rows * grid.num_cols:
            return i
        


if __name__ == '__main__':
    input = 'inputs/11.txt'
    print("On the eleventh day of Christmas...")
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
