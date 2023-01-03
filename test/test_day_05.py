
import unittest

from pathlib import Path
from day_05 import day_05
from day_05.day_05 import Day5, Move, Stack


class Day5Test(unittest.TestCase):

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
        self.input_file = Path("./day_05/input.txt")
        self.day4: Day5 = Day5(self.setup, self.moves)
        self.move: Move = Move(self.moves[0])
        self.raw_data_file: list[str] = day_05.load_file(self.input_file)
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