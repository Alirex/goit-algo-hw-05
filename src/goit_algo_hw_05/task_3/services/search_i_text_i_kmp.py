from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from goit_algo_hw_05.task_3.services.search_text_shared import MainText, PositionOrNone, TextPattern

type LPSArray = list[int]
"""Longest Prefix Suffix array type"""


def compute_lps(pattern: TextPattern) -> LPSArray:
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    return lps


def search_i_text_i_kmp(main_string: MainText, pattern: TextPattern) -> PositionOrNone:
    pattern_len = len(pattern)
    text_len = len(main_string)

    lps = compute_lps(pattern)

    text_index = 0
    pattern_index = 0

    while text_index < text_len:
        if pattern[pattern_index] == main_string[text_index]:
            text_index += 1
            pattern_index += 1
        elif pattern_index != 0:
            pattern_index = lps[pattern_index - 1]
        else:
            text_index += 1

        if pattern_index == pattern_len:
            return text_index - pattern_index

    return None
