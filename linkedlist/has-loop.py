from __future__ import annotations

from typing import Any


class ContainsLoopError(Exception):
    pass


class Node:
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Node | None = None

    def __iter__(self):
        node = self
        visited = []
        while node:
            if node in visited:
                raise ContainsLoopError
            visited.append(node)
            yield node.data
            node = node.next

    @property
    def has_loop(self):
        try:
            list(self)
            return False
        except ContainsLoopError:
            return True

