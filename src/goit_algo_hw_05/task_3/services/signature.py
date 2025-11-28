from collections.abc import Callable

from goit_algo_hw_05.task_3.services.search_text_shared import MainText, PositionOrNone, TextPattern

type SearchFuncSignature = Callable[[MainText, TextPattern], PositionOrNone]
