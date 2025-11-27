import pytest

from goit_algo_hw_05.task_1.main import HashTable


def test_hash_table() -> None:
    size = 5
    hash_table = HashTable[str, int].create(size=size)

    assert len(hash_table) == 0

    apple_key = "apple"
    apple_value = 10

    with pytest.raises(KeyError):
        hash_table.get(apple_key)

    hash_table.insert(apple_key, apple_value)
    hash_table.insert("orange", 20)
    hash_table.insert("banana", 30)

    assert len(hash_table) == 3  # noqa: PLR2004

    assert hash_table.get(apple_key) == apple_value

    hash_table.delete(apple_key)

    assert len(hash_table) == 2  # noqa: PLR2004

    with pytest.raises(KeyError):
        hash_table.get(apple_key)

    with pytest.raises(KeyError):
        hash_table.delete(apple_key)
