""" 0001. Two Sum """

from typing import List, TextIO, Tuple, Any
from leetcode.utils.python import run_tests, to_ints, to_int


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numbers_map = {value: index for index, value in enumerate(nums)}
        
        for index, value in enumerate(nums):
            left = target - value
            if (left_index := numbers_map.get(left, None)) is not None:
                if index != left_index:
                    return [index, left_index]

        return []


def main():
    """ Запуск тестов """

    def test_parser(file: TextIO) -> Tuple[Any, Any]:
        """ Считывание данных для отдельного теста """
        nums = to_ints(file.readline())
        target = to_int(file.readline())
        expected = to_ints(file.readline())
        return (nums, target), expected

    run_tests(
        func=Solution().twoSum,
        test_filename='tests',
        test_parser=test_parser
    )


if __name__ == '__main__':
    main()
