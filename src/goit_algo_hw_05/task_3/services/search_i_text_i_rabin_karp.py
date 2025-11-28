from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from goit_algo_hw_05.task_3.services.search_text_shared import MainText, PositionOrNone, TextPattern

type TextPart = str
"""Text part.

For getting hash value.
"""

type HashValue = int
"""Hash value."""


def polynomial_hash(s: TextPart, base: int, modulus: int) -> HashValue:
    """Calculates the polynomial hash of a string."""
    n = len(s)
    hash_value = 0
    for i, char in enumerate(s):
        power_of_base = pow(base, n - i - 1) % modulus
        hash_value = (hash_value + ord(char) * power_of_base) % modulus
    return hash_value


def search_i_text_i_rabin_karp(main_string: MainText, substring: TextPattern) -> PositionOrNone:
    # Lengths of the main string and substring of the search
    substring_length = len(substring)
    main_string_length = len(main_string)

    # Base number for hashing and modulus
    base = 256  # Because of the ASCII table and "ord" function
    modulus = 101

    # Hash value for the search substring and the current segment in the main string
    substring_hash = polynomial_hash(substring, base, modulus)
    current_slice_hash = polynomial_hash(main_string[:substring_length], base, modulus)

    # Previous value for hash recalculation
    h_multiplier = pow(base, substring_length - 1) % modulus

    # We go through the main line
    for i in range(main_string_length - substring_length + 1):
        if substring_hash == current_slice_hash and main_string[i : i + substring_length] == substring:
            return i

        if i < main_string_length - substring_length:
            current_slice_hash = (current_slice_hash - ord(main_string[i]) * h_multiplier) % modulus
            current_slice_hash = (current_slice_hash * base + ord(main_string[i + substring_length])) % modulus

            if current_slice_hash < 0:
                current_slice_hash += modulus

    return None
