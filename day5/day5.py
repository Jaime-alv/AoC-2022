import unittest
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


class Day4Test(unittest.TestCase):

    def setUp(self) -> None:
        self.setup: dict[int, list[str]] = {
            1: ['Z', 'N'],
            2: ['M', 'C', 'D'],
            3: ['P']
        }

        self.moves: list[str] = [
            'move 1 from 2 to 1',
            'move 3 from 1 to 3',
            'move 2 from 2 to 1',
            'move 1 from 1 to 2',
        ]

        self.raw_data: list[str] = [
            "    [D]    ",
            "[N] [C]    ",
            "[Z] [M] [P]",
            " 1   2   3 ",
        ]
        self.input_file = pathlib.Path("./day5/input.txt")
        self.day4: Day5 = Day5(self.setup, self.moves)
        self.move: Move = Move(self.moves[0])
        self.raw_data_file: list[str] = load_file(input_file)
        self.stack: Stack = Stack(self.raw_data_file[0:9])
        self.true_moves: list[str] = self.raw_data_file[10:]
        return super().setUp()

    def test_setup(self):
        self.assertEqual(self.day4.test_conforming(1), ['Z', 'N'])
        self.assertEqual(self.day4.test_conforming(2), ['M', 'C', 'D'])
        self.assertEqual(self.day4.test_conforming(3), ['P'])

    def test_move(self):
        self.assertEqual(self.move.show_move(), "m: 1 f: 2 t: 1")

    def test_raw_data(self):
        self.assertEqual(self.raw_data[0][5], "D")
        self.assertEqual(self.raw_data[1][1], "N")
        self.assertEqual(self.raw_data[2][9], "P")

    def test_column(self):
        self.assertEqual(self.stack.load_column(
            1), (1, ['D', 'L', 'V', 'T', 'M', 'H', 'F']))
        self.assertEqual(self.stack.load_column(
            5), (2, ['H', 'Q', 'G', 'J', 'C', 'T', 'N', 'P']))
        self.assertEqual(self.stack.load_column(
            13), (4, ['L', 'B', 'V', 'F']))

    def test_raw_data_dict(self):
        self.assertDictEqual(self.setup, Stack(self.raw_data).create_dict())

    def test_complete_setup(self):
        self.assertEqual(Day5(Stack(self.raw_data).create_dict(),
                         self.moves).test_conforming(1), ['Z', 'N'])

    def test_first_move(self):
        self.assertEqual(self.true_moves[0], "move 1 from 7 to 6")

    def test_move_letter(self):
        self.assertEqual(self.day4.test_conforming(1), ['Z', 'N'])
        self.day4.move_letter(self.move)
        self.assertEqual(self.day4.test_conforming(1), ['Z', 'N', 'D'])

    def test_show_result(self):
        self.assertEqual(Day5(self.setup, self.moves).show_result(), 'NDP')
        Day5(self.setup, self.moves).iterate_moves()
        self.assertEqual(Day5(self.setup, self.moves).show_result(), 'CMZ')

    def test_process(self):
        self.assertEqual(
            Day5(self.setup, self.moves).full_process_part1(), 'CMZ')

    def test_move_stack(self):
        self.assertEqual(self.day4.test_conforming(1), ['Z', 'N'])
        self.day4.move_stack(Move(self.moves[0]))
        self.assertEqual(self.day4.test_conforming(1), ['Z', 'N', 'D'])
        self.day4.move_stack(Move(self.moves[1]))
        self.assertEqual(self.day4.test_conforming(1), [])
        self.assertEqual(self.day4.test_conforming(3), ['P', 'Z', 'N', 'D'])

    def test_part2(self):
        self.assertEqual(
            Day5(self.setup, self.moves).full_process_part2(), 'MCD')


if __name__ == '__main__':
    input_file: pathlib.Path = pathlib.Path("./day5/input.txt")
    raw_data: list[str] = load_file(input_file)
    # print(Day5(Stack(raw_data[0:9]).create_dict(),
    #       raw_data[10:]).full_process_part1())
    # print(Day5(Stack(raw_data[0:9]).create_dict(),
    #       raw_data[10:]).full_process_part2())
    unittest.main(verbosity=2)
