from typing import TYPE_CHECKING

import pytest

from goit_algo_hw_05.task_3.services.articles import ARTICLES_CONFIGS, Articles
from goit_algo_hw_05.task_3.services.search_i_text_i_boyer_moore import search_i_text_i_boyer_moore
from goit_algo_hw_05.task_3.services.search_i_text_i_kmp import search_i_text_i_kmp
from goit_algo_hw_05.task_3.services.search_i_text_i_rabin_karp import search_i_text_i_rabin_karp

if TYPE_CHECKING:
    from _pytest.mark import ParameterSet
    from pytest_benchmark.fixture import BenchmarkFixture

    from goit_algo_hw_05.task_3.services.signature import SearchFuncSignature


def get_parametrized_fixtures() -> list[ParameterSet]:
    functions = [
        search_i_text_i_rabin_karp,
        search_i_text_i_boyer_moore,
        search_i_text_i_kmp,
    ]

    fixtures: list[ParameterSet] = []
    for article in Articles:
        article_config = ARTICLES_CONFIGS[article]

        text = article_config.get_article_text()

        for func in functions:
            fixtures.extend(
                [
                    pytest.param(
                        func,
                        text,
                        article_config.pattern_i_existed,
                        id=f"{func.__name__}-{article.value}-existed-pattern",
                    ),
                    pytest.param(
                        func,
                        text,
                        article_config.pattern_not_i_existed,
                        id=f"{func.__name__}-{article.value}-not-existed-pattern",
                    ),
                ],
            )

    return fixtures


@pytest.mark.parametrize(
    ("func", "data", "pattern"),
    get_parametrized_fixtures(),
)
@pytest.mark.benchmark
def test_search_text_benchmark(
    func: SearchFuncSignature,
    data: str,
    pattern: str,
    benchmark: BenchmarkFixture,
) -> None:
    benchmark(func, data, pattern)
