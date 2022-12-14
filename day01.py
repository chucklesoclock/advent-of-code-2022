from utils import INPUT_DIR
from pathlib import Path
from collections import Counter
import pytest

data_path = INPUT_DIR / "data01"


def part1(elf_counter: Counter):
    return max(elf_counter.values())


def part2(elf_counter: Counter):
    return sum(x[1] for x in elf_counter.most_common(3))


def common_counter(p: Path = data_path):
    elf_i = 0
    elves = Counter()
    with p.open() as f:
        for line in f:
            if line != "\n":
                elves[elf_i] += int(line)
            else:
                elf_i += 1
                continue
    return elves


if __name__ == "__main__":
    elf_counter = common_counter()
    print(part1(elf_counter))
    print(part2(elf_counter))


@pytest.fixture
def sample_elf_counter():
    sample_data_path = INPUT_DIR / ("sample01")
    return common_counter(sample_data_path)


def test_sample_input_part1(sample_elf_counter):
    assert part1(sample_elf_counter) == 24000


def test_sample_input_part2(sample_elf_counter):
    assert part2(sample_elf_counter) == 45000
