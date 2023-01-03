import pathlib


def split_pairs(pair: str) -> tuple[tuple[int, int], tuple[int, int]]:
    hold: list[str] = pair.split(",")
    first: tuple[int, int] = form_tuple(hold[0])
    second: tuple[int, int] = form_tuple(hold[1])
    return first, second


def form_tuple(element: str) -> tuple[int, int]:
    return int(element.split("-")[0]), int(element.split("-")[1])


def convert_to_list(data: tuple[int, int]) -> list[int]:
    return list(range(data[0], data[1] + 1))


def contain(data: tuple[tuple[int, int], tuple[int, int]]) -> bool:
    first: list[int] = convert_to_list(data[0])
    second: list[int] = convert_to_list(data[1])
    if map_through(first, second) or map_through(second, first):
        return True
    return False


def map_through(list1: list[int], list2: list[int]) -> bool:
    for number in list1:
        if number not in list2:
            return False
    return True


def counter(data: list[str]) -> int:
    result: int = 0
    for element in data:
        first, second = split_pairs(element)
        if contain((first, second)):
            result += 1
    return result


def load_file(file: pathlib.Path) -> list[str]:
    with file.open("r") as open_file:
        parsed = open_file.readlines()
        clean_data = [e.strip("\n") for e in parsed]
        return clean_data


def part1(file: pathlib.Path) -> int:
    return counter(load_file(file))


def overlap(list1: list[int], list2: list[int]) -> list[int]:
    return list(filter(lambda x: x in list2, list1))


def part2(file: pathlib.Path) -> int:
    data: list[str] = load_file(file)
    return loop_counter(data)


def process_tuple(data: tuple[tuple[int, int], tuple[int, int]]) -> list[int]:
    first: list[int] = convert_to_list(data[0])
    second: list[int] = convert_to_list(data[1])
    return overlap(first, second)


def loop_counter(data: list[str]) -> int:
    result: int = 0
    for element in data:
        first, second = split_pairs(element)
        buffer_list: list[int] = process_tuple((first, second))
        if len(buffer_list) > 0:
            result += 1
    return result


if __name__ == '__main__':
    input_file = pathlib.Path("./day_04/input.txt")
    print(part1(input_file))
    print(part2(input_file))
