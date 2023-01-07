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


class ForestMatrix:
    counter: int = 0

    def __init__(self, data: list[str]) -> None:
        self.data = data

    def check_all_smaller(self, tree_house: int, trees: list[int]) -> bool:
        return all(map(lambda x: x < tree_house, trees))

    def parse_list(self,
                   number: int,
                   top: list[int],
                   down: list[int],
                   left: list[int],
                   right: list[int]) -> bool:
        tautology: tuple[bool, bool, bool, bool] = (
            self.check_all_smaller(number, top),
            self.check_all_smaller(number, down),
            self.check_all_smaller(number, left),
            self.check_all_smaller(number, right),
        )
        return any(tautology)

    def iterate_data(self) -> int:
        for index_row, v_row in enumerate(self.data):
            print(self.parse_line_notice(index_row))
            for i_column, v_column in enumerate((self.data[index_row])):
                top, down = self.conform_column_list(i_column, index_row)
                left, right = self.conform_row_list(v_row, i_column)
                number: int = int(v_column)
                if self.parse_list(
                        number=number,
                        top=top,
                        down=down,
                        left=left,
                        right=right):
                    self.counter += 1
        return self.counter

    def conform_column_list(self, index: int, div: int) -> tuple[list[int], list[int]]:
        tmp: list[int] = []
        for line in self.data:
            tmp.append(int(line[index]))
        return tmp[0:div], tmp[div + 1:]

    def conform_row_list(self, line: str, index: int) -> tuple[list[int], list[int]]:
        conversion: list[int] = [int(x) for x in line]
        return conversion[:index], conversion[index + 1:]

    def parse_line_notice(self, index: int) -> str:
        return f"Parsing line: ({index + 1}/{len(self.data)})"

    def part_one(self) -> str:
        result: int = self.iterate_data()
        return f"Result for part one is: {result}"


if __name__ == '__main__':
    puzzle = Puzzle("day_08")()
    forest = ForestMatrix(puzzle)
    print(forest.part_one())
