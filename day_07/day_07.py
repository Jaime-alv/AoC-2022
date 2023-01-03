
import re
import unittest
from pathlib import Path
from re import Pattern
from typing import Any


def load_file(file: Path) -> list[str]:
    with file.open("r") as open_file:
        parsed = open_file.readlines()
        clean_data = [e.strip("\n") for e in parsed]
        return clean_data


class Day07:
    directory: dict[str, Any] = {}

    change_dir: Pattern[str] = re.compile(r"\$ cd")

    def __init__(self, data: list[str]) -> None:
        self.data = data

    def sum_files(self, folder: list[str]) -> int:
        return sum(int(x.split(' ', 1)[0]) for x in folder)

    def conform_directory(self) -> None:
        tmp: list[str] = []
        for line in self.data:
            if line.startswith("$ cd") is False:
                tmp.append(line)
            else:
                self.directory.setdefault(line, tmp)
                tmp.clear()




if __name__ == '__main__':
    unittest.main()
