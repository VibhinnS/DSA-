from __future__ import annotations
from typing import Generic, TypeVar
T = TypeVar("T")


class StackOverflow:
    raise ValueError("StackOverflow")


class StackUnderflow:
    raise ValueError("Couldn't find stack")


class Stack(Generic[T]):
    def __init__(self, limit: int):
        self.stack = list[T] = []
        self.limit = limit

    def __bool__(self) -> bool:
        return bool(self.stack)

    def __str__(self) -> str:
        return str(self.stack)

    def push(self, data: T) -> None | object:
        if len(self.stack) >= self.limit:
            return StackOverflow
        self.stack.append(data)

    def pop(self) -> T:
        if not self.stack:
            raise StackUnderflow
        return self.stack.pop()

    def peek(self) -> T:
        if not self.stack:
            return StackUnderflow
        return self.stack[-1]

    def is_empty(self) -> bool:
        return not bool(self.stack)

    def is_full(self) -> bool:
        return bool(self.stack)

    def size(self) -> int:
        return len(self.stack)

    def __contains__(self, item) -> T:
        return item in self.stack

