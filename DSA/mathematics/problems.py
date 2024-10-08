<<<<<<< HEAD
from typing import List


def sum_of_n_natural_numbers(n: int) -> int:
    """
    sum of n natural number
    """
    return (n * (n + 1)) // 2


def array_delete_shift(arr: List[int], n: int, index: int) -> List[int]:
    arr.pop(index)
    arr.append(0)
    return arr


class Solution:
    def median(self, A: List[int], N: int) -> int:
        pass

    def mean(self, A, N):
        pass


if __name__ == "__main__":
    ans = sum_of_n_natural_numbers(10)
    print(ans)

    ans = array_delete_shift([1, 2, 3, 4, 5, 6], 6, 3)

    print(ans)
=======
from typing import List


def sum_of_n_natural_numbers(n: int) -> int:
    """
    sum of n natural number
    """
    return (n * (n + 1)) // 2


def array_delete_shift(arr: List[int], n: int, index: int) -> List[int]:
    arr.pop(index)
    arr.append(0)
    return arr


class Solution:
    def median(self, A: List[int], N: int) -> int:
        pass

    def mean(self, A, N):
        pass


if __name__ == "__main__":
    ans = sum_of_n_natural_numbers(10)
    print(ans)

    ans = array_delete_shift([1, 2, 3, 4, 5, 6], 6, 3)

    print(ans)
>>>>>>> 97ed5d77ef971ade0973f4b0714a4aeb250c0bf4
