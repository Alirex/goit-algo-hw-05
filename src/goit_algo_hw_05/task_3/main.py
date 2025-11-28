import logging
import timeit
from typing import TYPE_CHECKING

from pydantic import BaseModel

from goit_algo_hw_05.task_3.services.articles import ARTICLES_CONFIGS, Articles
from goit_algo_hw_05.task_3.services.search_i_text_i_boyer_moore import search_i_text_i_boyer_moore
from goit_algo_hw_05.task_3.services.search_i_text_i_kmp import search_i_text_i_kmp
from goit_algo_hw_05.task_3.services.search_i_text_i_rabin_karp import search_i_text_i_rabin_karp
from logging_custom.init_logging import init_logging

if TYPE_CHECKING:
    from goit_algo_hw_05.task_3.services.signature import SearchFuncSignature

type TimeInSeconds = float
"""Time in seconds.

https://docs.python.org/3/library/time.html#time.perf_counter

Fractional seconds.
"""


type FuncName = str
"""Name of the function that used for comparison."""

type DataName = str
"""Name of the data set."""


class CompareInfoAggregated(BaseModel):
    func_name: FuncName
    data_name: str
    min_duration: float
    max_duration: float
    avg_duration: float


type CompareResults = list[CompareInfoAggregated]


def convert_seconds_to_milliseconds_text(seconds: TimeInSeconds) -> str:
    return f"{seconds * 1000:.2f} ms"


def search_text_compare(
    rounds: int = 1000,
) -> None:
    logger = logging.getLogger(__name__)
    functions = [
        search_i_text_i_rabin_karp,
        search_i_text_i_boyer_moore,
        search_i_text_i_kmp,
    ]

    results: CompareResults = []

    logger.info("Starting search text comparison...")

    for article in Articles:
        article_config = ARTICLES_CONFIGS[article]

        text = article_config.get_article_text()

        for func in functions:
            results.append(
                handle_data(
                    data_name=f"{article_config.file_name}-existed_pattern",
                    func=func,
                    logger=logger,
                    text_to_use=text,
                    pattern_to_search=article_config.pattern_i_existed,
                    rounds=rounds,
                ),
            )

            results.append(
                handle_data(
                    data_name=f"{article_config.file_name}-not_existed_pattern",
                    func=func,
                    logger=logger,
                    text_to_use=text,
                    pattern_to_search=article_config.pattern_not_i_existed,
                    rounds=rounds,
                ),
            )

    logger.info("Finished search text comparison.")

    for compare_info in sorted(results, key=lambda x: x.avg_duration):
        print(
            f"{compare_info.func_name}: {compare_info.data_name} - "
            f"min: {convert_seconds_to_milliseconds_text(compare_info.min_duration)}, "
            f"max: {convert_seconds_to_milliseconds_text(compare_info.max_duration)}, "
            f"avg: {convert_seconds_to_milliseconds_text(compare_info.avg_duration)}",
        )


def handle_data(  # noqa: PLR0913
    data_name: DataName,
    func: SearchFuncSignature,
    #
    logger: logging.Logger,
    #
    text_to_use: str,
    pattern_to_search: str,
    #
    rounds: int,
) -> CompareInfoAggregated:
    func_name = func.__name__
    results: list[TimeInSeconds] = []
    logger.info(f"Starting data set: {data_name} for function: {func_name}, rounds: {rounds}")

    for _ in range(rounds):
        start = timeit.default_timer()

        func(
            text_to_use,
            pattern_to_search,
        )
        duration = timeit.default_timer() - start
        results.append(duration)

    logger.info(f"Finished data set: {data_name} for function: {func_name}, rounds: {rounds}")

    return CompareInfoAggregated(
        func_name=func_name,
        data_name=data_name,
        min_duration=min(results),
        max_duration=max(results),
        avg_duration=sum(results) / len(results),
    )


def main() -> None:
    init_logging()
    search_text_compare(
        rounds=1000,
    )


if __name__ == "__main__":
    main()
