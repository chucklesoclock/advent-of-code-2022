from pathlib import Path
from collections import Counter

data_path = Path("input/data01")


def part1(p: Path = data_path):
    most_cals = 0
    with p.open() as f:
        elf_cals = 0
        for line in f:
            if line != "\n":
                elf_cals += int(line)
            else:
                if elf_cals > most_cals:
                    most_cals = elf_cals
                elf_cals = 0
                continue
    return most_cals


def part2(p: Path = data_path):
    elf_i = 0
    elves = Counter()
    with p.open() as f:
        for line in f:
            if line != "\n":
                elves[elf_i] += int(line)
            else:
                elf_i += 1
                continue
    return sum(x[1] for x in elves.most_common(3))


if __name__ == "__main__":
    print(part1())
    print(part2())

sample_data_path = Path("input/sample01")


def test_sample_input_part1():
    assert part1(sample_data_path) == 24000


def test_sample_input_part2():
    assert part2(sample_data_path) == 45000
