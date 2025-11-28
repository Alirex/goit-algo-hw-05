from typing import Any

from pydantic import BaseModel, ConfigDict

from comparable import Comparable


class Some[T: Comparable[Any]](BaseModel):
    value: T

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def __lt__(self, value: Some[T], /) -> bool:
        return self.value < value.value

    def __gt__(self, value: Some[T], /) -> bool:
        return self.value > value.value

    def __le__(self, value: Some[T], /) -> bool:
        return self.value <= value.value

    def __ge__(self, value: Some[T], /) -> bool:
        return self.value >= value.value
