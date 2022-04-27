""" Вспомогательные методы и функции """

from typing import Callable, Tuple, Any, TextIO, List


def to_int(string: str) -> int:
    """ Конвертация строки в целочисленное значение """
    return int(string.strip())


def to_ints(string: str, separator: str = ' ') -> List[int]:
    """ Конвертация строки в набор целочисленных значений """
    return list(map(to_int, (x for x in string.strip().split(separator) if x)))


def run_tests(
        func: Callable,
        test_filename: str,
        test_parser: Callable[[TextIO], Tuple[Any, Any]]
) -> None:
    """ Запуск тестов """

    print(f'Reading tests from file: {test_filename}')

    tests = []
    with open(test_filename, 'r') as file:
        tests_num = to_int(file.readline())
        for index in range(1, tests_num + 1):
            args, expected = test_parser(file)
            tests.append((args, expected))

    print(f'Read {tests_num} tests')

    for index, (args, expected) in enumerate(tests):
        result = func(*args)
        test_num = str(index + 1).rjust(3, '0')
        status = '[ OK ]' if result == expected else '[ ERROR ]'
        status = ('[ OK ]' if result == expected else '[ ERROR ]').ljust(10)
        print(f'Test {test_num}: {status} (result = {result}, expected = {expected}')
