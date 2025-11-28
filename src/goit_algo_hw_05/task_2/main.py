from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any

from comparable import Comparable

type CollectionIndex = int
"""An index in a collection."""

type PresortedCollection[Item: Comparable[Any]] = Sequence[Item]
"""A presorted collection of comparable items."""

type IterationsAmount = int
"""The number of iterations performed during a search."""

type UpperBoundResult[T] = T
"""The result of the search.

The nearest (lesser) value that is greater than or equal to the target.
"""

type BinarySearchResult[T] = tuple[IterationsAmount, UpperBoundResult[T]]
"""The result of the binary search."""


@dataclass
class NotFoundTraceableError(
    LookupError,
):
    """An error indicating that a value was not found during a search."""

    iterations: IterationsAmount


def binary_search_traceable[Item: Comparable[Any]](
    collection: PresortedCollection[Item],
    target: Item,
) -> BinarySearchResult[Item]:
    """Perform binary search on a sorted list of floats and return a tuple.

    Raises:
        NotFoundTraceableError: If the target and upper bound are not found.
    """
    iterations = 0

    low_index: CollectionIndex = 0
    high_index: CollectionIndex = len(collection) - 1

    candidate: UpperBoundResult[Item] | None = None

    while low_index <= high_index:
        mid_index: CollectionIndex = (low_index + high_index) // 2
        iterations += 1
        value = collection[mid_index]

        if value > target:
            candidate = value
            # look left to find a smaller value >= target
            high_index = mid_index - 1
        elif value < target:
            # look right to find a value >= target
            low_index = mid_index + 1
        else:
            # exact match found
            candidate = value
            break

    if candidate is None:
        raise NotFoundTraceableError(iterations=iterations)

    return iterations, candidate
