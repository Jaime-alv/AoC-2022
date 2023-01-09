from pathlib import Path


class Puzzle:

    def __init__(self, folder_name: str) -> None:
        self.file = Path(f"./{folder_name}/input.txt")

    def load_file(self) -> list[str]:
        with self.file.open("r", encoding='UTF-8') as open_file:
            parsed = open_file.readlines()
            clean_data = [e.strip("\n") for e in parsed]
            return clean_data

    def __call__(self) -> list[str]:
        return self.load_file()
