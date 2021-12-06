
class LanternfishPopulation:
    def __init__(self, list_of_intervals: list[int]):
        self.reproduction_intervals = [0] * 9
        for interval in list_of_intervals:
            self.reproduction_intervals[interval] += 1
    
    def evolve(self, days: int):
        for _ in range(days):
            self.__evolve_one_day()
    
    def size(self):
        return sum(self.reproduction_intervals)
 
    def __evolve_one_day(self):
        new_reproduction_intervals = [0] * 9
        for interval, pop in enumerate(self.reproduction_intervals):
            if not interval:
                new_reproduction_intervals[8] += pop
                new_reproduction_intervals[6] += pop
            else:
                new_reproduction_intervals[interval-1] += pop
        self.reproduction_intervals = new_reproduction_intervals

def part1(input_file: str) -> int:
    line = [line.rstrip() for line in open(input_file, 'r', encoding='utf-8')]
    fish_days = [int(x) for x in line[0].split(',')]
    population = LanternfishPopulation(fish_days)
    population.evolve(80)
    return population.size()

def part2(input_file: str) -> int:
    line = [line.rstrip() for line in open(input_file, 'r', encoding='utf-8')]
    fish_days = [int(x) for x in line[0].split(',')]
    population = LanternfishPopulation(fish_days)
    population.evolve(256)
    return population.size()

if __name__ == '__main__':
    input = 'inputs/6.txt'
    print("On the sixth day of Christmas...")
    print(f"Part 1: {part1(input)}")
    print(f"Part 2: {part2(input)}")
