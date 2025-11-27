from typing import Self

from pydantic import BaseModel

type HashIndex = int
"""Hash index type"""

type KeyValuePair[Key, Value] = tuple[Key, Value]
"""Key-Value pair type"""

type MultiCell[Key, Value] = list[KeyValuePair[Key, Value]]
"""Multi-cell type for handling collisions in hash table."""


class HashTable[Key, Value](BaseModel):
    """Hash table class."""

    size: int
    table: list[MultiCell[Key, Value]]

    @classmethod
    def create(cls, size: int) -> Self:
        """Creates a new hash table with a given size.

        Main constructor.
        """
        return cls(size=size, table=[[] for _ in range(size)])

    def _hash_function(self, key: Key) -> HashIndex:
        return hash(key) % self.size

    def insert(self, key: Key, value: Value) -> None:
        key_hash = self._hash_function(key)
        key_value: KeyValuePair[Key, Value] = (key, value)

        if not self.table[key_hash]:
            self.table[key_hash] = [key_value]
            return

        for index, pair in enumerate(self.table[key_hash]):
            if pair[0] == key:
                self.table[key_hash][index] = key_value
                return

        self.table[key_hash].append(key_value)

        return

    def __len__(self) -> int:
        return sum(len(cell) for cell in self.table)

    def get(self, key: Key) -> Value:
        """Returns the value associated with a given key.

        Raises:
            KeyError: If the key is not found in the hash table.
        """
        key_hash = self._hash_function(key)
        if self.table[key_hash]:
            for pair in self.table[key_hash]:
                if pair[0] == key:
                    return pair[1]

        msg = f"Key {key} not found in hash table."
        raise KeyError(msg)

    def delete(self, key: Key) -> None:
        """Deletes a key-value pair from the hash table.

        Raises:
            KeyError: If the key is not found in the hash table.
        """
        key_hash = self._hash_function(key)

        if self.table[key_hash]:
            for index, pair in enumerate(self.table[key_hash]):
                if pair[0] == key:
                    del self.table[key_hash][index]
                    return

        msg = f"Key {key} not found in hash table."
        raise KeyError(msg)
