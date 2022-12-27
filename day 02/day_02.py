from pathlib import Path
import unittest


def load_file(file: Path) -> list[str]:
    with file.open("r") as open_file:
        parsed = open_file.readlines()
        clean_data = [e.strip("\n") for e in parsed]
        return clean_data


class Day2:

    win: list[str] = [
        'C X',
        'A Y',
        'B Z'
    ]

    tie: list[str] = [
        'A X',
        'B Y',
        'C Z'
    ]

    loose: list[str] = [
        'B X',
        'C Y',
        'A Z'
    ]

    pc: dict[str, str] = {
        'A': 'Rock',
        'B': 'Paper',
        'C': 'Scissors'
    }

    player: dict[str, str] = {
        'X': 'Rock',
        'Y': 'Paper',
        'Z': 'Scissors'
    }

    def __init__(self, data: list[str]) -> None:
        self.data = data

    def additional_points(self, player: str) -> int:
        match player:
            case 'X': return 1
            case 'Y': return 2
            case _: return 3

    def resolve_hand(self, move: str) -> int:
        if move in self.win:
            return 6
        if move in self.tie:
            return 3
        return 0

    def get_player_move(self, move: str) -> int:
        player: str = move[2]
        return self.additional_points(player)

    def process_part_1(self) -> int:
        result: int = 0
        for hand in self.data:
            result += self.resolve_hand(hand)
            result += self.get_player_move(hand)
        return result

class TestDay2(unittest.TestCase):
    example: list[str] = [
        'A Y',
        'B X',
        'C Z',
    ]

    base: Day2 = Day2(example)

    def test_enum(self):
        self.assertEqual(self.base.resolve_hand('A Y'), 6)
        self.assertEqual(self.base.resolve_hand('B X'), 0)
        self.assertEqual(self.base.resolve_hand('C Z'), 3)

    def test_part_1(self):
        self.assertEqual(self.base.process_part_1(), 15)
        self.assertEqual(Day2(load_file(input_file)).process_part_1(), 11906)


if __name__ == '__main__':
    input_file: Path = Path("./day 02/input.txt")
    unittest.main()
