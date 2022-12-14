import pathlib

INPUT_DIR = pathlib.Path("input")


def read_input_lines(day: int, sample: bool = False) -> list[str]:
    with get_data_or_sample_path(day, sample).open() as f:
        return f.readlines()


def get_data_or_sample_path(day, sample):
    prefix = "data" if not sample else "sample"
    data_path = INPUT_DIR / f"{prefix}{day:02d}"
    return data_path


def parse_input_ints(day: int, sample: bool = False) -> list[int]:
    data_path = get_data_or_sample_path(day, sample)
    with data_path.open() as f:
        return [int(x) for x in f.readlines()]
