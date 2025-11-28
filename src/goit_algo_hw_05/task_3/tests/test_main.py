from typing import TYPE_CHECKING

import pytest

from goit_algo_hw_05.task_3.services.search_i_text_i_boyer_moore import search_i_text_i_boyer_moore
from goit_algo_hw_05.task_3.services.search_i_text_i_kmp import search_i_text_i_kmp
from goit_algo_hw_05.task_3.services.search_i_text_i_rabin_karp import search_i_text_i_rabin_karp

if TYPE_CHECKING:
    from goit_algo_hw_05.task_3.services.signature import SearchFuncSignature


@pytest.mark.parametrize(
    "func",
    [
        search_i_text_i_rabin_karp,
        search_i_text_i_boyer_moore,
        search_i_text_i_kmp,
    ],
)
def test_main(
    func: SearchFuncSignature,
) -> None:
    text = "Being a developer is not easy"
    pattern = "developer"
    position = 8

    result = func(text, pattern)

    assert result == position


@pytest.mark.parametrize(
    "func",
    [
        search_i_text_i_rabin_karp,
        search_i_text_i_boyer_moore,
        search_i_text_i_kmp,
    ],
)
def test_not_found(
    func: SearchFuncSignature,
) -> None:
    text = "Being a developer is not easy"
    pattern = "python"
    position = None
    result = func(text, pattern)
    assert result == position
