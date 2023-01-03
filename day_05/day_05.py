import pathlib
import re


def load_file(file: pathlib.Path) -> list[str]:
    with file.open("r") as open_file:
        parsed = open_file.readlines()
        clean_data = [e.strip("\n") for e in parsed]
        return clean_data


class Move:
    def __init__(self, move: str) -> None:
        self.move = move

        self.move_row: int
        self.from_row: int
        self.to_row: int

        self.read_move()

    def read_move(self):
        pattern = re.compile(
            r"move (?P<move>\d+) from (?P<from>\d) to (?P<to>\d)")
        search = pattern.search(self.move)
        self.move_row = int(search.group("move"))
        self.from_row = int(search.group("from"))
        self.to_row = int(search.group("to"))

    def show_move(self):
        return f"m: {self.move_row} f: {self.from_row} t: {self.to_row}"


class Stack:
    result: dict[int, list[str]] = {}

    def __init__(self, puzzle: list[str]) -> None:
        self.puzzle = puzzle

    def load_column(self, column: int) -> tuple[int, list[str]]:
        result: list[str] = []
        for row in self.puzzle:
            result.append(row[column])
        index: int = int(result[-1])
        result.pop()
        result.reverse()
        return index, list(filter(lambda x: x != ' ', result))

    def create_dict(self) -> dict[int, list[str]]:
        for i in range(1, len(self.puzzle[0]), 4):
            index, tmp = self.load_column(i)
            self.result.setdefault(index, tmp)
        return self.result


class Day5:
    def __init__(self, setup: dict[int, list[str]], moves: list[str]) -> None:
        self.setup = setup
        self.moves = moves

    def test_conforming(self, index: int) -> list[str]:
        return self.setup[index]

    def move_letter(self, move: Move) -> None:
        from_list: list[str] = self.setup[move.from_row]
        to_list: list[str] = self.setup[move.to_row]
        to_list.append(from_list[-1])
        from_list.pop()

    def iterate_moves(self):
        for actual_move in self.moves:
            move: Move = Move(actual_move)
            iterate: int = 0
            while iterate < move.move_row:
                self.move_letter(move)
                iterate += 1

    def show_result(self) -> str:
        result: list[str] = []
        for item in self.setup:
            result.append(self.setup[item][-1])
        return ''.join(result)

    def full_process_part1(self) -> str:
        self.iterate_moves()
        return self.show_result()

    def move_stack(self, move: Move) -> None:
        from_list: list[str] = self.setup[move.from_row]
        to_list: list[str] = self.setup[move.to_row]
        stack: int = move.move_row
        to_list.extend(from_list[-stack:])
        iterate: int = 0
        while iterate < stack:
            from_list.pop()
            iterate += 1

    def iterate_stacks(self):
        for actual_move in self.moves:
            move: Move = Move(actual_move)
            self.move_stack(move)

    def full_process_part2(self) -> str:
        self.iterate_stacks()
        return self.show_result()


if __name__ == '__main__':
    input_file: pathlib.Path = pathlib.Path("./day_05/input.txt")
    raw_data: list[str] = load_file(input_file)
    # print(Day5(Stack(raw_data[0:9]).create_dict(),
    #       raw_data[10:]).full_process_part1())
    # print(Day5(Stack(raw_data[0:9]).create_dict(),
    #       raw_data[10:]).full_process_part2())
