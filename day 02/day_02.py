from pathlib import Path
import unittest


def load_file(file: Path) -> list[str]:
    with file.open("r") as open_file:
        parsed = open_file.readlines()
        clean_data = [e.strip("\n") for e in parsed]
        return clean_data


class Day2:
    rps: dict[str, int] = {
        "X": 1,
        "Y": 2,
        "Z": 3,
    }

    eq: dict[str, str] = {
        "X": "A",
        "Y": "B",
        "Z": "C"
    }

    win: dict[str, str] = {
        "A": "C",
        "B": "A",
        "C": "B"
    }

    loose: dict[str, str] = {
        "A": "B",
        "B": "C",
        "C": "A"
    }

    rps_letter: dict[str, int] = {
        "A": 1,
        "B": 2,
        "C": 3,
    }

    def day2_part1(self, rounds: list[str]) -> int:
        points: int = 0
        for element in rounds:
            elf = element[0]
            you = element[2]

            points += int(self.rps[you])

            if elf == self.eq.get(you):
                points += 3
            elif ((elf == "A" and you == "Y")
                    or (elf == "B" and you == "Z")
                    or (elf == "C" and you == "X")):
                points += 6

        return points

    def day2_part2(self, rounds: list[str]) -> int:
        points: int = 0
        for element in rounds:
            elf = element[0]
            you = element[2]

            match you:
                case "X":
                    points += 0
                    result = self.win[elf]
                    points += int(self.rps_letter[result])
                case "Y":
                    points += 3
                    points += int(self.rps_letter[elf])
                case _:
                    points += 6
                    result = self.loose[elf]
                    points += int(self.rps_letter[result])

        return points


class TestDay2(unittest.TestCase):
    example: list[str] = [
        'A Y',
        'B X',
        'C Z',
    ]

    def test_part_1(self):
        self.assertEqual(Day2().day2_part1(self.example), 15)

    def test_part_2(self):
        self.assertEqual(Day2().day2_part2(self.example), 12)


if __name__ == '__main__':
    input_file: Path = Path("./day 02/input.txt")
    print(Day2().day2_part1(load_file(input_file)))
    print(Day2().day2_part2(load_file(input_file)))
    unittest.main()
