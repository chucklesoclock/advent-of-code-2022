from enum import IntEnum
from utils import INPUT_DIR
from typing import Literal, Generator
import functools
from timethis import timethis
import pytest


class Throw(IntEnum):
    rock = 1
    paper = 2
    scissors = 3


class MatchResult(IntEnum):
    loss = 0
    draw = 3
    win = 6


throw_map = dict(
    A=Throw.rock,
    B=Throw.paper,
    C=Throw.scissors,
    X=Throw.rock,
    Y=Throw.paper,
    Z=Throw.scissors,
)

win_map = dict(X=MatchResult.loss, Y=MatchResult.draw, Z=MatchResult.win)


def parse_input(
    part: Literal[1, 2], sample: bool = False
) -> Generator[tuple[Throw, Throw | MatchResult], None, None]:
    data_path = INPUT_DIR / f"{'data' if not sample else 'sample'}02"
    parse_code_to_throw = throw_map.__getitem__
    match part:
        case 1:
            second_col_prase = parse_code_to_throw
        case 2:
            second_col_prase = win_map.__getitem__
        case _:
            raise ValueError(f"param part must be in [1, 2]: {part=}")
    return (
        (parse_code_to_throw(x), second_col_prase(y))
        for x, y in (line.split() for line in data_path.read_text().splitlines())
    )


@functools.cache
def get_match_result(throws: tuple[Throw, Throw]) -> MatchResult:
    elf, me = throws
    if elf is me:
        return MatchResult.draw
    elif elf is Throw.rock:
        match me:
            case Throw.scissors:
                return MatchResult.loss
            case Throw.paper:
                return MatchResult.win
    elif elf is Throw.paper:
        match me:
            case Throw.scissors:
                return MatchResult.win
            case Throw.rock:
                return MatchResult.loss
    elif elf is Throw.scissors:
        match me:
            case Throw.rock:
                return MatchResult.win
            case Throw.paper:
                return MatchResult.loss


def part1(guide: list[tuple[Throw, Throw]]) -> int:
    return sum(line[1] + get_match_result(line) for line in guide)


@functools.cache
def determine_throw(line):
    elf, result = line
    if result is MatchResult.draw:
        return elf
    else:
        for throw in (t for t in Throw if t is not elf):
            if get_match_result((elf, throw)) is result:
                return throw


def part2(guide: list[tuple[Throw, MatchResult]]) -> int:
    return sum(line[1] + determine_throw(line) for line in guide)


@timethis
def main():
    guide = parse_input(part=1)
    print(part1(guide))
    guide = parse_input(part=2)
    print(part2(guide))


if __name__ == "__main__":
    main()


@pytest.fixture
def sample_guide_part_1():
    return parse_input(part=1, sample=True)


def test_part1(sample_guide_part_1):
    assert part1(sample_guide_part_1) == 15


@pytest.fixture
def sample_guide_part_2():
    return parse_input(part=2, sample=True)


def test_part2(sample_guide_part_2):
    assert part2(sample_guide_part_2) == 12
