from typing import Generic, TypeVar
T = TypeVar("T")
class StackOverflowError(BaseException):
    pass

class StackUnderflowError(BaseException):
    pass

class Stack(Generic[T]):
    def __init__(self, limit:int = 10):
        self.stack = list[T] = []
        self.limit = limit
        
    def __bool__(self):
        return bool(self.stack)
    
    def __str__(self):
        return str(self.stack)
    
    def push(self,data: T):
        if len(self.stack) >= limit:
            raise StackOverflowError
        self.stack.append(data)
        
    def pop(self):
        if not self.stack:
            raise StackUnderflowError
        return self.stack.pop()
    
    def peek(self):
        if not self.stack:
            raise StackUnderflowError
        return self.stack[-1]
    
    def is_empty(self):
        return not bool(self.stack)
    
    def size(self):
        return len(self.stack)
    
    def is_full(self):
        return self.size() == self.limit

    def __contains__(self, item: T):
        return item in self.stack
    
    
    
    