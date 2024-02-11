from collections.abc import Iterable
from typing import Generic, TypeVar

T = TypeVar("T")


class QueueWithList(Generic[T]):
    def __init__(self, iterable: Iterable[T]) -> None:
        self.entries: list[T] = list(iterable or [])

    def __len__(self) -> int:
        return len(self.entries)

    def __repr__(self) -> str:
        return f"Queue({tuple(self.entries)}"

    def put(self, item: T) -> None:
        self.entries.append(item)

    def get(self) -> T:
        if not self.entries:
            raise IndexError("Queue is Empty")
        return self.entries.pop(0)

    