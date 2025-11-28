from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from goit_algo_hw_05.task_3.services.search_text_shared import MainText, PositionOrNone, TextPattern

type CharacterFromPattern = str
"""Character from pattern."""

type OffsetIfMismatch = int
"""Offset by character.

Number of characters to shift when a mismatch occurs.
"""

type ShiftTable = dict[CharacterFromPattern, OffsetIfMismatch]
"""Shift table type for Boyer-Moore algorithm"""


def build_shift_table(pattern: TextPattern) -> ShiftTable:
    """Create a shift table for the Boyer-Moore algorithm."""
    length = len(pattern)

    table: ShiftTable = {char: length - index - 1 for index, char in enumerate(pattern[:-1])}
    # If the character is not in the table, the offset will be equal to the length of the substring
    table.setdefault(pattern[-1], length)
    return table


def search_i_text_i_boyer_moore(text: MainText, pattern: TextPattern) -> PositionOrNone:
    # Create a shift table for the pattern (substring)
    shift_table = build_shift_table(pattern)

    i = 0  # Initialize the starting index for the main text

    # We go through the main text, comparing it with the subtext
    while i <= len(text) - len(pattern):
        j = len(pattern) - 1  # We start from the end of the substring

        # Compare characters from the end of a substring to its beginning
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1  # Moving to the beginning of the substring

        # If the entire substring matches, return its position in the text
        if j < 0:
            return i  # Substring found

        # Shift index i based on the shift table
        # This allows you to "jump" over non-matching parts of the text
        i += shift_table.get(text[i + len(pattern) - 1], len(pattern))

    return None
