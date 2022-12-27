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

    map_input = {'A': 'Rock', 'B': 'Paper', 'C': 'Scissors',
                 'X': 'Lose', 'Y': 'Draw', 'Z': 'Win'}
    points_per_shape = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
    points_per_outcome = {'Lose': 0, 'Draw': 3, 'Win': 6}

    def points_per_round2(self, move: str) -> int:
        opponent_shape = self.map_input[move[0]]
        our_goal = self.map_input[move[2]]

        if (opponent_shape, our_goal) in [('Rock', 'Draw'), ('Paper', 'Lose'), ('Scissors', 'Win')]:
            return self.points_per_outcome[our_goal] + self.points_per_shape['Rock']
        elif (opponent_shape, our_goal) in [('Rock', 'Win'), ('Paper', 'Draw'), ('Scissors', 'Lose')]:
            return self.points_per_outcome[our_goal] + self.points_per_shape['Paper']
        else:
            return self.points_per_outcome[our_goal] + self.points_per_shape['Scissors']

    def part2(self) -> int:
        return sum([self.points_per_round2(move) for move in self.data])


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
        self.assertEqual(Day2(load_file(input_file)).part2(), 11186)


if __name__ == '__main__':
    input_file: Path = Path("./day 02/input.txt")
    unittest.main()
