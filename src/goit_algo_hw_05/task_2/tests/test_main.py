from decimal import Decimal
from fractions import Fraction
from typing import Any

import pytest

from comparable import Comparable
from goit_algo_hw_05.task_2.extra_class import Some
from goit_algo_hw_05.task_2.main import BinarySearchResult, NotFoundTraceableError, binary_search_traceable


@pytest.mark.parametrize(
    ("arr", "target", "expected"),
    [
        # Float values
        (  # exact match
            [0.5, 1.0, 1.5, 2.0],
            1.5,
            (2, 1.5),
        ),
        # Steps to find 1.5:
        # 1: mid=(0+3)//2=1 (1.0) < 1.5 -> go right
        # 2: mid=(2+3)//2=2 (1.5) == 1.5 -> found
        # ---
        (  # between 1.0 and 1.5
            [0.5, 1.0, 1.5, 2.0],
            1.25,
            (2, 1.5),
        ),
        # Steps to find 1.25:
        # 1: mid=(0+3)//2=1 (1.0) < 1.25 -> go right
        # 2: mid=(2+3)//2=2 (1.5) >= 1.25 -> candidate=1.5, go left
        # 3: low=2 > high=1 -> exit loop. Use candidate=1.5
        # ---
        # Duplicate values
        (
            [1.0, 1.5, 1.5, 1.5, 2.0],
            1.5,
            (1, 1.5),
        ),
        # Steps to find 1.5:
        # 1: mid=(0+4)//2=2 (1.5) == 1.5 -> exact match found
        # ---
        (
            [1.0, 1.5, 1.5, 1.5, 2.0],
            1.4,
            (3, 1.5),
        ),
        # Steps to find 1.4:
        # 1: mid=(0+4)//2=2 (1.5) >= 1.4 -> candidate=1.5, go left
        # 2: mid=(0+1)//2=0 (1.0) < 1.4 -> go right
        # 3: mid=(1+1)//2=1 (1.5) >= 1.4 -> candidate=1.5, go left
        # 4: low=2 > high=1 -> exit loop. Use candidate=1.5
        # ---
        # Integer values
        (
            [1, 3, 5, 7, 9],
            6,
            (2, 7),
        ),
        # Steps to find 6:
        # 1: mid=(0+4)//2=2 (5) < 6 -> go right
        # 2: mid=(3+4)//2=3 (7) >= 6 -> candidate=7, go left
        # 3: low=3 > high=2 -> exit loop. Use candidate=7
        # ---
        # Negative values
        (
            [-5.0, -3.0, -1.0, 0.0, 2.0],
            -2.0,
            (3, -1.0),
        ),
        # Steps to find -2.0:
        # 1: mid=(0+4)//2=2 (-1.0) >= -2.0 -> candidate=-1.0, go left
        # 2: mid=(0+1)//2=0 (-5.0) < -2.0 -> go right
        # 3: mid=(1+1)//2=1 (-3.0) >= -2.0 -> candidate=-1.0, go left
        # 4: low=2 > high=1 -> exit loop. Use candidate=-1.0
        # ---
        # Single element array
        (
            [2.0],
            2.0,
            (1, 2.0),
        ),
        # Steps to find 2.0:
        # 1: mid=(0+0)//2=0 (2.0) == 2.0 -> exact match found
        # ---
        # Decimal values
        (  # exact match
            [Decimal("0.1"), Decimal("0.2"), Decimal("0.3"), Decimal("0.4")],
            Decimal("0.3"),
            (2, Decimal("0.3")),
        ),
        # Steps to find 0.3:
        # 1: mid=(0+3)//2=1 (0.2) < 0.3 -> go right
        # 2: mid=(2+3)//2=2 (0.3) == 0.3 -> exact match found
        (  # upper bound
            [Decimal("1.1"), Decimal("2.2"), Decimal("3.3")],
            Decimal("2.5"),
            (
                2,
                Decimal("3.3"),
            ),
        ),
        # Steps to find 2.5:
        # 1: mid=(0+2)//2=1 (2.2) < 2.5 -> go right
        # 2: mid=(2+2)//2=2 (3.3) >= 2.5 -> candidate=3.3, go left
        # 3: low=2 > high=1 -> exit loop. Use candidate=3.3
        # ---
        # Fraction values
        (  # exact match
            [Fraction(1, 4), Fraction(1, 2), Fraction(3, 4)],
            Fraction(1, 2),
            (1, Fraction(1, 2)),
        ),
        # Steps to find 1/2:
        # 1: mid=(0+2)//2=1 (1/2) == 1/2 -> exact match found
        # ---
        (  # upper bound
            [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)],
            Fraction(3, 5),
            (2, Fraction(2, 3)),
        ),  # Steps to find 3/5:
        # 1: mid=(0+2)//2=1 (1/2) < 3/5 -> go right
        # 2: mid=(2+2)//2=2 (2/3) >= 3/5 -> candidate=2/3, go left
        # 3: low=2 > high=1 -> exit loop. Use candidate=2/3
        # ---
        # Custom comparable class
        (  # exact match
            [Some(value=1), Some(value=3), Some(value=5)],
            Some(value=3),
            (1, Some(value=3)),
        ),
        # Steps to find Some(3):
        # 1: mid=(0+2)//2=1 (Some(3)) == Some(3) -> exact match found
        # ---
        (  # upper bound
            [Some(value=1), Some(value=3), Some(value=5)],
            Some(value=4),
            (2, Some(value=5)),
        ),  # Steps to find Some(4):
        # 1: mid=(0+2)//2=1 (Some(3)) < Some(4) -> go right
        # 2: mid=(2+2)//2=2 (Some(5)) >= Some(4) -> candidate=Some(5), go left
        # 3: low=2 > high=1 -> exit loop. Use candidate=Some(5)
        # ---
    ],
)
def test_binary_search[T: Comparable[Any]](
    arr: list[T],
    target: T,
    expected: BinarySearchResult[T],
) -> None:
    result = binary_search_traceable(arr, target)

    assert result == expected


@pytest.mark.parametrize(
    ("arr", "target", "iterations"),
    [
        (  # empty array
            [],
            1.5,
            0,
        ),
        # Steps to find 1.5:
        # Array is empty, so 0 iterations
        # ---
        (  # above max
            [0.5, 1.0, 1.5, 2.0, 2.5],
            3.0,
            3,
        ),
        # Steps to find 3.0:
        # 1: mid=(0+4)//2=2 (1.5) < 3.0 -> go right
        # 2: mid=(3+4)//2=3 (2.0) < 3.0 -> go right
        # 3: mid=(4+4)//2=4 (2.5) < 3.0 -> go right
        # 4: low=5 > high=4 -> exit loop. No candidate found.
        # ---
        (
            [2.0],
            3.0,
            1,
        ),
        # Steps to find 3.0:
        # 1: mid=(0+0)//2=0 (2.0) < 3.0 -> go right
        # 2: low=1 > high=0 -> exit loop. No candidate found.
        # ---
    ],
)
def test_binary_search_not_found[T: Comparable[Any]](
    arr: list[T],
    target: T,
    iterations: int,
) -> None:
    with pytest.raises(NotFoundTraceableError) as exc_info:
        binary_search_traceable(arr, target)

    assert exc_info.value.iterations == iterations
