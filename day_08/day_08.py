from pathlib import Path


def load_file(file: Path) -> list[str]:
    with file.open("r") as open_file:
        parsed = open_file.readlines()
        clean_data = [e.strip("\n") for e in parsed]
        return clean_data


def transform_into_int(file: list[str]) -> list[int]:
    return list(int(x) for x in file)


class Day08:
    def __init__(self, data: list[int]) -> None:
        self.data = data


if __name__ == '__main__':
    pass
